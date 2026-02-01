# sentiment_pipeline.py
import os
import subprocess
import sys
import time

os.environ['PYTHONIOENCODING'] = 'utf-8'

HDFS_INPUT = "/user/jianw/input"
HDFS_OUTPUT = f"/user/jianw/output_sentiment_{int(time.time())}"
LOCAL_DIR = "sentiment_job"
HADOOP_JAR = "/home/jianw/hadoop-3.4.0/share/hadoop/tools/lib/hadoop-streaming-3.4.0.jar"

def run_cmd(cmd, desc=None, fail_ok=False):
    if desc:
        print(f"[INFO] {desc}")
    proc = subprocess.run(cmd, shell=True, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.stdout:
        print(proc.stdout.strip())
    if proc.stderr:
        print(proc.stderr.strip(), file=sys.stderr)
    if proc.returncode != 0 and not fail_ok:
        raise RuntimeError(f"[ERROR] Command failed: {desc or cmd}")
    return proc.stdout

def run_sentiment_pipeline():
    try:
        run_cmd(f"hdfs dfs -rm -r -f {HDFS_OUTPUT}", "Removing old HDFS output", fail_ok=True)
        run_cmd(f"hdfs dfs -mkdir -p {HDFS_INPUT}", "Creating HDFS input directory")
        run_cmd(f"hdfs dfs -put -f {LOCAL_DIR}/tweets.txt {HDFS_INPUT}/", "Uploading tweets.txt to HDFS")
        run_cmd(f"hdfs dfs -ls {HDFS_INPUT}", "Listing HDFS input directory")

        files = " ".join([
            f"-file {LOCAL_DIR}/mapper.py",
            f"-file {LOCAL_DIR}/reducer.py",
            f"-file {LOCAL_DIR}/sentiment_model.joblib",
            f"-file {LOCAL_DIR}/vectorizer.joblib"
        ])

        streaming_cmd = (
            f'hadoop jar "{HADOOP_JAR}" '
            f'-input {HDFS_INPUT}/tweets.txt '
            f'-output {HDFS_OUTPUT} '
            f'-mapper "python3 mapper.py" '
            f'-reducer "python3 reducer.py" '
            f'{files}'
        )
        run_cmd(streaming_cmd, "Running Hadoop Streaming job")

        run_cmd(f"hdfs dfs -ls {HDFS_OUTPUT}", "Listing HDFS output directory")
        result = run_cmd(f"hdfs dfs -cat {HDFS_OUTPUT}/part-00000", "Reading Hadoop output", fail_ok=True)

        return result.strip() or "[No data found in part-00000]"
    except Exception as e:
        return f"[ERROR] {e}"
