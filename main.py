from utility.data_loader import DataLoader
from algoRepository.algos_de import AlgosDE
from algoRepository.algos_multi import AlgosMulti
from algoRepository.algos_eng import AlgosENG


def run():
    #Google API key see: https://developers.google.com/codelabs/setup-perspective-api?hl=de#0
    API_KEY = ''

    #csv with a 'text' column
    input_file = DataLoader.load_file_csv("data/INPUT.csv")

    #set name to algorithm tested
    name_output = 'XX.csv'

    AlgosMulti.annotate_robaconfi(input_file, 'a.csv')
    AlgosMulti.annotate_xlm_Roberta_Large(input_file,'b.csv')


    #ENG

    #AlgosENG.annotate_IMSyPP(input_file, name_output)

    #AlgosENG.annotate_roberta(input_file,name_output)

    #AlgosENG.annotate_google_jigsaw(input_file, name_output, API_KEY)


    #DE

    #AlgosDE.annotate_google_jigsaw(input_file, name_output, API_KEY)


    # Multi (DE, ENG +)

    #AlgosMulti.annotate_robaconfi(input_file, name_output)

    #AlgosMulti.annotate_xlm_Roberta_Large(input_file, name_output)



if __name__ == '__main__':
    run()
