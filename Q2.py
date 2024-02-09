import os
import pickle

def create_inverted_index(folder_path):
    inverted_index = {}
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                for word in file.read().split():
                    if word in inverted_index:
                        inverted_index[word].append(filename)
                    else:
                        inverted_index[word] = [filename]
    return inverted_index

folder_path = '/Users/mj/Desktop/Work/Sem6/IR/IRAssignment/newtextfiles'
inverted_index = create_inverted_index(folder_path)
with open('inverted_index.pkl', 'wb') as outfile:
    pickle.dump(inverted_index, outfile)
with open('inverted_index.pkl', 'rb') as infile:
    loaded_inverted_index = pickle.load(infile)

def query_and(doc_list1, doc_list2):

    return list(set(doc_list1).intersection(set(doc_list2)))

def query_or(doc_list1, doc_list2):
    return list(set(doc_list1) | set(doc_list2))

def query_and_not(doc_list1, doc_list2):
    return list(set(doc_list1) - set(doc_list2))

def query_or_not(doc_list1, doc_list2, all_docs):
    return list((set(all_docs) - set(doc_list2)) | set(doc_list1))

def execute_query(inverted_index, query_terms, operations):
    result = inverted_index.get(query_terms[0], [])
    result = list(set(result))
    all_docs = [file for file in inverted_index.values() for file in file]
    all_docs = list(set(all_docs))
  
    for i, operation in enumerate(operations):

        next_term_docs = inverted_index.get(query_terms[i + 1], [])
        next_term_docs = list(set(next_term_docs))
    
        if operation == 'AND' or operation == 'and':
            result = query_and(result, next_term_docs)
        elif operation == 'OR' or operation == 'or':
            result = query_or(result, next_term_docs)
        elif operation == 'AND NOT' or operation == 'and not':
            result = query_and_not(result, next_term_docs)
        elif operation == 'OR NOT' or operation == 'or not':
            result = query_or_not(result, next_term_docs, all_docs)
    return result

with open('inverted_index.pkl', 'rb') as infile:
    inverted_index = pickle.load(infile)


def main():
    N = int(input("Enter number of queries: "))
    for i in range(N):
        query = input("Enter query: ")
        operations = input("Enter operations: ").split(', ')
        
        preprocessed_query = preprocess_text(query)
    
        query_terms = preprocessed_query.split() 
    
        results = execute_query(inverted_index, query_terms, operations)
        results = sorted(results)
        
        print(f"Query {i+1}: {' '.join([query_terms[0]] + [op + ' ' + term for op, term in zip(operations, query_terms[1:])])}")
        print(f"Number of documents retrieved for query {i+1}: {len(results)}")
        print(f"Names of the documents retrieved for query {i+1}: {', '.join(results)}")

if __name__ == "__main__":
    main()
