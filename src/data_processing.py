import pandas as pd
import pdb 

SYMPTOMS = [
    "Heavy / Extreme menstrual bleeding",
    "Menstrual pain (Dysmenorrhea)",
    "Painful / Burning pain during sex (Dyspareunia)",
    "Pelvic pain",
    "Irregular / Missed periods",
    "Cramping",
    "Abdominal pain / pressure",
    "Back pain",
    "Painful bowel movements",
    "Nausea",
    "Menstrual clots",
    "Infertility",
    "Painful cramps during period",
    "Pain / Chronic pain",
    "Diarrhea",
    "Long menstruation",
    "Constipation / Chronic constipation",
    "Vomiting / constant vomiting",
    "Fatigue / Chronic fatigue",
    "Painful ovulation",
    "Stomach cramping",
    "Migraines",
    "Extreme / Severe pain",
    "Leg pain",
    "Irritable Bowel Syndrome (IBS)",
    "Syncope (fainting, passing out)",
    "Mood swings",
    "Depression",
    "Bleeding",
    "Lower back pain",
    "Fertility Issues",
    "Ovarian cysts",
    "Painful urination",
    "Headaches",
    "Constant bleeding",
    "Pain after Intercourse",
    "Digestive / GI problems",
    "IBS-like symptoms",
    "Excessive bleeding",
    "Anaemia / Iron deficiency",
    "Hip pain",
    "Vaginal Pain/Pressure",
    "Sharp / Stabbing pain",
    "Bowel pain",
    "Anxiety",
    "Cysts (unspecified)",
    "Dizziness",
    "Malaise / Sickness",
    "Abnormal uterine bleeding",
    "Fever",
    "Hormonal problems",
    "Bloating",
    "Feeling sick",
    "Decreased energy / Exhaustion",
    "Abdominal Cramps during Intercourse",
    "Insomnia / Sleeplessness",
    "Acne / pimples",
    "Loss of appetite",
]

MACROS_SYMPTOMS = {
    "DIGESTIVE": [
        "Painful bowel movements",
        "Nausea",
        "Diarrhea",
        "Constipation / Chronic constipation",
        "Vomiting / constant vomiting",
        "Painful ovulation",
        "Stomach cramping",
        "Irritable Bowel Syndrome (IBS)",
        "Digestive / GI problems",
        "IBS-like symptoms",
        "Bowel pain",
        "Bloating",
        "Loss of appetite",
    ],
    "PERIODS": [
        "Heavy / Extreme menstrual bleeding",
        "Menstrual pain (Dysmenorrhea)",
        "Irregular / Missed periods",
        "Menstrual clots",
        "Painful cramps during period",
        "Long menstruation",
    ],
    "SKIN": ["Acne / pimples"],
    "BLOOD": [
        "Bleeding",
        "Constant bleeding",
        "Excessive bleeding",
        "Anaemia / Iron deficiency",
        "Abnormal uterine bleeding",
    ],
    "SEXUAL": [
        "Painful / Burning pain during sex (Dyspareunia)",
        "Pain after Intercourse",
        "Abdominal Cramps during Intercourse",
    ],
    "MSK": ["Cramping", "Back pain", "Leg pain", "Lower back pain", "Hip pain"],
    "MENTAL HEALTH": ["Mood swings", "Depression"],
    "HORMONAL": ["Hormonal problems"],
    "OTHER PAINS": [
        "Pelvic pain",
        "Abdominal pain / pressure",
        "Pain / Chronic pain",
        "Extreme / Severe pain",
        "Painful urination",
        "Vaginal Pain/Pressure",
        "Sharp / Stabbing pain",
        "Cysts (unspecified)",
    ],
    "REPRODUCTIVE": [
        "Infertility",
        "Fertility Issues",
        "Ovarian cysts",
    ],
    "SICKNESS / ENERGY": [
        "Fatigue / Chronic fatigue",
        "Migraines",
        "Syncope (fainting, passing out)",
        "Headaches",
        "Dizziness",
        "Malaise / Sickness",
        "Fever",
        "Feeling sick",
        "Decreased energy / Exhaustion",
        "Insomnia / Sleeplessness",
    ],
}

def prepare_data():
    data = pd.read_excel("../data/dataset.xlsx")

    y = data["label"].values
    data = data.drop(data.columns[0], axis=1)  # remove first columns
    data = data.drop(["row"], axis=1)
    # remove symptoms with less than 20 datapoints 
    for column in data.columns:
        if data[column].sum() < 20:
            data = data.drop([column])
    return data


def create_macros_symptoms(data):
    
    data = data.drop(columns=["label"])
    df = data.copy()
    for macro_symptom, ls_symptoms in MACROS_SYMPTOMS.items():
        df[macro_symptom] = (data[ls_symptoms].sum(1)>0).astype(int)
    return df     


if __name__ == "__main__":

    data = prepare_data()
    create_macros_symptoms(data)
