from random import *



class Operatives:
    class Protection:
        def Smoke(star):
            Tasks = ['''ИГРАТЬ ТОЛЬКО С M590A1 (ДРОБОВИК) И SMG-11 (МИНИ ПП)''','''ИГРАТЬ ТОЛЬКО С FMG-9 (ПИСТОЛЕТ-ПУЛЕМЕТ) (БЕЗ ПРИЦЕЛА)''']
            Star_Tasks = ['''К сожалению на данного опреативника нету заданий со звёздочкой''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks)

        def MUTE(star):
            Tasks = ['''ИГРАТЬ ТОЛЬКО С M590A1 (ДРОБОВИК) И SMG-11 (МИНИ ПП)''','''ИГРАТЬ ТОЛЬКО С MP5K (ПИСТОЛЕТ-ПУЛЕМЕТ) (БЕЗ ПРИЦЕЛА)''']
            Star_Tasks = ['''УБИТЬ С ПОМОЩЬЮ ДОП. УСТРОЙСТВА С4 (ВЗРЫВЧАТКА )''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks)  

        def CASTLE(star):
            Tasks = ['''ИГРАТЬ ТОЛЬКО С M1014 (ДРОБОВИК) И SUPER SHORTY (ДРОБОВИК)''','''ИГРАТЬ ТОЛЬКО С UMP45 (ПИСТОЛЕТ-ПУЛЕМЕТ) И 5.7 USG (ПИСТОЛЕТ)''']
            Star_Tasks = ['''УБИТЬ С ПОМОЩЬЮ ДОП. УСТРОЙСТВА УДАРНАЯ ГРАНАТА (ИМПАКТ)''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks)  
        
        def PULSE(star):
            Tasks = ['''ИГРАТЬ ТОЛЬКО С M1014 (ДРОБОВИК) И M45 MEUSOC (ПИСТОЛЕТ)''','''ИГРАТЬ ТОЛЬКО С UMP45 (ПИСТОЛЕТ-ПУЛЕМЕТ) И 5.7 USG (ПИСТОЛЕТ)''']
            Star_Tasks = ['''УБИТЬ >1  С ПОМОЩЬЮ ДОП. УСТРОЙСТВА С4 (ВЗРЫВЧАТКА )''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks)

        def JAGER(star):
            Tasks = ['''ИГРАТЬ ТОЛЬКО С M870 (ДРОБОВИК) И P12 (ПИСТОЛЕТ)''','''ИГРАТЬ ТОЛЬКО С 416-C CARBINE (ШТУРМОВАЯ ВИНТОВКА) И P12 (ПИСТОЛЕТ)''']
            Star_Tasks = ['''( УБИТЬ >1 НА СПАВНПИКЕ)''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks)
                
        def BANDIT(star):
            Tasks = ['''ИГРАТЬ ТОЛЬКО С M870 (ДРОБОВИК) И P12 (ПИСТОЛЕТ)''','''ИГРАТЬ ТОЛЬКО С MP7 (ПИСТОЛЕТ-ПУЛЕМЕТ) И P12 (ПИСТОЛЕТ)''']
            Star_Tasks = ['''( УБИТЬ С ПОМОЩЬЮ ДОП. УСТРОЙСТВА С4 (ВЗРЫВЧАТКА ))''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks)   

        def DOC(star):
            Tasks = ['''ИГРАТЬ ТОЛЬКО С SG-CQB (ДРОБОВИК) И LFP586 (РЕВОЛЬВЕР)''','''ИГРАТЬ ТОЛЬКО С MP5 (ПИСТОЛЕТ-ПУЛЕМЕТ) И LFP586 (РЕВОЛЬВЕР)''','''ИГРАТЬ ТОЛЬКО С P90 (ПИСТОЛЕТ-ПУЛЕМЕТ) И P9 (ПИСТОЛЕТ)''']
            Star_Tasks = ['''К сожалению на данного опреативника нету заданий со звёздочкойТУ''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks)

        def ROOK(star):
            Tasks = ['''ИГРАТЬ ТОЛЬКО С SG-CQB (ДРОБОВИК) И LFP586 (РЕВОЛЬВЕР)''','''ИГРАТЬ ТОЛЬКО С MP5 (ПИСТОЛЕТ-ПУЛЕМЕТ) И LFP586 (РЕВОЛЬВЕР)''','''ИГРАТЬ ТОЛЬКО С P90 (ПИСТОЛЕТ-ПУЛЕМЕТ) И P9 (ПИСТОЛЕТ)''']
            Star_Tasks = ['''УБИТЬ С ПОМОЩЬЮ ДОП. УСТРОЙСТВА УДАРНАЯ ГРАНАТА (ИМПАКТ)''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks)  

        def TACHANKA(star):
            Tasks = ['''ИГРАТЬ ТОЛЬКО С SASG-12 (ДРОБОВИК) И PMM(ПИСТОЛЕТ)''','''ИГРАТЬ ТОЛЬКО С 9X19VSN (ПИСТОЛЕТ-ПУЛЕМЕТ) И GSH-18 (ПИСТОЛЕТ)''']
            Star_Tasks = ['''К сожалению на данного опреативника нету заданий со звёздочкой''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks)   

        def KAPKAN(star):
            Tasks = ['''ИГРАТЬ ТОЛЬКО С DP27 (РУЧНОЙ ПУЛЕМЕТ) И PMM(ПИСТОЛЕТ)''','''ИГРАТЬ ТОЛЬКО С 9X19VSN (ПИСТОЛЕТ-ПУЛЕМЕТ) И GSH-18 (ПИСТОЛЕТ)''']
            Star_Tasks = ['''УБИТЬ С ПОМОЩЬЮ ДОП. УСТРОЙСТВА С4 (ВЗРЫВЧАТКА )''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks)        

        def FROST(star):
            Tasks = ['''ИГРАТЬ ТОЛЬКО С SUPER 90 (ДРОБОВИК) И MK19MM(ПИСТОЛЕТ)''','''ИГРАТЬ ТОЛЬКО С 9mmC1 (ПИСТОЛЕТ-ПУЛЕМЕТ) И ITA12S (ДРОБОВИК)''']
            Star_Tasks = ['''УБИТЬ С ПОМОЩЬЮ ДОП. УСТРОЙСТВА С4 (ВЗРЫВЧАТКА )''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks)  

        def CAVEIRA(star):
            Tasks = ['''ИГРАТЬ ТОЛЬКО С M12 (ПИСТОЛЕТ-ПУЛЕМЕТ) И LUISON (ПИСТОЛЕТ)''','''ИГРАТЬ ТОЛЬКО С SPAS-15 (ДРОБОВИК) И LUISON (ПИСТОЛЕТ)''']
            Star_Tasks = ['''УБИТЬ С ПОМОЩЬЮ ДОП. УСТРОЙСТВА УДАРНАЯ ГРАНАТА (ИМПАКТ)''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks)   

        def ECHO(star):
            Tasks = ['''ИГРАТЬ ТОЛЬКО С MP5SD (ПИСТОЛЕТ-ПУЛЕМЕТ) И P229 (ПИСТОЛЕТ)''',''''Играешь только с SUPERNOVA (ДРОБОВИК) и BERING 9 (ПИСТОЛЕТ-ПУДЕМЕТ)''']
            Star_Tasks = ['''УБИТЬ С ПОМОЩЬЮ ДОП. УСТРОЙСТВА УДАРНАЯ ГРАНАТА (ИМПАКТ)''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks)  

        def MIRA(star):
            Tasks = ['''ИГРАТЬ ТОЛЬКО С VECTOR .45 ACP (ПИСТОЛЕТ-ПУЛЕМЕТ) И ITA12S (ДРОБОВИК)''',''''Играешь только с ITA12L (ДРОБОВИК) и USP40 (ПИСТОЛЕТ)''']
            Star_Tasks = ['''УБИТЬ С ПОМОЩЬЮ ДОП. УСТРОЙСТВА (ВЗРЫВЧАТКА)''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks)

        def LESION(star):
            Tasks = ['''ИГРАТЬ ТОЛЬКО С T-5 SMG (ПИСТОЛЕТ-ПУЛЕМЕТ) И Q-929 (ПИСТОЛЕТ)''',''''Играешь только с SIX12 SD (ДРОБОВИК) и Q-929 (ПИСТОЛЕТ)''']
            Star_Tasks = ['''УБИТЬ С ПОМОЩЬЮ ДОП. УСТРОЙСТВА (ВЗРЫВЧАТКА)''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks)   

        def ELA(star):
            Tasks = ['''ИГРАТЬ ТОЛЬКО С SCORPION EVO 3 A1 (ПИСТОЛЕТ-ПУЛЕМЕТ) И RG15 (ПИСТОЛЕТ)''',''''Играешь только с FO-12 (ДРОБОВИК) и RG15 (ПИСТОЛЕТ)''']
            Star_Tasks = ['''К сожалению на данного опреативника нету заданий со звёздочкой''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks) 

        def VIGIL(star):
            Tasks = ['''ИГРАТЬ ТОЛЬКО С K1A (ПИСТОЛЕТ-ПУЛЕМЕТ) И C75 AUTO (МИНИ-ПП)''',''''Играешь только с BOSG.12.2 (ДРОБОВИК) и SMG-12 (МИНИ-ПП)''']
            Star_Tasks = ['''УБИТЬ С ПОМОЩЬЮ ДОП. УСТРОЙСТВА УДАРНАЯ ГРАНАТА (ИМПАКТ)''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks)        

        def ALIBI(star):
            Tasks = ['''ИГРАТЬ ТОЛЬКО С MX4 STORM (ПИСТОЛЕТ-ПУЛЕМЕТ) И BAILIFF 410 (ПИСТОЛЕТ)''',''''Играешь только с ACS12 (ДРОБОВИК) и KERATOS .357 (ПИСТОЛЕТ)''']
            Star_Tasks = ['''УБИТЬ С ПОМОЩЬЮ ДОП. УСТРОЙСТВА УДАРНАЯ ГРАНАТА (ИМПАКТ)''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks) 

        def MAESTRO(star):
            Tasks = ['''ИГРАТЬ ТОЛЬКО С ALDA 5.56 (РУЧНОЙ ПУЛЕМЕТ) И BAILIFF 410 (ПИСТОЛЕТ)''',''''Играешь только с ACS12 (ДРОБОВИК) и KERATOS .357 (ПИСТОЛЕТ)''']
            Star_Tasks = ['''УБИТЬ С ПОМОЩЬЮ ДОП. УСТРОЙСТВА УДАРНАЯ ГРАНАТА (ИМПАКТ)''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks)  

        def CLASH(star):
            Tasks = ['''ИГРАТЬ ТОЛЬКО С SUPER SHORTY (ДРОБОВИК)''',''''Играешь только с SPSMG9 (МИНИ-ПП)''']
            Star_Tasks = ['''УБИТЬ С ПОМОЩЬЮ ЩИТ ЭШС''','''УБИТЬ С ПОМОЩЬЮ ДОП. УСТРОЙСТВА УДАРНАЯ ГРАНАТА (ИМПАКТ)''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks)    

        def KAID(star):
            Tasks = ['''ИГРАТЬ ТОЛЬКО С AUG A3 (Штурмавая винтовка) и LFP586 (ПИСТОЛЕТ)''',''''Играешь только с TCSG12 (ДРОБОВИК) и .44 MAG SEMI-AUTO (ПИСТОЛЕТ)''']
            Star_Tasks = ['''УБИТЬ С ПОМОЩЬЮ КОЛЮЧАЯ ПРОВОЛОКА + ТОКОПРОВОДНИК "RTILA"''','''УБИТЬ С ПОМОЩЬЮ ДОП. УСТРОЙСТВА ВЗРЫВЧАТКА (С4)''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks)   

        def MOZZIE(star):
            Tasks = ['''ИГРАТЬ ТОЛЬКО С COMMANDO 9 (Штурмавая винтовка) и SDP 9MM (ПИСТОЛЕТ)''',''''Играешь только с P10 RONI (ПИСТОЛЕТ-ПУЛЕМЕТ) и SDP 9MM (ПИСТОЛЕТ)''']
            Star_Tasks = ['''УБИТЬ С ПОМОЩЬЮ ДОП. УСТРОЙСТВА ВЗРЫВЧАТКА (С4)''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks)

        def WARDEN(star):
            Tasks = ['''ИГРАТЬ ТОЛЬКО С M590A1 (ДРОБОВИК) и SMG-12 (МИНИ-ПП)''',''''Играешь только с MPX (ПИСТОЛЕТ-ПУЛЕМЕТ) и P-10C (ПИСТОЛЕТ)''']
            Star_Tasks = ['''УБИТЬ С ПОМОЩЬЮ ДОП. УСТРОЙСТВА ВЗРЫВЧАТКА (С4)''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks)   

        def GOYO(star):
            Tasks = ['''ИГРАТЬ ТОЛЬКО С TCSG12 (ДРОБОВИК) и P229 RC (ПИСТОЛЕТ)''',''''Играешь только с VECTOR .45 ACP (ПИСТОЛЕТ-ПУЛЕМЕТ) и P229 RC (ПИСТОЛЕТ)''']
            Star_Tasks = ['''УБИТЬ С ПОМОЩЬЮ ДОП. УСТРОЙСТВА ВЗРЫВЧАТКА (С4)''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks)

        def WAMAI(star):
            Tasks = ['''ИГРАТЬ ТОЛЬКО С AUG A2 (Штурмавая винтовка) и D-40 (ПИСТОЛЕТ)''',''''Играешь только с MP5K (ПИСТОЛЕТ-ПУЛЕМЕТ) и P12 (ПИСТОЛЕТ)''']
            Star_Tasks = ['''УБИТЬ С ПОМОЩЬЮ ДОП. УСТРОЙСТВА УДАРНАЯ ГРАНАТА (ИМПАКТ)''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks) 

        def ORYX(star):
            Tasks = ['''ИГРАТЬ ТОЛЬКО С SPAS-12 (ДРОБОВИК) и USP40 (ПИСТОЛЕТ)''',''''Играешь только с T-5 SMG (ПИСТОЛЕТ-ПУЛЕМЕТ) и BAILIFF 410 (ПИСТОЛЕТ)''']
            Star_Tasks = ['''К сожалению на данного опреативника нету заданий со звёздочкой''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks)   

        def MELUSI(star):
            Tasks = ['''ИГРАТЬ ТОЛЬКО С SUPER 90 (ДРОБОВИК) и RG15 (ПИСТОЛЕТ)''',''''Играешь только с MP5 (ПИСТОЛЕТ-ПУЛЕМЕТ) и RG15 (ПИСТОЛЕТ)''']
            Star_Tasks = ['''УБИТЬ С ПОМОЩЬЮ ДОП. УСТРОЙСТВА УДАРНАЯ ГРАНАТА (ИМПАКТ)''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks)  

        def ARUNI(star):
            Tasks = ['''ИГРАТЬ ТОЛЬКО С MK 14 EBR (СНАЙПЕРСКАЯ ВИНТОВКА) и PRB92 (ПИСТОЛЕТ)''',''''Играешь только с P10 RONI (ПИСТОЛЕТ-ПУЛЕМЕТ) и PRB92 (ПИСТОЛЕТ)''']
            Star_Tasks = ['''УБИТЬ нажом''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks) 

        def THUNDERBIRD(star):
            Tasks = ['''ИГРАТЬ ТОЛЬКО С SPAS-15 (ДРОБОВИК) и BEARING 9 (МИНИ-ПП)''',''''Играешь только с SPEAR .308 (ШТУРМОВАЯ ВИНТОВКА) и Q-929 (ПИСТОЛЕТ)''']
            Star_Tasks = ['''УБИТЬ С ПОМОЩЬЮ ДОП. УСТРОЙСТВА УДАРНАЯ ГРАНАТА (ИМПАКТ)''','''УБИТЬ С ПОМОЩЬЮ ДОП. УСТРОЙСТВА ВЗРЫВЧАТКА (С4)''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks)  

        def THORN(star):
            Tasks = ['''ИГРАТЬ ТОЛЬКО С M870 (ДРОБОВИК) и C75 AUTO (МИНИ-ПП)''',''''Играешь только с UZK50GI (ПИСТОЛЕТ-ПУЛЕМЕТ) и 1911 TACOPS (ПИСТОЛЕТ)''']
            Star_Tasks = ['''К сожалению на данного опреативника нету заданий со звёздочкой''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks)  

        def AZAMI(star):
            Tasks = ['''ИГРАТЬ ТОЛЬКО С ACS12 (ДРОБОВИК) и D-50 (ПИСТОЛЕТ)''',''''Играешь только с 9X19SVN (ПИСТОЛЕТ-ПУЛЕМЕТ) и D-50 (ПИСТОЛЕТ)''']
            Star_Tasks = ['''УБИТЬ С ПОМОЩЬЮ ДОП. УСТРОЙСТВА УДАРНАЯ ГРАНАТА (ИМПАКТ)''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks)        
    class Attack:

        def SLEDGE(star):
            Tasks = ['''Играешь только с M590A1 (ДРОБОВИК) и P226 MK 25 (ПИСТОЛЕТ)	''','''Играешь только с L85A2 (ШТУРМОВАЯ ВИНТОВКА) без обвесов и P226 MK 25 (ПИСТОЛЕТ)''']
            Star_Tasks = ['''К сожалению на данного опреативника нету заданий со звёздочкой''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks)
                
        def THATCHER(star):
            Tasks = ['''Играешь только с M590A1 (ДРОБОВИК) и P226 MK 25 (ПИСТОЛЕТ)	''','''Играешь только с L85A2 (ШТУРМОВАЯ ВИНТОВКА) без обвесов и P226 MK 25 (ПИСТОЛЕТ)''','''Играешь только с AR33(ШТУРМОВАЯ ВИНТОВКА) без обвесов и P226 MK 25 (ПИСТОЛЕТ)	''']
            Star_Tasks = ['''К сожалению на данного опреативника нету заданий со звёздочкой''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks)

        def ASH(star):
            Tasks = ['''Играешь только с R4-C (ШТУРМОВАЯ ВИНТОВКА) и M45 MEUSOC (ПИСТОЛЕТ)''','''Играешь только с G36C (ШТУРМОВАЯ ВИНТОВКА) без обвесов и 5.7 USG (ПИСТОЛЕТ)''']
            Star_Tasks = ['''К сожалению на данного опреативника нету заданий со звёздочкой''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks)

        def THERMITE(star):
            Tasks = ['''Играешь только с M1014 (ДРОБОВИК) и M45 MEUSOC (ПИСТОЛЕТ)''','''Играешь только с 556XI (ШТУРМОВАЯ ВИНТОВКА) без обвесов и 5.7 USG (ПИСТОЛЕТ)''']
            Star_Tasks = ['''К сожалению на данного опреативника нету заданий со звёздочкой''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks)   

        def TWITCH(star):
            Tasks = ['''Играешь только с F2 (ШТУРМОВАЯ ВИНТОВКА) и P9 (ПИСТОЛЕТ)''','''Играешь только с 417 (СНАЙПЕРСКАЯ ВИНТОВКА) без обвесов и LFP586 (ПИСТОЛЕТ)''','''Играешь только с SG-CQB (ДРОБОВИК) без обвесов и LFP586 (ПИСТОЛЕТ)''']
            Star_Tasks = ['''К сожалению на данного опреативника нету заданий со звёздочкой''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks) 

        def IQ(star):
            Tasks = ['''Играешь только с AUG A2 (ШТУРМОВАЯ ВИНТОВКА) и P12 (ПИСТОЛЕТ)''','''Играешь только с 552 COMMANDO (ШТУРМОВАЯ ВИНТОВКА) без обвесов и P12 (ПИСТОЛЕТ)''','''Играешь только с G8A1 (РУЧНОЙ ПУЛЕМЕТ) без обвесов и P12 (ПИСТОЛЕТ)''']
            Star_Tasks = ['''К сожалению на данного опреативника нету заданий со звёздочкой''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks)        

        def MONTAGNE(star):
            Tasks = ['''Играешь только с P9 (ПИСТОЛЕТ) и Щитом''','''Играешь только с LFP586 (ПИСТОЛЕТ) и Щитом''']
            Star_Tasks = ['''Сделать >1 убийства с Щита''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks)  

        def GLAZ(star):
            Tasks = ['''Играешь только с OTS-03 (СНАЙПЕРСКАЯ ВИНТОВКА) и PMM (ПИСТОЛЕТ)''','''Играешь только с OTS-03 (СНАЙПЕРСКАЯ ВИНТОВКА) и GONNE-6 (ОДНОЗАРЯДНЫЙ ПИСТОЛЕТ)''']
            Star_Tasks = ['''Сделать >1 убийства с доп. устройства (ГРАНАТА)''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks) 

        def FUZE(star):
            Tasks = ['''Играешь только с AK-12 (ШТУРМОВАЯ ВИНТОВКА) и PMM (ПИСТОЛЕТ)''','''Играешь только с 6P41 (РУЧНОЙ ПУЛЕМЕТ) и GONNE-6 (ОДНОЗАРЯДНЫЙ ПИСТОЛЕТ)''','''Играешь только с БАЛЛИСТИЧЕСКИМ ЩИТОМ и GSH-18 (ПИСТОЛЕТ)''']
            Star_Tasks = ['''Сделать >1 убийства с Щита''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks)   

        def BLITZ(star):
            Tasks = ['''Играешь только с G52-TACTICAL SHIELD (БАЛЛИСТИЧЕСКИЙ ЩИТ) и P12 (ПИСТОЛЕТ)''']
            Star_Tasks = ['''Сделать >1 убийства с Щита''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks)                               

        def BUCK(star):
            Tasks = ['''Играешь только с C8-SFW (ШТУРМОВАЯ ВИНТОВКА) и MK1 9MM (ПИСТОЛЕТ)''','''Играешь только с CAMRS SHIELD (СНАЙПЕРСКАЯ ВИНТОВКА) и MK1 9MM (ПИСТОЛЕТ)''']
            Star_Tasks = ['''К сожалению на данного опреативника нету заданий со звёздочкой''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks)        

        def BLACKBEARD(star):
            Tasks = ['''Играешь только с MK17 CQB (ШТУРМОВАЯ ВИНТОВКА) и D-50 (ПИСТОЛЕТ)''','''Играешь только с SR-25 (СНАЙПЕРСКАЯ ВИНТОВКА) и D-50 (ПИСТОЛЕТ)''']
            Star_Tasks = ['''К сожалению на данного опреативника нету заданий со звёздочкой''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks)        

        def CAPITAO(star):
            Tasks = ['''Играешь только с PARA-308 (ШТУРМОВАЯ ВИНТОВКА) и PRB92 (ПИСТОЛЕТ)''','''Играешь только с M249 (РУЧНОЙ ПУЛЕМЕТ) и PRB92 (ПИСТОЛЕТ)''']
            Star_Tasks = ['''Сделать убийство с помощью допю устройства (МИНА)''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks) 

        def HIBANA(star):
            Tasks = ['''Играешь только с TYPE-89 (ШТУРМОВАЯ ВИНТОВКА) и P229 RC (ПИСТОЛЕТ)''','''Играешь только с SUPERNOVA (ДРОБОВИК) и BERING 9 (ПИСТОЛЕТ-ПУДЕМЕТ)''']
            Star_Tasks = ['''К сожалению на данного опреативника нету заданий со звёздочкой''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks)               

        def JACKAL(star):
            Tasks = ['''Играешь только с C7E (ШТУРМОВАЯ ВИНТОВКА) и ITA12S (ДРОБОВИК)''','''Играешь только с PDW9 (ПИСТОЛЕТ-ПУЛЕМЕТ) и ITA12S (ДРОБОВИК)''','''Играешь только с ITA12L (ДРОБОВИК) и USP40 (ПИСТОЛЕТ)''']
            Star_Tasks = ['''Сделать убийство с помощью доп. устройства (МИНА)''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks)

        def YING(star):
            Tasks = ['''Играешь только с T-95 LSW (РУЧНОЙ ПУЛЕМЕТ) и Q-929 (ПИСТОЛЕТ)''','''Играешь только с SIX12 (ДРОБОВИК) и Q-929 (ПИСТОЛЕТ)''']
            Star_Tasks = ['''К сожалению на данного опреативника нету заданий со звёздочкой''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks)

        def ZOFIA(star):
            Tasks = ['''Играешь только с LMG-E (РУЧНОЙ ПУЛЕМЕТ) и RG15 (ПИСТОЛЕТ)''','''Играешь только с M762 (ШТУРМОВАЯ ВИНТОВКА) и RG15 (ПИСТОЛЕТ)''']
            Star_Tasks = ['''Сделать убийство с помощью доп. устройства (МИНА)''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks)

        def DOKKAEBI(star):
            Tasks = ['''Играешь только с MK 14 EBR (СНАЙПЕРСКАЯ ВИНТОВКА) и SMG-12 (МИНИ-ПП)''','''Играешь только с BOSG.12.2 (ДРОБОВИК) и GONNE-6 (ОДНОЗАРЯДНЫЙ ПИСТОЛЕТ)''']
            Star_Tasks = ['''К сожалению на данного опреативника нету заданий со звёздочкой''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks)

        def FINKA(star):
            Tasks = ['''Играешь только с SPEAR .308 (ШТУРМОВАЯ ВИНТОВКА) и PMM (ПИСТОЛЕТ)''','''Играешь только с 6P41 (РУЧНОЙ ПУЛЕМЕТ) и PMM (ПИСТОЛЕТ)''','''Играешь только с SASG-12 (ДРОБОВИК) и GONNE-6 (ОДНОЗАРЯДНЫЙ ПИСТОЛЕТ)''']
            Star_Tasks = ['''К сожалению на данного опреативника нету заданий со звёздочкой''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks)

        def LION(star):
            Tasks = ['''Играешь только с V308 (ШТУРМОВАЯ ВИНТОВКА) и LFP586 (ПИСТОЛЕТ)''','''Играешь только с 417 (СНАЙПЕРСКАЯ ВИНТОВКА) и LFP586 (ПИСТОЛЕТ)''','''Играешь только с SG-CQB (ДРОБОВИК) и GONNE-6 (ОДНОЗАРЯДНЫЙ ПИСТОЛЕТ)''']
            Star_Tasks = ['''К сожалению на данного опреативника нету заданий со звёздочкой''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks)

        def MAVERICK(star):
            Tasks = ['''Играешь только с AR-15.50 (ШТУРМОВАЯ ВИНТОВКА) и 1911 TACOPS (ПИСТОЛЕТ)''','''Играешь только с M4 GS (ШТУРМОВАЯ ВИНТОВКА) и 1911 TACOPS (ПИСТОЛЕТ)''']
            Star_Tasks = ['''УБИТЬ С ПОМОЩЬЮ ДОП. УСТРОЙСТВА (ГРАНАТА)''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks)

        def NOMAD(star):
            Tasks = ['''Играешь только с AK-74M (ШТУРМОВАЯ ВИНТОВКА) и .44 MAG SEMI-AUTO (ПИСТОЛЕТ)''','''Играешь только с ARX200 (ШТУРМОВАЯ ВИНТОВКА) и PRB92 (ПИСТОЛЕТ)''']
            Star_Tasks = ['''К сожалению на данного опреативника нету заданий со звёздочкой''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks)

        def GRIDLOCK(star):
            Tasks = ['''Играешь только с F90 (ШТУРМОВАЯ ВИНТОВКА) и SUPER SHORTY (ДРОБОВИК)''','''Играешь только с M249 SAW (РУЧНОЙ ПУЛЕМЕТ) и GONNE-6 (ОДНОЗАРЯДНЫЙ ПИСТОЛЕТ)''']
            Star_Tasks = ['''К сожалению на данного опреативника нету заданий со звёздочкой''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks)

        def NOKK(star):
            Tasks = ['''Играешь только с FMG-9 (ПИСТОЛЕТ-ПУЛЕМЕТ) и D-50 (ПИСТОЛЕТ)''','''Играешь только с SIX12 SD (ДРОБОВИК) и 5.7 USG (ПИСТОЛЕТ)''']
            Star_Tasks = ['''УБИТЬ С ПОМОЩЬЮ ДОП. УСТРОЙСТВА (ГРАНАТА)''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks)

        def AMARU(star):
            Tasks = ['''Играешь только с G8A1 (РУЧНОЙ ПУЛЕМЕТ) и GONNE-6 (ОДНОЗАРЯДНЫЙ ПИСТОЛЕТ)''','''Играешь только с SUPERNOVA (ДРОБОВИК) и SMG-11 (МИНИ-ПП)''']
            Star_Tasks = ['''К сожалению на данного опреативника нету заданий со звёздочкой''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks)

        def KALI(star):
            Tasks = ['''Играешь только с CSRX 300 (СНАЙПЕРСКАЯ ВИНТОВКА) и SPSMG9 (МИНИ-ПП)''','''Играешь только с CSRX 300 (СНАЙПЕРСКАЯ ВИНТОВКА) и C75 AUTO (МИНИ-ПП)''']
            Star_Tasks = ['''Сделать убийство с помощью доп. устройства (МИНА)''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks)
                
        def IANA(star):
            Tasks = ['''Играешь только с ARX200 (ШТУРМОВАЯ ВИНТОВКА) и GONNE-6 (ОДНОЗАРЯДНЫЙ ПИСТОЛЕТ)''','''Играешь только с G36C (ШТУРМОВАЯ ВИНТОВКА) и MK1 9MM (ПИСТОЛЕТ)''']
            Star_Tasks = ['''УБИТЬ С ПОМОЩЬЮ ДОП. УСТРОЙСТВА (ГРАНАТА)''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks)

        def ACE(star):
            Tasks = ['''Играешь только с AK-12 (ШТУРМОВАЯ ВИНТОВКА) и P9 (ПИСТОЛЕТ)''','''Играешь только с M1014 (ДРОБОВИК) и P9 (ПИСТОЛЕТ)''']
            Star_Tasks = ['''Сделать убийство с помощью доп. устройства (МИНА)''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks)

        def ZERO(star):
            Tasks = ['''Играешь только с SC3000K (ШТУРМОВАЯ ВИНТОВКА) и GONNE-6 (ОДНОЗАРЯДНЫЙ ПИСТОЛЕТ)''','''Играешь только с MP7 (ПИСТОЛЕТ-ПУЛЕМЕТ) и 5.7 USG (ПИСТОЛЕТ)''']
            Star_Tasks = ['''Сделать убийство с помощью доп. устройства (МИНА)''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks)

        def FLORES(star):
            Tasks = ['''Играешь только с AR33 (ШТУРМОВАЯ ВИНТОВКА) и GSH-18 (ПИСТОЛЕТ)''','''Играешь только с SR-25 (СНАЙПЕРСКАЯ ВИНТОВКА) и GSH-18 (ПИСТОЛЕТ)''']
            Star_Tasks = ['''Сделать убийство с помощью доп. устройства (МИНА)''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks)    

        def OSA(star):
            Tasks = ['''Играешь только с 556XI (ШТУРМОВАЯ ВИНТОВКА) и PMM (ПИСТОЛЕТ)''','''Играешь только с PDW9 (ПИСТОЛЕТ-ПУЛЕМЕТ) и PMM (ПИСТОЛЕТ)''']
            Star_Tasks = ['''Сделать убийство с помощью доп. устройства (МИНА)''']
            if star == 1:
                return choice(Star_Tasks)
            elif star == 2:
                return choice(Tasks)