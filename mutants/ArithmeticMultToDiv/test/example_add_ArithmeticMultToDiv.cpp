#include <gtest/gtest.h>

#include "example_ArithmeticMultToDiv.h"

TEST(example_ArithmeticMultToDiv, add) {
  double res;
  res = add_numbers(1.0, 2.0);
  ASSERT_NEAR(res, 3.0, 1.0e-11);
}
