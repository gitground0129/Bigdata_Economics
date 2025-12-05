import matplotlib.pyplot as plt
import seaborn as sns

RESULT_DIR = "results"
# 유가, 소비자물가, 금리, 실업률을 연도(또는 날짜) 단위로 추적하는 라인플롯
def plot_all_trends(df):
    fig, ax = plt.subplots(figsize=(12, 6))

    ax.plot(df["date"], df["oil"], label="Oil Price")
    ax.plot(df["date"], df["cpi"], label="CPI")
    ax.plot(df["date"], df["rate"], label="Interest Rate")
    ax.plot(df["date"], df["unemployment"], label="Unemployment Rate")

    ax.legend()
    ax.set_title("Economic Indicators Trend")
    ax.set_xlabel("Date")
    ax.set_ylabel("Value")
    ax.grid(True)

    fig.tight_layout()
    fig.savefig(f"{RESULT_DIR}/plot_all_trends.png")
    plt.close(fig)

    fig.savefig(f"{RESULT_DIR}/plot_all_trends.png")
    plt.close()

# 유가, 소비자 물가 지수, 금리, 실업률의 상관관계를 보여주는 heatmap
def plot_correlation_heatmap(df):
    corr = df[["oil", "cpi", "rate", "unemployment"]].corr()

    fig, ax = plt.subplots(figsize=(6, 4))
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", ax=ax)

    ax.set_title("O/C/R/U Major Correlation ")
    fig.tight_layout()

    fig.savefig(f"{RESULT_DIR}/corr_heatmap.png")
    plt.close(fig)

# 시간에 따른 금리와 실업률변화를 두 축으로 비교
def plot_rate_vs_unemployment(df):
    fig, ax1 = plt.subplots(figsize=(12, 6))

    # 왼쪽 Y축: 금리
    ax1.plot(df["date"], df["rate"], label="Rate", color="tab:blue")
    ax1.set_ylabel("Interest Rate", color="tab:blue")
    ax1.tick_params(axis='y', labelcolor="tab:blue")

    # 오른쪽 Y축: 실업률
    ax2 = ax1.twinx()
    ax2.plot(df["date"], df["unemployment"], label="Unemployment", color="tab:red")
    ax2.set_ylabel("Unemployment Rate", color="tab:red")
    ax2.tick_params(axis='y', labelcolor="tab:red")

    plt.title("Interest Rate vs Unemployment")
    fig.tight_layout()
    fig.savefig(f"{RESULT_DIR}/rate_vs_unemployment.png")
    plt.close(fig)

# 실업률과 다른 지표(예: 유가, CPI)의 관계를 산점도로 확인
def plot_unemployment_scatter(df):
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # 실업률 vs 유가
    axes[0].scatter(df["unemployment"], df["oil"])
    axes[0].set_xlabel("Unemployment Rate")
    axes[0].set_ylabel("Oil Price")
    axes[0].set_title("Unemployment vs Oil Price")

    # 실업률 vs CPI
    axes[1].scatter(df["unemployment"], df["cpi"])
    axes[1].set_xlabel("Unemployment Rate")
    axes[1].set_ylabel("CPI")
    axes[1].set_title("Unemployment vs CPI")

    plt.tight_layout()
    plt.show()

    fig.savefig(f"{RESULT_DIR}/unemp_scatter.png")
    plt.close(fig)

def save_all_plots(merged_df):
    plot_all_trends(merged_df)
    plot_correlation_heatmap(merged_df)
    plot_rate_vs_unemployment(merged_df)
    plot_unemployment_scatter(merged_df)