#!/bin/bash

N=$2
D=$4
AGENT=$6

#==============================================================================
#                               mediumClassic
#==============================================================================

start=$SECONDS
if (($D != 0)); then
    res_0=`python pacman.py -p $AGENT -q -a depth=$D -l mediumClassic -k 0 -n $N | cut -d":" -f2 | head -$N`
fi
res_1=`python pacman.py -p $AGENT -q -a depth=$D -l mediumClassic -k 1 -n $N | cut -d":" -f2 | head -$N`
res_2=`python pacman.py -p $AGENT -q -a depth=$D -l mediumClassic -k 2 -n $N | cut -d":" -f2 | head -$N`
res_3=`python pacman.py -p $AGENT -q -a depth=$D -l mediumClassic -k 3 -n $N | cut -d":" -f2 | head -$N`
res_4=`python pacman.py -p $AGENT -q -a depth=$D -l mediumClassic -k 4 -n $N | cut -d":" -f2 | head -$N`
res_5=`python pacman.py -p $AGENT -q -a depth=$D -l mediumClassic -k 5 -n $N | cut -d":" -f2 | head -$N`
res_d=`python pacman.py -p $AGENT -q -a depth=$D -l mediumClassic -n $N | cut -d":" -f2 | head -$N`
end=$SECONDS

duration_mediumClassic=$((end-start))
sum_mediumClassic=0

if (($D != 0)); then
    for r in $res_0; do
        sum_mediumClassic=$(($sum_mediumClassic+$r))
    done
fi
for r in $res_1; do
    sum_mediumClassic=$(($sum_mediumClassic+$r))
done
for r in $res_2; do
    sum_mediumClassic=$(($sum_mediumClassic+$r))
done
for r in $res_3; do
    sum_mediumClassic=$(($sum_mediumClassic+$r))
done
for r in $res_4; do
    sum_mediumClassic=$(($sum_mediumClassic+$r))
done
for r in $res_5; do
    sum_mediumClassic=$(($sum_mediumClassic+$r))
done
for r in $res_d; do
    sum_mediumClassic=$(($sum_mediumClassic+$r))
done

echo mediumClassic DONE

#==============================================================================
#                               capsuleClassic
#==============================================================================

start=$SECONDS
if (($D != 0)); then
    res_0=`python pacman.py -p $AGENT -q -a depth=$D -l capsuleClassic -k 0 -n $N | cut -d":" -f2 | head -$N`
fi
res_1=`python pacman.py -p $AGENT -q -a depth=$D -l capsuleClassic -k 1 -n $N | cut -d":" -f2 | head -$N`
res_2=`python pacman.py -p $AGENT -q -a depth=$D -l capsuleClassic -k 2 -n $N | cut -d":" -f2 | head -$N`
res_3=`python pacman.py -p $AGENT -q -a depth=$D -l capsuleClassic -k 3 -n $N | cut -d":" -f2 | head -$N`
res_4=`python pacman.py -p $AGENT -q -a depth=$D -l capsuleClassic -k 4 -n $N | cut -d":" -f2 | head -$N`
res_5=`python pacman.py -p $AGENT -q -a depth=$D -l capsuleClassic -k 5 -n $N | cut -d":" -f2 | head -$N`
res_d=`python pacman.py -p $AGENT -q -a depth=$D -l capsuleClassic -n $N | cut -d":" -f2 | head -$N`
end=$SECONDS

duration_capsuleClassic=$((end-start))
sum_capsuleClassic=0

if (($D != 0)); then
    for r in $res_0; do
        sum_capsuleClassic=$(($sum_capsuleClassic+$r))
    done
fi
for r in $res_1; do
    sum_capsuleClassic=$(($sum_capsuleClassic+$r))
done
for r in $res_2; do
    sum_capsuleClassic=$(($sum_capsuleClassic+$r))
done
for r in $res_3; do
    sum_capsuleClassic=$(($sum_capsuleClassic+$r))
done
for r in $res_4; do
    sum_capsuleClassic=$(($sum_capsuleClassic+$r))
done
for r in $res_5; do
    sum_capsuleClassic=$(($sum_capsuleClassic+$r))
done
for r in $res_d; do
    sum_capsuleClassic=$(($sum_capsuleClassic+$r))
done

echo capsuleClassic DONE

#==============================================================================
#                               contestClassic
#==============================================================================

start=$SECONDS
if (($D != 0)); then
    res_0=`python pacman.py -p $AGENT -q -a depth=$D -l contestClassic -k 0 -n $N | cut -d":" -f2 | head -$N`
fi
res_1=`python pacman.py -p $AGENT -q -a depth=$D -l contestClassic -k 1 -n $N | cut -d":" -f2 | head -$N`
res_2=`python pacman.py -p $AGENT -q -a depth=$D -l contestClassic -k 2 -n $N | cut -d":" -f2 | head -$N`
res_3=`python pacman.py -p $AGENT -q -a depth=$D -l contestClassic -k 3 -n $N | cut -d":" -f2 | head -$N`
res_4=`python pacman.py -p $AGENT -q -a depth=$D -l contestClassic -k 4 -n $N | cut -d":" -f2 | head -$N`
res_5=`python pacman.py -p $AGENT -q -a depth=$D -l contestClassic -k 5 -n $N | cut -d":" -f2 | head -$N`
res_d=`python pacman.py -p $AGENT -q -a depth=$D -l contestClassic -n $N | cut -d":" -f2 | head -$N`
end=$SECONDS

duration_contestClassic=$((end-start))
sum_contestClassic=0

if (($D != 0)); then
    for r in $res_0; do
        sum_contestClassic=$(($sum_contestClassic+$r))
    done
fi
for r in $res_1; do
    sum_contestClassic=$(($sum_contestClassic+$r))
done
for r in $res_2; do
    sum_contestClassic=$(($sum_contestClassic+$r))
done
for r in $res_3; do
    sum_contestClassic=$(($sum_contestClassic+$r))
done
for r in $res_4; do
    sum_contestClassic=$(($sum_contestClassic+$r))
done
for r in $res_5; do
    sum_contestClassic=$(($sum_contestClassic+$r))
done
for r in $res_d; do
    sum_contestClassic=$(($sum_contestClassic+$r))
done

echo contestClassic DONE

#==============================================================================
#                               minimaxClassic
#==============================================================================

start=$SECONDS
if (($D != 0)); then
    res_0=`python pacman.py -p $AGENT -q -a depth=$D -l minimaxClassic -k 0 -n $N | cut -d":" -f2 | head -$N`
fi
res_1=`python pacman.py -p $AGENT -q -a depth=$D -l minimaxClassic -k 1 -n $N | cut -d":" -f2 | head -$N`
res_2=`python pacman.py -p $AGENT -q -a depth=$D -l minimaxClassic -k 2 -n $N | cut -d":" -f2 | head -$N`
res_3=`python pacman.py -p $AGENT -q -a depth=$D -l minimaxClassic -k 3 -n $N | cut -d":" -f2 | head -$N`
res_4=`python pacman.py -p $AGENT -q -a depth=$D -l minimaxClassic -k 4 -n $N | cut -d":" -f2 | head -$N`
res_5=`python pacman.py -p $AGENT -q -a depth=$D -l minimaxClassic -k 5 -n $N | cut -d":" -f2 | head -$N`
res_d=`python pacman.py -p $AGENT -q -a depth=$D -l minimaxClassic -n $N | cut -d":" -f2 | head -$N`
end=$SECONDS

duration_minimaxClassic=$((end-start))
sum_minimaxClassic=0

if (($D != 0)); then
    for r in $res_0; do
        sum_minimaxClassic=$(($sum_minimaxClassic+$r))
    done
fi
for r in $res_1; do
    sum_minimaxClassic=$(($sum_minimaxClassic+$r))
done
for r in $res_2; do
    sum_minimaxClassic=$(($sum_minimaxClassic+$r))
done
for r in $res_3; do
    sum_minimaxClassic=$(($sum_minimaxClassic+$r))
done
for r in $res_4; do
    sum_minimaxClassic=$(($sum_minimaxClassic+$r))
done
for r in $res_5; do
    sum_minimaxClassic=$(($sum_minimaxClassic+$r))
done
for r in $res_d; do
    sum_minimaxClassic=$(($sum_minimaxClassic+$r))
done

echo minimaxClassic DONE

#==============================================================================
#                               openClassic
#==============================================================================

start=$SECONDS
if (($D != 0)); then
    res_0=`python pacman.py -p $AGENT -q -a depth=$D -l openClassic -k 0 -n $N | cut -d":" -f2 | head -$N`
fi
res_1=`python pacman.py -p $AGENT -q -a depth=$D -l openClassic -k 1 -n $N | cut -d":" -f2 | head -$N`
res_2=`python pacman.py -p $AGENT -q -a depth=$D -l openClassic -k 2 -n $N | cut -d":" -f2 | head -$N`
res_3=`python pacman.py -p $AGENT -q -a depth=$D -l openClassic -k 3 -n $N | cut -d":" -f2 | head -$N`
res_4=`python pacman.py -p $AGENT -q -a depth=$D -l openClassic -k 4 -n $N | cut -d":" -f2 | head -$N`
res_5=`python pacman.py -p $AGENT -q -a depth=$D -l openClassic -k 5 -n $N | cut -d":" -f2 | head -$N`
res_d=`python pacman.py -p $AGENT -q -a depth=$D -l openClassic -n $N | cut -d":" -f2 | head -$N`
end=$SECONDS

duration_openClassic=$((end-start))
sum_openClassic=0

if (($D != 0)); then
    for r in $res_0; do
        sum_openClassic=$(($sum_openClassic+$r))
    done
fi
for r in $res_1; do
    sum_openClassic=$(($sum_openClassic+$r))
done
for r in $res_2; do
    sum_openClassic=$(($sum_openClassic+$r))
done
for r in $res_3; do
    sum_openClassic=$(($sum_openClassic+$r))
done
for r in $res_4; do
    sum_openClassic=$(($sum_openClassic+$r))
done
for r in $res_5; do
    sum_openClassic=$(($sum_openClassic+$r))
done
for r in $res_d; do
    sum_openClassic=$(($sum_openClassic+$r))
done

echo openClassic DONE

#==============================================================================
#                               originalClassic
#==============================================================================

start=$SECONDS
if (($D != 0)); then
    res_0=`python pacman.py -p $AGENT -q -a depth=$D -l originalClassic -k 0 -n $N | cut -d":" -f2 | head -$N`
fi
res_1=`python pacman.py -p $AGENT -q -a depth=$D -l originalClassic -k 1 -n $N | cut -d":" -f2 | head -$N`
res_2=`python pacman.py -p $AGENT -q -a depth=$D -l originalClassic -k 2 -n $N | cut -d":" -f2 | head -$N`
res_3=`python pacman.py -p $AGENT -q -a depth=$D -l originalClassic -k 3 -n $N | cut -d":" -f2 | head -$N`
res_4=`python pacman.py -p $AGENT -q -a depth=$D -l originalClassic -k 4 -n $N | cut -d":" -f2 | head -$N`
res_5=`python pacman.py -p $AGENT -q -a depth=$D -l originalClassic -k 5 -n $N | cut -d":" -f2 | head -$N`
res_d=`python pacman.py -p $AGENT -q -a depth=$D -l originalClassic -n $N | cut -d":" -f2 | head -$N`
end=$SECONDS

duration_originalClassic=$((end-start))
sum_originalClassic=0

if (($D != 0)); then
    for r in $res_0; do
        sum_originalClassic=$(($sum_originalClassic+$r))
    done
fi
for r in $res_1; do
    sum_originalClassic=$(($sum_originalClassic+$r))
done
for r in $res_2; do
    sum_originalClassic=$(($sum_originalClassic+$r))
done
for r in $res_3; do
    sum_originalClassic=$(($sum_originalClassic+$r))
done
for r in $res_4; do
    sum_originalClassic=$(($sum_originalClassic+$r))
done
for r in $res_5; do
    sum_originalClassic=$(($sum_originalClassic+$r))
done
for r in $res_d; do
    sum_originalClassic=$(($sum_originalClassic+$r))
done

echo originalClassic DONE

#==============================================================================
#                               smallClassic
#==============================================================================

start=$SECONDS
if (($D != 0)); then
    res_0=`python pacman.py -p $AGENT -q -a depth=$D -l smallClassic -k 0 -n $N | cut -d":" -f2 | head -$N`
fi
res_1=`python pacman.py -p $AGENT -q -a depth=$D -l smallClassic -k 1 -n $N | cut -d":" -f2 | head -$N`
res_2=`python pacman.py -p $AGENT -q -a depth=$D -l smallClassic -k 2 -n $N | cut -d":" -f2 | head -$N`
res_3=`python pacman.py -p $AGENT -q -a depth=$D -l smallClassic -k 3 -n $N | cut -d":" -f2 | head -$N`
res_4=`python pacman.py -p $AGENT -q -a depth=$D -l smallClassic -k 4 -n $N | cut -d":" -f2 | head -$N`
res_5=`python pacman.py -p $AGENT -q -a depth=$D -l smallClassic -k 5 -n $N | cut -d":" -f2 | head -$N`
res_d=`python pacman.py -p $AGENT -q -a depth=$D -l smallClassic -n $N | cut -d":" -f2 | head -$N`
end=$SECONDS

duration_smallClassic=$((end-start))
sum_smallClassic=0

if (($D != 0)); then
    for r in $res_0; do
        sum_smallClassic=$(($sum_smallClassic+$r))
    done
fi
for r in $res_1; do
    sum_smallClassic=$(($sum_smallClassic+$r))
done
for r in $res_2; do
    sum_smallClassic=$(($sum_smallClassic+$r))
done
for r in $res_3; do
    sum_smallClassic=$(($sum_smallClassic+$r))
done
for r in $res_4; do
    sum_smallClassic=$(($sum_smallClassic+$r))
done
for r in $res_5; do
    sum_smallClassic=$(($sum_smallClassic+$r))
done
for r in $res_d; do
    sum_smallClassic=$(($sum_smallClassic+$r))
done

echo smallClassic DONE

#==============================================================================
#                               testClassic
#==============================================================================

start=$SECONDS
if (($D != 0)); then
    res_0=`python pacman.py -p $AGENT -q -a depth=$D -l testClassic -k 0 -n $N | cut -d":" -f2 | head -$N`
fi
res_1=`python pacman.py -p $AGENT -q -a depth=$D -l testClassic -k 1 -n $N | cut -d":" -f2 | head -$N`
res_2=`python pacman.py -p $AGENT -q -a depth=$D -l testClassic -k 2 -n $N | cut -d":" -f2 | head -$N`
res_3=`python pacman.py -p $AGENT -q -a depth=$D -l testClassic -k 3 -n $N | cut -d":" -f2 | head -$N`
res_4=`python pacman.py -p $AGENT -q -a depth=$D -l testClassic -k 4 -n $N | cut -d":" -f2 | head -$N`
res_5=`python pacman.py -p $AGENT -q -a depth=$D -l testClassic -k 5 -n $N | cut -d":" -f2 | head -$N`
res_d=`python pacman.py -p $AGENT -q -a depth=$D -l testClassic -n $N | cut -d":" -f2 | head -$N`
end=$SECONDS

duration_testClassic=$((end-start))
sum_testClassic=0

if (($D != 0)); then
    for r in $res_0; do
        sum_testClassic=$(($sum_testClassic+$r))
    done
fi
for r in $res_1; do
    sum_testClassic=$(($sum_testClassic+$r))
done
for r in $res_2; do
    sum_testClassic=$(($sum_testClassic+$r))
done
for r in $res_3; do
    sum_testClassic=$(($sum_testClassic+$r))
done
for r in $res_4; do
    sum_testClassic=$(($sum_testClassic+$r))
done
for r in $res_5; do
    sum_testClassic=$(($sum_testClassic+$r))
done
for r in $res_d; do
    sum_testClassic=$(($sum_testClassic+$r))
done

echo testClassic DONE

##==============================================================================
##                               trappedClassic
##==============================================================================
#
#start=$SECONDS
#res_0=`python pacman.py -p ReflexAgent -q -l trappedClassic -k 0 -n $N | cut -d":" -f2 | head -$N`
#res_1=`python pacman.py -p ReflexAgent -q -l trappedClassic -k 1 -n $N | cut -d":" -f2 | head -$N`
#res_2=`python pacman.py -p ReflexAgent -q -l trappedClassic -k 2 -n $N | cut -d":" -f2 | head -$N`
#res_3=`python pacman.py -p ReflexAgent -q -l trappedClassic -k 3 -n $N | cut -d":" -f2 | head -$N`
#res_4=`python pacman.py -p ReflexAgent -q -l trappedClassic -k 4 -n $N | cut -d":" -f2 | head -$N`
#res_5=`python pacman.py -p ReflexAgent -q -l trappedClassic -k 5 -n $N | cut -d":" -f2 | head -$N`
#res_d=`python pacman.py -p ReflexAgent -q -l trappedClassic -n $N | cut -d":" -f2 | head -$N`
#end=$SECONDS
#
#duration_trappedClassic=$((end-start))
#sum_trappedClassic=0
#
#for r in $res_0; do
#    sum_trappedClassic=$(($sum_trappedClassic+$r))
#done
#for r in $res_1; do
#    sum_trappedClassic=$(($sum_trappedClassic+$r))
#done
#for r in $res_2; do
#    sum_trappedClassic=$(($sum_trappedClassic+$r))
#done
#for r in $res_3; do
#    sum_trappedClassic=$(($sum_trappedClassic+$r))
#done
#for r in $res_4; do
#    sum_trappedClassic=$(($sum_trappedClassic+$r))
#done
#for r in $res_5; do
#    sum_trappedClassic=$(($sum_trappedClassic+$r))
#done
#for r in $res_d; do
#    sum_trappedClassic=$(($sum_trappedClassic+$r))
#done
#
##==============================================================================
##                               trickyClassic
##==============================================================================
#
#start=$SECONDS
#res_0=`python pacman.py -p ReflexAgent -q -l trickyClassic -k 0 -n $N | cut -d":" -f2 | head -$N`
#res_1=`python pacman.py -p ReflexAgent -q -l trickyClassic -k 1 -n $N | cut -d":" -f2 | head -$N`
#res_2=`python pacman.py -p ReflexAgent -q -l trickyClassic -k 2 -n $N | cut -d":" -f2 | head -$N`
#res_3=`python pacman.py -p ReflexAgent -q -l trickyClassic -k 3 -n $N | cut -d":" -f2 | head -$N`
#res_4=`python pacman.py -p ReflexAgent -q -l trickyClassic -k 4 -n $N | cut -d":" -f2 | head -$N`
#res_5=`python pacman.py -p ReflexAgent -q -l trickyClassic -k 5 -n $N | cut -d":" -f2 | head -$N`
#res_d=`python pacman.py -p ReflexAgent -q -l trickyClassic -n $N | cut -d":" -f2 | head -$N`
#end=$SECONDS
#
#duration_trickyClassic=$((end-start))
#sum_trickyClassic=0
#
#for r in $res_0; do
#    sum_trickyClassic=$(($sum_trickyClassic+$r))
#done
#for r in $res_1; do
#    sum_trickyClassic=$(($sum_trickyClassic+$r))
#done
#for r in $res_2; do
#    sum_trickyClassic=$(($sum_trickyClassic+$r))
#done
#for r in $res_3; do
#    sum_trickyClassic=$(($sum_trickyClassic+$r))
#done
#for r in $res_4; do
#    sum_trickyClassic=$(($sum_trickyClassic+$r))
#done
#for r in $res_5; do
#    sum_trickyClassic=$(($sum_trickyClassic+$r))
#done
#for r in $res_d; do
#    sum_trickyClassic=$(($sum_trickyClassic+$r))
#done





sum=0
sum=$(($sum+$sum_mediumClassic))
sum=$(($sum+$sum_capsuleClassic))
sum=$(($sum+$sum_contestClassic))
sum=$(($sum+$sum_minimaxClassic))
sum=$(($sum+$sum_openClassic))
sum=$(($sum+$sum_originalClassic))
sum=$(($sum+$sum_smallClassic))
sum=$(($sum+$sum_testClassic))
#sum=$(($sum+$sum_trappedClassic))
#sum=$(($sum+$sum_trickyClassic))
echo -n "score: "
if (($D != 0)); then
    echo $(( $sum/$((56*$N)) ))
else
    echo $(( $sum/$((48*$N)) ))
fi

duration=0
duration=$(($duration+$duration_mediumClassic))
duration=$(($duration+$duration_capsuleClassic))
duration=$(($duration+$duration_contestClassic))
duration=$(($duration+$duration_minimaxClassic))
duration=$(($duration+$duration_openClassic))
duration=$(($duration+$duration_originalClassic))
duration=$(($duration+$duration_smallClassic))
duration=$(($duration+$duration_testClassic))
#duration=$(($duration+$duration_trappedClassic))
#duration=$(($duration+$duration_trickyClassic))
echo -n "duration: "
echo $(($duration))


