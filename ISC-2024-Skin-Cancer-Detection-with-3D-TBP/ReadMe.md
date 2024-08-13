https://www.kaggle.com/competitions/isic-2024-challenge

Timeline



    June 26, 2024 - Start Date.

    August 30, 2024 - Entry Deadline. You must accept the competition rules before this date in order to compete.

    August 30, 2024 - Team Merger Deadline. This is the last day participants may join or merge teams.

    September 6, 2024 - Final Submission Deadline.

    September 20, 2024 - Deadline for potential prize-winners to publish their solution code and write-ups.

All deadlines are at 11:59 PM UTC on the corresponding day unless otherwise noted. The competition organizers reserve the right to update the contest timeline if they deem it necessary.



Overview

In this competition, you'll develop image-based algorithms to identify histologically confirmed skin cancer cases with single-lesion crops from 3D total body photos (TBP). The image quality resembles close-up smartphone photos, which are regularly submitted for telehealth purposes. Your binary classification algorithm could be used in settings without access to specialized care and improve triage for early skin cancer detection.

Description

Skin cancer can be deadly if not caught early, but many populations lack specialized dermatologic care. Over the past several years, dermoscopy-based AI algorithms have been shown to benefit clinicians in diagnosing melanoma, basal cell, and squamous cell carcinoma. However, determining which individuals should see a clinician in the first place has great potential impact. Triaging applications have a significant potential to benefit underserved populations and improve early skin cancer detection, the key factor in long-term patient outcomes.

Dermatoscope images reveal morphologic features not visible to the naked eye, but these images are typically only captured in dermatology clinics. Algorithms that benefit people in primary care or non-clinical settings must be adept to evaluating lower quality images. This competition leverages 3D TBP to present a novel dataset of every single lesion from thousands of patients across three continents with images resembling cell phone photos.

This competition challenges you to develop AI algorithms that differentiate histologically-confirmed malignant skin lesions from benign lesions on a patient. Your work will help to improve early diagnosis and disease prognosis by extending the benefits of automated skin cancer detection to a broader population and settings.

Evaluation
Primary Scoring Metric

Submissions are evaluated on partial area under the ROC curve (pAUC) above 80% true positive rate (TPR) for binary classification of malignant examples. (See the implementation in the notebook ISIC pAUC-aboveTPR.)

The receiver operating characteristic (ROC) curve illustrates the diagnostic ability of a given binary classifier system as its discrimination threshold is varied. However, there are regions in the ROC space where the values of TPR are unacceptable in clinical practice. Systems that aid in diagnosing cancers are required to be highly-sensitive, so this metric focuses on the area under the ROC curve AND above 80% TRP. Hence, scores range from [0.0, 0.2].

The shaded regions in the following example represents the pAUC of two arbitrary algorithms (Ca and Cb) at an arbitrary minimum TPR:
"pAUC defined by constraining TPR" by ProfGigio is licensed under CC-BY-SA-4.0
"pAUC defined by constraining TPR" by ProfGigio is licensed under CC-BY-SA-4.0
Submission File

For each image (isic_id) in the test set, you must predict the probability (target) that the lesion is malignant. The file should contain a header and have the following format:

isic_id,target
ISIC_0015657,0.7
ISIC_0015729,0.9
ISIC_0015740,0.8
etc.
