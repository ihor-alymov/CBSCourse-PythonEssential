class Editor:
    """Базовий клас редактора документів.

    Надає базову функціональність для перегляду документів.
    Редагування обмежене в безкоштовній версії.
    """

    document = None

    def __init__(self, name: str = "Безкоштовний редактор"):
        """Ініціалізує редактор з назвою.

        Args:
            name: Назва редактора
        """
        self.name = name

    def view_document(self, document):
        print(f"{self.name}\n{document.__str__()}")

    def edit_document(self, _):
        """Спроба редагування документу.

        У безкоштовній версії редагування недоступне.
        """
        print(f"[{self.name}] ❌ Редагування документів недоступне для безкоштовної версії.")


class ProEditor(Editor):
    """Професійна версія редактора з повним функціоналом.

    Розширює базовий клас Editor додаючи можливість редагування документів.
    """

    def __init__(self):
        """Ініціалізує Pro-редактор.

        """
        super().__init__("Pro редактор")

    def edit_document(self, document):
        """Редагування документу в Pro-версії.

        Надає повний доступ до редагування документів.
        """
        print(f"[{self.name}] ✅ Документ відкрито для редагування.")


def validate_license_key(key: str):
    """Перевіряє валідність ліцензійного ключа.

    Args:
        key: Ліцензійний ключ для перевірки

    Returns:
        True якщо ключ валідний, False в іншому випадку
    """
    # Список валідних ліцензійних ключів
    valid_keys = [
        "PRO-2024-PYTHON",
        "EDITOR-PREMIUM-KEY",
        "CBS-COURSE-LICENSE"
    ]

    return key.strip().upper() in valid_keys


def create_editor():
    """Створює відповідний екземпляр редактора на основі ліцензійного ключа.

    Returns:
        Екземпляр Editor або ProEditor залежно від валідності ліцензійного ключа
    """
    try:
        print("Ласкаво просимо до системи редагування документів!")
        print("=" * 60)

        license_key = input("Введіть ліцензійний ключ (або натисніть Enter для безкоштовної версії): ").strip()

        if not license_key:
            print("\n🆓 Використовується безкоштовна версія редактора.")
            return Editor()

        if validate_license_key(license_key):
            print(f"\n✅ Ліцензійний ключ '{license_key}' підтверджено!")
            print("🎉 Активовано Pro-версію редактора!")
            return ProEditor()
        else:
            print(f"\n❌ Ліцензійний ключ '{license_key}' недійсний.")
            print("🆓 Використовується безкоштовна версія редактора.")
            return Editor()

    except KeyboardInterrupt:
        print("\n\nПрограму перервано користувачем.")
    except Exception as e:
        print(f"\nПомилка при створенні редактора: {e}")


def main():
    document = "Тестовий документ для демонстраціі редактора."

    try:
        # Створення відповідного редактора
        editor = create_editor()

        print("\n" + "=" * 60)
        print("ДЕМОНСТРАЦІЯ РОБОТИ РЕДАКТОРА")
        print("=" * 60)

        # Демонстрація перегляду документу
        print("\n1. Перегляд документу:")
        print("-" * 30)
        editor.view_document(document)

        # Демонстрація редагування документу
        print("\n2. Спроба редагування документу:")
        print("-" * 40)
        editor.edit_document(document)

        print("\n" + "=" * 60)
        print("Дякуємо за використання нашого редактора!")

    except Exception as e:
        print(f"Критична помилка в програмі: {e}")


if __name__ == "__main__":
    # Інформація про валідні ліцензійні ключі для тестування
    print("💡 Підказка: Валідні ліцензійні ключі для тестування:")
    print("   - PRO-2024-PYTHON")
    print("   - EDITOR-PREMIUM-KEY")
    print("   - CBS-COURSE-LICENSE")
    print()

    main()