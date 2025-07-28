% this code is to do the etl process for the pnsd dataset
% the pnsd dataset is a dataset about the patient with the parkinson's disease
% the dataset is from the UCI machine learning repository
% the dataset is in the csv format
% the dataset is about the patient with the parkinson's disease

select * from pnsd
where time between 2022-05-01 and 2022-06-01 and name ='nick'
