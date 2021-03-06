{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "week13_A107260035_李旻翰.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyP0XjRk1jn/7Bv/CaBXfbEs",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/minhanl/introduction-to-data-science/blob/master/week13_A107260035_%E6%9D%8E%E6%97%BB%E7%BF%B0.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "M4z49sRnolGL",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 121
        },
        "outputId": "9e0606e3-c09b-4b07-c706-7ae0ce242560"
      },
      "source": [
        "n_vowels = 0\n",
        "for i in 'azcbobobegghakl':\n",
        "  if i in ['a','e','i','o','u']:\n",
        "    print(i)\n",
        "    n_vowels +=1\n",
        "print(n_vowels)"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "a\n",
            "o\n",
            "o\n",
            "e\n",
            "a\n",
            "5\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "3qXdbrSQowDt",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 243
        },
        "outputId": "57eb86e4-df5d-46c6-ec62-f6eee25843da"
      },
      "source": [
        "test_str = 'azcbobobegghakl'\n",
        "n_char = len(test_str)\n",
        "print(n_char)\n",
        "for i in range(12):\n",
        "  print(test_str[i:i+3])"
      ],
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "15\n",
            "azc\n",
            "zcb\n",
            "cbo\n",
            "bob\n",
            "obo\n",
            "bob\n",
            "obe\n",
            "beg\n",
            "egg\n",
            "ggh\n",
            "gha\n",
            "hak\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "OLsBeHiQo1AK",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "outputId": "ec3aa940-63a3-4b85-8f98-5d4b2cb843e9"
      },
      "source": [
        "test_str = 'azcbobobegghak'\n",
        "n_char = len(test_str)\n",
        "n_bobs = 0\n",
        "for i in range(n_char - 2):\n",
        "    #print(test_str[i:i+3])\n",
        "    if test_str[i:i+3] == 'bob':\n",
        "        n_bobs += 1\n",
        "print(n_bobs)\n"
      ],
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "2\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "O85IVn94o5B8",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "outputId": "5019b34c-8f45-4262-b4f4-275ad0693bed"
      },
      "source": [
        "x = list(range(1, 101))\n",
        "N = len(x)\n",
        "x_bar = sum(x) / N\n",
        "sse = 0\n",
        "for xi in x:\n",
        "  # error = xi - x_bar\n",
        "  squared_error = (xi - x_bar)**2\n",
        "  sse += squared_error # sse = sse + squared_error\n",
        "sample_mse = sse / (N-1)\n",
        "sample_stdev = sample_mse**(0.5)\n",
        "print(sample_stdev)"
      ],
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "29.011491975882016\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ShDLFMnGo8Fi",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "def get_fahrenheit(x):\n",
        "    \"\"\"\n",
        "    Transform a Celsius degree into  Farenheit scale\n",
        "    \"\"\"\n",
        "    fah = x * 9/5 + 32\n",
        "    return fah"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "k6wQoQCho_QS",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "outputId": "89fa35ac-6149-4be3-c386-8527c42dcdc2"
      },
      "source": [
        "get_fahrenheit(32)"
      ],
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "89.6"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "2TwTb6u0pBQr",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "def get_bmi(height, weight):\n",
        "    \"\"\"\n",
        "    Calculate BMI based on height and weight\n",
        "    \"\"\"\n",
        "    height = height / 100\n",
        "    bmi = weight / height**2\n",
        "    return bmi"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "zphQxfndpD8q",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "outputId": "39c0911b-46ae-4c2d-e31a-f801f04bf24f"
      },
      "source": [
        "get_bmi(180, 77)"
      ],
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "23.76543209876543"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 9
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "QwrpxNW-pKCM",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "def is_prime(x):\n",
        "  \"\"\"\n",
        "  Retuen True if x is a prime, or return False\n",
        "  \"\"\"\n",
        "  divisors = []\n",
        "  for i in range(1, x+1):\n",
        "    if x % i ==0:\n",
        "      divisors.append(i)\n",
        "  n_divisors = len(divisors)\n",
        "  return n_divisors == 2"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "7wLxNGVvpPWG",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "outputId": "e683ee8e-1644-44af-e62d-34249cb05f7d"
      },
      "source": [
        "is_prime(11)"
      ],
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 12
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "fLk68wUkpXcK",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "outputId": "470fe75e-1944-402b-e4aa-8c6a886c7d29"
      },
      "source": [
        "is_prime(9)"
      ],
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "False"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 13
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "o1yVargxpZz6",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "outputId": "6ec0ed62-329c-4aa3-b98e-696b1f311cd8"
      },
      "source": [
        "is_prime(91)"
      ],
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "False"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 15
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "RTDhGWrBpdKM",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "outputId": "6fab92fd-90d0-4047-c559-8a56d307e25f"
      },
      "source": [
        "is_prime(23)"
      ],
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 14
        }
      ]
    }
  ]
}