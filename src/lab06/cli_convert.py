import argparse
import sys
sys.path.append(r'C:\Users\First\Documents\GitHub\python_labs\src')
from lab05.json_csv import json_to_csv, csv_to_json
from lab05.csv_xlsx import csv_to_xlsx

def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd")

    p1 = sub.add_parser("json2csv")
    p1.add_argument("--in", dest="input", required=True, help="Входной файл json")
    p1.add_argument("--out", dest="output", required=True, help="Выходной файл csv")

    p2 = sub.add_parser("csv2json")
    p2.add_argument("--in", dest="input", required=True, help="Входной файл csv")
    p2.add_argument("--out", dest="output", required=True, help="Выходной файл json")

    p3 = sub.add_parser("csv2xlsx")
    p3.add_argument("--in", dest="input", required=True, help="Входной файл csv")
    p3.add_argument("--out", dest="output", required=True, help="Выходной файл xlsx")

    try:
        args = parser.parse_args()

        if args.cmd == "json2csv":
            """Конвертация файла json в csv"""
            json_to_csv(args.input, args.output)
        elif args.cmd == "csv2json":
            """Конвертация файла csv в json"""
            csv_to_json(args.input, args.output)
        elif args.cmd == "csv2xlsx":
            "Конвертация файда csv в xlsx"
            csv_to_xlsx(args.input, args.output)
    except FileNotFoundError:
        print(f"FileNotFoundError: Отсутствие входного файла {args.input}")
    except SystemExit:
        print("\nИсправьте аргументы и попробуйте снова")
        sys.exit(1)

if __name__=="__main__":
    main()
