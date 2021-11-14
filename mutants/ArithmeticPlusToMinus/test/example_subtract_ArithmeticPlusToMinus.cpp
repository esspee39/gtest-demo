#include <gtest/gtest.h>

#include "example_ArithmeticPlusToMinus.h"

TEST(example_ArithmeticPlusToMinus, subtract) {
  double res;
  res = subtract_numbers(1.0, 2.0);
  ASSERT_NEAR(res, -1.0, 1.0e-11);
}