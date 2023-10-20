def apply_production_rule(symptoms, rule_conditions, disease):
    if all(condition in symptoms for condition in rule_conditions):
        return disease
    return None


def diagnose(symptoms):
    knowledge_base = {
        "Грип": (["температура 38", "кашель"], "Лікування грипу"),
        "Застуда": (["нежить", "кашель", "ненормальна втомлюваність"], "Лікування застуди"),
        "Ангіна": (["біль в горлі", "збільшені мигдалики"], "Лікування ангіни"),
        "Бронхіт": (["кашель", "проблеми з диханням"], "Лікування бронхіту"),
        "Алергія": (["сльози", "чхання"], "Лікування алергії"),
    }

    possible_diagnoses = []
    for disease, (conditions, treatment) in knowledge_base.items():
        result = apply_production_rule(symptoms, conditions, disease)
        if result:
            possible_diagnoses.append((disease, treatment))

    return possible_diagnoses


def main():
    print("Ласкаво просимо до експертної системи діагностики захворювань.")
    symptoms = []
    while True:
        symptom = input("Введіть симптом (або натисніть Enter, щоб завершити введення симптомів): ")
        if not symptom:
            break
        symptoms.append(symptom)

    if not symptoms:
        print("Не введено жодного симптому.")
    else:
        result = diagnose(symptoms)
        if result:
            print("Можливі діагнози та лікування:")
            for disease, treatment in result:
                print(f"{disease}: {treatment}")
        else:
            print("Захворювання не визначено.")


if __name__ == "__main__":
    main()
