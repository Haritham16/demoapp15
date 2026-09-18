def health_check():
    return {
        "status": "UP",
        "message": "Banking application is healthy"
    }


if __name__ == "__main__":
    print(health_check())
