stammbaum = {
    "Kinder": ["Tim Schneider", "Ina Schneider"],
    "Eltern": {
        "Vater": {
            "Name": "Rene Schneider",
            "Eltern": {
                "Vater": {
                    "Name": "Karl Schneider",
                    "Eltern": {
                        "Vater": {
                            "Name": "Wilhelm Schneider",
                            "Eltern": {
                                "Vater": "Johann Schneider",
                                "Mutter": "Elisabeth Schneider"
                            }
                        },
                        "Mutter": {
                            "Name": "Martha Schneider",
                            "Eltern": {
                                "Vater": "Friedrich Bauer",
                                "Mutter": "Anna Bauer"
                            }
                        }
                    }
                },
                "Mutter": {
                    "Name": "Greta Schneider",
                    "Eltern": {
                        "Vater": {
                            "Name": "Ernst Müller",
                            "Eltern": {
                                "Vater": "Heinrich Müller",
                                "Mutter": "Paula Müller"
                            }
                        },
                        "Mutter": {
                            "Name": "Hilde Müller",
                            "Eltern": {
                                "Vater": "Otto Weber",
                                "Mutter": "Else Weber"
                            }
                        }
                    }
                }
            }
        },
        "Mutter": {
            "Name": "In Huankanueng",
            "Eltern": {
                "Vater": {
                    "Name": "Somchai Huankanueng",
                    "Eltern": {
                        "Vater": {
                            "Name": "Prasit Huankanueng",
                            "Eltern": {
                                "Vater": "Krit Huankanueng",
                                "Mutter": "Malee Huankanueng"
                            }
                        },
                        "Mutter": {
                            "Name": "Suda Huankanueng",
                            "Eltern": {
                                "Vater": "Boonsri Jittapong",
                                "Mutter": "Nok Jittapong"
                            }
                        }
                    }
                },
                "Mutter": {
                    "Name": "Malee Kanchana",
                    "Eltern": {
                        "Vater": {
                            "Name": "Chai Kanchana",
                            "Eltern": {
                                "Vater": "Sakda Kanchana",
                                "Mutter": "Urai Kanchana"
                            }
                        },
                        "Mutter": {
                            "Name": "Orn Kanchana",
                            "Eltern": {
                                "Vater": "Manop Srithong",
                                "Mutter": "Pim Srithong"
                            }
                        }
                    }
                }
            }
        }
    }
}
# 2. Hilfsfunktion, falls ein Name als String kommt
def vort_setze_namen_feld(eingabe):
    if isinstance(eingabe, str):
        return {"Name": eingabe}
    return eingabe
def zeige_stammbaum(person, ebene=0):
    einrueckung = "    " * ebene
    if isinstance(person, dict):
        for schluessel, wert in person.items():
            if schluessel == "Name":
                print(f"{einrueckung}- {wert}")
            elif schluessel == "Kinder":
                print(f"{einrueckung}{schluessel}:")
                for kind in wert:
                    print(f"{einrueckung}  - {kind}")
            else:
                print(f"{einrueckung}{schluessel}:")
                zeige_stammbaum(vort_setze_namen_feld(wert), ebene + 1)
    elif isinstance(person, str):
        print(f"{einrueckung}- {person}")


# Kleiner Helfer, falls bei einem Elternteil direkt nur ein Name angegeben wurde:
def vort_setze_namen_feld(eingabe):
    if isinstance(eingabe, str):
        return {"Name": eingabe}
    return eingabe


# Aufruf mit dem Stammbaum:
zeige_stammbaum(stammbaum)
