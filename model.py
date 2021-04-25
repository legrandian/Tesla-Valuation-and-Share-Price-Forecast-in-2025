import numpy as np
import pandas as pd

class TeslaValuation:

    evCol = "Electric Vehicles"
    insCol = "Insurance"
    rhHumanCol = "Ride-hail, Human driven"
    rhAutoCol = "Ride-hail, Autonomous"
    rhCombinedCol = "Ride-hail, Combined"
    consolidatedCol = "Tesla Consolidated"

    yearCol = "Year"
    carsProdCol = "Cars Produceable (units, not in millions)"
    carsSoldCol = "Cars sold"
    cumCarsSoldCol = "Cumulative cars sold (modeled estimate)"
    ASPCol = "ASP (not in millions)"
    revenueEVCol = "Revenue (EV business only, ex credits)"
    partLaborOtherCostPerVehicleCol = "Part and labor and other cost per vehicle (not in millions)"
    capConsumedPerVehicleCol = "Capital consumed per vehicle"
    totalCOGsPerVehicleCol = "Total COGs per vehicle"
    grossMarginCol = "Gross Margin (ex credits)"
    grossProfitCol = "Gross Profit"
    SGACol = "SG&A"
    SGAOverSalesCol = "SG&A/Sales"
    RDCol = "R&D"
    RDOverSalesCol = "R&D/Sales"
    EBITEVCol = "EBIT (EV business only)"
    EBITMarginCol = "EBIT margin"
    grossPPECol = "Gross property, plant and equipment"
    accumDeprCol = "Accumulated depreciation"
    annualDeprCol = "Annual depreciation"
    netPPECol = "Net property, plant and equipment"
    deprOverGrossPPECol = "Depreciation/Gross PP&E"
    workingCapDaysCol = "Working capital days"
    workingCapCol = "Working capital"
    totalLongTermDebtCol = "Total long term debt"
    avgInterestPaidCol = "Average interest paid (%)"
    yearEndCashForInvestCol = "Year end cash for investment (includes anticipated equity raise)"
    maxCashDeployableCol = "Max cash deployable given scaling constraint"
    spilloverCashNotDeployedCol = "Spillover cash not deployed"

    percCarsSoldWithInsuranceCol = "Percent of cars sold with insurance (non ride-hail cars)"
    carsInsuredCol = "Cars Insured (non ride-hail cars, not in millions)"
    cumNonRideHailCarsInsuredCol = "Cumulative non ride-hail cars insured (not in millions)"
    personalCarInsuranceMilesCol = "Personal Car Insurance miles"
    humanDrivenRideHailInsuranceMilesCol = "Human Driven Ride-hail insurance miles"
    premiumOverMileCol = "Premium/mile (not in millions)"
    rideHailPremiumOverMileCol = "Ride-hail premium/mile (not in millions)"
    grossPremiumsCol = "Gross premiums"
    teslaCommissionCol = "Tesla commission"
    teslaInsuranceRevenueCol = "Tesla Insurance revenue"
    benefitCostPerMileHumanDrivenPersonalCarCol = "Benefit cost per mile human driven personal car"
    benefitCostPerMileHumanDrivenRideHailCol = "Benefit cost per mile human driven ride-hail"
    totalBenefitCostCol = "Total Benefit cost"
    benefitCostOverSalesCol = "Benefits cost/sales"
    EBITOverSalesCol = "EBIT/sales"
    EBITCol = "EBIT"

    percCarsSoldIntoHumanDrivenRideHailNetCol = "% of cars sold into human driven ride-hail network"
    percRideHailCarsInAutonomousNetCol = "% of ride-hail cars fed into autonomous network"
    humanRideHailCarsAddedAnnuallyCol = "Human ride-hail cars added annually (not in millions)"
    cumHumanRideHailCarsCol = "Cumulative human ride-hail cars (not in millions)"
    milesPerYearPerHumanDrivenRideHailCarCol = "Miles per year per human-driven ride-hail car (not in millions)"
    totalHumanDrivenMilesCol = "Total human-driven miles (not in millions)"
    humanRideHailPlatformCutCol = "Human Ridehail Platform cut"

    fullyAutonomousCapableFleetCol = "Fully Autonomous Capable Fleet (not in millions)"
    percFleetInChinaCol = "% of fleet in China"
    percFleetRobotaxiPlatformCol = "% of Teslas on robotaxi platform"
    cumRobotaxisCol = "Tesla robotaxis cumulative (not in millions)"
    potentialMilesPerRobotaxiCol = "Potential miles per Taxi (not in millions)"
    totalRobotaxiMilesCol = "Total robotaxi miles (not in millions)"
    autonomousPlatformCutExChinaCol = "Autonomous Platform cut ex China"
    autonomousPlatformCutInChinaCol = "Autonomous Platform cut in China"

    totalRideHailMilesCol = "Total ride-hail miles (not in millions)"
    pricePerMileCol = "Price per mile"
    grossRideHailBillingsCol = "Gross Ride-hail Billings"
    netRideHailRevenueCol = "Net Ride-hail Revenue"
    EBITDAMarginCol = "EBITDA Margin"
    EBITDACol = "EBITDA"
    cashFromRideHailCol = "Cash from Ridehail"

    totalRevenueCol = "Total Revenue"
    totalEBITCol = "Total EBIT"
    totalEBITDACol = "Total EBITDA"
    debtToEBITDACol = "Debt to EBITDA"
    interestPaidCol = "Interest paid"
    debtToNetPPECol = "Debt to net PP&E"
    cashGenerationCol = "Cash generation"
    totalGrossMarginCol = "Total Gross Margin"
    totalEBITDAMarginCol = "Total EBITDA Margin"
    enterpriseValueCol = "Enterprise Value"
    marketCapCol = "Market Cap"
    sharesOutstandingCol = "Shares Outstanding"
    stockPriceCol = "Stock Price"
    cashFlowYieldCol = "Cash flow yield"

    columns = [
        ('', yearCol),
        
        (evCol, carsProdCol),
        (evCol, carsSoldCol),
        (evCol, cumCarsSoldCol),
        (evCol, ASPCol),
        (evCol, revenueEVCol),
        (evCol, partLaborOtherCostPerVehicleCol),
        (evCol, capConsumedPerVehicleCol),
        (evCol, totalCOGsPerVehicleCol),
        (evCol, grossMarginCol),
        (evCol, grossProfitCol),
        (evCol, SGACol),
        (evCol, SGAOverSalesCol),
        (evCol, RDCol),
        (evCol, RDOverSalesCol),
        (evCol, EBITEVCol),
        (evCol, EBITMarginCol),
        (evCol, grossPPECol),
        (evCol, accumDeprCol),
        (evCol, annualDeprCol),
        (evCol, netPPECol),
        (evCol, deprOverGrossPPECol),
        (evCol, workingCapDaysCol),
        (evCol, workingCapCol),
        (evCol, totalLongTermDebtCol),
        (evCol, avgInterestPaidCol),
        (evCol, yearEndCashForInvestCol),
        (evCol, maxCashDeployableCol),
        (evCol, spilloverCashNotDeployedCol),
        
        (insCol, percCarsSoldWithInsuranceCol),
        (insCol, carsInsuredCol),
        (insCol, cumNonRideHailCarsInsuredCol),
        (insCol, personalCarInsuranceMilesCol),
        (insCol, humanDrivenRideHailInsuranceMilesCol),
        (insCol, premiumOverMileCol),
        (insCol, rideHailPremiumOverMileCol),
        (insCol, grossPremiumsCol),
        (insCol, teslaCommissionCol),
        (insCol, teslaInsuranceRevenueCol),
        (insCol, benefitCostPerMileHumanDrivenPersonalCarCol),
        (insCol, benefitCostPerMileHumanDrivenRideHailCol),
        (insCol, totalBenefitCostCol),
        (insCol, benefitCostOverSalesCol),
        (insCol, EBITOverSalesCol),
        (insCol, EBITCol),
        
        (rhHumanCol, percCarsSoldIntoHumanDrivenRideHailNetCol),
        (rhHumanCol, percRideHailCarsInAutonomousNetCol),
        (rhHumanCol, humanRideHailCarsAddedAnnuallyCol),
        (rhHumanCol, cumHumanRideHailCarsCol),
        (rhHumanCol, milesPerYearPerHumanDrivenRideHailCarCol),
        (rhHumanCol, totalHumanDrivenMilesCol),
        (rhHumanCol, humanRideHailPlatformCutCol),
        
        (rhAutoCol, fullyAutonomousCapableFleetCol),
        (rhAutoCol, percFleetInChinaCol),
        (rhAutoCol, percFleetRobotaxiPlatformCol),
        (rhAutoCol, cumRobotaxisCol),
        (rhAutoCol, potentialMilesPerRobotaxiCol),
        (rhAutoCol, totalRobotaxiMilesCol),
        (rhAutoCol, autonomousPlatformCutExChinaCol),
        (rhAutoCol, autonomousPlatformCutInChinaCol),
        
        (rhCombinedCol, totalRideHailMilesCol),
        (rhCombinedCol, pricePerMileCol),
        (rhCombinedCol, grossRideHailBillingsCol),
        (rhCombinedCol, netRideHailRevenueCol),
        (rhCombinedCol, EBITDAMarginCol),
        (rhCombinedCol, EBITDACol),
        (rhCombinedCol, cashFromRideHailCol),
        
        (consolidatedCol, totalRevenueCol),
        (consolidatedCol, totalEBITCol),
        (consolidatedCol, totalEBITDACol),
        (consolidatedCol, debtToEBITDACol),
        (consolidatedCol, interestPaidCol),
        (consolidatedCol, debtToNetPPECol),
        (consolidatedCol, cashGenerationCol),
        (consolidatedCol, totalGrossMarginCol),
        (consolidatedCol, totalEBITDAMarginCol),
        (consolidatedCol, enterpriseValueCol),
        (consolidatedCol, marketCapCol),
        (consolidatedCol, sharesOutstandingCol),
        (consolidatedCol, stockPriceCol),
        (consolidatedCol, cashFlowYieldCol),
    ]

    ASPByYear = {
        "2021": 57405, 
        "2022": 54136, 
        "2023": 53486, 
        "2024": 44304, 
        "2025": 36108, 
    }
    pricePerMileByYear = {
        "2021": 4,
        "2022": 3.09692644494456,
        "2023": 2.01014844533137,
        "2024": 1.0667142088479,
        "2025": 0.621379222980201,
    }

    def __init__(self):
        # Key drivers

        # Gross margin is driven by Wright's Law. 
        # This input is the max gross margin that the model allows Tesla to achieve on electric vehicles; 
        # if Tesla were to feel competitive pressure it could continue to add range/battery capacity to its vehicles 
        # and so generate less gross profit than Wright's Law would otherwise suggest. 
        # For more on Wright's Law, see: https://ark-invest.com/wrights-law/ 
        self.maxGrossMargin = 0.25 
        # Capital efficiency (gross capex per unit production, not in millions)
        # The cost per unit of new production capacity. Lower = more efficient
        self.capitalEfficiency = 6000
        # Provides an upper bound for vehicle production 
        # to accommodate management bandwidth constraints in building out factories.
        self.maxAnnualProductionIncrease = 0.9
        # % of cars sold into human driven ride-hail network in 2025
        self.fractionInHumanDriveRideHailNetwork = 0.4
        # % of all Teslas in autonomous fleet in 2025
        self.fractionInAutonomousFleet = 0.6

        # Balance sheet assumptions

        # Percent of factory-build debt-funded. Determines how much debt Tesla raises as it scales
        self.fractionDebtFundedFactoryBuild = 0.6
        # Weighted average market cap at which equity raised. 
        # Determines the amount equity dilution Tesla takes on. 
        # For simplicity all equity raises happen at this value.
        self.avgMarketCapEquityRaised = 800000000000
        # Equity raise for capex. 
        # Tesla raised $7 billion in equity in 2020. 
        # ARK estimates Tesla will not need to raise additional capital in the next 5 years.
        self.equityRaiseForCapex = 0
        # Equity raise for incentive compensation. 
        # For simplicity all raises for incentive comp use [weighted average market cap at which equity raised] line
        self.equityRaiseForIncentiveCompensation = 3000000000

        # Margin assumptions

        # Wright's Law learning rate. The percent cost decline for every cumulative doubling of production.
        self.wrightsLawLearningRate = 0.15
        # Factory utilization factor. 
        # This is relative to Tesla's historical utilization rates. Applied uniformly across all years. 
        self.factoryUtilizationFactor = 0.95
        # Percent of each model/price segment that Tesla penetrates.
        # Provides an upper bound for addressable market within each vehicle segment.
        self.segmentPenetrationPercentage = 0.25
        # Tax rate. Tax loss carry-forwards are not built into this model.
        self.taxRate = 0.2
        # Interest rate. Applied uniformly across all years for simplicity.
        self.interestRate = 0.06


        # Insurance assumptions

        # % of cars sold with Tesla insurance in 2025
        self.percentageCarsSoldWithInsurance = 0.4
        # Tesla comission as an insurance agent
        self.insuranceCommission = 0.12
        # Premium/mile for personally owned Tesla car (not in millions)
        self.premiumPerMile = 0.18
        # Ride-hail insurance premium addition
        self.rideHailInsurancePremiumAddition = 0.05 / self.premiumPerMile
        # Beginning loss ratio (when Tesla first begins underwriting its own policies)
        self.beginningLossRatio = 0.7
        # Annual safety increase of Tesla cars (% safer)
        self.annualSafetyIncrease = 0.05
        # Miles per personal car per year (not in millions)
        self.milesPerCarPerYear = 13500

        # Ride-hail assumptions

        # Miles per year per car (not in millions)
        self.milesPerYearPerCar = 30000
        # Platform fee at scale
        self.platformFeeAtScale = 0.3

        # Autonomous assumptions

        # Miles traveled per robotaxi (not in millions): 110k ~= 16 hours per day at 20 miles per hour.			
        self.milesPerRobotaxi = 110000
        # Tesla platform fee. 
        # We believe autonomous platforms will be able to command a fee on the high end because they will offer more value.
        # https://ark-invest.com/research/autonomous-ridehailing-fees
        self.autonomousPlatformFee = 0.5
        # Tesla platform fee China. Assumes that Chinese partners capture some of the China monetization.
        self.autonomousPlatformFeeChina = 0.1
        # % of fleet in China. Only relevant for the autonomous platform fee calculation. 
        # Value stays the same across all years for simplicity.
        self.fleetPercentageChina = 0.33

        # Valuation assumption

        # SG&A as % of electric vehicle sales. Roughly comparable to premium auto competitors
        self.sgaPercentageEVSales = 0.1
        # R&D as % of electric vehicle sales. Roughly comparable to premium auto competitors
        self.rdPercentageEVSales = 0.05
        # Autonomous EBITDA margin. This is margin on net platform fee revenues.
        self.autonomousEBITDAMargin = 0.5
        # EV=Enterprise Value = (Market capitalization) + (total debt) − (cash and cash equivalents)
        # EBITDA=Earnings before interest, taxes, depreciation and amortization
        # Enterprise Multiple = EV / EBITDA for electric vehicle business. Daimler is 12.5 as of 3/17/21 source:ycharts
        self.enterpriseMultipleEV = 13
        # Enterprise Multiple = EV / EBITDA for insurance business. Roughly equivolent to industry average
        # http://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/vebitda.html
        self.enterpriseMultipleInsurance = 10
        # Enterprise Multiple = EV / EBITDA for autonomous robotaxi business. Much less than industry average for software.
        # http://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/vebitda.html
        self.enterpriseMultipleRobotaxis = 19.2

        # Dataframe
        self.df = pd.DataFrame(columns=list(range(len(self.columns))))
        self.df.columns = pd.MultiIndex.from_tuples(self.columns)

    def getRowByYear(self, year):
        return self.df[self.df[('', self.yearCol)] == year]

    def getRowFromRealData(self, year, carsProd, carsSold,
                 revenueEV, grossProfit, SGAOverSales, RDOverSales, 
                 grossPPE, accumDepr, netPPE, 
                 workingCap, totalLongTermDebt, 
                 avgInterestPaid, yearEndCashForInvest,
                 
                 totalRevenue, totalGrossMargin, 
                 sharesOutstanding, stockPrice):
    
        lastYearRow = self.getRowByYear(year - 1)
        nextYearRow = self.getRowByYear(year + 1)
        
        # TESLA AUTOMOTIVE
        
        if len(lastYearRow) == 0:
            cumCarsSold = 800000
        else:
            cumCarsSold = lastYearRow[(self.evCol, self.cumCarsSoldCol)].values[0] + carsSold
        
        ASP = revenueEV / carsProd


        grossMargin = grossProfit / revenueEV
        
        # REVIEW: depreciation / gross PPE 11% for 2019, 9% for rest?
        deprOverGrossPPE = 0.09
        annualDepr = grossPPE * deprOverGrossPPE
        capConsumedPerVehicle = annualDepr / carsSold
        
        partLaborOtherCostPerVehicle = ASP * (1 - grossMargin) - capConsumedPerVehicle        
        totalCOGsPerVehicle = max(sum([capConsumedPerVehicle, partLaborOtherCostPerVehicle]), (1 - self.maxGrossMargin) * ASP)
        
        # REVIEW: SGAOverSales is supposed to mean SG&A as a percentage of total revenue
        # Here, only revenue from EV sales is considered
        # Same for R&D, EBIT
        SGA = revenueEV * SGAOverSales
        RD = revenueEV * RDOverSales
        
        # REVIEW: 
        EBITEV = grossProfit - SGA - RD
        EBITMargin = EBITEV / revenueEV
        
        # REVIEW: again, total working capital is used while revenue for EV business is used for calculations
        workingCapDays = workingCap / revenueEV

        if year == 2019:
            nextYearCarsProd = 509737
        else:
            nextYearCarsProd = (grossPPE - lastYearRow[(self.evCol, self.grossPPECol)].values[0]) / self.capitalEfficiency + carsProd
        maxCashDeployable = nextYearCarsProd * self.maxAnnualProductionIncrease * self.capitalEfficiency * (1 - self.fractionDebtFundedFactoryBuild)
        
        if yearEndCashForInvest - maxCashDeployable > 0:
            spilloverCashNotDeployed = yearEndCashForInvest - maxCashDeployable
        elif yearEndCashForInvest < 0:
            spilloverCashNotDeployed = yearEndCashForInvest
        else:
            spilloverCashNotDeployed = 0 
            
        # TESLA RIDE HAIL AUTONOMOUS

        fullyAutonomousCapableFleet = cumCarsSold - 200000
        percFleetInChina = self.fleetPercentageChina
            
        # TESLA RIDE HAIL HUMAN DRIVEN
        if year > 2019:
            percCarsSoldIntoHumanDrivenRideHailNet = 0
            percRideHailCarsInAutonomousNet = 0
            humanRideHailCarsAddedAnnually = round(percCarsSoldIntoHumanDrivenRideHailNet*carsSold - (percRideHailCarsInAutonomousNet*percCarsSoldIntoHumanDrivenRideHailNet*carsSold + percRideHailCarsInAutonomousNet*lastYearRow[(self.rhHumanCol, self.cumHumanRideHailCarsCol)].values[0]))
            cumHumanRideHailCars = 0
            milesPerYearPerHumanDrivenRideHailCar = self.milesPerYearPerCar
            totalHumanDrivenMiles = cumHumanRideHailCars * milesPerYearPerHumanDrivenRideHailCar
            humanRideHailPlatformCut = 0.2
            
        # TESLA RIDE HAIL COMBINED
        
            totalRideHailMiles = 0
            pricePerMile = 4
            grossRideHailBillings = totalRideHailMiles * pricePerMile
            totalRobotaxiMiles = 0
            autonomousPlatformCutInChina = 0
            autonomousPlatformCutExChina = 0
            netRideHailRevenue = pricePerMile * (humanRideHailPlatformCut * totalHumanDrivenMiles + totalRobotaxiMiles * (percFleetInChina * autonomousPlatformCutInChina + autonomousPlatformCutExChina * (1 - percFleetInChina)))
            EBITDAMargin = self.autonomousEBITDAMargin
            EBITDA = netRideHailRevenue * EBITDAMargin
            cashFromRideHail = EBITDA * (1 - self.taxRate - self.interestRate)
        
        # TESLA INSURANCE
            percCarsSoldWithInsurance = min(self.percentageCarsSoldWithInsurance / (2 ** (2025 - year)), self.percentageCarsSoldWithInsurance)
            carsInsured = percCarsSoldWithInsurance * carsSold * (1 - percCarsSoldIntoHumanDrivenRideHailNet)
            cumNonRideHailCarsInsured = carsInsured
            if year > 2020:
                cumNonRideHailCarsInsured = carsInsured + lastYearRow[(self.insCol, self.cumNonRideHailCarsInsuredCol)].values[0]
            personalCarInsuranceMiles = cumNonRideHailCarsInsured * self.milesPerCarPerYear
            humanDrivenRideHailInsuranceMiles = totalHumanDrivenMiles
            
            premiumOverMile = self.premiumPerMile
            if year > 2020:
                year2020 = self.getRowByYear(2020)
                premiumOverMile = self.premiumPerMile / year2020[ASP] * ASP
            
            rideHailPremiumOverMile = premiumOverMile * (1 + self.rideHailInsurancePremiumAddition)
            grossPremiums = personalCarInsuranceMiles * premiumOverMile + humanDrivenRideHailInsuranceMiles * rideHailPremiumOverMile
            teslaCommission = self.insuranceCommission
            if year > 2022:
                teslaCommission = 1
                
            teslaInsuranceRevenue = grossPremiums * teslaCommission
            
            EBIT = teslaInsuranceRevenue
        
        else:
            percCarsSoldWithInsurance = 0
            carsInsured = 0
            cumNonRideHailCarsInsured = 0
            personalCarInsuranceMiles = 0
            humanDrivenRideHailInsuranceMiles = 0
            premiumOverMile = 0
            rideHailPremiumOverMile = 0
            grossPremiums = 0
            teslaCommission = 0
            teslaInsuranceRevenue = 0
            
            percCarsSoldIntoHumanDrivenRideHailNet = 0
            percRideHailCarsInAutonomousNet = 0
            humanRideHailCarsAddedAnnually = 0
            cumHumanRideHailCars = 0
            milesPerYearPerHumanDrivenRideHailCar = 0
            totalHumanDrivenMiles = 0
            humanRideHailPlatformCut = 0
            
            totalRobotaxiMiles = 0
            autonomousPlatformCutInChina = 0
            autonomousPlatformCutExChina = 0
            
            totalRideHailMiles = 0
            pricePerMile = 0
            grossRideHailBillings = 0
            netRideHailRevenue = 0
            EBITDAMargin = 0
            EBITDA = 0
            cashFromRideHail = 0
            
            EBIT = 0

        # TESLA CONSOLIDATED
        
        totalEBIT = EBITEV + EBIT + EBITDA
        totalEBITDA = totalEBIT + annualDepr
        if year == 2020:
            totalEBIT = EBITEV + EBITDA
            totalEBITDA = totalEBIT + annualDepr + 752000000
        
        debtToEBITDA = totalLongTermDebt / totalEBITDA
        interestPaid = totalLongTermDebt * self.interestRate
        debtToNetPPE = totalLongTermDebt / netPPE
        cashGeneration = EBITEV + EBITDA + annualDepr - interestPaid - (EBITEV + EBITDA - interestPaid) * self.taxRate
        
        totalEBITDAMargin = totalEBITDA / totalRevenue
        marketCap = sharesOutstanding * stockPrice
        enterpriseValue = marketCap + totalLongTermDebt - workingCap
        
        return [
            year,
        
            carsProd,
            carsSold,
            cumCarsSold,
            ASP,
            revenueEV,
            partLaborOtherCostPerVehicle,
            capConsumedPerVehicle,
            totalCOGsPerVehicle,
            grossMargin,
            grossProfit,
            SGA,
            SGAOverSales,
            RD,
            RDOverSales,
            EBITEV,
            EBITMargin,
            grossPPE,
            accumDepr,
            annualDepr,
            netPPE,
            deprOverGrossPPE,
            workingCapDays,
            workingCap,
            totalLongTermDebt,
            avgInterestPaid,
            yearEndCashForInvest,
            maxCashDeployable,
            spilloverCashNotDeployed,

            percCarsSoldWithInsurance,
            carsInsured,
            cumNonRideHailCarsInsured,
            personalCarInsuranceMiles,
            humanDrivenRideHailInsuranceMiles,
            premiumOverMile,
            rideHailPremiumOverMile,
            grossPremiums,
            teslaCommission,
            teslaInsuranceRevenue,
            None,
            None,
            None,
            None,
            None,
            EBIT,

            percCarsSoldIntoHumanDrivenRideHailNet,
            percRideHailCarsInAutonomousNet,
            humanRideHailCarsAddedAnnually,
            cumHumanRideHailCars,
            milesPerYearPerHumanDrivenRideHailCar,
            totalHumanDrivenMiles,
            humanRideHailPlatformCut,

            fullyAutonomousCapableFleet,
            percFleetInChina,
            None,
            None,
            None,
            totalRobotaxiMiles,
            autonomousPlatformCutExChina,
            autonomousPlatformCutInChina,

            totalRideHailMiles,
            pricePerMile,
            grossRideHailBillings,
            netRideHailRevenue,
            EBITDAMargin,
            EBITDA,
            cashFromRideHail,

            totalRevenue,
            totalEBIT,
            totalEBITDA,
            debtToEBITDA,
            interestPaid,
            debtToNetPPE,
            cashGeneration,
            totalGrossMargin,
            totalEBITDAMargin,
            enterpriseValue,
            marketCap,
            sharesOutstanding,
            stockPrice,
            None
        ]

    def addRowFromRealData(self, year, carsProd, carsSold,
                           revenueEV, grossProfit, SGAOverSales, RDOverSales, 
                           grossPPE, accumDepr, netPPE, 
                           workingCap, totalLongTermDebt, 
                           avgInterestPaid, yearEndCashForInvest,
                           totalRevenue, totalGrossMargin, 
                           sharesOutstanding, stockPrice):
        newRow = self.getRowFromRealData(year, carsProd, carsSold,
                                         revenueEV, grossProfit, SGAOverSales, RDOverSales, 
                                         grossPPE, accumDepr, netPPE, 
                                         workingCap, totalLongTermDebt, 
                                         avgInterestPaid, yearEndCashForInvest,
                                         totalRevenue, totalGrossMargin, 
                                         sharesOutstanding, stockPrice)
        self.df.loc[len(self.df)] = newRow

    def getSimulatedRow(self, year, ASP, pricePerMile):
    
        lastYearRow = self.getRowByYear(year - 1)
        prev2YearRow = self.getRowByYear(year - 2)
        
        # TESLA AUTOMOTIVE
        
        carsProd = (lastYearRow[(self.evCol, self.grossPPECol)].values[0] - prev2YearRow[(self.evCol, self.grossPPECol)].values[0]) / self.capitalEfficiency + lastYearRow[(self.evCol, self.carsProdCol)].values[0]
        carsSold = carsProd * self.factoryUtilizationFactor
        cumCarsSold = lastYearRow[(self.evCol, self.cumCarsSoldCol)].values[0] + carsSold
        revenueEV = carsSold * ASP
        partLaborOtherCostPerVehicle = lastYearRow[(self.evCol, self.partLaborOtherCostPerVehicleCol)].values[0] * (cumCarsSold / lastYearRow[(self.evCol, self.cumCarsSoldCol)].values[0])**(np.log(1 - self.wrightsLawLearningRate) / np.log(2))
        
        if lastYearRow[(self.evCol, self.yearEndCashForInvestCol)].values[0] < 0:
            lastYearCash = 0
        else:
            lastYearCash = min(lastYearRow[(self.evCol, self.yearEndCashForInvestCol)].values[0], lastYearRow[(self.evCol, self.maxCashDeployableCol)].values[0])
        
        grossPPE = lastYearRow[(self.evCol, self.grossPPECol)].values[0] + lastYearCash / (1 - self.fractionDebtFundedFactoryBuild)
        deprOverGrossPPE = 0.09
        annualDepr = grossPPE * deprOverGrossPPE
        capConsumedPerVehicle = annualDepr / carsSold
        totalCOGsPerVehicle = max(sum([capConsumedPerVehicle, partLaborOtherCostPerVehicle]), (1 - self.maxGrossMargin) * ASP)
        grossMargin = 1 - totalCOGsPerVehicle / ASP
        grossProfit = revenueEV * grossMargin
        SGAOverSales = 0.1
        SGA = revenueEV * SGAOverSales
        RDOverSales = 0.05
        RD = revenueEV * RDOverSales
        EBITEV = grossProfit - SGA - RD
        EBITMargin = EBITEV / revenueEV
        annualDepr = grossPPE * deprOverGrossPPE
        accumDepr = lastYearRow[(self.evCol, self.accumDeprCol)].values[0] - annualDepr
        netPPE = grossPPE + accumDepr
        
        # Assumption: using 2020's working capital
        workingCap = lastYearRow[(self.evCol, self.workingCapCol)].values[0]
        workingCapDays = workingCap / revenueEV * 365
        totalLongTermDebt = lastYearRow[(self.evCol, self.totalLongTermDebtCol)].values[0] + (grossPPE - lastYearRow[(self.evCol, self.grossPPECol)].values[0])    
        avgInterestPaid = 0.06 
        
        # TESLA RIDE HAIL AUTONOMOUS
        
        fullyAutonomousCapableFleet = cumCarsSold - 200000
        percFleetInChina = 0.33
        if year < 2022:
            percFleetRobotaxiPlatform = 0
        else:
            percFleetRobotaxiPlatform = min(self.fractionInAutonomousFleet / (3 ** (2025 - year)), self.fractionInAutonomousFleet)
        cumRobotaxis = fullyAutonomousCapableFleet * percFleetRobotaxiPlatform
        if year < 2022:
            potentialMilesPerRobotaxi = 0
        else:
            potentialMilesPerRobotaxi = self.milesPerRobotaxi
        totalRobotaxiMiles = fullyAutonomousCapableFleet * percFleetRobotaxiPlatform * potentialMilesPerRobotaxi
        autonomousPlatformCutExChina = self.autonomousPlatformFee
        autonomousPlatformCutInChina = self.autonomousPlatformFeeChina
            
        # TESLA RIDE HAIL HUMAN DRIVEN
        
        if year < 2021:
            percCarsSoldIntoHumanDrivenRideHailNet = 0
        else:
            percCarsSoldIntoHumanDrivenRideHailNet = min(self.fractionInHumanDriveRideHailNetwork / (2 ** (2025 - year)), self.fractionInHumanDriveRideHailNetwork)
        if year < 2022:
            percRideHailCarsInAutonomousNet = 0
        else:
            if self.fractionInHumanDriveRideHailNetwork == 0 or self.fractionInAutonomousFleet == 0:
                percRideHailCarsInAutonomousNet = 0
            else:
                if year == 2022:
                    minPercInAutoNet = 0.25
                elif year == 2023:
                    minPercInAutoNet = 0.5
                elif year == 2024:
                    minPercInAutoNet = 0.75
                else:
                    minPercInAutoNet = 1
                percRideHailCarsInAutonomousNet = min(minPercInAutoNet, (cumRobotaxis - lastYearRow[(self.rhAutoCol, self.cumRobotaxisCol)].values[0]) / (percCarsSoldIntoHumanDrivenRideHailNet * carsSold + lastYearRow[(self.rhHumanCol, self.cumHumanRideHailCarsCol)].values[0]))
        
        if percCarsSoldIntoHumanDrivenRideHailNet == 0:
            humanRideHailCarsAddedAnnually = 0
        else:
            humanRideHailCarsAddedAnnually = round(percCarsSoldIntoHumanDrivenRideHailNet*carsSold - (percRideHailCarsInAutonomousNet*percCarsSoldIntoHumanDrivenRideHailNet*carsSold + percRideHailCarsInAutonomousNet*lastYearRow[(self.rhHumanCol, self.cumHumanRideHailCarsCol)].values[0]))
            
        cumHumanRideHailCars = humanRideHailCarsAddedAnnually
        for yr in range(2020, year):
            cumHumanRideHailCars += self.getRowByYear(yr)[(self.rhHumanCol, self.cumHumanRideHailCarsCol)].values[0]

        milesPerYearPerHumanDrivenRideHailCar = self.milesPerYearPerCar
        totalHumanDrivenMiles = milesPerYearPerHumanDrivenRideHailCar * cumHumanRideHailCars
        humanRideHailPlatformCut = 0.3
        if year == 2021:
            humanRideHailPlatformCut = 0.25
            
        # TESLA RIDE HAIL COMBINED

        totalRideHailMiles = totalHumanDrivenMiles + totalRobotaxiMiles
        grossRideHailBillings = totalRideHailMiles * pricePerMile
        netRideHailRevenue = pricePerMile * (humanRideHailPlatformCut * totalHumanDrivenMiles + totalRobotaxiMiles * (percFleetInChina * autonomousPlatformCutInChina + autonomousPlatformCutExChina * (1 - percFleetInChina))) 
        EBITDAMargin = self.autonomousEBITDAMargin
        EBITDA = netRideHailRevenue * EBITDAMargin
        cashFromRideHail = EBITDA * (1 - self.taxRate - self.interestRate)
        
        
        # TESLA INSURANCE
        
        if year == 2021:
            percCarsSoldWithInsurance = 0.025
        else:
            percCarsSoldWithInsurance = lastYearRow[(self.insCol, self.percCarsSoldWithInsuranceCol)].values[0] / 2
        carsInsured = percCarsSoldWithInsurance * (carsSold * (1 - percCarsSoldIntoHumanDrivenRideHailNet))
        cumNonRideHailCarsInsured = lastYearRow[(self.insCol, self.cumNonRideHailCarsInsuredCol)].values[0] + carsInsured
        personalCarInsuranceMiles = cumNonRideHailCarsInsured * self.milesPerCarPerYear
        
        humanDrivenRideHailInsuranceMiles = totalHumanDrivenMiles
        premiumOverMile = lastYearRow[(self.insCol, self.premiumOverMileCol)].values[0] / lastYearRow[(self.evCol, self.ASPCol)].values[0] * ASP
        rideHailPremiumOverMile = premiumOverMile * (1 + self.rideHailInsurancePremiumAddition)    
        grossPremiums = personalCarInsuranceMiles * premiumOverMile + rideHailPremiumOverMile * humanDrivenRideHailInsuranceMiles
        teslaCommission = 1
        if year < 2023:
            teslaCommission = 0.12
        teslaInsuranceRevenue = grossPremiums * teslaCommission
        
        benefitCostPerMileHumanDrivenPersonalCar = None
        benefitCostPerMileHumanDrivenRideHail = None
        totalBenefitCost = None
        benefitCostOverSales = None
        EBITOverSales = None
        EBIT = teslaInsuranceRevenue
        if year >= 2023:
            yearsCount = year - 2023 + 1
            benefitCostPerMileHumanDrivenPersonalCar = self.beginningLossRatio * premiumOverMile * (1 - self.annualSafetyIncrease)**yearsCount
            benefitCostPerMileHumanDrivenRideHail = rideHailPremiumOverMile / premiumOverMile * benefitCostPerMileHumanDrivenPersonalCar
            totalBenefitCost = benefitCostPerMileHumanDrivenPersonalCar * personalCarInsuranceMiles + humanDrivenRideHailInsuranceMiles * benefitCostPerMileHumanDrivenRideHail        
            benefitCostOverSales = 0
            if teslaInsuranceRevenue > 0:
                benefitCostOverSales = totalBenefitCost / teslaInsuranceRevenue
            EBITOverSales = 1 - benefitCostOverSales
            EBIT = EBITOverSales * teslaInsuranceRevenue
        
        # TESLA CONSOLIDATED
        
        totalRevenue = revenueEV + teslaInsuranceRevenue + netRideHailRevenue
        totalEBIT = EBITEV + EBIT + EBITDA
        totalEBITDA = totalEBIT + annualDepr
        debtToEBITDA = totalLongTermDebt / totalEBITDA
        interestPaid = self.interestRate * totalLongTermDebt
        debtToNetPPE = totalLongTermDebt / netPPE
        cashGeneration = EBITEV + annualDepr + EBITDA + EBIT - interestPaid - (EBITEV + EBITDA + EBIT - interestPaid) * self.taxRate
        
        
        # PART OF AUTOMOTIVE
        yearEndCashForInvest = lastYearRow[(self.evCol, self.workingCapCol)].values[0] - workingCap + cashGeneration + lastYearRow[(self.evCol, self.spilloverCashNotDeployedCol)].values[0]
        nextYearCarsProd = (grossPPE - lastYearRow[(self.evCol, self.grossPPECol)].values[0]) / self.capitalEfficiency + carsProd
        maxCashDeployable = nextYearCarsProd * self.maxAnnualProductionIncrease * self.capitalEfficiency * (1 - self.fractionDebtFundedFactoryBuild)

        if yearEndCashForInvest - maxCashDeployable > 0:
            spilloverCashNotDeployed = yearEndCashForInvest - maxCashDeployable
        elif yearEndCashForInvest < 0:
            spilloverCashNotDeployed = yearEndCashForInvest
        else:
            spilloverCashNotDeployed = 0
        # PART OF AUTOMOTIVE
        
        
        # REVIEW: Assumes 80% gross margin for autonomous business
        totalGrossMargin = (netRideHailRevenue * 0.8 + grossProfit) / totalRevenue
        totalEBITDAMargin = totalEBITDA / totalRevenue
        
        enterpriseValue = self.enterpriseMultipleEV * (EBITEV + annualDepr) + self.enterpriseMultipleRobotaxis * EBITDA + self.enterpriseMultipleInsurance * EBIT
        marketCap = enterpriseValue - totalLongTermDebt + yearEndCashForInvest + workingCap
        
        shares2020 = self.getRowByYear(2020)[(self.consolidatedCol, self.sharesOutstandingCol)].values[0]
        sharesOutstanding = (self.equityRaiseForCapex + self.equityRaiseForIncentiveCompensation) / (self.avgMarketCapEquityRaised / shares2020) + shares2020
        stockPrice = marketCap / sharesOutstanding
        cashFlowYield = cashGeneration / marketCap
        
        return [
            year,
            carsProd,
            carsSold,
            cumCarsSold,
            ASP,
            revenueEV,
            partLaborOtherCostPerVehicle,
            capConsumedPerVehicle,
            totalCOGsPerVehicle,
            grossMargin,
            grossProfit,
            SGA,
            SGAOverSales,
            RD,
            RDOverSales,
            EBITEV,
            EBITMargin,
            grossPPE,
            accumDepr,
            annualDepr,
            netPPE,
            deprOverGrossPPE,
            workingCapDays,
            workingCap,
            totalLongTermDebt,
            avgInterestPaid,
            yearEndCashForInvest,
            maxCashDeployable,
            spilloverCashNotDeployed,

            percCarsSoldWithInsurance,
            carsInsured,
            cumNonRideHailCarsInsured,
            personalCarInsuranceMiles,
            humanDrivenRideHailInsuranceMiles,
            premiumOverMile,
            rideHailPremiumOverMile,
            grossPremiums,
            teslaCommission,
            teslaInsuranceRevenue,
            benefitCostPerMileHumanDrivenPersonalCar,
            benefitCostPerMileHumanDrivenRideHail,
            totalBenefitCost,
            benefitCostOverSales,
            EBITOverSales,
            EBIT,

            percCarsSoldIntoHumanDrivenRideHailNet,
            percRideHailCarsInAutonomousNet,
            humanRideHailCarsAddedAnnually,
            cumHumanRideHailCars,
            milesPerYearPerHumanDrivenRideHailCar,
            totalHumanDrivenMiles, 
            humanRideHailPlatformCut,

            fullyAutonomousCapableFleet,
            percFleetInChina,
            percFleetRobotaxiPlatform,
            cumRobotaxis,
            potentialMilesPerRobotaxi,
            totalRobotaxiMiles,
            autonomousPlatformCutExChina,
            autonomousPlatformCutInChina,

            totalRideHailMiles,
            pricePerMile,
            grossRideHailBillings,
            netRideHailRevenue,
            EBITDAMargin,
            EBITDA,
            cashFromRideHail,

            totalRevenue,
            totalEBIT,
            totalEBITDA,
            debtToEBITDA,
            interestPaid,
            debtToNetPPE,
            cashGeneration, 
            totalGrossMargin,
            totalEBITDAMargin,
            enterpriseValue,
            marketCap,
            sharesOutstanding,
            stockPrice,
            cashFlowYield
        ]

    def addSimulatedRow(self, year, ASP, pricePerMile):
        newRow = self.getSimulatedRow(year, ASP, pricePerMile)
        self.df.loc[len(self.df)] = newRow

    def setAssumptions(self, maxGrossMargin, capitalEfficiency, fractionInHumanDriveRideHailNetwork, 
                      fractionInAutonomousFleet, avgMarketCapEquityRaised, equityRaiseForCapex, 
                      equityRaiseForIncentiveCompensation, fractionDebtFundedFactoryBuild, 
                      wrightsLawLearningRate, maxAnnualProductionIncrease, factoryUtilizationFactor, 
                      segmentPenetrationPercentage, taxRate, interestRate, percentageCarsSoldWithInsurance, 
                      insuranceCommission, premiumPerMile, rideHailInsurancePremiumAddition, beginningLossRatio, 
                      annualSafetyIncrease, milesPerCarPerYear, milesPerYearPerCar, platformFeeAtScale, 
                      milesPerRobotaxi, autonomousPlatformFee, autonomousPlatformFeeChina, fleetPercentageChina, 
                      sgaPercentageEVSales, rdPercentageEVSales, autonomousEBITDAMargin, enterpriseMultipleEV, 
                      enterpriseMultipleInsurance, enterpriseMultipleRobotaxis):
        # Max gross margin
        self.maxGrossMargin = maxGrossMargin
        # Capital efficiency (gross capex per unit of annual production capacity) (not in millions)
        self.capitalEfficiency = capitalEfficiency
        # % of cars sold into human driven ride-hail network in 2025
        self.fractionInHumanDriveRideHailNetwork = fractionInHumanDriveRideHailNetwork
        # Probability that robotaxis launch: binary value that affects fractionInAutonomousFleet

        # In the event that robotaxis launch, percent of capable Teslas in autonomous fleet in 2025
        self.fractionInAutonomousFleet = fractionInAutonomousFleet

        # Weighted average market capitalization at which equity is raised
        self.avgMarketCapEquityRaised = avgMarketCapEquityRaised
        # Equity raise for capex
        self.equityRaiseForCapex = equityRaiseForCapex
        # Equity raise for incentive compensation
        self.equityRaiseForIncentiveCompensation = equityRaiseForIncentiveCompensation
        # Percent of factory-build that will be debt funded
        self.fractionDebtFundedFactoryBuild = fractionDebtFundedFactoryBuild

        # Wright's Law learning rate
        self.wrightsLawLearningRate = wrightsLawLearningRate
        # Max annual production increase (given management bandwidth constraints)
        self.maxAnnualProductionIncrease = maxAnnualProductionIncrease
        # Factory utilization factor
        self.factoryUtilizationFactor = factoryUtilizationFactor
        # Percent of each model/price segment that Tesla penetrates
        self.segmentPenetrationPercentage = segmentPenetrationPercentage
        # Tax rate
        self.taxRate = taxRate
        # Interest rate
        self.interestRate = interestRate

        # % of cars sold with Tesla insurance
        self.percentageCarsSoldWithInsurance = percentageCarsSoldWithInsurance
        # Tesla commission as an insurance agent
        self.insuranceCommission = insuranceCommission
        # Premium/mile for personally owned Tesla car (not in millions)
        self.premiumPerMile = premiumPerMile
        # Ride-hail insurance premium addition
        self.rideHailInsurancePremiumAddition = rideHailInsurancePremiumAddition
        # Beginning loss ratio (when Tesla first begins underwriting its own policies)
        self.beginningLossRatio = beginningLossRatio
        # Annual safety increase of Tesla cars (% safer)
        self.annualSafetyIncrease = annualSafetyIncrease
        # Miles per personal car per year
        self.milesPerCarPerYear = milesPerCarPerYear

        # Miles per year per car (not in millions)
        self.milesPerYearPerCar = milesPerYearPerCar
        # Platform fee at scale
        self.platformFeeAtScale = platformFeeAtScale

        # Miles traveled per robotaxi (not in millions)
        self.milesPerRobotaxi = milesPerRobotaxi
        # Tesla platform cut
        self.autonomousPlatformFee = autonomousPlatformFee
        # Tesla platform cut in China
        self.autonomousPlatformFeeChina = autonomousPlatformFeeChina
        # Percent of fleet in China
        self.fleetPercentageChina = fleetPercentageChina

        # SG&A as % of electric vehicle sales
        self.sgaPercentageEVSales = sgaPercentageEVSales
        # R&D as % of electric vehicle sales
        self.rdPercentageEVSales = rdPercentageEVSales
        # Autonomous EBITDA margin
        self.autonomousEBITDAMargin = autonomousEBITDAMargin
        # EV/EBITDA electric vehicle business
        self.enterpriseMultipleEV = enterpriseMultipleEV
        # EV/EBITDA insurance business
        self.enterpriseMultipleInsurance = enterpriseMultipleInsurance
        # EV/EBITDA autonomous robotaxi business
        self.enterpriseMultipleRobotaxis = enterpriseMultipleRobotaxis