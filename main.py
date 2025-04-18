import sys
from stats import num_words
from stats import dic_count_chars
from stats import dicsList
from stats import sort_on_CharDicList




def main():
    #path = "books/frankenstein.txt"
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    book_path = sys.argv[1]
    text = get_book_text(path)
    word_count = num_words(text)
    char_dic = dic_count_chars(text)
    char_dicS_List = dicsList(char_dic)
    reportSort = sort_on_CharDicList(char_dicS_List)


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...") # type: ignore
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in reportSort:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['count']}")
    print("============= END ===============")

    
    



def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()





#OLD main for bootdotdev_ch2_l6
'''def main():
    # Use the relative path to your frankenstein.txt file
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    
    word_count = num_words(text)
    print(f"{word_count} words found in the document")
    
    char_dic = count_chars(text)
    print (char_dic)
'''







# CALL main() at the BOTTOM of your file!!!
main()


    
