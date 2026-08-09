import uvicorn
from src.config.config_loader import CONFIG


def main():
    print("🚀 Starting Customer Churn API...")
    print(f"🌐 Host: {CONFIG['api']['host']}")
    print(f"🔌 Port: {CONFIG['api']['port']}")

    uvicorn.run(
        "src.api.main:app",
        host=CONFIG["api"]["host"],
        port=CONFIG["api"]["port"],
        reload=True  # remove in production (EC2)
    )


if __name__ == "__main__":
    main()