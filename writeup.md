## Question 1

Take a look at the file labeled `data/phase0.txt`. Why might we have missing values or values that state "NO DATA" in this dataset? While we are currently ignoring these values, what might be the risk of filtering these values out?

### **Answer:**

There are only **two primary reasons** why we have issues with some values in the dataset:

1. **Technical Issues with the Device:**
   - **Signal or Data Transfer Errors:** The device may temporarily lose connection or encounter issues during data transfer, resulting in incomplete or missing records due to weak signals, software glitches, or corrupted data.  
   - **Battery Depletion (Less likely):** If the device’s battery dies, it will not record heart rate data, but this is probably not the case because the invalid data is sporadic rather than continuous.
2. **Sensor Installation Issues:**  
   - **Improper Installation of Sensors:** If sensors are not properly attached or installed, it can result in incorrect or missing data points. Poor contact with the skin or misalignment could lead to unreliable measurements.  
3. **Participant Non-Compliance:**
   - **Improper Device Usage:** The participant may not wear the device correctly, causing recording errors.  
   - **Intentional Device Removal or Pausing:** Temporary removal or turning off the device can result in data gaps, particularly during activities where the device is uncomfortable or inconvenient to wear.

### **Risk of Filtering Out Invalid/Missing Entries:**

- **Data Quality and Interpretation:** Ignoring invalid data can lead to **biased or incomplete analysis**, especially if the missing values are not randomly distributed.
- **Patterns in Missing Data:** Analyzing when and why data is missing can reveal **valuable insights** about device functionality or user behavior.
- **Statistical Impact:** Filtering out too much data can **reduce the sample size**, potentially affecting the statistical power of the analysis and leading to less reliable conclusions.

## **Summary of Findings**  

| Phase   | Average Heart Rate (BPM) | Maximum Heart Rate (BPM) | Standard Deviation |
|---------|--------------------------|--------------------------|--------------------|
| Phase0  | 64.59                     | 93                       | 8.53               |
| Phase1  | 87.3                      | 110                      | 9.9                |
| Phase2  | 85.18                     | 117                      | 13.38              |
| Phase3  | 60.65                     | 99                       | 11.0               |

---

## Question 2

During sleep, we expect maximum heart rate of a phase to be **lower** than the maximum heart rate of all other phases. Observe the visualizations and descriptive statistics that you've calculated. Using these findings, in which phase does sleep occur? Mention numerical details that back your findings.

### **Phase0 (Sleep Phase)**  

Based on the findings, **Phase0** fits the **sleeping phase**:  

1. **Low Average Heart Rate (64.59 BPM):** Typical for resting or sleep.  
2. **Low Maximum Heart Rate (93 BPM):** No significant spikes, indicating minimal activity.  
3. **Low Standard Deviation (8.53):** Heart rate is stable, as expected during sleep.  
4. **Visualization:** The heart rate starts higher and gradually decreases, becoming steady, which suggests the participant was **falling asleep**.

#### **Plot: Phase0 (Sleep Phase)**

![Phase0 Sleep Plot](images/phase0.png)

## Question 3

During exercise, we expect the maximum heart rate of a phase to be **higher** the maximum heart rate of all other phases. Observe the visualizations and descriptive statistics that you've calculated. Using these findings, in which phase(s) does exercise occur? Mention numerical details that back your findings.

### **Phase2 (Exercise Phase) & Phase1 (Moderate Activity)**

Based on the findings, **Phase2** likely corresponds to **intense exercise**, while **Phase1** suggests **moderate physical activity**.  

1. **High Maximum Heart Rate (117 BPM in Phase2):**  
   - The highest heart rate recorded, indicating intense exercise.  
   - Clear spikes visible in the **Phase2 plot**.  

2. **Moderate Maximum Heart Rate (110 BPM in Phase1):**  
   - Slightly lower but still elevated, suggesting moderate activity.  
   - Less dramatic spikes compared to Phase2.  

3. **Higher Standard Deviation (13.38 in Phase2):**  
   - Greater variability typical of exercise.  

4. **Visualization:**  
   - The **Phase2 plot** shows clear spikes, while **Phase1** shows less dramatic but still elevated levels.  

#### **Plot: Phase1 (Moderate Exercise)**

![Phase1 Plot](images/phase1.png)

#### **Plot: Phase2 (Intense Exercise)**

![Phase2 Plot](images/phase2.png)

## Question 4

During regular periods of awake activity, we expect the average heart rate of a phase to be relatively **lower** than the average heart rate of other phases, but we also expect standard deviation to be **higher**. In which phase do we notice this trend?

### **Phase3 (Awake, Light Activity)**  

The data indicates that **Phase3** likely corresponds to periods of being awake but not exercising, such as walking, talking, or light movement.  

1. **Low Average Heart Rate (60.65 BPM):**  
   - The lowest average heart rate besides the sleep phase (**Phase0**), suggesting a calm but awake state.  

2. **Moderate Variability (Standard Deviation 11.0):**  
   - Higher than during sleep but lower than during exercise, which matches normal daily activities.  

3. **Moderate Maximum Heart Rate (99 BPM):**  
   - Occasional increases but nothing extreme, typical for light activity.  

4. **Visualization:**  
   - The **Phase3 plot** shows mild fluctuations without extreme spikes, consistent with light, everyday activity.  

#### **Plot: Phase3 (Awake Activity)**  

![Phase3 Plot](images/phase3.png)
