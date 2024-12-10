import subprocess

def run_a_out():
    process = subprocess.Popen(['timeout','3', './a.out'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    returncode = process.returncode
    ret = {
        "stdout": stdout.decode('utf-8'),
        "stderr": stderr.decode('utf-8'),
        "returncode": returncode
    }
    return ret

def analyse_runout_differential(diff_runout_rec, tstname, runout1_exist, runout2_exist, out1, out2):
    res=open(diff_runout_rec,'a+')
    doubted=tstname+'\n'+'Suspected symptom: '

    if runout1_exist ^ runout2_exist:
        doubted=doubted+"\tOne does not compile an executable\n"
        doubted=doubted+'\n-------------------------\n'
        res.write(doubted)
        res.close()
        return True
    
    if not runout1_exist and not runout2_exist:
        return False

    if out1["returncode"] == 0 and out2["returncode"] == 0 \
        and out1["stdout"] == out2["stdout"] \
        and (out1["stderr"] == "" and out2["stderr"] == ""):
        return False
    

    if out1["returncode"] != 0 or out2["returncode"] != 0:
        doubted=doubted+"\tnot 0 returncode\n"
    if out1["stdout"] != out2["stdout"]:
        doubted=doubted+"\tdifferent stdout\n"
    if out1["stderr"] != "" or out2["stderr"] != "":
        doubted=doubted+"\trun time error\n"
        if out1["stdout"] != out2["stdout"]:
            doubted=doubted+"\t\tdifferent stderr\n"
    doubted=doubted+'\n-------------------------\n'
    res.write(doubted)
    res.close()
    return True