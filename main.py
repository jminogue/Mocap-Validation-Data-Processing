##******** README ********##
#FreeMocap exports a csv of all joint positions (locations) of it's identified landmarks, which can be found at the following link: https://github.com/google/mediapipe/blob/master/docs/solutions/pose.md
#This code is meant to extract those positions from the FreeMocap outputted csv and use them to calculate joint angles. A new csv with joint angles be created.
#This current version of the code is only concered with sagittal plane data


## Importing the necessary libraries for this code
import pandas as pd
import numpy as np


## Creating Dataframe by pulling in the FreeMocap csv raw output
df = pd.read_csv('mediapipe_body_3d_xyz.csv')


## Calculating Knee Angle
#Calculating the distances between the landmarks (forming a triangle)
df['aK'] = np.sqrt((df['right_knee_x'] - df['right_ankle_x'])**2 + (df['right_knee_z'] - df['right_ankle_z'])**2)
df['bK'] = np.sqrt((df['right_hip_x'] - df['right_knee_x'])**2 + (df['right_hip_z'] - df['right_knee_z'])**2)
df['cK'] = np.sqrt((df['right_ankle_x'] - df['right_hip_x'])**2 + (df['right_ankle_z'] - df['right_hip_z'])**2)
#Using Law of Cosines to solve for knee angle
df['R_knee_flexion'] = np.degrees(np.arccos(((df['aK']**2) + (df['bK']**2) - (df['cK']**2)) / (2*df['aK']*df['bK'])))


## Calculating Hip Angle
#Calculating the distances between the landmarks (forming a triangle)
df['aH'] = np.sqrt((df['right_shoulder_x'] - df['right_hip_x'])**2 + (df['right_shoulder_z'] - df['right_hip_z'])**2)
df['bH'] = np.sqrt((df['right_hip_x'] - df['right_knee_x'])**2 + (df['right_hip_z'] - df['right_knee_z'])**2)
df['cH'] = np.sqrt((df['right_knee_x'] - df['right_shoulder_x'])**2 + (df['right_knee_z'] - df['right_shoulder_z'])**2)
#Using Law of Cosines to solve for hip angle
df['R_hip_flexion'] = np.degrees(np.arccos(((df['aH']**2) + (df['bH']**2) - (df['cH']**2)) / (2*df['aH']*df['bH'])))


## Calculating Ankle Angle
#Calculating the distances between the landmarks (forming a triangle)
df['aA'] = np.sqrt((df['right_knee_x'] - df['right_ankle_x'])**2 + (df['right_knee_z'] - df['right_ankle_z'])**2)
df['bA'] = np.sqrt((df['right_ankle_x'] - df['right_foot_index_x'])**2 + (df['right_ankle_z'] - df['right_foot_index_z'])**2)
df['cA'] = np.sqrt((df['right_foot_index_x'] - df['right_knee_x'])**2 + (df['right_foot_index_z'] - df['right_knee_z'])**2)
#Using Law of Cosines to solve for ankle angle
df['R_ankle_flexion'] = np.degrees(np.arccos(((df['aA']**2) + (df['bA']**2) - (df['cA']**2)) / (2*df['aA']*df['bA'])))


## Showing the resulting Dataframe
print(df)


## Sending Dataframe to csv file
df.to_csv('results.csv', index=False)