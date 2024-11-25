from langchain_google_vertexai import VertexAIEmbeddings
import configparser

configuration = configparser.ConfigParser()
configuration.read('config.ini')

embeddings = VertexAIEmbeddings(model=configuration['EMBEDDING']['model'])

def main():
    pass

if __name__=="__main__":
    main()