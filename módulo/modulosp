import redis

r = redis.Redis(host='redis-10364.c325.us-east-1-4.ec2.cloud.redislabs.com',
  port=10364,
  password='9oxEjbS4slyRNmxknio5Ryi8UaasqLYC')

def crearRegistro(nreg, lista):
    cond=14
    if lista[0]!="M" and lista[0]!="F":
        sex=False
    else:
        sex=True
    if int(lista[1])>=0 and int(lista[1])<=100:
        age=True
    else:
        age=False
    for i in range (2,16):
        if lista[i]!="1" and lista[i]!="2":
            cond+=1
    if cond==14 and sex==True and age==True:
        r.hset(nreg, "sexo", lista[0])
        r.hset(nreg, "edad", lista[1])
        r.hset(nreg, "fumador", lista[2])
        r.hset(nreg, "dedos_amarillos", lista[3])
        r.hset(nreg, "ansiedad", lista[4])
        r.hset(nreg, "presion_de_grupo", lista[5])
        r.hset(nreg, "enfermedad_cronica", lista[6])
        r.hset(nreg, "fatiga", lista[7])
        r.hset(nreg, "alergia", lista[8])
        r.hset(nreg, "sibilancias", lista[9])
        r.hset(nreg, "consumo_alcohol", lista[10])
        r.hset(nreg, "tos", lista[11])
        r.hset(nreg, "dificultad_respirar", lista[12])
        r.hset(nreg, "dificultad_tragar", lista[13])
        r.hset(nreg, "dolor_en_pecho", lista[14])
        r.hset(nreg, "cancer_pulmon", lista[15])
    else:
        print("Valores no validos")

def obtenerNoRegistro():
    lastreg=r.keys("*")
    lastreg=lastreg[0]
    nreg=lastreg[6:]
    newreg=int(nreg)
    newreg+=1
    nextreg="public"+str(newreg).zfill(5)
    return nextreg