#include <gtest/gtest.h>

#include "example.h"

TEST(example, mod) {

  ASSERT_EQ(2, mod_numbers(10.0, 8.0));
}