from setuptools import setup, find_packages

setup(
    name='frappe_expense_claim_print',
    version='1.0.0',
    description='Print Expense Claim with merged attachments',
    author='Your Name',
    packages=find_packages(),
    include_package_data=True,
    install_requires=["PyPDF2"]
)
