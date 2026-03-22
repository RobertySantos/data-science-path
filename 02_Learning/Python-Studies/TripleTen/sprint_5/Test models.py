
#Study notes for Sprint 5 — TripleTen Data Analysis Program.
#Covers: string manipulation, list operations, and basic DataFrame creation.

#Author  : Roberty
#Updated : 2025
import pandas as pd


# =============================================================================
# SECTION 1 — String Basics & Escape Characters
# =============================================================================

name = "Roberty"

# Escape characters let us embed special chars without breaking the string.
# \\ = literal backslash, \" = quote inside a double-quoted string.
dialogue     = 'Bianca: "Poderia me ajudar?"'   # cleaner: use single quotes outside
line_break   = "Vamos pular \na linha"            # \n = newline
tab_spacing  = "Está muito \tlonge?"              # \t = horizontal tab (one stop)

print("--- Escape Characters ---")
print(dialogue)
print(line_break)
print(tab_spacing)


# =============================================================================
# SECTION 2 — Indexing & Slicing
# =============================================================================

# Strings are zero-indexed sequences — same mental model as lists and arrays.
char_at_index   = dialogue[3]      # single char: 'a'
substring_slice = dialogue[0:6]    # half-open interval: index 0 included, 6 excluded

print("\n--- Indexing & Slicing ---")
print(f"Char at index 3  : {char_at_index!r}")
print(f"Slice [0:6]      : {substring_slice!r}")

# QA CHECK: confirm slice length matches expectation before using it downstream.
assert len(substring_slice) == 6, "Slice length mismatch — review index logic."


# =============================================================================
# SECTION 3 — String Formatting
# =============================================================================

# f-strings (PEP 498) are preferred: evaluated at runtime, readable, fast.
greeting_fstring = f"Meu nome é {name}"

# .format() is older but still common in legacy codebases — good to know.
greeting_format = "Meu nome também é {}".format(name)

print("\n--- Formatting ---")
print(greeting_fstring)
print(greeting_format)


# =============================================================================
# SECTION 4 — String Methods
# =============================================================================

raw_input = "     Bem Espaçado    "

# .strip() is critical in data pipelines: extra whitespace from CSV exports
# or copy-paste frequently causes silent mismatches in joins and filters.
cleaned     = raw_input.strip()
lowercased  = cleaned.lower()
uppercased  = cleaned.upper()

# .replace() works on any substring — useful for normalizing separators or
# fixing encoding artifacts (e.g., replacing "R$" before casting to float).
replaced = greeting_format.replace("R", "Nosso")

print("\n--- String Methods ---")
print(f"strip  : {cleaned!r}")
print(f"lower  : {lowercased}")
print(f"upper  : {uppercased}")
print(f"replace: {replaced}")

# split() + join() are a common pair for reshaping text data.
words          = greeting_fstring.split()        # default separator: whitespace
hyphen_joined  = "-".join(words)

print(f"split  : {words}")
print(f"join   : {hyphen_joined}")


# =============================================================================
# SECTION 5 — String Validation Methods
# =============================================================================

# These return bool — useful for input validation before type conversion.
print("\n--- Validation ---")
print(f"islower : {name.islower()}")   # False — 'R' is uppercase
print(f"isdigit : {name.isdigit()}")   # False — letters, not digits
print(f"isalpha : {name.isalpha()}")   # True  — only letters, no spaces/punctuation


# =============================================================================
# SECTION 6 — List Operations
# =============================================================================

# Avoid naming variables 'list' — it shadows Python's built-in list() function.
sample_items  = ["Item 1", "Item 2"]
nested_example = ["Lista aninhada"]

first_item  = sample_items[0]
nested_item = nested_example[0]   # double-index demo preserved
sliced      = sample_items[0:2]

print("\n--- List Access ---")
print(f"first_item  : {first_item}")
print(f"nested_item : {nested_item}")
print(f"sliced      : {sliced}")

# Mutation methods — these modify the list IN PLACE (no return value to assign).
sample_items.append("Novo item")
sample_items.extend(["Item Novo", "Item mais novo ainda"])
sample_items.insert(1, "Fui inserido")

# QA CHECK: confirm list length after bulk mutations.
print(f"\nList após mutações (len={len(sample_items)}): {sample_items}")

# .pop() removes by index and RETURNS the removed item — useful for stack logic.
removed = sample_items.pop(2)
print(f"Removido com pop(2): {removed!r}")

# sorted() vs .sort(): sorted() returns a new list — safer when you need
# to keep the original for comparison or logging.
sample_items.sort()
number_list = [20, 10, 12, 14, 56, 24, 65, 102]
sorted_numbers = sorted(number_list)   # original preserved

print(f"\nsorted_numbers : {sorted_numbers}")
print(f"number_list    : {number_list}  ← original unchanged")


# =============================================================================
# SECTION 7 — Aggregate Functions on Lists
# =============================================================================

list_sum = sum(number_list)
list_max = max(number_list)
list_min = min(number_list)

print("\n--- Aggregations ---")
print(f"sum : {list_sum}")
print(f"max : {list_max}")
print(f"min : {list_min}")

# QA CHECK: basic sanity — min should always be less than max.
assert list_min < list_max, "Aggregation error: min >= max. Check the input list."


# =============================================================================
# SECTION 8 — Basic DataFrame Creation & Validation
# =============================================================================

# Passing column names at creation makes the DataFrame self-documenting.
# Without them, Pandas assigns 0, 1, 2... which is hard to read downstream.
df = pd.DataFrame(
    data={
        "index_col"  : [0, 1, 2, 3, 4],
        "label_col"  : ["primeiro", "segundo", "terceiro", "quarto", "quinto"],
    }
)

print("\n--- DataFrame ---")
print(df)

# QA CHECKS — two things a junior analyst commonly skips:
# 1. Shape confirms the DataFrame has the expected number of rows and columns.
# 2. .isnull().sum() catches silent NaN values before any analysis runs.
print(f"\nShape     : {df.shape}")
print(f"Null count:\n{df.isnull().sum()}")