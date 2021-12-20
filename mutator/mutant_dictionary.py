from MutatorClass import Mutator

all_mutant_keys = ["EqualityEqualsToNotEquals", "EqualityNotEqualsToEquals", "LogicalAndToOr", "LogicalOrToAnd", "LogicalBitwiseOrToAnd" ,
                   "LogicalBitwiseAndToOr", "ArithmeticIncrementToDecrement" , "ArithmeticDecrementToIncrement", "ArithmeticDivEqualsToMultEquals",
                   "ArithmeticMultEqualsToDivEquals", "ArithmeticModEqualsToMultEquals", "ArithmeticMultEqualsToModEquals", "ArithmeticDivToMult",
                   "ArithmeticMultToDiv", "ArithmeticMultToMod", "ArithmeticModToMult", "ArithmeticPlusToMinus", "ArithmeticMinusToPlus" ,
                   "ArithmeticMinusAssignToPlusAssign", "ArithmeticPlusAssignToMinusAssign", "StringToEmpty", "ConditionalLessEqualsToLess",
                   "ConditionalGreaterEqualsToGreater", "ConditionalGreaterToGreaterEquals", "ConditionalLessToLessEquals", "BooleanTrueToFalse",
                   "BooleanFalseToTrue", "IfToFalse", "IfToTrue"]

all_mutants = {
    "EqualityEqualsToNotEquals": Mutator("==","!=","EqualityEqualsToNotEquals"),
    "EqualityNotEqualsToEquals": Mutator("!=", "==","EqualityNotEqualsToEquals"),
    "LogicalAndToOr": Mutator("&&", "||", "LogicalAndToOr"),
    "LogicalOrToAnd": Mutator("[||][^ ]", "&&", "LogicalOrToAnd"),
    "LogicalBitwiseOrToAnd": Mutator("(?<!\|)\|(?!\|)", "&", "LogicalBitwiseOrToAnd"),
    "LogicalBitwiseAndToOr": Mutator("(?<!\&)\&(?!\&)", "|", "LogicalBitwiseAndToOr"),
    "ArithmeticIncrementToDecrement": Mutator("[+]{2}", "--", "ArithmeticIncrementToDecrement"),
    "ArithmeticDecrementToIncrement": Mutator("[-]{2}", "++", "ArithmeticDecrementToIncrement"),
    "ArithmeticDivEqualsToMultEquals": Mutator("[\/][=]", "*=", "ArithmeticDivEqualsToMultEquals"),
    "ArithmeticMultEqualsToDivEquals": Mutator("\*[=]", "/=", "ArithmeticMultEqualsToDivEquals"),
    "ArithmeticModEqualsToMultEquals": Mutator("%[=]", "*=", "ArithmeticModEqualsToMultEquals"),
    "ArithmeticMultEqualsToModEquals": Mutator("(?<![+=*%\<>-])[*][=](?![+=*%\<>-])", "%=", "ArithmeticMultEqualsToModEquals"),
    "ArithmeticDivToMult": Mutator("(?<![+=*\/-])\/(?![+=*\/-])", "*", "ArithmeticDivToMult"),
    "ArithmeticMultToDiv": Mutator("(?<![+=*\/-])\*(?![+=*\/-])", "/", "ArithmeticMultToDiv"),
    "ArithmeticMultToMod": Mutator("(?<![+=*\/-])\*(?![+=*\/-])", "%", "ArithmeticMultToMod"),
    "ArithmeticModToMult": Mutator("(?<![+=*%\/-])\%(?![+=*%\/-])", "*", "ArithmeticModToMult"),
    "ArithmeticPlusToMinus": Mutator("(?<![+=*\/-])\+(?![+=*\/-])", "-", "ArithmeticPlusToMinus"),
    "ArithmeticMinusToPlus": Mutator("(?<![+=*\/-])\-(?![+=*\/-])", "+", "ArithmeticMinusToPlus"),
    "ArithmeticMinusAssignToPlusAssign": Mutator("(?<![+=*%\<>-])-=(?![+=*%\<>-])", "+=", "ArithmeticMinusAssignToPlusAssign"),
    "ArithmeticPlusAssignToMinusAssign": Mutator("(?<![+=*%\<>-])\+=(?![+=*%\<>-])", "-=", "ArithmeticPlusAssignToMinusAssign"),
    "StringToEmpty": Mutator("\"[a-zA-Z\d\s~`!@#$%^&*()+=,.<>/?\';:\[\]\{\}\\-]*\"", "", "StringToEmpty"),
    "ConditionalLessEqualsToLess": Mutator("(?<![+=*%\<>-])<=(?![+=*%\<>-])", "<", "ConditionalLessEqualsToLess"),
    "ConditionalGreaterEqualsToGreater": Mutator("(?<![+=*%\<>-])>=(?![+=*%\<>-])", ">", "ConditionalGreaterEqualsToGreater"),
    "ConditionalGreaterToGreaterEquals": Mutator("(?<![+=*%\<>-])\>(?![+=*%\<>-])", ">=", "ConditionalGreaterToGreaterEquals"),
    "ConditionalLessToLessEquals": Mutator("(?<![+=*%\><-])\<(?![+=*%\><-])", "<=", "ConditionalLessToLessEquals"),
    "BooleanTrueToFalse": Mutator("(?<![+!*%;\/-])(true)(?![+=*%\/-])", "false", "BooleanTrueToFalse"),
    "BooleanFalseToTrue": Mutator("(?<![+!*%;\/-])(false)(?![+=*%\/-])", "true", "BooleanFalseToTrue"),
    "IfToFalse": Mutator("(?<=(if))\(.*\)(?!;)", "(false)", "IfToFalse"),
    "IfToTrue": Mutator("(?<=(if))\(.*\)(?!;)", "(true)", "IfToTrue")
}

#print(mutant_dictionary)
