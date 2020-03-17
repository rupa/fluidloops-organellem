import os
from sf2utils.sf2parse import Sf2File

for file in os.listdir(os.getcwd() + "/sf2/"):
    if os.path.splitext(file)[-1].lower() == ".txt":
        os.remove(os.getcwd() + "/sf2/" + file)

listFile = ""

for file in sorted(os.listdir(os.getcwd() + "/sf2/")):

    with open(os.getcwd() + "/sf2/" + str(file), 'rb') as sf2_file:
        sf2 = Sf2File(sf2_file)

    sf2Name = str(os.path.splitext(file)[0])
    if len(sf2Name) > 20:
        sf2Name = sf2Name[0:20]
    sf2Name = sf2Name.rstrip().replace(' ', '_')
    # sf2Name is repeated now, older versions used the embedded name of the sf2
    listFile = listFile +" "+sf2Name+" "+sf2Name+" "+str(len(sf2Name))

    presetsList = []
    for instNume, preset in enumerate(sf2.raw.pdta["Phdr"]):
        instName = preset.name.rstrip('\x00').replace(' ', '_').rstrip()

        if instName[0:3] != "EOP": # End of presets tags
            presetsList.append([preset.bank, preset.preset, instName])

            print(
                '{}: preset={} bank={} bag={} library={} genre={} morphology={}'
                .format(
                    instName,
                    preset.preset,
                    preset.bank,
                    preset.bag,
                    preset.library,
                    preset.genre,
                    preset.morphology
                )
            )

    soundfontFile = ""
    for p in sorted(presetsList):
        soundfontFile = soundfontFile + p[2] +";"+"\n"

    listFile = listFile+" "+str(instNume)+";"+"\n"

    with open(os.getcwd() + "/sf2/"+ str(os.path.splitext(file)[0]) + ".txt", "w") as text_file:
        text_file.write(soundfontFile)
    print('')

with open(os.getcwd() + "/sf2/"+ "list.txt", "w") as text_file:
    text_file.write(listFile)
