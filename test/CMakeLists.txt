include(FetchContent)
FetchContent_Declare(gtest
  QUIET
  URL https://github.com/google/googletest/archive/release-1.10.0.tar.gz
)
# configure build of googletest
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
set(BUILD_GMOCK OFF CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(gtest)

add_executable(
    unit_tests
    example_add.cpp
    example_subtract.cpp
    example_equality.cpp
    example_iterate.cpp
    example_decrement.cpp
    example_divideEquals.cpp
    example_multiEquals.cpp
    example_and.cpp
    example_bitwiseand.cpp
    example_bitwiseor.cpp
    example_booleanfalse.cpp
    example_booleantrue.cpp
    example_greaterthan.cpp
    example_greaterthanequals.cpp
    example_lessthan.cpp
    example_lessthanequals.cpp
    example_notequals.cpp
    example_or.cpp
    example_mod.cpp
    )

target_link_libraries(unit_tests
  PRIVATE
    example
    gtest_main
  )

# automatic discovery of unit tests
include(GoogleTest)
gtest_discover_tests(unit_tests
  PROPERTIES
    LABELS "unit"
  DISCOVERY_TIMEOUT  # how long to wait (in seconds) before crashing
    240
  )
