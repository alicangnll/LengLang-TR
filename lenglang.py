import sys, subprocess, argparse

from lexer import *
import tokens

from parser import *
import rules

from code_gen import *

class NoMainFunctionException(Exception):
    def __str__(self): return "No \"int main()\" function found."

if __name__=="__main__":


    parser = argparse.ArgumentParser(description='LengLang v2 Compiler.')


    parser.add_argument('input', metavar='input_file',
                        type=argparse.FileType('r'), help="lng dosyasını derle")


    parser.add_argument('-o', metavar='output_file', dest='output',
                        help="çıktı dosyası oluştur")


    parser.add_argument('-S', dest='asm_only', action='store_const', const=True,
                        default=False, help="sadece asm dosyası oluştur")
    args = parser.parse_args()

    try:

        program_text = args.input.read()
    except:
        print("Giriş Dosyası Oluşturulamadı.")
    else:

        try:
            token_list = tokenize(program_text, tokens.prims)
        except TokenException as e:
            print(e)
            sys.exit(1)
        else:
            try:


                parse_root = generate_tree(token_list, rules.rules, rules.S,
                                           tokens.comment_start,
                                           tokens.comment_end,
                                           add_rule = rules.E_add,
                                           neg_rule = rules.E_neg,
                                           mult_rule = rules.E_mult,
                                           pointer_rule = rules.E_point,
                                           dec_sep_rule = rules.declare_separator_base,
                                           dec_exp_symbol = rules.declare_expression)
            except ParseException as e: 
                print(e)
                sys.exit(1)
            else:
                try:

                    code = CodeManager()
                    info = StateInfo()


                    info = make_code(parse_root, info, code)


                    mainfunc = info.get_func("main")
                    if mainfunc["args"] or mainfunc["ftype"] != Type("int", 0): raise NoMainFunctionException()


                    complete_code = code.get_code(mainfunc["label"])
                except (RuleGenException,
                        VariableRedeclarationException,
                        VariableNotDeclaredException,
                        NoMainFunctionException) as e:


                    print(e)
                    sys.exit(1)
                else:
                    try:

                        if args.output: output_name = args.output
                        else: output_name = args.input.name.split(".")[0]

                        g = open(output_name + ".s", "w")
                    except:
                        print("ASM Dosyası Oluşturulamadı.")
                    else:


                        g.write(complete_code)
                        g.close()

                        print("Derleme Tamamlandı.")



                        if not args.asm_only:
                            subprocess.call(["nasm", "-f", "macho64", output_name + ".s"])
                            subprocess.call(["ld", output_name + ".o", "-o", output_name])
                            print("Bitti.")
    finally:
        args.input.close()
