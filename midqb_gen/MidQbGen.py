from midqb_functions import *
from CreatePAK import pakMaker
from mido import MidiFile, MidiTrack
from io import StringIO
import os
import sys
import re


sys.path.append("..\\pak_extract")

from pak_extract.pak_functions import createHeaderDict
from pak_extract.QB2Text import convert_qb_file, qb_bytes, print_qb_text_file
from pak_extract.Text2QB import main as t2q_main


tbp = 480



def make_mid(midfile, hopo, filename = "", *args, **kwargs):
    mid = MidiFile(midfile, clip = True)
    midQS = ""
    consoleType = 1
    if filename == "":
        filename = os.path.splitext(os.path.basename(midfile))[0]

    headerDict = createHeaderDict(filename)
    # print(headerDict)
    if "ghwt" in args:
        qb_dict = parse_wt_qb(mid, hopo, *args)
        if "replace_perf" in args:
            perf_file = args[args.index("replace_perf") + 1]

            if perf_file.endswith(".txt"):
                with open(perf_file, "r") as f:
                    perf_qb = f.read().replace("song_performance", f"{filename}_performance")
                    if "qb_file = " not in perf_qb:
                        perf_qb = f"qb_file = songs/{filename}.mid.qb\n" + perf_qb
                    perf_qb = t2q_main(perf_qb, game = "GHWT")
            else:
                with open(perf_file, "rb") as f:
                    perf_qb = f.read()
            qb_sections = convert_qb_file(qb_bytes(perf_qb), filename, headerDict,
                                          "PC")
            for x in qb_sections:
                if "_performance" in x.section_id and not "notes" in x.section_id:
                    qb_dict["performance"] = x
                    '''if qb_dict["performance_mid"]:
                        sorted_section = {}
                        for y in qb_dict["performance"].section_data:
                            sorted_section[y.data_value[0].data_value] = y                            
                        qb_dict["performance"].section_data += qb_dict["performance_mid"]'''
                    break
        QBSections, midQS = create_wt_qb_sections(qb_dict, filename, *args)
        midQB = create_wt_qb(QBSections, filename)
        if "performance" in qb_dict:
            midQB = convert_qb_file(qb_bytes(midQB), filename, headerDict, "PC")
            for x in midQB:
                if "_performance" in x.section_id and not "notes" in x.section_id:
                    if x.section_data == [0, 0]:
                        x.array_node_type = qb_dict["performance"].array_node_type
                        x.section_data = qb_dict["performance"].section_data
                    else:
                        x.section_data += qb_dict["performance"].section_data
                        cam_list = list(qb_dict["anim"]["CAMERAS"].keys())
                        sorted_section = {}
                        for y in x.section_data:
                            event_time = y.data_value[0].data_value
                            if re.search(r'Band_PlayLoop', y.data_value[1].data_value, flags = re.IGNORECASE):
                                closest_value = min(cam_list, key=lambda x: abs(y.data_value[0].data_value - x))
                                if event_time != closest_value and abs(event_time - closest_value) < 1000:
                                    event_time = closest_value
                                    y.data_value[0].data_value = event_time
                            if event_time in sorted_section:
                                sorted_section[event_time].append(y)
                            else:
                                sorted_section[event_time] = [y]
                        sorted_section = dict(sorted(sorted_section.items()))
                        new_perf = []
                        for z in sorted_section:
                            new_perf.extend(sorted_section[z])
                        x.section_data = new_perf
                    break
            result = StringIO()
            orig_stdout = sys.stdout
            sys.stdout = result
            print_qb_text_file(midQB)
            sys.stdout = orig_stdout
            qb_text = result.getvalue()
            midQB = t2q_main(qb_text, game = "GHWT")
            # print()
    else:
        midParsed = parseGH3QB(mid, hopo)
        midQB = makeMidQB(midParsed, filename, headerDict, consoleType)
    """with open(f"{filename}_song.mid.qb", 'wb') as f:
        f.write(midQB)"""
    if "qb" in args:
        pakFile = {"qb": midQB, "qs": midQS}
    else:
        to_pak = [[midQB, f"songs\\{filename}.mid.qb"]]
        if midQS:
            to_pak.append([midQS, f"songs\\{filename}.mid.qs"])
        if "add_ska" in args:
            for files in os.listdir(args[args.index("add_ska") + 1]):
                to_pak.append([open(f"{args[args.index('add_ska') + 1]}\\{files}", 'rb').read(), files])
        if "song_script" in args:
            song_script_file = args[args.index("song_script") + 1]
            if song_script_file.endswith(".txt"):
                song_script = ""
                with open(song_script_file, "r") as f:
                    song_script_raw = f.read()
                    if not "qb_file = " in song_script_raw:
                        song_script = f"qb_file = songs/{filename}_song_scripts.qb\n"
                    if not "_song_startup = " in song_script_raw:
                        song_script += f'script {filename}_song_startup = "29 b6 24 06 00 00 00 09 00 00 00 09 01 16 f8 2d 15 1a 2c 01 24"\n'
                    song_script += song_script_raw
                    if not f"_anim_struct_{filename}" in song_script:
                        song_script = song_script.replace("anim_struct", f"anim_struct_{filename}")
                song_script = t2q_main(song_script, game = "GHWT")
            else:
                with open(song_script_file, "rb") as f:
                    song_script = f.read()
            to_pak.append([song_script, f"songs\\{filename}_song_scripts.qb"])
        pakFile = pakMaker(to_pak)

    return pakFile, filename

if __name__ == "__main__":
    consoleType = 1  # 0 for Wii, 1 for PC, 2 for 360, 3 for XBX, 4 for PS2, 5 for WPC
    midfile = sys.argv[1]
    if len(sys.argv) == 3:
        hopo = int(sys.argv[2])
    else:
        hopo = 170

    pakFile, filename = make_mid(midfile, hopo, "", *sys.argv)

    if "qb" in sys.argv:
        with open(f".\\Pak Input\\songs\\{filename}.mid.qb.xen", 'wb') as f:
            f.write(pakFile["qb"])
        if pakFile["qs"]:
            with open(f".\\Pak Input\\songs\\{filename}.mid.qs.xen", 'wb') as f:
                f.write(pakFile["qs"])
    else:
        with open(f"{filename}_song.pak.xen", 'wb') as f:
            f.write(pakFile)

