# NutriCow

- [Project summary](#project-summary)
  - [The issue we are hoping to solve](#the-issue-we-are-hoping-to-solve)
  - [How our technology solution can help](#how-our-technology-solution-can-help)
  - [Our idea](#our-idea)
- [Technology implementation](#technology-implementation)
  - [IBM AI service(s) used](#ibm-ai-services-used)
  - [Other IBM technology used](#other-ibm-technology-used)
  - [Solution architecture](#solution-architecture)
- [Presentation materials](#presentation-materials)
  - [Solution demo video](#solution-demo-video)
  - [Project development roadmap](#project-development-roadmap)
- [Additional details](#additional-details)
  - [How to run the project](#how-to-run-the-project)
  - [Live demo](#live-demo)
- [About this template](#about-this-template)
  - [Contributing](#contributing)
  - [Versioning](#versioning)
  - [Authors](#authors)
  - [License](#license)
  - [Acknowledgments](#acknowledgments)

_INSTRUCTIONS: Complete all required deliverable sections below._

## Project summary

### The issue we are hoping to solve

NutriCow aims to address the pressing sustainability problem of inefficient livestock nutrition management in the farming industry. Traditional methods of formulating cattle rations often lead to resource wastage, increased production costs, and suboptimal animal health. Inefficient ration management contributes to excessive greenhouse gas emissions, overuse of natural resources, and decreased farm profitability.

### How our technology solution can help

NutriCow streamlines and optimizes cattle nutrition management, offering farmers a data-driven tool to create balanced rations for their herds, ensuring efficient resource utilization and improved livestock health.

### Our idea

Cattle farming plays a vital role in meeting global food demand. However, it is also a significant contributor to environmental challenges such as methane emissions and resource overuse. One of the key factors impacting these challenges is the suboptimal feeding of livestock. Farmers often struggle to formulate well-balanced rations tailored to their specific resources, resulting in lower milk production, slower weight gain, and increased costs.

NutriCow was conceived as an innovative technological solution to revolutionize cattle nutrition management. Our platform harnesses the power of data analytics and AI to provide farmers with precise, cost-effective ration formulation. Here's how NutriCow works:

1. Data-Driven Ration Formulation:
NutriCow takes the guesswork out of creating cattle rations. Farmers input details about their available raw materials, such as types of crops, grains, and forage, along with their nutritional profiles. The platform's algorithms then analyze this data and calculate the optimal ration to meet specific nutritional requirements for different growth stages and production goals.

2. Cost Optimization:
Beyond nutrition, NutriCow helps farmers minimize costs by suggesting alternatives for raw materials based on market prices and availability. This cost optimization feature ensures that farmers achieve maximum yield while staying within budget constraints.

3. Real-time Updates and Monitoring:
NutriCow provides real-time monitoring of cattle performance. Farmers can track milk production, weight gain, and overall health indicators. Any deviations from expected performance trigger alerts, allowing timely interventions to ensure herd well-being.

4. Inventory Management:
To prevent shortages or excess inventory, NutriCow includes an inventory management component. Farmers can monitor their available resources and receive alerts when it's time to replenish certain ingredients.

5. Sustainability Insights:
Our platform offers valuable sustainability insights by quantifying the environmental impact of different ration formulations. This empowers farmers to make choices that reduce greenhouse gas emissions, lower water usage, and decrease the overall ecological footprint of their operations.

Why NutriCow Is an Improvement:

Compared to traditional ration formulation methods, NutriCow offers several advantages:

Precision: NutriCow's data-driven approach ensures that rations are precisely tailored to the specific needs of each herd, resulting in healthier and more productive cattle.

Cost Efficiency: By optimizing raw material usage and suggesting cost-effective alternatives, NutriCow helps farmers reduce expenses and improve profitability.

Environmental Impact: NutriCow's sustainability insights assist farmers in making eco-conscious decisions, contributing to a more sustainable and responsible livestock industry.

Real-time Monitoring: The platform's real-time updates enable prompt actions, preventing potential issues and ensuring animal welfare.

NutriCow represents a significant leap forward in sustainable cattle farming, addressing environmental concerns while enhancing profitability for farmers. It empowers farmers with data and technology to make informed decisions, contributing to a more sustainable and efficient livestock industry.

More detail is available in our [description document](/DESCRIPTION.md).

## Technology implementation

### IBM AI service(s) used

_INSTRUCTIONS: Included here is a list of commonly used IBM AI services. Remove any services you did not use, or add others from the linked catalog not already listed here. Leave only those included in your solution code. Provide details on where and how you used each IBM AI service to help judges review your implementation. Remove these instructions._

- [IBM Natural Language Understanding](https://cloud.ibm.com/catalog/services/natural-language-understanding) - WHERE AND HOW THIS IS USED IN OUR SOLUTION
- [Watson Assistant](https://cloud.ibm.com/catalog/services/watson-assistant) - WHERE AND HOW THIS IS USED IN OUR SOLUTION
- [Watson Discovery](https://cloud.ibm.com/catalog/services/watson-discovery) - WHERE AND HOW THIS IS USED IN OUR SOLUTION
- [Watson Speech to Text](https://cloud.ibm.com/catalog/services/speech-to-text) - WHERE AND HOW THIS IS USED IN OUR SOLUTION
- [Watson Text to Speech](https://cloud.ibm.com/catalog/services/text-to-speech) - WHERE AND HOW THIS IS USED IN OUR SOLUTION
- List any additional [IBM AI services](https://cloud.ibm.com/catalog?category=ai#services) used or remove this line

### Other IBM technology used

INSTRUCTIONS: List any other IBM technology used in your solution and describe how each component was used. If you can provide links to/details on exactly where these were used in your code, that would help the judges review your submission.

### Solution architecture

Diagram and step-by-step description of the flow of our solution:

![NutriCow Architecture](https://github.com/nafakbar12/NutriCow_2/blob/main/NutriCow%20System%20Architecture.jpg)

1. The user navigates to the site and uploads a video file.
2. Watson Speech to Text processes the audio and extracts the text.
3. Watson Translation (optionally) can translate the text to the desired language.
4. The app stores the translated text as a document within Object Storage.

## Presentation materials

_INSTRUCTIONS: The following deliverables should be officially posted to your My Team > Submissions section of the [Call for Code Global Challenge resources site](https://cfc-prod.skillsnetwork.site/), but you can also include them here for completeness. Replace the examples seen here with your own deliverable links._

### Solution demo video

[![Watch the video](https://raw.githubusercontent.com/Liquid-Prep/Liquid-Prep/main/images/readme/IBM-interview-video-image.png)](https://youtu.be/vOgCOoy_Bx0)

### Project development roadmap

The project currently does the following things.

- Feature 1
- Feature 2
- Feature 3

In the future we plan to...

See below for our proposed schedule on next steps after Call for Code 2023 submission.

![Roadmap](./images/roadmap.jpg)

## Additional details

_INSTRUCTIONS: The following deliverables are suggested, but **optional**. Additional details like this can help the judges better review your solution. Remove any sections you are not using._

### How to run the project

INSTRUCTIONS: In this section you add the instructions to run your project on your local machine for development and testing purposes. You can also add instructions on how to deploy the project in production.

### Live demo

You can find a running system to test at...

See our [description document](./docs/DESCRIPTION.md) for log in credentials.

---

_INSTRUCTIONS: You can remove the below section from your specific project README._

## About this template

### Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

### Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

### Authors

<a href="https://github.com/Call-for-Code/Project-Sample/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=Call-for-Code/Project-Sample" />
</a>

- **Billie Thompson** - _Initial work_ - [PurpleBooth](https://github.com/PurpleBooth)

### License

This project is licensed under the Apache 2 License - see the [LICENSE](LICENSE) file for details.

### Acknowledgments

- Based on [Billie Thompson's README template](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2).
