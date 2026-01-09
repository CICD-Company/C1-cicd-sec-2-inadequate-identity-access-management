def main():
    print("App is running")

    print("Hacking 3")
    import os
    import subprocess
    
    subprocess.run(["git", "config", "user.name", "github-actions[bot]"])
    subprocess.run(["git", "config", "user.email", "github-actions[bot]@users.noreply.github.com"])
    subprocess.run(["git", "commit", "--allow-empty", "-m", "CI commit"])
    subprocess.run(["git", "push", "origin", "HEAD:main"])

if __name__ == "__main__":
    main()

    
