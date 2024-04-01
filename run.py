import subprocess

def run_backend():
    print("Running the backend...")
    backend_command = ["uvicorn", "Algorithm.app:app", "--reload"]
    return backend_command

def run_frontend():
    print("Running the frontend...")
    frontend_command = ["npm", "start"]
    return frontend_command

if __name__ == "__main__":
    try:
        backend_process = subprocess.Popen(run_backend())

        frontend_process = subprocess.Popen(run_frontend(), cwd="frontend")

        backend_process.wait()
        frontend_process.wait()
    except KeyboardInterrupt:
        backend_process.kill()
        frontend_process.kill()
