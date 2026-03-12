class DataAnalyzer:
    def load_data(self, data):
        self.data = data
        print("Data loaded successfully.")

    def analyze_data(self):
        pass  # Placeholder for data analysis logic

    def generate_report(self):
        pass  # Placeholder for report generation logic

class NumericDataAnalyzer(DataAnalyzer):
    def analyze(self):
        self.mean = sum(self.data) / len(self.data)
        self.median = sorted(self.data)[len(self.data) // 2]
        self.mode = max(set(self.data), key=self.data.count)
        self.maximum = max(self.data)
        self.minimum = min(self.data)

    