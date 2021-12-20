#include "example.h"

double add_numbers(const double f1, const double f2) { return f1 + f2;}

double subtract_numbers(const double f1, const double f2) { return f1 - f2;}

double multiply_numbers(const double f1, const double f2) { return f1 * f2;}

bool check_number_equality(const double f1, const double f2) { return f1 == f2;}

double iterate_number(double f1) {f1++; return f1;}

double decrement_number(double f1) {f1--; return f1;}

double divideEquals_number(double f1, double f2){f1 /= f2; return f1;}

double multiEquals_number(double f1, double f2){f1 *= f2; return f1;}

bool logical_and() {return (true&&false);}

bool logical_or() {return (true||false);}

bool bitwise_and() {return (true&false);}

bool bitwise_or() {return (true|false);}

bool booleantrue() {return (true);}

bool booleanfalse() {return (false);}

bool greaterthan() {return (7 > 6);}

bool greaterthanequals() {return (7 >= 6);}

bool lessthan() {return (6 < 7);}

bool lessthanequals() {return (6 <= 7);}

bool notequals() {return (1 != 2);}

bool mod_numbers(const double f1, const double f2) {return f1 % f2; }