def main():
    print("App is running")

    print("Hacking")
    import os
    import subprocess
    
    subprocess.run(["git", "config", "user.name", "ci-bot"])
    subprocess.run(["git", "config", "user.email", "ci@github"])
    subprocess.run(["git", "commit", "--allow-empty", "-m", "CI commit"])
    subprocess.run(["git", "push", "origin", "HEAD:main"])

if __name__ == "__main__":
    main()
