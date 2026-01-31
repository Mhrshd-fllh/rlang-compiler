grammar RLang;

// ============================================================
// ۱. قوانین لغوی (Lexer Rules)
// ============================================================

// کلمات کلیدی
KEYWORD_ENV: 'ENVIRONMENT';
KEYWORD_STATE: 'STATE';
KEYWORD_ACTION: 'ACTION';
KEYWORD_ACTIONS: 'ACTIONS';
KEYWORD_DYNAMICS: 'DYNAMICS';
KEYWORD_REWARDS: 'REWARDS';
KEYWORD_TRAINING: 'TRAINING';
KEYWORD_ALWAYS: 'always';
KEYWORD_WHEN: 'when';
KEYWORD_MATCH: 'match';
KEYWORD_IF: 'if';
IN: 'in';

// انواع داده
TYPE_CONT: 'continuous';
TYPE_DISC: 'discrete';



// شناسه‌ها و مقادیر
ID: [a-zA-Z_] [a-zA-Z0-9_]*;
NUMBER: [0-9]+ ('.' [0-9]+)?;
STRING: '"' .*? '"';

// عملگرها و علائم
ASSIGN_COLON: ':';
ASSIGN_EQ: '=';
SEMI: ';';
COMMA: ',';
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
LBRACK: '[';
RBRACK: ']';
ARROW: '->';
EQ: '==';
NEQ: '!=';
GT: '>';
LT: '<';
PLUS: '+';
MINUS: '-';
MUL: '*';
DIV: '/';
AND: '&';
OR: '|';

// نادیده گرفتن فاصله‌ها و کامنت‌ها
WS: [ \t\r\n]+ -> skip;
COMMENT: '//' ~[\r\n]* -> skip;

// ============================================================
// ۲. قوانین نحوی (Parser Rules)
// ============================================================

prog: environmentDef EOF;

environmentDef
    : KEYWORD_ENV ID LBRACE
        stateDef
        actionsDef
        dynamicsDef?
        rewardsDef?
        trainingDef?
      RBRACE
    ;

// --- STATE ---
stateDef
    : KEYWORD_STATE LBRACE (varDecl)* RBRACE
    ;

varDecl
    : ID ASSIGN_COLON type paramList SEMI
    ;

type
    : TYPE_CONT   # ContinuousType
    | TYPE_DISC   # DiscreteType
    ;

paramList
    : LPAREN (expr (COMMA expr)*)? RPAREN   # ContinuousParams
    | LBRACK (expr (COMMA expr)*)? RBRACK   # DiscreteParams
    ;

// --- ACTIONS ---
actionsDef
    : KEYWORD_ACTIONS LBRACE (ID (COMMA ID)*)? RBRACE
    ;

// --- DYNAMICS ---
dynamicsDef
    : KEYWORD_DYNAMICS LBRACE (dynamicsRule)* RBRACE
    ;

dynamicsRule
    : KEYWORD_ALWAYS LBRACE statementList RBRACE          # AlwaysRule
    | KEYWORD_WHEN LPAREN condition RPAREN LBRACE statementList RBRACE # WhenRule
    ;

// لیست دستورات: فقط مجموعه‌ای از statement است (سمی‌کالن داخل خود statement است)
statementList
    : (statement)*
    ;

// هر دستور باید با سمی‌کالن تمام شود (مگر اینکه بلوک {} باشد)
statement
    : assignment SEMI?
    | ifStatement SEMI?
    | matchStatement SEMI?
    | LBRACE statementList RBRACE  // بلوک خالی یا تودرتو بدون سمی‌کالن خارجی
    ;

assignment
    : ID ASSIGN_EQ expr SEMI?
    ;

ifStatement
    : KEYWORD_IF LPAREN condition RPAREN statement
    ;

matchStatement
    : KEYWORD_MATCH KEYWORD_ACTION LBRACE (matchCase)* RBRACE
    ;

matchCase
    : ID ARROW statement SEMI
    ;

// --- REWARDS ---
rewardsDef
    : KEYWORD_REWARDS LBRACE (rewardRule)* RBRACE
    ;

rewardRule
    : KEYWORD_IF LPAREN condition RPAREN ARROW expr SEMI
    ;

// --- TRAINING ---
trainingDef
    : KEYWORD_TRAINING LBRACE (configAssign)* RBRACE
    ;

configAssign
    : ID ASSIGN_COLON expr SEMI
    ;

// --- CONDITIONS & EXPR ---
condition
    : ID IN LBRACK (expr (COMMA expr)*)? RBRACK   # ActionInListCondition
    | expr op=(EQ | NEQ | GT | LT) expr           # SimpleCondition
    ;

expr
    : expr op=(MUL | DIV) expr   # MulDiv
    | expr op=(PLUS | MINUS) expr # AddSub
    | ID                        # IdExpr
    | NUMBER                    # NumberExpr
    | LPAREN expr RPAREN        # ParenExpr
    ;