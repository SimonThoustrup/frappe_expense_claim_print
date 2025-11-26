from setuptools import setup, find_packages

setup(
    name='frappe_expense_claim_print',
    version='1.0.0',
    description='Add Print with Attachments to Expense Claim',
    author='Your Name',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "PyPDF2"
    ]
)
