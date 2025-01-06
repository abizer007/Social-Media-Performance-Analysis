# 🚀 **Social Media Performance Analysis For SuperMind Hackathon**

Welcome to the **Social Media Performance Analysis Workflow** repository. This project implements an advanced LangFlow workflow to analyze and manage social media performance metrics, leveraging the capabilities of DataStax Astra DB for efficient data management as an assignment by AI Syndicate 404.
---

https://astra.datastax.com/langflow/dbe5d54e-de57-4d8f-b927-72d732204353/flow/14aecd59-decf-493a-8a02-67a94b283b0c

---

## 🎯 **Project Overview**

This workflow is designed to accomplish the following objectives:

- **Install** and configure LangFlow along with required dependencies.
- **Integrate** and utilize DataStax Astra DB for secure and scalable data storage.
- **Develop** prompts and agents for analyzing social media metrics.
- **Generate actionable insights** into engagement rates, growth trends, and other key performance indicators.

---

## 📦 **Setup Instructions**

### 1. Clone the Repository
```bash
git clone https://github.com/abizer007/Social-Media-Performance-Analysis.git
cd Social-Media-Performance-Analysis
```

### 2. Install Dependencies
```bash
pip install langflow
gpip install astrapy
```

### 3. Run the Workflow
Start the LangFlow server to initiate the workflow:
```bash
langflow serve
```

### 4. Configure Astra DB
Ensure your Astra DB credentials are set up as environment variables:
```bash
export ASTRA_DB_APPLICATION_TOKEN="your-token"
```

---

## 🛠 **Workflow Details**

This section provides a comprehensive explanation of the nodes used in the LangFlow workflow.

### 🔧 **Nodes in the Workflow**

#### 1. **Chat Input Node** 🗨️
- **Description:** Captures user input, such as specific social media metrics or analysis goals.
- **Implementation:**
  - Accepts textual or file-based inputs.
  - Allows for customization of sender types and message attributes.

#### 2. **Prompt Node** 💡
- **Description:** Creates structured prompts with dynamic variables to analyze engagement rates and growth trends.
- **Configuration:**
  - Template: "Analyze the engagement rate and growth trends for {platform}."
  - Dynamic fields: Accepts parameters such as platform names (e.g., Instagram, Twitter).

#### 3. **Astra DB Tool Node** 🗄️
- **Description:** Integrates with DataStax Astra DB to manage transactional data storage and retrieval.
- **Capabilities:**
  - Collection: `social_media_engagements`
  - API Endpoint: `https://9adfc868-0c92-4854-8776-c4c641f0d3e7-us-east-2.apps.astra.datastax.com`
  - Projections: Allows filtering specific fields.

#### 4. **Agent Node** 🤖
- **Description:** Employs large language models (LLMs), such as OpenAI GPT, to interpret prompts and deliver insights.
- **Key Features:**
  - Memory support for contextual understanding.
  - Incorporates tools like date retrieval and result parsers.

#### 5. **Chat Output Node** 📤
- **Description:** Formats and displays the analytical results in a user-friendly manner.
- **Customizations:**
  - Background colors, icons, and text styling for improved presentation.

### 🖼️ **Workflow Diagram**
Insert your workflow diagram here:
![Workflow Diagram]![WhatsApp Image 2025-01-06 at 22 07 31_06f9013f](https://github.com/user-attachments/assets/4559f944-a565-495b-8459-62f498627623)


---

## 📊 **Output Example**

An example JSON output generated by the workflow:
```json
{
  "platform": "Instagram",
  "engagement_rate": "4.5%",
  "growth_trend": "Positive"
}
```
![WhatsApp Image 2025-01-06 at 22 23 37_11ed5679](https://github.com/user-attachments/assets/da8bf14b-d4f7-4df6-89ea-b82465e08c3d)
![WhatsApp Image 2025-01-06 at 22 24 24_964940e3](https://github.com/user-attachments/assets/6ea42d2c-abdc-4ca8-989c-d5809ac5a31d)


---

## 🧑‍🤝‍🧑 **AI Syndicate 404**

**Team Lead:**
- 👩‍💻 [Abizer Masavi](https://github.com/abizer007)

**Team Members:**
- 🧑‍💻 [Swapnil Pal](https://github.com/Swapnill1435)
- 🧑‍💻 [Shreyash Nikam](https://github.com/ShreyashDevelop)
- 🧑‍💻 [Zaid Rahman](https://github.com/zaidr09275)

---

## 🌟 **Key Features**

- **Real-Time Analysis:** Provides instantaneous insights on engagement and growth metrics.
- **Scalable Data Management:** Utilizes Astra DB for secure and efficient handling of large datasets.
- **Customizable Prompts and Agents:** Enables user-defined templates and adaptive agents for nuanced analysis.

---

## 🎉 **Contributing**

Contributions are welcome! Please review the [Contribution Guide](CONTRIBUTING.md) for guidelines.

---

## 📜 **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for detailed information.

---

## 🖼️ **Screenshots and Media**

Include screenshots or media showcasing the workflow and its outputs to enhance documentation clarity.
![WhatsApp Image 2025-01-06 at 22 07 31_06f9013f](https://github.com/user-attachments/assets/c917f3bd-b723-41cf-8344-cdb84acba3c7)

![WhatsApp Image 2025-01-06 at 22 13 16_152198ca](https://github.com/user-attachments/assets/0e81548c-9361-409a-9f6c-50dd1d96a470)

---

