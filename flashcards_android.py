import random
import sys

class Flashcards:
    def __init__(self):
        self.cards = self.load_questions_and_answers()
        self.lessons = self.extract_lessons()
        random.shuffle(self.cards)

    def load_questions_and_answers(self):
        questions_and_answers = """
        DNA and RNA Structural Properties|What are the structural differences between DNA and RNA?|DNA is typically double-stranded, with a double helix structure, while RNA is usually single-stranded. Additionally, DNA contains deoxyribose sugar, and RNA contains ribose sugar.
        DNA and RNA Structural Properties|Explain the double helix structure of DNA.|DNA's double helix structure consists of two antiparallel strands of nucleotides held together by hydrogen bonds between complementary base pairs (adenine with thymine and guanine with cytosine).
        DNA and RNA Structural Properties|Discuss the major and minor grooves in the DNA double helix.|The major and minor grooves are spaces between the DNA strands. The major groove is wider and provides access for proteins, while the minor groove is narrower.
        DNA and RNA Structural Properties|How is the DNA double helix stabilized?|The DNA double helix is stabilized by hydrogen bonding between complementary base pairs, hydrophobic interactions, and stacking interactions between adjacent base pairs.
        DNA and RNA Structural Properties|Explain the importance of base pairing in DNA structure.|Base pairing ensures specificity in DNA structure and replication. Adenine pairs with thymine, and guanine pairs with cytosine, forming complementary base pairs.
        DNA and RNA Structural Properties|What is the role of DNA supercoiling?|Supercoiling allows DNA to be more compact and fit into the limited space of the cell. It also plays a role in DNA replication and transcription.
        DNA and RNA Structural Properties|Describe the structure of RNA.|RNA is typically single-stranded and contains ribose sugar. It has four nitrogenous bases: adenine, uracil, guanine, and cytosine. RNA can fold into complex secondary and tertiary structures.
        DNA and RNA Structural Properties|Explain the significance of RNA secondary structures.|RNA secondary structures, such as hairpins and loops, are formed by intramolecular base pairing. They play crucial roles in RNA stability, function, and interactions with other molecules.
        DNA and RNA Structural Properties|Discuss the three types of RNA and their functions.|mRNA (messenger RNA) carries genetic information from DNA to the ribosome. rRNA (ribosomal RNA) is a structural component of ribosomes. tRNA (transfer RNA) carries amino acids to the ribosome during protein synthesis.
        DNA and RNA Structural Properties|How does RNA differ from DNA in terms of structure and function?|RNA is usually single-stranded, contains ribose sugar, and uses uracil instead of thymine. Functionally, RNA is involved in various cellular processes, including protein synthesis, gene regulation, and catalysis.
        DNA and RNA Structural Properties|Explain the concept of DNA melting (denaturation) and its applications.|DNA melting involves the separation of the DNA double helix into single strands. It is used in techniques such as PCR (polymerase chain reaction) and DNA sequencing.
        Nucleotides' Structure and Functions|What is the basic structure of a nucleotide?|A nucleotide consists of three components: a sugar molecule (ribose or deoxyribose), a phosphate group, and a nitrogenous base.
        Nucleotides' Structure and Functions|Differentiate between ribonucleotides and deoxyribonucleotides.|Ribonucleotides contain ribose sugar, while deoxyribonucleotides contain deoxyribose sugar. They serve as the building blocks for RNA and DNA, respectively.
        Nucleotides' Structure and Functions|Explain the role of nucleotides in nucleic acids.|Nucleotides are the monomeric units that polymerize to form nucleic acids, such as DNA and RNA, which carry and transmit genetic information.
        Nucleotides' Structure and Functions|Describe the structure of a purine nucleotide.|A purine nucleotide consists of a purine base (adenine or guanine), a sugar molecule (ribose or deoxyribose), and a phosphate group.
        Nucleotides' Structure and Functions|What is the function of nucleotides in DNA replication?|Nucleotides serve as the building blocks for the synthesis of new DNA strands during DNA replication, ensuring accurate transmission of genetic information.
        Nucleotides' Structure and Functions|Explain the complementary base pairing in nucleotides.|In DNA, adenine pairs with thymine, and guanine pairs with cytosine through hydrogen bonding, ensuring specificity in base pairing.
        Nucleotides' Structure and Functions|Discuss the role of nucleotides in RNA transcription.|During transcription, nucleotides are used to synthesize a complementary RNA strand from a DNA template, allowing the transfer of genetic information.
        Nucleotides' Structure and Functions|What is the function of ATP (adenosine triphosphate) in cellular energy transfer?|ATP serves as the primary energy currency in cells, transferring energy through the hydrolysis of its high-energy phosphate bonds.
        Nucleotides' Structure and Functions|Explain the structure and function of cAMP (cyclic adenosine monophosphate).|cAMP is a nucleotide derivative that functions as a second messenger in cellular signaling, transmitting signals initiated by various hormones.
        Nucleotides' Structure and Functions|Discuss the role of nucleotides in cellular signaling pathways.|Nucleotides, such as cAMP and cGMP, play key roles in mediating cellular responses to extracellular signals, regulating various physiological processes.
        Nucleotides' Structure and Functions|How do nucleotides contribute to the structure of tRNA (transfer RNA)?|Nucleotides are the building blocks of tRNA, and the specific sequence of nucleotides in tRNA is crucial for its structure and function in facilitating protein synthesis.
        Peptides|What is a peptide in the context of biomolecules?|A peptide is a short chain of amino acids linked by peptide bonds, typically consisting of fewer than 50 amino acids.
        Peptides|Differentiate between a peptide and a protein.|While both peptides and proteins are composed of amino acids, peptides are shorter chains, typically containing fewer than 50 amino acids, whereas proteins are longer and more complex.
        Peptides|Explain the formation of a peptide bond between amino acids.|A peptide bond forms through a condensation reaction between the carboxyl group of one amino acid and the amino group of another, resulting in the release of water.
        Peptides|What is the significance of the amino acid sequence in a peptide?|The amino acid sequence determines the unique structure and function of a peptide, influencing its interactions and biological activities.
        Peptides|Discuss the classification of peptides based on their size.|Peptides can be classified into oligopeptides (2-20 amino acids), polypeptides (20-50 amino acids), and proteins (50 or more amino acids).
        Peptides|Explain the role of peptides as signaling molecules.|Peptides function as signaling molecules in cellular communication, with examples such as hormones, neurotransmitters, and growth factors.
        Peptides|How are peptides synthesized in living organisms?|Peptides are synthesized through ribosomal protein synthesis, where amino acids are linked in a specific sequence based on the genetic code.
        Peptides|Discuss the structural diversity of peptides.|Peptides can exhibit various structures, including alpha helices, beta sheets, and random coils, contributing to their diverse functions.
        Peptides|What are antimicrobial peptides, and what role do they play in the immune system?|Antimicrobial peptides are small peptides that have antimicrobial properties, contributing to the innate immune system's defense against pathogens.
        Peptides|Explain the significance of peptide hormones in the endocrine system.|Peptide hormones, such as insulin and growth hormone, play crucial roles in regulating various physiological processes, including metabolism, growth, and stress responses.
        Proteins' 3D Structure|What is the primary structure of a protein?|The primary structure of a protein is the linear sequence of amino acids linked by peptide bonds, forming the protein's backbone.
        Proteins' 3D Structure|Describe the secondary structure of proteins.|The secondary structure involves the folding of the polypeptide chain into alpha helices or beta sheets, stabilized by hydrogen bonds between amino acids.
        Proteins' 3D Structure|What forces drive the formation of the secondary structure in proteins?|Hydrogen bonds between amino acids contribute to the formation of secondary structures in proteins.
        Proteins' 3D Structure|Explain the significance of the tertiary structure in proteins.|The tertiary structure represents the three-dimensional arrangement of a protein's secondary structure elements, crucial for its function and stability.
        Proteins' 3D Structure|What types of interactions stabilize the tertiary structure of proteins?|Interactions such as hydrophobic interactions, hydrogen bonding, disulfide bridges, and van der Waals forces stabilize the tertiary structure.
        Proteins' 3D Structure|Discuss the quaternary structure of proteins.|The quaternary structure results from the assembly of multiple polypeptide subunits, forming a functional protein complex.
        Proteins' 3D Structure|How do chaperone proteins contribute to proper protein folding?|Chaperone proteins assist in the folding of other proteins, preventing misfolding and promoting the correct three-dimensional structure.
        Proteins' 3D Structure|Explain the denaturation of proteins.|Denaturation involves the disruption of a protein's structure, often caused by factors such as heat, pH extremes, or chemical agents, leading to loss of function.
        Proteins' 3D Structure|What is the Ramachandran plot, and what does it illustrate about protein structure?|The Ramachandran plot is a graphical representation of the angles of rotation about the phi (ϕ) and psi (ψ) bonds in a protein backbone, revealing allowed and disallowed regions for stable structures.
        Proteins' 3D Structure|How does the amino acid sequence determine a protein's folding pattern?|The specific sequence of amino acids in the primary structure dictates the interactions that drive the protein's folding into its unique three-dimensional structure.
        Proteins' 3D Structure|Discuss the role of structural motifs in protein function.|Structural motifs, such as alpha helices and beta sheets, are recurring patterns in protein structures that often contribute to specific functions or binding sites.
        Myoglobins|What is the primary function of myoglobin?|Myoglobin functions as an oxygen storage and transport molecule within muscle cells, facilitating oxygen delivery for muscle metabolism.
        Myoglobins|Describe the structure of myoglobin.|Myoglobin is a globular protein with a single heme group containing iron, allowing it to bind and release oxygen.
        Myoglobins|How does myoglobin differ from hemoglobin in terms of structure and function?|Myoglobin has a single subunit and functions as an intracellular oxygen carrier in muscles, while hemoglobin has multiple subunits and transports oxygen throughout the bloodstream.
        Myoglobins|Explain the role of myoglobin in the oxygenation of muscles during exercise.|Myoglobin releases stored oxygen to muscles during exercise, ensuring a local supply for aerobic respiration and energy production.
        Myoglobins|What is the significance of the heme group in myoglobin?|The heme group in myoglobin, similar to hemoglobin, is essential for binding and carrying oxygen, thanks to the iron atom within the heme.
        Myoglobins|How does myoglobin contribute to the color of meat?|Myoglobin's color changes during cooking, affecting the color of meat. The iron in myoglobin undergoes chemical changes, leading to different shades (e.g., red to brown) as temperature increases.
        Myoglobins|Discuss the oxygen saturation curve of myoglobin compared to hemoglobin.|Myoglobin exhibits a hyperbolic oxygen saturation curve, indicating high affinity for oxygen at low partial pressures, suitable for oxygen storage in muscles.
        Myoglobins|What is the role of myoglobin in preventing hypoxia in muscle tissue?|Myoglobin acts as an oxygen reservoir in muscle cells, preventing hypoxia by releasing oxygen when local concentrations are low.
        Myoglobins|Explain the Bohr effect in the context of myoglobin.|Similar to hemoglobin, the Bohr effect in myoglobin describes how factors like pH and carbon dioxide levels influence its oxygen-binding capacity.
        Myoglobins|How does myoglobin contribute to the regulation of oxygen levels in muscle cells?|Myoglobin releases oxygen to muscle cells based on their metabolic needs, contributing to oxygen homeostasis during changes in activity levels.
        Hemoglobins|What is the primary function of hemoglobin?|Hemoglobin's main function is to transport oxygen from the lungs to tissues and organs throughout the body.
        Hemoglobins|Describe the structure of hemoglobin.|Hemoglobin is a protein composed of four globular subunits, each containing an iron-containing heme group that binds to oxygen.
        Hemoglobins|What is the significance of the iron in the heme group?|The iron in the heme group of hemoglobin is essential for binding and transporting oxygen molecules.
        Hemoglobins|Explain the cooperative binding of oxygen by hemoglobin.|Cooperative binding refers to the increased affinity of hemoglobin for oxygen after binding to an initial oxygen molecule, making it easier for subsequent oxygen molecules to bind.
        Hemoglobins|What is the Bohr effect in relation to hemoglobin?|The Bohr effect describes how the affinity of hemoglobin for oxygen is influenced by pH and carbon dioxide levels, enhancing oxygen release in tissues.
        Hemoglobins|Discuss the role of fetal hemoglobin (HbF).|Fetal hemoglobin has a higher affinity for oxygen than adult hemoglobin, facilitating oxygen transfer from the mother to the developing fetus.
        Hemoglobins|What is sickle cell anemia, and how does it relate to hemoglobin?|Sickle cell anemia is a genetic disorder where a mutation in the hemoglobin gene leads to the production of abnormal hemoglobin, causing red blood cells to become misshapen.
        Hemoglobins|Explain the process of oxygen loading and unloading by hemoglobin.|In the lungs, hemoglobin loads oxygen (oxyhemoglobin), and in tissues, it unloads oxygen (deoxyhemoglobin) for cellular use.
        Hemoglobins|What factors influence the oxygen-hemoglobin dissociation curve?|Factors like pH, temperature, and carbon dioxide levels can affect the curve, determining how readily hemoglobin binds and releases oxygen.
        Hemoglobins|Discuss the role of hemoglobin in carbon dioxide transport.|Hemoglobin can bind to carbon dioxide and transport it from tissues to the lungs for elimination.
        Carbohydrates|What are carbohydrates?|Carbohydrates are organic compounds composed of carbon, hydrogen, and oxygen in a 1:2:1 ratio. They serve as a primary source of energy for living organisms.
        Carbohydrates|What is the basic structural unit of carbohydrates?|The basic structural unit of carbohydrates is a monosaccharide, such as glucose or fructose.
        Carbohydrates|Differentiate between monosaccharides and disaccharides.|Monosaccharides are single sugar molecules (e.g., glucose), while disaccharides are composed of two monosaccharide units (e.g., sucrose or lactose).
        Carbohydrates|Explain the role of carbohydrates in energy storage.|Carbohydrates, especially polysaccharides like glycogen in animals and starch in plants, serve as a storage form of energy.
        Carbohydrates|What is the function of cellulose in plants?|Cellulose, a polysaccharide, provides structural support to plant cell walls and contributes to the rigidity of plant tissues.
        Carbohydrates|Define the term glycosidic bond.|A glycosidic bond is a covalent bond formed between two sugar molecules, resulting in the formation of disaccharides or polysaccharides.
        Carbohydrates|What is the process of glycolysis?|Glycolysis is the metabolic pathway that breaks down glucose into pyruvate, producing ATP and NADH in the cytoplasm of cells.
        Carbohydrates|How do carbohydrates contribute to blood glucose levels?|Carbohydrates are broken down into glucose during digestion, and the resulting glucose is absorbed into the bloodstream, influencing blood glucose levels.
        Carbohydrates|Explain the difference between simple and complex carbohydrates.|Simple carbohydrates, like sugars, consist of one or two sugar units, while complex carbohydrates, like starch and fiber, are composed of multiple sugar units.
        Carbohydrates|What is the significance of carbohydrates in a balanced diet?|Carbohydrates provide a quick and efficient source of energy, and a balanced diet includes a mix of simple and complex carbohydrates for overall health.
        Biomolecules|What are biomolecules?|Biomolecules are molecules that are essential for the structure and function of living organisms, including carbohydrates, lipids, proteins, and nucleic acids.
        Biomolecules|What is the primary function of carbohydrates?|Carbohydrates serve as a primary source of energy and play a structural role in cell walls (e.g., cellulose) and exoskeletons (e.g., chitin).
        Biomolecules|Explain the structure of an amino acid.|An amino acid consists of an amino group, a carboxyl group, and a side chain (R group), with 20 different amino acids forming the building blocks of proteins.
        Biomolecules|What is the role of proteins in biological systems?|Proteins have diverse functions, including enzyme catalysis, structural support, transport of molecules, and immune response.
        Biomolecules|What is the difference between DNA and RNA?|DNA (deoxyribonucleic acid) carries genetic information and has a double-stranded helical structure, while RNA (ribonucleic acid) is involved in protein synthesis and is usually single-stranded.
        Biomolecules|What is the function of ATP (adenosine triphosphate)?|ATP is the primary energy currency of the cell, storing and transferring energy for various cellular activities.
        Biomolecules|Define the term enzyme.|An enzyme is a biological catalyst that accelerates chemical reactions by lowering the activation energy, without being consumed in the process.
        Biomolecules|What are the three types of RNA involved in protein synthesis?|The three types of RNA are mRNA (messenger RNA), tRNA (transfer RNA), and rRNA (ribosomal RNA), each playing a specific role in protein synthesis.
        Biomolecules|Explain the structure of a nucleotide.|A nucleotide consists of a sugar (ribose or deoxyribose), a phosphate group, and a nitrogenous base (adenine, thymine/uracil, cytosine, or guanine), serving as the building blocks of nucleic acids.
        Biomolecules|What is the importance of carbohydrates in energy metabolism?|Carbohydrates are a primary source of energy, and their breakdown during cellular respiration provides ATP for cellular activities.
        Lipids|What are lipids?|Lipids are a diverse group of hydrophobic organic molecules, including fats, oils, phospholipids, and steroids.
        Lipids|What is the primary function of triglycerides?|Triglycerides serve as a concentrated source of energy storage in adipose tissue.
        Lipids|Explain the structure of a fatty acid.|A fatty acid consists of a hydrocarbon chain with a carboxyl group at one end.
        Lipids|What is the difference between saturated and unsaturated fats?|Saturated fats have no double bonds in their hydrocarbon chains, while unsaturated fats have one or more double bonds.
        Lipids|What role do phospholipids play in cell membranes?|Phospholipids form the basic structure of cell membranes, with hydrophilic heads and hydrophobic tails creating a lipid bilayer.
        Lipids|What are the functions of cholesterol in the body?|Cholesterol is a precursor to steroid hormones, helps regulate membrane fluidity, and plays a role in vitamin D synthesis.
        Lipids|Describe the process of lipolysis.|Lipolysis is the breakdown of triglycerides into fatty acids and glycerol, releasing stored energy.
        Lipids|What are essential fatty acids?|Essential fatty acids, such as omega-3 and omega-6, cannot be synthesized by the body and must be obtained from the diet.
        Lipids|How do lipoproteins transport lipids in the bloodstream?|Lipoproteins are complexes of lipids and proteins that transport cholesterol and triglycerides in the bloodstream.
        Lipids|What is the function of adipose tissue?|Adipose tissue stores energy in the form of triglycerides and provides insulation and cushioning for organs.
        Glycoses|What is the significance of carbohydrates in living organisms?|Carbohydrates serve as a primary source of energy, play structural roles in cells and tissues, and participate in various cellular processes.
        Glycoses|Define monosaccharide and provide an example.|A monosaccharide is the simplest form of carbohydrate, and an example is glucose, which is a hexose sugar.
        Glycoses|Explain the difference between glucose and fructose.|Glucose and fructose are both monosaccharides, but they differ in their chemical structures. Glucose is a hexose with a six-carbon ring, while fructose is a ketose with a five-carbon ring.
        Glycoses|What are disaccharides, and give an example.|Disaccharides are carbohydrates composed of two monosaccharide units linked by a glycosidic bond. An example is sucrose, which consists of glucose and fructose.
        Glycoses|Discuss the role of carbohydrates in energy storage.|Carbohydrates, in the form of glycogen in animals and starch in plants, serve as a storage reservoir for energy, which can be easily mobilized when needed.
        Glycoses|What is the function of cellulose in plant cells?|Cellulose is a polysaccharide that provides structural support to plant cell walls, contributing to the rigidity and strength of plant cells.
        Glycoses|Explain the concept of blood glucose regulation in the human body.|Blood glucose levels are regulated by the hormones insulin and glucagon, which control the uptake and release of glucose by cells, ensuring a stable blood sugar concentration.
        Glycoses|Define glycoproteins and their role in cell communication.|Glycoproteins are proteins with attached carbohydrate chains. They play a crucial role in cell communication, cell recognition, and immune responses.
        Glycoses|What is lactose intolerance, and how does it relate to carbohydrates?|Lactose intolerance is the inability to digest lactose, a disaccharide found in milk. It results from a deficiency of the enzyme lactase, which breaks down lactose into its constituent sugars.
        Glycoses|Discuss the role of carbohydrates in glycolysis.|Carbohydrates are broken down through glycolysis, a process that converts glucose into pyruvate, releasing energy that can be used for cellular activities.
        Glycoses|Explain the concept of glycemic index in relation to carbohydrates.|The glycemic index measures how quickly carbohydrates raise blood glucose levels after consumption. Low glycemic index foods cause a slower, more gradual increase in blood sugar, while high glycemic index foods cause a rapid spike.
        """

        cards = [tuple(line.strip().split('|')) for line in questions_and_answers.split('\n') if line.strip()]
        return cards

    def extract_lessons(self):
        return list(set(card[0] for card in self.cards))

    def start_flashcards(self):
        try:
            print("Choose a lesson:")
            for i, lesson in enumerate(self.lessons, start=1):
                print(f"{i}-{lesson}")
            print(f"{len(self.lessons) + 1}-All Lessons")

            choice = input("Enter the number of the lesson you want to study: ")

            if choice.isdigit() and 1 <= int(choice) <= len(self.lessons) + 1:
                if int(choice) == len(self.lessons) + 1:
                    filtered_cards = self.cards
                else:
                    selected_lesson = self.lessons[int(choice) - 1]
                    filtered_cards = [card for card in self.cards if card[0] == selected_lesson]

                for card in filtered_cards:
                    print(f"Question: {card[1]}")
                    input("")
                    print(f"Answer: {card[2]}")
                    print("-" * 40)  # Separator line
                    input("")

            else:
                print("Invalid choice. Please enter a valid number.")

        except KeyboardInterrupt:
            print("\nExiting the program.")

if __name__ == "__main__":
    flashcards_app = Flashcards()
    flashcards_app.start_flashcards()