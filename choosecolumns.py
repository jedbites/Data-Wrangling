import pandas as pd

df = pd.read_csv('Allan_IT_Developer.csv')
important_columns = ['category',
                     'company_id',
                     'company_name',
                     'linkedin_company_url',
                     'job_title',
                     'job_description',
                     'type',
                     'remote_allowed',
                     'linkedin_job_id',
                     'linkedin_job_url',
                     'domain',
                     'website',
                     'geographic_area',
                     'city',
                     'country',
                     'location',
                     'headquarters',
                     'linkedin_employees_url',
                     'employees',
                     'apply_url',
                     'phone',
                     'postal_code',
                     'sales_navigator_company_url',
                     'year_founded']

df_to_import = df[important_columns]

df_to_import.to_excel('Allan_IT_Developer.xlsx', index=False)