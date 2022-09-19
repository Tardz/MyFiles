#!/usr/bin/env python3
"""
Unit testing for lab 4 built on the unittest module.

Note:
If you have downloaded the scripts from the website it might not
have the access right. To solve this run:
$ chmod +x <path_to_test_4.py>

Usage (case insensitive for parameters to --test):
$ ./test_4.py --test a <path_to_lab>
to test lab 4A
$ ./test_4.py --test b <path_to_lab>
to test lab 4B
$ ./test_4.py <path_to_lab>
to test whole lab 4

Initial version by Erik Hansson <erik.b.hansson@liu.se>
Updated for TDDE23 by Frans Skarman <frask812@student.liu.se>

Changelog:
 * 31/8-2016: Updated the printed traceback in case that the given file
   can not be imported.
 * 11/10-2019: Add more tests to avoid getting incorrect solutions.
 * 18/12-2019: Follow PEP8/PEP257
"""


from argparse import ArgumentParser
from importlib.machinery import SourceFileLoader
import sys
from traceback import format_exc
from copy import deepcopy


def is_same_list(a, b):
    """
    Check if two lists have the same values
    and nested lists.
    """
    if not isinstance(a, list) or not isinstance(b, list):
        return a == b

    for a_elem, b_elem in zip(a, b):
        if isinstance(a_elem, list) or isinstance(b_elem, list):
            if not is_same_list(a_elem, b_elem):
                return False
        else:
            if not a == b:
                return False
    return True


def is_same_dict(a, b):
    """
    Check if two dictionaries have the same
    elements in them.
    """

    def equality(key):
        return key in a and key in b and a[key] == b[key]

    return all(map(equality, a.keys())) and all(map(equality, b.keys()))


message_a = [
    "hTEeSj_CO",
    "'lMiED)teD5E,_hLAe;Nm,0@Dli&Eg ,#4aI?rN@T§&e7#4E #<(S0A?<)NT8<0'",
    "fTlH-yE((g 48aQnUdI#5eC_K§b 29äB>cRkO7-aW-0sN#i 0>nFeOrX=!_ =!sJöUkM1aP(>"
    "_Sh wOiV,lE4aR3_ pTåH_Em jLuA§kZ`aY>_ @tDuO5vGo$r1",
    "vJ4&eO1m _E`äNr #!_S´-dÄ=eR+nD!-nE1eL>?_EtS+e <$sK9#cLoO_Ka lK6(lAaT9;_T;"
    "t>a0l1´&a76?r$_15o,m§",
    "WhEa'n<=R_´Ek o§Nm&O_,7 s!So1TmR_%Ae%Nt#@GtE_/Ry`2Sr>! v*;Tä>Od<< eLr44O_"
    "Ve0En)|_/+ a6YpOrUi/& lKa9Nf§Ot<Wo$ n1*T_8Ho`7Ec/= hR_?0Uh0La8<EdSe32 _`1"
    "Ae%0Nt*Dt _35ShOö2 gDaOn ä,Is|k rAu; s>$F_7UiL_@Le8 n&C_`%Os;Mv6+Må2In+Tg"
    "<<Mr=5Ee,Nm+T_&'oSm _0(Wh#HaAl*5Ts e5In5'.M_`? c&>Tl,Ha@5IrNa9(K_Io#$Nc$?"
    "Gh5 _5?OlFo!|t tYeOnU_? vWoOr(´Uo34L_)Di>Nn(3'n6@Te?> _=Gm#2Ee;Td§$ _7Ts,"
    "HkIö>St! e#Fk3Ra0On=M_ a%At!)Nt!8Y_? hOäTm%1Ht74Ea+R_8; hGo=Un-*Yo)|m´& _"
    "<§Ip&4 åJ_UdSa=´Tl% a-+Wr)AöN_Nb=5Ar yTg)Eg4LaL; _Ym7Oe&Un _3§Hd/Oe%8Wt5 "
    "_Id-3'r=/Mö j?!FdEe1E_Le73IvNiGg?1|h<% e´(Gt@*Oe,Tr%T,A_ iMn6An`§Ka2En3! "
    "_47Yd5´OeU_ k@Uo-NmDmEo%R_SiT_&<Ab)NåDt69|.",
    "+Y_8O&d5§(Uon5 A'`LtL7_ §bS5e_T3sI>oLL_ haH(Ar´=dV7E_o+ >Zn´§_OI2$yDo1*uB"
    "0E6rsReG4#!l3#f ,7_1*/f´ry.2_y!8`o-u§?;9_lo-5st-_/´§*t4*h8;e_)46w>om/=a;n"
    "-78_7o8f$_*y`/o7u3r;_>d`0#7r$§-e>am´@,s,&$<_(;=bu42t1_`3yo;<u_s>5=t`i´0l("
    "l(_1h,@a$4*v3/61e_z>6o=3i#d@ber(0g<-.",
]

expected_a = [
    ("hej_", "TESCO"),
    ("lite_hemligare", "MEDDELANDE INTE SANT"),
    (
        "flygande_bäckasiner_söka_hwila_på_mjuka_tuvor",
        "THE QUICK BROWN FOX JUM" "PS OVER THE LAZY DOG",
    ),
    ("vem_är_denne_tesco_alla_talar_om", "JO EN SÄRDELES KLOK KATT"),
    (
        "han_kom_som_ett_yrväder_en_aprilafton_och_hade_ett_höganäskrus_i_en_svån"
        "grem_om_halsen._clara_och_lotten_voro_inne_med_skötekan_att_hämta_honom_"
        "på_dalarö_brygga_men_det_dröjde_evigheter_innan_de_kommo_i_båt.",
        "WERE "
        "NO STRANGERS TO LOVE| YOU KNOW THE RULES AND SO DO I| A FULL COMMITMENTS"
        " WHAT IM THINKING OF| YOU WOULDNT GET THIS FROM ANY OTHER GUY| I JUST WA"
        "NNA TELL YOU HOW IM FEELING| GOTTA MAKE YOU UNDERSTAND|",
    ),
    (
        "_dont_be_so_hard_on_yourself_fry._you_lost_the_woman_of_your_dreams_but_"
        "you_still_have_zoidberg.",
        "YOU ALL STILL HAVE ZOIDBERG ",
    ),
]


def test_split_it():
    """
    Tests the split_it function
    """
    for msg, expected in zip(message_a, expected_a):
        assert (
            lab4.split_it(msg) == expected
        ), '\nsplit_it("{}"):\nexpected: {}\ngot: {}'.format(
            msg, str(expected), str(lab4.split_it(msg))
        )


def test_split_rec():
    """
    Tests the split_rec function
    """
    for msg, expected in zip(message_a, expected_a):
        assert (
            lab4.split_rec(msg) == expected
        ), '\nsplit_it("{}"):\nexpected: {}\ngot: {}'.format(
            msg, str(expected), str(lab4.split_rec(msg))
        )


def test_interpret_wrapper(expr, defs, expected):
    backup_expr = deepcopy(expr)
    backup_defs = defs.copy()
    result = lab4.interpret(expr, defs)
    assert (
        result == expected
    ), '''interpret({}, {}):\nexpected: "{}"\ngot: "{}"'''.format(
        backup_expr, backup_defs, expected, result
    )
    assert is_same_list(expr, backup_expr), "Not allowed to modify arguments."
    assert is_same_dict(defs, backup_defs), "Not allowed to modify arguments."


def test_interpret():
    """
    Tests the interpret function
    """
    test_interpret_wrapper(
        ["door_open", "AND", "cat_gone"],
        {"door_open": "false", "cat_gone": "true", "cat_asleep": "true"},
        "false",
    )
    test_interpret_wrapper(
        ["cat_asleep", "OR", ["NOT", "cat_gone"]],
        {"door_open": "false", "cat_gone": "true", "cat_asleep": "true"},
        "true",
    )
    test_interpret_wrapper(["true", "OR", "true"], {}, "true")
    test_interpret_wrapper(
        "cat_gone", {"door_open": "false", "cat_gone": "true"}, "true"
    )
    test_interpret_wrapper(
        ["NOT", ["NOT", ["NOT", ["cat_asleep", "OR", ["NOT", "cat_asleep"]]]]],
        {"cat_asleep": "false"},
        "false",
    )
    test_interpret_wrapper(["NOT", "AND", "OR"], {"NOT": "true", "OR": "true"}, "true")

    test_interpret_wrapper(["NOT", "true"], {"NOT": "false"}, "false")
    test_interpret_wrapper(["NOT", "NOT"], {"NOT": "false"}, "true")
    test_interpret_wrapper(["NOT", "AND"], {"AND": "false"}, "true")
    test_interpret_wrapper(["AND", "AND", "AND"], {"AND": "true"}, "true")
    test_interpret_wrapper("true", {"cat_gone": "false"}, "true")
    test_interpret_wrapper([["true", "OR", "false"], "AND", "true"], {}, "true")

    test_interpret_wrapper(["true", "OR", "true"], {}, "true")
    test_interpret_wrapper(["false", "OR", "true"], {}, "true")
    test_interpret_wrapper(["true", "OR", "false"], {}, "true")
    test_interpret_wrapper(["false", "OR", "false"], {}, "false")

    test_interpret_wrapper(["true", "AND", "true"], {}, "true")
    test_interpret_wrapper(["false", "AND", "true"], {}, "false")
    test_interpret_wrapper(["true", "AND", "false"], {}, "false")
    test_interpret_wrapper(["false", "AND", "false"], {}, "false")


if __name__ == "__main__":
    arg_parser = ArgumentParser()
    arg_parser.add_argument(
        "--test", choices=["a", "A", "b", "B"], default="", required=False
    )
    arg_parser.add_argument("file")
    args = arg_parser.parse_args()
    if args.file.rfind("/") != -1:
        sys.path.append(args.file[: args.file.rfind("/")])
        potential_name = args.file[args.file.rfind("/") + 1 :]
    else:
        sys.path.append(".")
        potential_name = args.file
    if potential_name.rfind("."):
        name = potential_name[: potential_name.rfind(".")]
    else:
        name = potential_name
    try:
        lab4 = SourceFileLoader(name, args.file).load_module()
    except FileNotFoundError:
        print("Could not import lab: " + args.file)
        print("See traceback for further information:")
        print()
        stack_trace = format_exc().split("\n")
        importlib_has_started = False
        importlib_has_ended = False
        for line in stack_trace:
            if (
                not importlib_has_ended
                and importlib_has_started
                and line.lstrip().startswith("File")
                and "importlib" not in line
            ):
                importlib_has_ended = True
            if importlib_has_ended:
                print(line)
            elif (
                not importlib_has_started
                and line.lstrip().startswith("File")
                and "importlib" in line
            ):
                importlib_has_started = True
        exit(1)
    if args.test.upper() == "A":
        test_split_it()
        test_split_rec()
    elif args.test.upper() == "B":
        test_interpret()
    elif args.test == "":
        test_split_it()
        test_split_rec()
        test_interpret()
    else:
        print("Unknown arguemnt for --test: " + args.test)
        exit(2)
    print("The code passed all the tests")
