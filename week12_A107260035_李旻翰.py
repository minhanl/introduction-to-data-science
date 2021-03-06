{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "week12_A107260035_李旻翰.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyNxy0L8kSxqcSV8x2LaK+//",
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
        "<a href=\"https://colab.research.google.com/github/minhanl/introduction-to-data-science/blob/master/week12_A107260035_%E6%9D%8E%E6%97%BB%E7%BF%B0.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "hSqBah7rBa-R",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 890
        },
        "outputId": "cd7d19d1-b7ce-4082-de24-11f683255dec"
      },
      "source": [
        "x = int(input(\"請輸入起始的正整數：\")) \n",
        "y = int(input(\"請輸入終止的正整數：\"))\n",
        "for i in range(x, y+1):\n",
        "  print(i)"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "請輸入起始的正整數：1\n",
            "請輸入終止的正整數：50\n",
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
            "50\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "a_Np-Li6Bndh",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 87
        },
        "outputId": "bb8e9e3e-c839-4fa7-9609-267f04fb0081"
      },
      "source": [
        "x = int(input(\"請輸入起始的正整數：\")) \n",
        "y = int(input(\"請輸入終止的正整數：\"))\n",
        "odds = [] # 空的list\n",
        "for i in range(x, y+1):\n",
        "  mod = i % 2\n",
        "  if mod == 1:\n",
        "    odds.append(i)\n",
        "print(odds)"
      ],
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "請輸入起始的正整數：10\n",
            "請輸入終止的正整數：80\n",
            "[11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "7HV08puHBvmR",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 87
        },
        "outputId": "9df5749f-6f8e-4e2a-cb9e-711517ab07a7"
      },
      "source": [
        "user_int = int(input(\"請輸入一個正整數：\"))\n",
        "divisors = [] # 因數分解\n",
        "for i in range(1, user_int+1):\n",
        "  if user_int % 1 == 0:\n",
        "    divisors.append(i)\n",
        "print(divisors)\n",
        "n_divisors = len(divisors)\n",
        "if n_divisors == 2 :\n",
        "  print(\"{}是質數\".format(user_int))\n",
        "else:\n",
        "  print(\"{}不是質數\".format(user_int))"
      ],
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "請輸入一個正整數：30\n",
            "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]\n",
            "30不是質數\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "U6DWUFDTB72s",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 154
        },
        "outputId": "ee72de22-923c-4799-8660-4ab0bcad2395"
      },
      "source": [
        "# random 產生 1 個隨機數\n",
        "import random\n",
        "\n",
        "random.randint(1, 1000)\n",
        "# random 產生 100 個隨機數\n",
        "random_integers = [] # 隨機數\n",
        "for i in range(100): # 產生個數\n",
        "  rand_int = random.randint(1, 1000) # 範圍\n",
        "  random_integers.append(rand_int)\n",
        "print(random_integers)\n",
        "print(len(random_integers))\n",
        "# 找出第一大與第一小的數字\n",
        "print(max(random_integers))\n",
        "print(min(random_integers))\n",
        "# 找出第二大與第二小的數字\n",
        "rand_int_unique = set(random_integers)\n",
        "rand_int_unique_list = list(rand_int_unique)\n",
        "print(rand_int_unique_list)\n",
        "rand_int_unique_list.sort()\n",
        "print(rand_int_unique_list[1]) # second min\n",
        "print(rand_int_unique_list[-2]) # second max"
      ],
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[357, 203, 397, 252, 734, 376, 12, 544, 228, 824, 600, 93, 428, 416, 670, 316, 44, 908, 409, 492, 295, 33, 196, 483, 344, 253, 79, 119, 927, 407, 352, 289, 279, 418, 782, 17, 764, 396, 455, 548, 845, 942, 41, 687, 527, 607, 218, 809, 111, 876, 337, 14, 804, 758, 972, 273, 783, 477, 146, 595, 794, 746, 322, 524, 908, 409, 428, 163, 247, 88, 902, 222, 768, 617, 657, 74, 658, 600, 27, 387, 816, 745, 639, 498, 109, 838, 595, 757, 107, 673, 846, 84, 913, 551, 405, 393, 726, 228, 605, 865]\n",
            "100\n",
            "972\n",
            "12\n",
            "[12, 524, 14, 527, 17, 27, 544, 33, 548, 551, 41, 44, 74, 79, 595, 84, 600, 88, 93, 605, 607, 617, 107, 109, 111, 119, 639, 657, 146, 658, 670, 673, 163, 687, 196, 203, 726, 218, 734, 222, 228, 745, 746, 757, 758, 247, 764, 252, 253, 768, 782, 783, 273, 279, 794, 289, 804, 295, 809, 816, 824, 316, 322, 838, 845, 846, 337, 344, 352, 865, 357, 876, 376, 387, 902, 393, 908, 397, 396, 913, 405, 407, 409, 927, 416, 418, 428, 942, 455, 972, 477, 483, 492, 498]\n",
            "14\n",
            "942\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "rFShg9ONCX3V",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "4f61a67d-8a21-4b4c-f4e5-e674573a45ac"
      },
      "source": [
        "squared = []\n",
        "for i in range(10):\n",
        "  squared.append(i**2)\n",
        "print(squared)"
      ],
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "nvHfNtSZCAmN",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "262533df-1c3f-4519-ca4e-f09c552f2f5e"
      },
      "source": [
        "squared = [i**2 for i in range(10)] \n",
        "print(squared)"
      ],
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "dglQY707Cgdm",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "f08e9742-5510-4a04-d967-c1956cdb92ab"
      },
      "source": [
        "odds_squared = []\n",
        "for i in range(10):\n",
        "  if i % 2 == 1:\n",
        "    odds_squared.append(i**2)\n",
        "print(odds_squared)"
      ],
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[1, 9, 25, 49, 81]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "mgOqEc98CmEp",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "fd3e3815-3537-4589-c58a-3bc7e80e9b3f"
      },
      "source": [
        "odds_squared =[i**2 for i in range(10) if i % 2 == 1]\n",
        "print(odds_squared)"
      ],
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[1, 9, 25, 49, 81]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "EO_0jqwDCpff",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 50
        },
        "outputId": "ec4c5730-32c3-40d6-e2ed-51e7db073acb"
      },
      "source": [
        "random_integers = [random.randint(1, 100) for i in range(10)]\n",
        "is_odd_ints = []\n",
        "for i in random_integers:\n",
        "  if i % 2 == 1:\n",
        "    is_odd_ints.append(True)\n",
        "  else:\n",
        "    is_odd_ints.append(False)\n",
        "print(random_integers)\n",
        "print(is_odd_ints)"
      ],
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[41, 78, 66, 20, 68, 68, 44, 39, 94, 93]\n",
            "[True, False, False, False, False, False, False, True, False, True]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "elxvM2g8Cza4",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 70
        },
        "outputId": "b3c50436-9b40-4473-9aed-e873781d744a"
      },
      "source": [
        "random_integers = [random.randint(1, 100) for i in range(20)]\n",
        "is_odd_ints = [True if i % 2 == 1 else False for i in random_integers]\n",
        "print(random_integers)\n",
        "print(is_odd_ints)"
      ],
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[19, 82, 91, 65, 4, 41, 27, 52, 47, 11, 52, 59, 89, 12, 38, 70, 93, 49, 33, 80]\n",
            "[True, False, True, True, False, True, True, False, True, True, False, True, True, False, False, False, True, True, True, False]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "qSGZlCN2C2Y5",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "50003209-2122-48d4-8309-5755db4cadb3"
      },
      "source": [
        "avengers_ratings = [8.1, 7.3, 8.5, 8.8] \n",
        "recommendations = [i for i in avengers_ratings if i >= 8] \n",
        "print(recommendations)"
      ],
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[8.1, 8.5, 8.8]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "yjr_HNGoC6Qw",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 84
        },
        "outputId": "9d0833a7-2eae-47dd-f908-9a3cc396ad2f"
      },
      "source": [
        "avengers = [\"The Avengers\", \"Avengers: Age of Ultron\", \"Avengers: Infinity War\", \"Avengers: Endgame\"]\n",
        "for idx, movie in enumerate(avengers):\n",
        "    print(\"第 {} 部上映的復仇者聯盟電影:{}\".format(idx+1, movie))"
      ],
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "第 1 部上映的復仇者聯盟電影:The Avengers\n",
            "第 2 部上映的復仇者聯盟電影:Avengers: Age of Ultron\n",
            "第 3 部上映的復仇者聯盟電影:Avengers: Infinity War\n",
            "第 4 部上映的復仇者聯盟電影:Avengers: Endgame\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "VvtahaSQC8yy",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 84
        },
        "outputId": "415823da-26f1-4804-c0c8-e758a841819a"
      },
      "source": [
        "years = [2012, 2015, 2018, 2019]\n",
        "for year, movie in zip(years, avengers):\n",
        "    print(\"{}上映的年份是{}\".format(movie, year))"
      ],
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "The Avengers上映的年份是2012\n",
            "Avengers: Age of Ultron上映的年份是2015\n",
            "Avengers: Infinity War上映的年份是2018\n",
            "Avengers: Endgame上映的年份是2019\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}