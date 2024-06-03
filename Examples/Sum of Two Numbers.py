{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "de73d1ab",
   "metadata": {},
   "source": [
    "# Program 2 : Sum of Two Numbers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "24f30eae",
   "metadata": {},
   "outputs": [],
   "source": [
    "def main():\n",
    "    print(\"This program adds two numbers\")\n",
    "    \n",
    "    #taking 1st string input and converting to an integer before storing\n",
    "    num1 = int(input(\"Enter first number : \"))\n",
    "    \n",
    "    #taking 2nd string input and converting to an integer before storing\n",
    "    num2 = int(input(\"Enter second number : \"))\n",
    "    \n",
    "    #Sum of the two numbers\n",
    "    total = num1 + num2\n",
    "    \n",
    "    #printing the sum\n",
    "    print(\"The total is \"+ str(total) + \".\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "93146189",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "This program adds two numbers\n"
     ]
    }
   ],
   "source": [
    "main()"
   ]
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
   "version": "3.11.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
