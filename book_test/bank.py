#!/usr/bin/env python
#！-*- coding:UTF-8 -*-

class BankAccount():

    def __init__(self, accountName, account, totalMoney=0):
        self.accountName = accountName
        self.account = account
        self.totalMoney = totalMoney

    def saveMoney(self, money):
        self.totalMoney += money
        print 'AccountName:', self.accountName
        print 'Account:    ', self.account
        print 'TotalMoney: ', self.totalMoney
        print 'Hello, You Account have ' , self.totalMoney, 'yuan Now.'

    def takeMoney(self, money):
        if(self.totalMoney < money):
            print '账户余额不足'
            return

        self.totalMoney -= money
        print 'AccountName:', self.accountName
        print 'Account:    ', self.account
        print 'TotalMoney: ', self.totalMoney
        print 'Hello, You Account have ', self.totalMoney, 'yuan Now.'


BA = BankAccount('WangTT', '15721243265', 100)

BA.saveMoney(200)

BA.takeMoney(500)


class InterestAccount(BankAccount):

    interest = 0  #利息

    def __init__(self, accountName, account, totalMoney, tax, timeLimit=12):
        self.accountName = accountName
        self.account = account
        self.totalMoney = totalMoney
        self.tax = tax
        self.timeLimit = timeLimit

    def addInterest(self):
        InterestAccount.interest += self.totalMoney * self.tax / 100 * self.timeLimit / 12
        print '本金：', self.totalMoney , ', 利息：', InterestAccount.interest

    def print_data(self):
        print 'AccountName: ', self.accountName
        print 'Account:     ', self.account
        print 'Money     :  ', self.totalMoney
        print 'Tax Of Money:', self.tax
        print 'Time Limit:  ', self.timeLimit
        print 'TotalMoney:  ', self.totalMoney + InterestAccount.interest

IA = InterestAccount('Jack', 'Jack&Rose', 10000, 4.0, 36)
IA.addInterest()
IA.print_data()
print '======================='
IA.saveMoney(5000)
IA.addInterest()
IA.print_data()



