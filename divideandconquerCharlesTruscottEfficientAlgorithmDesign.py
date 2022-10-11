# -*- coding: utf-8 -*-
"""
Proudly an MIT 6.0001 grad and an MIT 6.0002 student
Thank you very much Eric Grimson, John Guttag and Ana Bell for being my teacher!
I have wanted to sit a unit from MIT since 2011, having purchased in 2011 Structure and Interpretation of Computer Programs (taught in LISP), the 1970s/80s rendition of MIT's 6.0001
And in 2014 I was on the 6.0001 OCW site to pick up `How to think like a Computer Scientist in Python` which taught me the basics of function calls and iteration
Very proudly had the world's #1 ranked Uni/College (QS) to learn to code
Charles Truscott, Byron Bay NSW, 2481

    

Trying to reach a faster algorithm for 1000+ len lists, 7:28 p.m. 11/10/2022

Improved the algorithm but still ends up greater than x ^ 2 * len(x) for the final step

Doctor's appointment at Suffolk Park Tomorrow, either vascular surgery for my face or brain tumour treatment, have about a quarter of human eyesight left from my brain tumour
MRI and beginning chemo, radiation, dopamine agonists, whatever is going to get rid of my brain tumour

Warm in bed with the heater on and about to have a cup of coffee

God Bless the USA, thank you MIT

I spent more than a quarter of my life as an enforced disappearance

Charles Thomas Wallace Truscott Watters, born 13/01/1993, father Mark William Watters and mother Kerri-Ann Truscott and brother Tai Truscott and Uncle Rodney Watters and Grandmother June Margaret Truscott and Grandfather Herbert Wallace Truscott

Byron Bay / Suffolk Park NSW 2481

9:25 p.m. 11/10/2022


runfile('C:/Users/VisualStudio2019/Desktop/merge_ordering_principle.py', wdir='C:/Users/VisualStudio2019/Desktop')
The list: [91, 5, 23, 36, 2, 61, 18, 95, 89, 70, 16, 28, 8, 48, 87, 37, 66, 53, 56, 83, 83, 99, 15, 55, 50, 26, 5, 47, 81, 87, 96, 93, 33, 23, 70, 10, 62, 75, 56, 5, 5, 36, 1, 94, 40, 62, 27, 57, 98, 51, 51, 28, 63, 19, 6, 76, 16, 52, 77, 73, 16, 3, 37, 11, 91, 58, 13, 6, 72, 55, 39, 71, 44, 34, 47, 69, 93, 85, 63, 73, 28, 27, 73, 24, 81, 29, 80, 19, 97, 27, 84, 0, 11, 8, 42, 20, 86, 2, 79, 97]




The maximum pairwise product: 9504 (99 x 96)
Charles Truscott Watters. More efficient, non pointer linked list algorithm
I love you big bro Tai. Thank you MIT


Now for a list of len(1000) 



YAYY!!!!

runfile('C:/Users/VisualStudio2019/Desktop/merge_ordering_principle.py', wdir='C:/Users/VisualStudio2019/Desktop')
The list: [845, 809, 694, 201, 575, 136, 88, 611, 998, 266, 787, 795, 892, 805, 37, 84, 163, 463, 900, 548, 766, 492, 729, 155, 215, 107, 67, 219, 634, 170, 656, 294, 539, 369, 612, 306, 961, 625, 42, 754, 630, 44, 930, 562, 109, 629, 535, 537, 414, 278, 996, 553, 427, 628, 867, 291, 233, 539, 79, 199, 427, 415, 536, 257, 209, 308, 872, 771, 670, 410, 1000, 585, 130, 974, 628, 380, 719, 989, 528, 135, 765, 139, 445, 874, 162, 673, 81, 523, 597, 486, 610, 937, 958, 387, 216, 546, 689, 660, 490, 46, 153, 684, 337, 56, 387, 534, 118, 697, 839, 124, 743, 126, 27, 589, 506, 511, 963, 315, 988, 231, 324, 498, 374, 195, 293, 944, 535, 899, 55, 562, 427, 53, 383, 685, 788, 201, 539, 481, 983, 380, 351, 661, 674, 306, 819, 113, 986, 885, 934, 673, 597, 179, 970, 546, 110, 427, 121, 770, 494, 957, 774, 796, 50, 760, 595, 200, 580, 686, 745, 703, 267, 870, 147, 236, 369, 57, 821, 36, 279, 945, 455, 478, 315, 212, 497, 180, 266, 207, 352, 734, 763, 606, 483, 926, 170, 219, 129, 803, 767, 952, 807, 698, 995, 180, 850, 966, 230, 707, 274, 646, 724, 95, 915, 725, 182, 408, 909, 37, 957, 504, 699, 68, 403, 919, 707, 732, 745, 248, 24, 123, 319, 155, 927, 985, 771, 455, 396, 706, 302, 161, 728, 701, 140, 244, 582, 312, 51, 488, 15, 32, 485, 839, 217, 183, 871, 819, 342, 981, 808, 164, 803, 96, 469, 40, 644, 8, 379, 686, 738, 974, 298, 194, 868, 720, 652, 654, 820, 904, 437, 740, 319, 401, 335, 380, 26, 948, 602, 496, 924, 935, 230, 924, 558, 219, 492, 811, 316, 347, 658, 683, 325, 497, 869, 170, 747, 887, 217, 932, 493, 480, 340, 214, 958, 331, 219, 205, 391, 532, 328, 825, 111, 74, 177, 674, 146, 508, 480, 225, 178, 99, 250, 661, 336, 293, 901, 389, 460, 128, 25, 7, 973, 781, 560, 71, 130, 637, 599, 849, 114, 13, 461, 887, 190, 789, 641, 43, 864, 476, 68, 465, 224, 912, 803, 332, 498, 548, 826, 969, 444, 761, 944, 796, 959, 913, 632, 885, 459, 660, 826, 815, 615, 406, 404, 683, 5, 842, 851, 932, 140, 449, 69, 741, 388, 515, 325, 797, 899, 769, 650, 103, 219, 118, 56, 596, 981, 383, 800, 224, 737, 149, 601, 887, 39, 738, 308, 820, 60, 320, 723, 254, 430, 827, 479, 159, 828, 509, 577, 955, 152, 728, 108, 512, 509, 54, 376, 70, 427, 929, 954, 460, 221, 715, 763, 609, 474, 537, 704, 277, 239, 94, 362, 175, 289, 204, 230, 450, 141, 369, 321, 733, 617, 649, 247, 145, 122, 400, 30, 199, 238, 906, 642, 952, 710, 957, 44, 87, 207, 418, 78, 519, 797, 861, 338, 644, 967, 772, 395, 984, 49, 850, 919, 437, 43, 945, 477, 976, 515, 291, 434, 765, 261, 568, 883, 951, 823, 671, 83, 227, 247, 261, 409, 303, 189, 252, 718, 782, 826, 376, 369, 518, 2, 842, 294, 364, 674, 792, 764, 171, 511, 857, 181, 865, 347, 803, 205, 680, 687, 728, 79, 724, 145, 785, 223, 244, 190, 352, 78, 355, 489, 533, 334, 23, 971, 894, 462, 650, 276, 698, 811, 818, 592, 654, 688, 731, 763, 204, 787, 200, 68, 276, 482, 187, 317, 198, 581, 586, 285, 28, 650, 6, 358, 660, 968, 670, 58, 532, 296, 604, 861, 147, 72, 527, 361, 928, 682, 753, 498, 30, 788, 13, 302, 853, 284, 396, 177, 986, 266, 993, 930, 466, 955, 820, 285, 598, 227, 753, 877, 182, 931, 238, 502, 907, 47, 554, 10, 335, 80, 993, 984, 389, 185, 233, 444, 63, 491, 513, 654, 115, 184, 395, 777, 298, 781, 605, 355, 936, 203, 795, 250, 513, 511, 153, 530, 200, 346, 712, 357, 313, 111, 887, 14, 650, 637, 63, 546, 113, 833, 282, 608, 535, 381, 32, 949, 735, 328, 316, 337, 138, 24, 156, 492, 136, 895, 376, 750, 936, 988, 674, 165, 62, 463, 89, 876, 990, 218, 551, 156, 25, 491, 132, 141, 883, 77, 252, 299, 518, 504, 467, 457, 252, 391, 879, 606, 325, 429, 996, 305, 588, 689, 901, 633, 692, 621, 205, 472, 482, 806, 174, 822, 664, 85, 42, 944, 174, 468, 393, 794, 416, 788, 292, 558, 735, 982, 963, 128, 215, 114, 973, 686, 260, 772, 519, 616, 285, 368, 711, 710, 56, 382, 842, 635, 25, 210, 524, 870, 874, 418, 213, 535, 564, 418, 774, 29, 115, 925, 772, 769, 455, 648, 493, 892, 782, 480, 636, 988, 773, 719, 889, 896, 449, 458, 943, 722, 480, 268, 21, 991, 571, 15, 980, 896, 75, 570, 274, 842, 227, 837, 999, 199, 960, 419, 178, 126, 622, 255, 841, 690, 358, 77, 924, 700, 15, 617, 346, 501, 64, 638, 193, 187, 34, 692, 335, 79, 548, 798, 624, 502, 695, 105, 264, 239, 296, 619, 229, 970, 537, 284, 567, 170, 777, 544, 444, 230, 130, 792, 760, 317, 901, 151, 307, 596, 57, 11, 609, 302, 621, 896, 564, 691, 656, 442, 823, 57, 524, 835, 361, 986, 757, 741, 803, 219, 861, 333, 683, 601, 449, 986, 964, 431, 641, 243, 786, 479, 139, 830, 213, 2, 453, 407, 259, 790, 435, 708, 222, 766, 701, 827, 52, 721, 6, 253, 591, 415, 186, 341, 727, 92, 571, 612, 417, 467, 298, 849, 273, 587, 18, 922, 316, 684, 145, 398, 736, 907, 255, 83, 344, 251, 778, 509, 8, 702, 798, 241, 141, 318, 337, 969, 781, 303, 202, 410, 832, 881, 68, 951, 557, 677, 885, 320, 931, 937, 834, 654, 734, 141, 342, 749, 864, 886, 748, 190, 131, 158, 555, 314, 431, 962, 521, 635, 887, 579, 51, 438, 268, 594, 870, 806, 715, 86, 737, 762, 453, 1, 677, 309, 373, 373, 409, 468, 797]




The maximum pairwise product: 996000 (996 x 1000)
Charles Truscott Watters. More efficient, non pointer linked list algorithm
I love you big bro Tai. Thank you MIT


really watching that logarithmic algorithmic complexity beat the latter chosen algorithm

nlog(n^2)

DIVIDE AND CONQUER


127 Broken Head Rd, Suffolk Park / Byron Bay NSW 2481

Thank you Woolworths for delivering my groceries and thank you Centrelink and Australian Government for my disability support payment income

Charles Truscott


    for x in range(0, 1000, 1):
        L.append(random.randint(0, 1000))
        
        

"""
import random

def merge_order(P=[], Q=[], R=[], S=[], SPARE = []):
    if len(P) > 2:
        R.append(P[:len(P)//2])
        R.append(P[len(P)//2:])
        merge_order(P[:len(P)//2], P[len(P)//2:], [], [])
    if len(Q) > 2:
        R.append(Q[:len(Q)//2])
        R.append(Q[len(Q)//2:])
        merge_order(Q[:len(Q)//2], Q[len(Q)//2:], [], [])
#    print(R)
    for x in range(0, len(R) - 1, 1):
        if (len(R[x]) == 1 and len(R[x + 1]) == 2) or (len(R[x + 1]) == 1 and len(R[x]) == 2):
            SPARE.append(R[x])
            SPARE.append(R[x + 1])

#            if len(R[x]) == 1 and len(R[x + 1]) == 2:
#                S.append([R[x][0], R[x + 1][0], R[x][0] * R[x + 1][0]])
#                S.append([R[x][0], R[x + 1][1], R[x][0] * R[x + 1][1]])
#            elif len(R[x + 1]) == 1 and len(R[x]) == 2:
#               S.append([R[x][0], R[x + 1][0], R[x][0] * R[x + 1][0]])
#                S.append([R[x][1], R[x + 1][0], R[x][1] * R[x * 1][0]])
        if len(R[x]) == 2:
            SPARE.append(R[x])
#        if len(R[x]) == 1:
#            SPARE.append(R[x])
#    print("SPARE: {}".format(SPARE))
    maximum = 0
    temp = 0
#    for x in range(0, len(SPARE), 1):
#        for y in range(0, len(SPARE), 1):
#            if x != y:
#                if len(SPARE[x]) == 1 and len(SPARE[y]) == 2:
##                    print("Multiplying {} by {}".format(SPARE[x][0], SPARE[y][0]))
#                    temp = SPARE[x][0] * SPARE[y][0]
#                    S.append([SPARE[x][0], SPARE[y][0], temp])
##                    print("Multiplying {} by {}".format(SPARE[x][0], SPARE[y][1]))
#                    temp = SPARE[x][0] * SPARE[y][1]
#                    S.append([SPARE[x][0], SPARE[y][1], temp])
##                    print("Multiplying {} by {}".format(SPARE[y][0], SPARE[y][1]))
#                    temp = SPARE[y][0] * SPARE[y][1]
#                    S.append([SPARE[y][0], SPARE[y][1], temp])
#                elif len(SPARE[x]) == 2 and len(SPARE[y]) == 1:
##                    print("Multiplying {} by {}".format(SPARE[x][0], SPARE[y][0]))
#                    temp = SPARE[x][0] * SPARE[y][0]
#                    S.append([SPARE[x][0], SPARE[y][0], temp])
##                    print("Multiplying {} by {}".format(SPARE[x][1], SPARE[y][0]))
#                    temp = SPARE[x][1] * SPARE[y][0]
#                    S.append([SPARE[x][1], SPARE[y][0], temp])
##                    print("Multiplying {} by {}".format(SPARE[x][0], SPARE[x][1]))
#                    temp = SPARE[x][0] * SPARE[x][1]
#                    S.append([SPARE[x][0], SPARE[x][1], temp])
#                    
#    for q in range(0, len(SPARE), 1):
#        for r in range(0, len(SPARE[q]), 1):
#           for s in range(len(SPARE[q]), -1, 1):
#                temp = SPARE[q][r] * SPARE[q][s]
#    for q in range(len(SPARE), 0, -1):
#        for x in range(0, len(SPARE), 1):
#            for y in range(0, len(SPARE[q]), 1):
#                print("SPARE: {}".format(SPARE[q]))
#                    temp = SPARE[q][y] * SPARE[x][z]
#                    print("{} x {} is {}".format(SPARE[q][y], SPARE[x][z], temp))
                    
#            print(SPARE[x], SPARE[y])
    i = 0
    j = 0
    p = 0
    q = 0
    if len(Q) == 0:
        for x in SPARE:
            for y in SPARE:
                for a in x:
                    for b in y:
                        if x.index(a) != y.index(b):
                            if i * j > maximum:
                                maximum = i * j
                                p = i
                                q = j
#                            print("The maximum value is currently: {}".format(maximum))
                            temp = a * b
    #                            print("{} x {} is {}".format(a, b, temp))
                            i = a
                            j = b
        return maximum, p, q
#        for x in range(0, len(SPARE), 1):
#            for y in range(0, len(SPARE), 1):
#                if x != y:
#                    for z in range(len(SPARE[x]) - 1):
#                        for t in range(len(SPARE[y]) - 1):
#                            temp = SPARE[x][z] * SPARE[y][t]
#                            print("{} x {} is {}".format(SPARE[x][z], SPARE[x][t], temp))
#   print(P, Q, R, S, SPARE, len(SPARE))

def main():
#    L = list(int(x) for x in range(1, 1 + 5, 1))
#    L = [1, 2, 3, 4, 5, 6, 20, 21, 21, 2]
    L = []
    for x in range(0, 1000, 1):
        L.append(random.randint(0, 1000))
    maximum, lhs, rhs = merge_order(L, [], [], [])
    print("The list: {}\n\n\n\n".format(L))
    print("The maximum pairwise product: {} ({} x {})".format(maximum, lhs, rhs))
    print("Charles Truscott Watters. More efficient, non pointer linked list algorithm")
    print("I love you big bro Tai. Thank you MIT")
if __name__ == "__main__": main()