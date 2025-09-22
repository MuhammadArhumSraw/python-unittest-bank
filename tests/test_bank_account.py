import pytest
from bank_account.bank_account import BankAccount


@pytest.fixture
def start_account():
    return BankAccount(100)


def test_deposit(start_account):
    start_account.deposit(50)
    assert start_account.balance == 150

def test_initial_balance_zero():
    acc = BankAccount()
    assert acc.balance == 0

def test_init_negative_raises():
    with pytest.raises(ValueError):
        BankAccount(-10)

def test_deposit_and_withdraw():
    acc = BankAccount(100)
    acc.deposit(50)
    assert acc.balance == 150
    acc.withdraw(70)
    assert acc.balance == 80

def test_deposit_negative_raises():
    acc = BankAccount()
    with pytest.raises(ValueError):
        acc.deposit(0)
    with pytest.raises(ValueError):
        acc.deposit(-10)

def test_withdraw_negative_or_overdraft():
    acc = BankAccount(50)
    with pytest.raises(ValueError):
        acc.withdraw(0)
    with pytest.raises(ValueError):
        acc.withdraw(1000)

def test_transfer():
    a = BankAccount(100)
    b = BankAccount(0)
    a.transfer_to(b, 60)
    assert a.balance == 40
    assert b.balance == 60

def test_transfer_invalid_target():
    a = BankAccount(100)
    with pytest.raises(ValueError):
        a.transfer_to("not an account", 10)
