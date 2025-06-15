from research_agent import generate_report

if __name__ == "__main__":
    topic = input("Enter research topic: ")
    report = generate_report(topic)

    with open("output/report.md", "w") as f:
        f.write(report)
    print("✅ Report written to output/report.md")
