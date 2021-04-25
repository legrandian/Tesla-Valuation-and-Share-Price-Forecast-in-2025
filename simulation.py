import numpy as np
import pandas as pd
from model import TeslaValuation

class MonteCarlo:
    def __init__(self):
        self.simResults = pd.DataFrame(columns=list(range(len(TeslaValuation.columns))))
        self.simResults.columns = pd.MultiIndex.from_tuples(TeslaValuation.columns)

    def simulate(self, count):
        self.simResults = self.simResults[0:0]
        for i in range(count):
            tesla = TeslaValuation()
            
            params = self.getRandomizedParams()
            tesla.setAssumptions(
                params["maxGrossMargin"], 
                params["capitalEfficiency"], 
                params["fractionInHumanDriveRideHailNetwork"], 
                params["fractionInAutonomousFleet"], 
                params["avgMarketCapEquityRaised"], 
                params["equityRaiseForCapex"], 
                params["equityRaiseForIncentiveCompensation"], 
                params["fractionDebtFundedFactoryBuild"], 
                params["wrightsLawLearningRate"], 
                params["maxAnnualProductionIncrease"], 
                params["factoryUtilizationFactor"], 
                params["segmentPenetrationPercentage"], 
                params["taxRate"], 
                params["interestRate"], 
                params["percentageCarsSoldWithInsurance"], 
                params["insuranceCommission"], 
                params["premiumPerMile"], 
                params["rideHailInsurancePremiumAddition"], 
                params["beginningLossRatio"], 
                params["annualSafetyIncrease"], 
                params["milesPerCarPerYear"], 
                params["milesPerYearPerCar"], 
                params["platformFeeAtScale"], 
                params["milesPerRobotaxi"], 
                params["autonomousPlatformFee"], 
                params["autonomousPlatformFeeChina"], 
                params["fleetPercentageChina"], 
                params["sgaPercentageEVSales"], 
                params["rdPercentageEVSales"], 
                params["autonomousEBITDAMargin"], 
                params["enterpriseMultipleEV"], 
                params["enterpriseMultipleInsurance"], 
                params["enterpriseMultipleRobotaxis"]
            )
            tesla.addRowFromRealData(2019, 365232, 367656,
                            20821000000, 4423000000, 0.11, 0.05, 
                            14130000000, 3734000000, 10396000000, 
                            1436000000, 11634000000, 
                            0.06, 6268000000,
                            24578000000, 0.21, 
                            959853504, 90)
            tesla.addRowFromRealData(2020, 509737, 499647,
                            27236000000, 6977000000, 0.1, 0.05, 
                            17864000000, 5117000000, 12747000000, 
                            12469000000, 9556000000, 
                            0.06, 19384000000,
                            
                            31536000000, 0.26, 
                            959853504, 700)
            for yr in range(2021, 2026):
                tesla.addSimulatedRow(yr, TeslaValuation.ASPByYear[str(yr)], TeslaValuation.pricePerMileByYear[str(yr)])
            
            row2025 = tesla.df[tesla.df[('', TeslaValuation.yearCol)] == 2025]
            self.simResults = self.simResults.append(row2025, ignore_index=True)

    def getRandomizedParams(self):
        params = {
            "maxGrossMargin": self.sampleFromNormal(0.2, 0.4, 0.6, 0.8),
            "capitalEfficiency": self.sampleFromNormal(4000, 13000, 5000, 17000),
            "fractionInHumanDriveRideHailNetwork": self.sampleFromNormal(0,	0.2, 0.6, 0.7),
            "fractionInAutonomousFleet": self.sampleFromNormal(0.05, 0.4, 0.6, 0.9) if np.random.random_sample() < 0.5 else 0,
            "avgMarketCapEquityRaised": self.sampleFromNormal(500000000000, 700000000000, 1000000000000, 2000000000000),
            "equityRaiseForCapex": 0,
            "equityRaiseForIncentiveCompensation": 3000000000,
            "fractionDebtFundedFactoryBuild": self.sampleFromNormal(0, 0.4, 0.8, 0.95),
            "wrightsLawLearningRate": self.sampleFromNormal(0.1, 0.135, 0.165, 0.2),
            "maxAnnualProductionIncrease": self.sampleFromNormal(0.2, 0.5, 1.1, 5),
            "factoryUtilizationFactor": self.sampleFromNormal(0.7, 0.95, 0.99, 1),
            "segmentPenetrationPercentage": self.sampleFromNormal(0.1, 0.15, 0.3, 0.7),
            "taxRate": self.sampleFromNormal(0.15, 0.15, 0.25, 0.25),
            "interestRate": self.sampleFromNormal(0.02, 0.035, 0.08, 0.08),
            "percentageCarsSoldWithInsurance": self.sampleFromNormal(0, 0.2, 0.6, 1),
            "insuranceCommission": self.sampleFromNormal(0.1, 0.12, 0.14, 0.15),
            "premiumPerMile": self.sampleFromNormal(0.14, 0.17, 0.19, 0.24),
            "rideHailInsurancePremiumAddition": self.sampleFromNormal(0.1, 0.26, 0.3, 0.4),
            "beginningLossRatio": self.sampleFromNormal(0.65, 0.75, 0.7, 0.8),
            "annualSafetyIncrease": self.sampleFromNormal(0, 0.02, 0.1, 0.25),
            "milesPerCarPerYear": self.sampleFromNormal(10000, 11500, 13500, 15000),
            "milesPerYearPerCar": self.sampleFromNormal(0, 20000, 40000, 60000),
            "platformFeeAtScale": self.sampleFromNormal(0.2, 0.25, 0.4, 0.5),
            "milesPerRobotaxi": self.sampleFromNormal(30000, 90000, 130000, 160000),
            "autonomousPlatformFee": self.sampleFromNormal(0.2, 0.4, 0.6, 0.7),
            "autonomousPlatformFeeChina": self.sampleFromNormal(0.05, 0.1, 0.2, 0.35),
            "fleetPercentageChina": self.sampleFromNormal(0.15, 0.25, 0.3, 0.5),
            "sgaPercentageEVSales": self.sampleFromNormal(0.08, 0.09, 0.11, 0.12),
            "rdPercentageEVSales": self.sampleFromNormal(0.03, 0.04, 0.06, 0.09),
            "autonomousEBITDAMargin": self.sampleFromNormal(0.2, 0.4, 0.6, 0.8),
            "enterpriseMultipleEV": 13,
            "enterpriseMultipleInsurance": 10,
            "enterpriseMultipleRobotaxis": 19,
        }
        return params

    def sampleFromNormal(self, min, leftStd, rightStd, max):
        mean = leftStd + (rightStd - leftStd)/2
        std = abs(rightStd - mean)
        rand = np.random.normal(mean, std)
        if rand > max:
            return max
        if rand < min:
            return min
        return rand

    def getResults(self):
        return self.simResults