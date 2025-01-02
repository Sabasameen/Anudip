{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "14a01aea-23a6-4596-9176-05f779d46966",
   "metadata": {},
   "source": [
    "### 1. Using input() function take one number from the user and using ternary operators check whether the number is even or odd \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "44328559-9f8b-4418-b90c-cede16fe97c8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter one number: 3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "This is odd number: \n"
     ]
    }
   ],
   "source": [
    "A = int(input('Enter one number:'))\n",
    "if A % 2 == 0:\n",
    "    print('This is even number: ')\n",
    "else:\n",
    "    print('This is odd number: ')\n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e931b497-a1c2-4b7e-b4c7-85006d4b514d",
   "metadata": {},
   "source": [
    "### 2. Using input function take two number and then swap the number"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "f013e94f-517e-4b42-b46d-0824a117d04f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the 1st number: 2\n",
      "Enter the 2nd number: 4\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "These are numbers: 2 4\n",
      "These are swaped numbers: 4 2\n"
     ]
    }
   ],
   "source": [
    "A = int(input(\"Enter the 1st number:\"))\n",
    "B = int(input(\"Enter the 2nd number:\"))\n",
    "print('These are numbers:', A, B)\n",
    "\n",
    "C = int( A ) \n",
    "A = B\n",
    "B = C\n",
    "\n",
    "print(\"These are swaped numbers:\" ,A, B )"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "132bf279-029e-44b3-a652-0fadab12176a",
   "metadata": {},
   "source": [
    "### 3. Write a Program to Convert Kilometers to Miles \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "8321694c-63af-4609-a361-ca5d463080a6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter value in kilometers: 1000\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "This is the value in miles 621.37\n"
     ]
    }
   ],
   "source": [
    "#1 kilometer (km) = 0.62137 miles (mi)\n",
    "\n",
    "A = int(input('Enter value in kilometers:'))\n",
    "B = 0.62137 * A\n",
    "print (\"This is the value in miles\" ,B)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a1c57cb5-7c48-4c17-8259-065dad3d8dd5",
   "metadata": {},
   "source": [
    "### 4. Find the Simple Interest on Rs. 200 for 5 years at 5% per year"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "9c393541-7fdd-4322-896c-3613eacda368",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "This is simple interest: 50.0\n"
     ]
    }
   ],
   "source": [
    "# S.I. = (P × R × T)/100, where P = Principal, R = Rate of Interest in % per annum, and T = Time, usually calculated as the number of years.\n",
    "P = int(200)\n",
    "R = int(5) \n",
    "T = int(5)\n",
    "S = P * R * T / 100\n",
    "print('This is simple interest:',S)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "23b537c1-fd9a-41d2-96e9-bda495522209",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
