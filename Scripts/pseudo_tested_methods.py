from projects import Project,method_id, Mutant
from tables import ConsoleTableBuilder, percentage
import matplotlib.pyplot as plt
from itertools import chain, cycle
from collections import defaultdict



class Record:
    def __init__(self, project):
        self.id = project.id
        self.project = project
        target_methods = project.target_methods
        descartes = project.descartes
        self.methods_under_analysis = target_methods
        self.pseudo_tested = {}
        self.not_covered = {}
        self.tested = {}
        self.partialy_tested = {}
        self.MUT = 0
        self.PseudoT = 0
        self.partiallyT = 0
        self.not_cov = 0
        self.Tes = 0
        for mut in self.methods_under_analysis:
            if mut['classification'] == 'pseudo-tested':
                self.PseudoT+=1
                self.pseudo_tested['methods'] = mut
            elif mut['classification'] == 'partially-tested':
                self.partiallyT+=1
                self.partialy_tested['methods'] = mut
            elif mut['classification'] == 'not-covered':
                self.not_cov+=1
                self.not_covered['methods'] = mut
            else:
                self.Tes+=1
                self.tested['methods'] = mut
          
        
        self.pt_ratio = self.PseudoT / len(self.methods_under_analysis)
        self.ptandps_ratio = (self.PseudoT+self.partiallyT)/len(self.methods_under_analysis)
   

def show_rates_table(records, build_table=ConsoleTableBuilder):
    table = build_table(('Project',), ('Under Analysis', 'r'), ('Pseudo-tested', 'r'),('partially-tested', 'r'), ('Not-covered', 'r'),('Ratio Partially and pseudo-test','r', percentage),('Ratio pseudo-test', 'r', percentage))
    for item in records:
        table.row(item.project.name, len(item.methods_under_analysis), item.PseudoT,item.partiallyT,item.not_cov,item.ptandps_ratio, item.pt_ratio)
    table.display()
def main():
    print("Loading data. This may take some time.")
    records = [Record(project) for project in Project.available_projects()]
    show_rates_table(records)
    plt.show()

if __name__ == "__main__":
    main()