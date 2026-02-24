import xml.etree.ElementTree as ET
import pandas as pd

def parse_plip_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    interactions = []

    for interaction in root.iter():
        if interaction.tag in ["hydrogen_bond", "hydrophobic_interaction",
                               "salt_bridge", "pi_stack", "water_bridge"]:
            
            residue = interaction.find("resnr")
            restype = interaction.find("restype")
            chain = interaction.find("reschain")

            if residue is not None:
                interactions.append({
                    "Residue_Number": residue.text,
                    "Residue_Name": restype.text,
                    "Chain": chain.text,
                    "Interaction_Type": interaction.tag
                })

    return pd.DataFrame(interactions)
