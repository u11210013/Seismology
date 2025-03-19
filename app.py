import streamlit as st
import matplotlib.pyplot as plt
from obspy import UTCDateTime
from obspy.clients.fdsn import Client
from io import BytesIO

# 設定 IRIS 客戶端
client = Client("IRIS")

# 修正 Matplotlib 可能黑畫面問題
plt.style.use("default")

st.title("🌍 地震波形監測系統")

# 測站與通道設定
stations = ["SSLB", "NACB", "TWGB", "TPUB", "YHNB", "YULB"]
channels = ["BHN", "BHE", "BHZ"]
network = "TW"

# 📌 兩個區塊：即時監測 & 地震事件分析
tab1, tab2 = st.tabs(["📡 即時監測", "📅 地震事件分析"])

# 📡 即時監測
with tab1:
    st.header("📡 即時監測")
    
    station = st.selectbox("選擇測站", stations, key="station1")
    channel = st.selectbox("選擇通道", channels, key="channel1")

    time_options = {
        "最近 5 分鐘": 5 * 60,
        "最近 10 分鐘": 10 * 60,
        "最近 30 分鐘": 30 * 60,
        "最近 1 小時": 60 * 60
    }
    selected_time = st.selectbox("選擇監測時間範圍", list(time_options.keys()), key="time1")
    time_window = time_options[selected_time]

    end_time = UTCDateTime()
    start_time = end_time - time_window

    st.write(f"📡 正在抓取 {station} 測站的 {channel} 通道數據...")
    
    try:
        st_data = client.get_waveforms(network, station, "*", channel, start_time, end_time)
    except Exception as e:
        st.error(f"⚠️ 無法獲取數據: {e}")
        st.stop()

    fig, ax = plt.subplots(figsize=(8, 4))
    for tr in st_data:
        ax.plot(tr.times(), tr.data, label=f"{tr.stats.station} - {tr.stats.channel}")
    ax.set_title(f"{station} - {channel} 波形圖")
    ax.set_xlabel("時間 (秒)")
    ax.set_ylabel("振幅")
    ax.legend()

    img_buffer = BytesIO()
    fig.savefig(img_buffer, format="png")
    img_buffer.seek(0)

    st.pyplot(fig)
    st.download_button(
        label="📥 下載波形圖",
        data=img_buffer,
        file_name=f"{station}_{channel}_real_time.png",
        mime="image/png"
    )

# 📅 地震事件分析
with tab2:
    st.header("📅 地震事件分析")

    station2 = st.selectbox("選擇測站", stations, key="station2")
    channel2 = st.selectbox("選擇通道", channels, key="channel2")

    event_time_str = st.text_input("輸入地震時間 (格式：YYYY-MM-DD HH:MM:SS)", "2024-02-25 12:00:00")
    
    if st.button("🔍 獲取地震波形圖"):
        try:
            event_time = UTCDateTime(event_time_str)
            start_time_event = event_time - 1800  # 前 30 分鐘
            end_time_event = event_time + 1800  # 後 30 分鐘

            st.write(f"📡 抓取 {station2} 測站的 {channel2} 通道數據 (地震前後 30 分鐘)...")
            st_data_event = client.get_waveforms(network, station2, "*", channel2, start_time_event, end_time_event)

            fig2, ax2 = plt.subplots(figsize=(8, 4))
            for tr in st_data_event:
                ax2.plot(tr.times(), tr.data, label=f"{tr.stats.station} - {tr.stats.channel}")
            ax2.set_title(f"{station2} - {channel2} 波形圖 (地震前後 30 分鐘)")
            ax2.set_xlabel("時間 (秒)")
            ax2.set_ylabel("振幅")
            ax2.legend()

            img_buffer_event = BytesIO()
            fig2.savefig(img_buffer_event, format="png")
            img_buffer_event.seek(0)

            st.pyplot(fig2)
            st.download_button(
                label="📥 下載地震波形圖",
                data=img_buffer_event,
                file_name=f"{station2}_{channel2}_event.png",
                mime="image/png"
            )

        except Exception as e:
            st.error(f"⚠️ 無法獲取數據: {e}")
