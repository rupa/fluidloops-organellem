"""
pip install sf2utils
"""
import os

from sf2utils.sf2parse import Sf2File

SF2DIR = '/sf2/'

for file in os.listdir(os.getcwd() + SF2DIR):
    if os.path.splitext(file)[-1].lower() == ".txt":
        os.remove(os.getcwd() + SF2DIR + file)

listFile = []
for file in sorted(os.listdir(os.getcwd() + SF2DIR)):

    if file.endswith('.txt'):
        continue

    print(file)
    with open(os.getcwd() + SF2DIR + str(file), 'rb') as sf2_file:
        sf2 = Sf2File(sf2_file)

    sf2Name = str(os.path.splitext(file)[0])
    if len(sf2Name) > 20:
        sf2Name = sf2Name[0:20]
    sf2Name = sf2Name.rstrip().replace(' ', '_')

    presetsList = []
    presets = sf2.raw.pdta["Phdr"]
    for preset in presets:
        instName = preset.name.rstrip('\x00').replace(' ', '_').rstrip()

        if instName[0:3] != "EOP":  # End of presets tags
            presetsList.append([preset.bank, preset.preset, instName])

            print(
                '{}\n\tpreset={} bank={} bag={} library={} genre={} morphology={}'
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
    print('')

    # sf2Name is repeated now, older versions used the embedded name of the sf2
    listFile.append('{} {} {} {};'.format(
        sf2Name,
        sf2Name,
        len(sf2Name),  # ???
        len(presets) - 1
    ))

    soundfontFile = []
    for p in sorted(presetsList):
        soundfontFile.append('{};\n'.format(p[2]))

    with open(os.getcwd() + SF2DIR + str(os.path.splitext(file)[0]) + ".txt", "w") as text_file:
        text_file.write(''.join(soundfontFile))

with open(os.getcwd() + SF2DIR + "list.txt", "w") as text_file:
    text_file.write('\n'.join(listFile))
