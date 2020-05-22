{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "week11_A107260035_李旻翰.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyOWcTwjq0oq4XWrmHJG+8wX",
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
        "<a href=\"https://colab.research.google.com/github/minhanl/introduction-to-data-science/blob/master/week11_A107260035_%E6%9D%8E%E6%97%BB%E7%BF%B0.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "nVvTaqyE-rXv",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "0fab87af-8c7c-48ff-e22c-953b5fa9d4c1"
      },
      "source": [
        "primes_list = [2, 3, 5, 7, 11]\n",
        "primes_list[-1] = 13 # update\n",
        "print(primes_list)"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[2, 3, 5, 7, 13]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "5e4h0yXX-zv8",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "18887fe6-2ff5-41a1-f187-b3f2a3b64cbe"
      },
      "source": [
        "primes_list.insert(-1, 11) # increase length\n",
        "print(primes_list)"
      ],
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[2, 3, 5, 7, 11, 13]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "7S1kpzRf-2UI",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "8187436e-9a42-4817-c99c-7f66f1a4a1d8"
      },
      "source": [
        "primes_list.pop()\n",
        "print(primes_list)"
      ],
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[2, 3, 5, 7, 11]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "jc7JzdA1-9Cw",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 67
        },
        "outputId": "2cb81d63-9584-4f91-a30c-7f867cc4f5d4"
      },
      "source": [
        "x = 0.25\n",
        "print(type(x))\n",
        "print(x.as_integer_ratio())\n",
        "print(type(x.as_integer_ratio()))"
      ],
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<class 'float'>\n",
            "(1, 4)\n",
            "<class 'tuple'>\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "_OR-XWDr_GOC",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 50
        },
        "outputId": "c36ea02c-6d60-4b61-ed83-ebfa0d8f6676"
      },
      "source": [
        "def where_are_you_from(city, country):\n",
        "    return city, country\n",
        "\n",
        "print(where_are_you_from(\"Taipei\", \"Taiwan\"))\n",
        "print(type(where_are_you_from(\"Taipei\", \"Taiwan\")))"
      ],
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "('Taipei', 'Taiwan')\n",
            "<class 'tuple'>\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "V2U6ezWt_IXi",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 50
        },
        "outputId": "9b323cde-d38a-4045-9901-a8db430d2377"
      },
      "source": [
        "my_city, my_country = where_are_you_from(\"Taipei\", \"Taiwan\")\n",
        "print(my_city)\n",
        "print(my_country)"
      ],
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Taipei\n",
            "Taiwan\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "2_Xrzx_g_Mf0",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 50
        },
        "outputId": "7a4de8c5-5b22-46a2-ba77-2b5c408cb53f"
      },
      "source": [
        "living_area = input(\"請輸入您的居住縣市:\")\n",
        "living_cost = None\n",
        "if living_area == '臺北市':\n",
        "    living_cost = 17005\n",
        "elif living_area == '新北市':\n",
        "    living_cost = 15500\n",
        "elif living_area == '桃園市':\n",
        "    living_cost = 15281\n",
        "elif living_area == '臺中市':\n",
        "    living_cost = 14596\n",
        "elif living_area == '臺南市':\n",
        "    living_cost = 12388\n",
        "elif living_area == '高雄市':\n",
        "    living_cost = 13099\n",
        "elif living_area == '非六都之縣市':\n",
        "    living_cost = 12388\n",
        "elif living_area == '金門縣連江縣':\n",
        "    living_cost = 11648\n",
        "\n",
        "if living_cost is None:\n",
        "    print(\"請重新輸入居住縣市\")\n",
        "else:\n",
        "    print(\"{}的每人每月最低生活費為{:,}\".format(living_area, living_cost))"
      ],
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "請輸入您的居住縣市:臺北市\n",
            "臺北市的每人每月最低生活費為17,005\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "af0fxQUw_cDW",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 50
        },
        "outputId": "cae6818a-652c-41a1-ea05-d485eb2130c7"
      },
      "source": [
        "   living_cost_dict = {\n",
        "    '臺北市': 17005,\n",
        "    '新北市': 15500,\n",
        "    '桃園市': 15281,\n",
        "    '臺中市': 14596,\n",
        "    '臺南市': 12388,\n",
        "    '高雄市': 13099,\n",
        "    '非六都之縣市': 12388,\n",
        "    '金門縣連江縣': 11648\n",
        "}\n",
        "living_area = input(\"請輸入您的居住縣市:\")\n",
        "try:\n",
        "    living_cost = living_cost_dict[living_area]\n",
        "    print(\"{}的每人每月最低生活費為{:,}\".format(living_area, living_cost))\n",
        "except KeyError:\n",
        "    print(\"請重新輸入居住縣市\")"
      ],
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "請輸入您的居住縣市:新北市\n",
            "新北市的每人每月最低生活費為15,500\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "piXCD8Nx_pXY",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "e413694b-3140-4e25-eab9-2e8081408fbb"
      },
      "source": [
        "primes_list = [2, 3, 5, 7, 11]\n",
        "I = iter(primes_list)\n",
        "next(I)"
      ],
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "2"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 11
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Jf6kRRC3_wCQ",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "1cb01d40-14d3-495a-beb9-886d9dc252ee"
      },
      "source": [
        "I = iter(living_cost_dict.keys())\n",
        "next(I)"
      ],
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'臺北市'"
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
        "id": "7AOo6Jwv_1Zb",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "44de5428-b893-4f38-b4c3-cda904e1713c"
      },
      "source": [
        "I = iter(living_cost_dict.items())\n",
        "next(I)"
      ],
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "('臺北市', 17005)"
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
        "id": "z2HBXbTy_4sx",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "outputId": "a2c18f6e-8ad5-4443-9246-f875f419ea2f"
      },
      "source": [
        "for i in range(1, 101, 1):\n",
        "    print(i)"
      ],
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "1\n",
            "2\n",
            "3\n",
            "4\n",
            "5\n",
            "6\n",
            "7\n",
            "8\n",
            "9\n",
            "10\n",
            "11\n",
            "12\n",
            "13\n",
            "14\n",
            "15\n",
            "16\n",
            "17\n",
            "18\n",
            "19\n",
            "20\n",
            "21\n",
            "22\n",
            "23\n",
            "24\n",
            "25\n",
            "26\n",
            "27\n",
            "28\n",
            "29\n",
            "30\n",
            "31\n",
            "32\n",
            "33\n",
            "34\n",
            "35\n",
            "36\n",
            "37\n",
            "38\n",
            "39\n",
            "40\n",
            "41\n",
            "42\n",
            "43\n",
            "44\n",
            "45\n",
            "46\n",
            "47\n",
            "48\n",
            "49\n",
            "50\n",
            "51\n",
            "52\n",
            "53\n",
            "54\n",
            "55\n",
            "56\n",
            "57\n",
            "58\n",
            "59\n",
            "60\n",
            "61\n",
            "62\n",
            "63\n",
            "64\n",
            "65\n",
            "66\n",
            "67\n",
            "68\n",
            "69\n",
            "70\n",
            "71\n",
            "72\n",
            "73\n",
            "74\n",
            "75\n",
            "76\n",
            "77\n",
            "78\n",
            "79\n",
            "80\n",
            "81\n",
            "82\n",
            "83\n",
            "84\n",
            "85\n",
            "86\n",
            "87\n",
            "88\n",
            "89\n",
            "90\n",
            "91\n",
            "92\n",
            "93\n",
            "94\n",
            "95\n",
            "96\n",
            "97\n",
            "98\n",
            "99\n",
            "100\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}