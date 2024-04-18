from bintrees import FastRBTree


class Dictionary:
    def __init__(self):
        self.dictionary = FastRBTree()
        self.popularity_counter = {}

    def add_translation(self, word, translation):
        if word in self.dictionary:
            self.dictionary[word].add(translation)
        else:
            self.dictionary[word] = {translation}
        self.update_popularity(word)

    def remove_translation(self, word, translation):
        if word in self.dictionary:
            self.dictionary[word].discard(translation)
            if not self.dictionary[word]:
                del self.dictionary[word]

    def add_word(self, word, translations):
        if word not in self.dictionary:
            self.dictionary[word] = translations
            for translation in translations:
                self.update_popularity(translation)

    def remove_word(self, word):
        if word in self.dictionary:
            translations = self.dictionary[word]
            del self.dictionary[word]
            for translation in translations:
                self.update_popularity(translation, increment=-1)

    def update_popularity(self, word, increment=1):
        self.popularity_counter[word] = self.popularity_counter.get(word, 0) + increment

    def top_popular_words(self, n=10):
        return sorted(self.popularity_counter, key=lambda x: self.popularity_counter[x], reverse=True)[:n]

    def top_unpopular_words(self, n=10):
        return sorted(self.popularity_counter, key=lambda x: self.popularity_counter[x])[:n]

    def show_word_translations(self, word):
        if word in self.dictionary:
            print(f"Переклади слова '{word}': {', '.join(self.dictionary[word])}")
            translations = self.dictionary[word]
            for translation in translations:
                self.update_popularity(translation, increment=+1)
        else:
            print(f"Слово '{word}' не знайдено в словнику.")

    def show_all_words(self):
        print("Словник:")
        for word, translations in self.dictionary.items():
            print(f"{word}: {', '.join(translations)}")


def main():
    initial_dictionary = {
        "apple": {"яблуко", "яблука"},
        "orange": {"апельсин", "апельсини"},
        "banana": {"банан"},
        "pear": {"груша"},
        "grape": {"виноград", "виноградина"}
    }

    dictionary = Dictionary()
    for word, translations in initial_dictionary.items():
        dictionary.add_word(word, translations)

    while True:
        print("\nМеню:")
        print("1. Додати переклад слова")
        print("2. Видалити переклад слова")
        print("3. Додати слово")
        print("4. Видалити слово")
        print("5. Показати переклади слова")
        print("6. Показати всі слова у словнику")
        print("7. Показати топ-10 популярних слів")
        print("8. Показати топ-10 непопулярних слів")
        print("0. Вихід")

        choice = input("Виберіть операцію: ")

        if choice == "1":
            word = input("Введіть слово: ")
            translation = input("Введіть переклад: ")
            dictionary.add_translation(word, translation)
        elif choice == "2":
            word = input("Введіть слово: ")
            translation = input("Введіть переклад: ")
            dictionary.remove_translation(word, translation)
        elif choice == "3":
            word = input("Введіть слово: ")
            translations = input("Введіть переклади (через кому): ").split(',')
            dictionary.add_word(word, translations)
        elif choice == "4":
            word = input("Введіть слово: ")
            dictionary.remove_word(word)
        elif choice == "5":
            word = input("Введіть слово: ")
            dictionary.show_word_translations(word)
        elif choice == "6":
            dictionary.show_all_words()
        elif choice == "7":
            print("Топ-10 популярних слів:", dictionary.top_popular_words())
        elif choice == "8":
            print("Топ-10 непопулярних слів:", dictionary.top_unpopular_words())
        elif choice == "0":
            print("Програма завершена.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
