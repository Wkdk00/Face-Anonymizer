import streamlit as st, requests, pandas as pd, time
from PIL import Image
from io import BytesIO

st.title("Face Anonymizer")
tab1, tab2 = st.tabs(["Process", "Statistics"])

with tab1:
    uploaded_file = st.file_uploader("Choose image or video...", type=["jpg", "jpeg", "png", "mp4", "avi", "mov"])
    method = st.selectbox("Anonymization method", ["blur", "black", "pixel"])
    
    if uploaded_file is not None:
        uploaded_file.seek(0)
        files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
        data = {"method": method}
        
        with st.spinner("Processing..."):
            try:
                response = requests.post("http://backend:8000/", files=files, data=data, timeout=300)
                response.raise_for_status()
            except requests.exceptions.HTTPError as e:
                st.error(f"Backend error: {response.status_code} — {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"Error accessing the backend: {e}")
                st.stop()
        
        if uploaded_file.type.startswith("video"):
            st.video(response.content)
            st.download_button(
                label="💾 Save video",
                data=response.content,
                file_name=f"anonymized_{uploaded_file.name.split('.')[0]}.webm",
                mime="video/webm"
            )
        else:
            st.image(Image.open(BytesIO(response.content)), caption="Anonymized image")
            st.download_button(
                label="💾 Save image",
                data=response.content,
                file_name=f"anonymized_{uploaded_file.name}",
                mime="image/jpeg"
            )

with tab2:
    st.title("Statistics")
    PROMETHEUS_URL = "http://prometheus:9090"
    def get_metric(query: str) -> float:
        try:
            resp = requests.get(f"{PROMETHEUS_URL}/api/v1/query", params={"query": query})
            resp.raise_for_status()
            data = resp.json()
            if data["status"] == "success" and data["data"]["result"]:
                return float(data["data"]["result"][0]["value"][1])
        except:
            pass
        return 0.0
    total = int(get_metric('http_requests_total{job="backend", handler="/"}'))
    st.metric("Total requests", total)
    rps = get_metric('rate(http_requests_total{job="backend", handler="/"}[1m])')
    st.metric("Requests per second", f"{rps:.2f}")
    latency = get_metric('histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{job="backend", handler="/"}[1m]))')
    st.metric("Processing time (95%)", f"{latency * 1000:.1f} мс")
    st.subheader("RPS in the last 10 minutes")
    now = int(time.time())
    ten_minutes_ago = now - 600
    resp = requests.get(f"{PROMETHEUS_URL}/api/v1/query_range", params={"query": 'rate(http_requests_total{job="backend", handler="/"}[1m])', "start": ten_minutes_ago, "end": now, "step": "15s"})
    resp.raise_for_status()
    data = resp.json()
    if data["data"]["result"]:
        points = data["data"]["result"][0]["values"]
        if points:
            df = pd.DataFrame(points, columns=["timestamp", "rps"])
            df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")
            df["rps"] = pd.to_numeric(df["rps"])
            st.line_chart(df.set_index("timestamp")["rps"])
        else:
            st.info("Нет данных за последние 10 минут")
    else:
        st.info("Prometheus вернул пустой результат")