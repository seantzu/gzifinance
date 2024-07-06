from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# Create your models here.


class user(AbstractUser):
    updated = models.BooleanField(default=False)


def get_upload_to(instance, filename):

    date = datetime.now()
    date = date.strftime("%m-%d-%Y-%H")  # to delete Time
    date = date.split('-')
    return 'files/{3}-{1}-{0}-{2}/{4}'.format(date[0], date[1], date[2], date[3], filename)


class UploadedFile(models.Model):
    file = models.FileField(blank=True, null=True, upload_to=get_upload_to)
    uploaded_at = models.DateTimeField(auto_now_add=True)


class GZIDATA(models.Model):
    UNDERLYING = models.TextField(default="", null=True, blank=True)
    SECTYPE = models.TextField(default="", null=True, blank=True)
    EXCHANGE = models.TextField(default="", null=True, blank=True)
    BIODATA = models.TextField(default="", null=True, blank=True)
    CRYPTODATA = models.TextField(default="", null=True, blank=True)
    FINDATA = models.TextField(default="", null=True, blank=True)


class FindataAttribute(models.Model):
    GZIDATA = models.ForeignKey(
        GZIDATA, on_delete=models.CASCADE, null=True, blank=True)

    EXCHANGE = models.CharField(max_length=255, default="")
    ISSUER_COUNTRY = models.CharField(max_length=255, default="")
    TRADING_CURRENCY = models.CharField(max_length=255, default="")
    SECTOR = models.CharField(max_length=255, default="")
    INDUSTRY = models.CharField(max_length=255, default="")
    CATEGORY = models.CharField(max_length=255, default="")
    FINANCIAL_INSTRUMENT = models.CharField(max_length=255, default="")
    LAST_DOLLAR = models.CharField(max_length=255, default="")
    LAST = models.CharField(max_length=255, default="")
    LOW_PRICE = models.CharField(max_length=255, default="")
    HIGH_PRICE = models.CharField(max_length=255, default="")
    CHANGE_PERCENTAGE = models.CharField(max_length=255, default="")
    RELATIVE_PRICE_PERCENT_CHANGE_YTD = models.CharField(
        max_length=255, default="")
    BETA = models.CharField(max_length=255, default="")
    QUICK_RATIO = models.CharField(max_length=255, default="")
    CURRENT_RATIO = models.CharField(max_length=255, default="")
    MARKET_CAP = models.CharField(max_length=255, default="")
    CURRENT_ENTERPRISE_VALUE = models.CharField(max_length=255, default="")
    ENTERPRISE_VALUE_TO_EBITDA_TTM = models.CharField(
        max_length=255, default="")
    SHARES_OUTSTANDING = models.CharField(max_length=255, default="")
    INST_SHARES_HELD = models.CharField(max_length=255, default="")
    INSIDER_SHARES_OWNED = models.CharField(max_length=255, default="")
    EPS_GROWTH = models.CharField(max_length=255, default="")
    REVENUE_GROWTH_RATE = models.CharField(max_length=255, default="")
    EPS_GROWTH_CURRENT_YEAR = models.CharField(max_length=255, default="")
    EPS_CHANGE_Y_Y = models.CharField(max_length=255, default="")
    EPS_CHANGE_TTM = models.CharField(max_length=255, default="")
    REVENUE_CHANGE_TTM = models.CharField(max_length=255, default="")
    REVENUE_CHANGE_Y_Y = models.CharField(max_length=255, default="")
    EPS_EXC_EXTR_ITEMS = models.CharField(max_length=255, default="")
    EPS_EXCLUDING_EXTRAORDINARY_ITEMS = models.CharField(
        max_length=255, default="")
    EPS_NORMALIZED = models.CharField(max_length=255, default="")
    EARNINGS_PER_SHARE = models.CharField(max_length=255, default="")
    ANALYST_FORECAST_OF_EPS = models.CharField(max_length=255, default="")
    P_E_CURRENT_YEAR = models.CharField(max_length=255, default="")
    FORWARD_P_E = models.CharField(max_length=255, default="")
    P_E_NORMALIZED = models.CharField(max_length=255, default="")
    P_E = models.CharField(max_length=255, default="")
    P_E_TO_GROWTH_CURRENT_YEAR = models.CharField(max_length=255, default="")
    BOOK_VALUE_COMMON_EQUITY_PER_SHARE = models.CharField(
        max_length=255, default="")
    PRICE_BOOK = models.CharField(max_length=255, default="")
    PRICE_BOOK_VALUE_CURRENT_YEAR = models.CharField(
        max_length=255, default="")
    BOOK_VALUE_TANGIBLE_PER_SHARE = models.CharField(
        max_length=255, default="")
    PRICE_TANG_BOOK_RATIO = models.CharField(max_length=255, default="")
    BOOK_VALUE_PER_SHARE_CURRENT_YEAR = models.CharField(
        max_length=255, default="")
    REVENUE = models.CharField(max_length=255, default="")
    PRICE_TO_REVENUES_MRQ = models.CharField(max_length=255, default="")
    REVENUE_SHARE = models.CharField(max_length=255, default="")
    REVENUE_SHARE_MRY = models.CharField(max_length=255, default="")
    REVENUE_EMPLOYEE_TTM = models.CharField(max_length=255, default="")
    FREE_CASH_FLOW_TTM = models.CharField(max_length=255, default="")
    FREE_CASH_FLOW_PER_SHARE_TTM = models.CharField(max_length=255, default="")
    PRICE_TO_FREE_CASH_FLOW_PER_SHARE_TTM = models.CharField(
        max_length=255, default="")
    CASH_PER_SHARE = models.CharField(max_length=255, default="")
    CASH_FLOW_PER_SHARE = models.CharField(max_length=255, default="")
    PRICE_TO_CASH_FLOW_PER_SHARE = models.CharField(max_length=255, default="")
    CASH_FLOW_PER_SHARE_MRY = models.CharField(max_length=255, default="")
    PRICE_TO_CASH_FLOW_PER_SHARE_MRQ = models.CharField(
        max_length=255, default="")
    FORWARD_PRICE_CASH_FLOW = models.CharField(max_length=255, default="")
    PRICE_CASH_FLOW_CURRENT_YEAR = models.CharField(max_length=255, default="")
    CASH_AND_SHORT_TERM_INVESTMENTS_MRQ = models.CharField(
        max_length=255, default="")
    CASH_FROM_OPERATING_ACTIVITIES_MRY = models.CharField(
        max_length=255, default="")
    CASH_FROM_OPERATING_ACTIVITIES_MRQ = models.CharField(
        max_length=255, default="")
    INVESTING_CASH_FLOW_ITEMS_MRY = models.CharField(
        max_length=255, default="")
    INVESTING_CASH_FLOW_ITEMS_MRQ = models.CharField(
        max_length=255, default="")
    FINANCING_CASH_FLOW_ITEMS_MRY = models.CharField(
        max_length=255, default="")
    FINANCING_CASH_FLOW_ITEMS_MRQ = models.CharField(
        max_length=255, default="")
    PRICE_TO_SALES = models.CharField(max_length=255, default="")
    PRICE_TO_SALES_CURRENT_YEAR = models.CharField(max_length=255, default="")
    NET_DEBT = models.CharField(max_length=255, default="")
    LFI = models.CharField(max_length=255, default="")
    TOTAL_DEBT_TOTAL_EQUITY = models.CharField(max_length=255, default="")
    LT_DEBT_EQUITY = models.CharField(max_length=255, default="")
    TOTAL_LONG_TERM_DEBT_MRQ = models.CharField(max_length=255, default="")
    NOTES_PAYABLE_SHORT_TERM_DEBT_MRY = models.CharField(
        max_length=255, default="")
    NOTES_PAYABLE_SHORT_TERM_DEBT_MRQ = models.CharField(
        max_length=255, default="")
    TOTAL_COMMON_EQUITY_MRQ = models.CharField(max_length=255, default="")
    NET_ISSUANCE_OF_DEBT_MRY = models.CharField(max_length=255, default="")
    NET_ISSUANCE_OF_DEBT_MRQ = models.CharField(max_length=255, default="")
    NET_ISSUANCE_OF_STOCK_MRY = models.CharField(max_length=255, default="")
    NET_ISSUANCE_OF_STOCK_MRQ = models.CharField(max_length=255, default="")
    NET_INCOME_EMPLOYEE_TTM = models.CharField(max_length=255, default="")
    NET_INCOME_AVAILABLE_TO_COMMON = models.CharField(
        max_length=255, default="")
    NORMALIZED = models.CharField(max_length=255, default="")
    NET_INCOME_AVAILABLE_TO_COMMON_TWO = models.CharField(
        max_length=255, default="")
    OPERATING_INCOME_MRY = models.CharField(max_length=255, default="")
    OPERATING_INCOME_MRQ = models.CharField(max_length=255, default="")
    NET_PROFIT_MARGIN = models.CharField(max_length=255, default="")
    OPERATING_MARGIN = models.CharField(max_length=255, default="")
    GROSS_MARGIN = models.CharField(max_length=255, default="")
    PRETAX_MARGIN_TTM = models.CharField(max_length=255, default="")
    PRETAX_MARGIN = models.CharField(max_length=255, default="")
    TOTAL_CURRENT_ASSETS_MRY = models.CharField(max_length=255, default="")
    TOTAL_CURRENT_ASSETS_MRQ = models.CharField(max_length=255, default="")
    TOTAL_ASSETS_MRQ = models.CharField(max_length=255, default="")
    TOTAL_CURRENT_LIABILITIES_MRY = models.CharField(
        max_length=255, default="")
    TOTAL_CURRENT_LIABILITIES_MRQ = models.CharField(
        max_length=255, default="")
    TOTAL_LIABILITIES_MRQ = models.CharField(max_length=255, default="")
    RETURN_ON_EQUITY_CURRENT_YEAR = models.CharField(
        max_length=255, default="")
    RETURN_ON_EQUITY = models.CharField(max_length=255, default="")
    RETURN_ON_INVESTMENT_MRY = models.CharField(max_length=255, default="")
    RETURN_ON_INVESTMENT = models.CharField(max_length=255, default="")
    RETURN_ON_AVERAGE_ASSETS_MRY = models.CharField(max_length=255, default="")
    RETURN_ON_AVERAGE_ASSETS_PERCENTAGE = models.CharField(
        max_length=255, default="")
    IMBALANCE = models.CharField(max_length=255, default="")
    IMBALANCE_PERCENTAGE = models.CharField(max_length=255, default="")
    PAYOUT_RATIO_PERCENTAGE = models.CharField(max_length=255, default="")
    DIVIDEND_YIELD_5_YR_AVG = models.CharField(max_length=255, default="")
    DIVIDEND_YIELD_TTM_PERCENTAGE = models.CharField(
        max_length=255, default="")
    DIVIDEND_YIELD_PERCENTAGE = models.CharField(max_length=255, default="")
    DIVIDEND_PER_SHARE_5_YR_AVG = models.CharField(max_length=255, default="")
    DIVIDEND_YIELD = models.CharField(max_length=255, default="")
    DIVIDEND_DATE = models.CharField(max_length=255, default="")
    DIVIDENDS = models.CharField(max_length=255, default="")
    DIVIDENDS_TTM = models.CharField(max_length=255, default="")
    FORWARD_DIVIDEND_YIELD = models.CharField(max_length=255, default="")
    DIVIDEND_YIELD_CURRENT_YEAR = models.CharField(max_length=255, default="")
    DIVIDENDS_PER_SHARE_CURRENT_YEAR = models.CharField(
        max_length=255, default="")
    PERCENTAGE_OF_NET_LIQ = models.CharField(max_length=255, default="")
    IMPLIED_VOL_PERCENTAGE = models.CharField(max_length=255, default="")
    HIST_VOL_PERCENTAGE = models.CharField(max_length=255, default="")
    IMPLIED_VOL_HIST_VOL = models.CharField(max_length=255, default="")
    OPT_IMPLIED_VOLATILITY = models.CharField(max_length=255, default="")

    WEEK_IV_RANK_52 = models.CharField(max_length=255, default="")
    WEEK_HV_RANK_52 = models.CharField(max_length=255, default="")
    WEEK_IV_PERCENTILE_52 = models.CharField(max_length=255, default="")
    WEEK_HV_PERCENTILE_52 = models.CharField(max_length=255, default="")
    WEEK_IV_HIGH_52 = models.CharField(max_length=255, default="")
    WEEK_HV_HIGH_52 = models.CharField(max_length=255, default="")
    WEEK_IV_LOW_52 = models.CharField(max_length=255, default="")
    WEEK_HV_LOW_52 = models.CharField(max_length=255, default="")

    WEEK_IV_RANK_26 = models.CharField(max_length=255, default="")
    WEEK_HV_RANK_26 = models.CharField(max_length=255, default="")
    WEEK_IV_PERCENTILE_26 = models.CharField(max_length=255, default="")
    WEEK_HV_PERCENTILE_26 = models.CharField(max_length=255, default="")
    WEEK_IV_HIGH_26 = models.CharField(max_length=255, default="")
    WEEK_HV_HIGH_26 = models.CharField(max_length=255, default="")
    WEEK_IV_LOW_26 = models.CharField(max_length=255, default="")
    WEEK_HV_LOW_26 = models.CharField(max_length=255, default="")

    WEEK_IV_RANK_13 = models.CharField(max_length=255, default="")
    WEEK_HV_RANK_13 = models.CharField(max_length=255, default="")
    WEEK_IV_PERCENTILE_13 = models.CharField(max_length=255, default="")
    WEEK_HV_PERCENTILE_13 = models.CharField(max_length=255, default="")
    WEEK_IV_HIGH_13 = models.CharField(max_length=255, default="")
    WEEK_HV_HIGH_13 = models.CharField(max_length=255, default="")
    WEEK_IV_LOW_13 = models.CharField(max_length=255, default="")
    WEEK_HV_LOW_13 = models.CharField(max_length=255, default="")

#
# class find_data_attribute_sub_type(models.Model):
#     find_data_attribute = models.ForeignKey(find_data_attribute, on_delete=models.CASCADE)
#     sub_attribute = models.CharField(max_length=255)
