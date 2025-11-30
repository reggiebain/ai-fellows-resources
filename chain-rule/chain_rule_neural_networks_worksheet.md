# How Does AI Learn? Tracing the Chain
## Student Discovery Worksheet

**Names:** ________________________________  **Date:** __________

**Group Members:** _____________________________________________________

---

## Introduction

You're going to discover how neural networks learn—using only the calculus you already know! A neural network is a mathematical function that learns from data by adjusting its internal parameters (called **weights**). Your challenge is to figure out HOW it adjusts these weights.

---

## The Network

Here's our simple neural network:

```
Input (x) → [×3, then add w₁] → Hidden (h) → [×2, then add w₂] → Output (y)
```

**Mathematical Form:**
- Hidden layer: h = 3x + w₁
- Output layer: y = 2h + w₂
- Error: E = ½(y - y_target)²

---

## Phase 1: Forward Pass - Understanding What We Have

**Given Information:**
- Input: x = 2
- Current weights: w₁ = 1, w₂ = 3
- Target output: y_target = 20
- Our network needs to predict 20, but it won't... yet!

### Task 1: Calculate the Current Output

**Step 1:** Calculate h (the hidden layer value)
```
h = 3x + w₁ = 3(___) + ___ = _____
```

**Step 2:** Calculate y (the output)
```
y = 2h + w₂ = 2(___) + ___ = _____
```

**Step 3:** Calculate the error
```
E = ½(y - y_target)² = ½(___ - ___)² = _____
```

**Discussion Question:** Is our network doing well? Why or why not?

___________________________________________________________________________

___________________________________________________________________________

---

## Phase 2: Experimental Discovery - How Do Weights Affect Error?

The network needs to adjust w₁ and w₂ to reduce the error. Let's experiment!

### Task 2: Exploring w₂ (The Output Weight)

**Try changing w₂ slightly and see what happens to the error:**

| w₂ Value | h (stays same) | New y | New Error E | Change in E |
|----------|----------------|-------|-------------|-------------|
| 3.0 (original) | | | | baseline |
| 3.1 | | | | |
| 2.9 | | | | |

**Observations:**
- When w₂ increases by 0.1, the error changes by approximately: __________

- When w₂ decreases by 0.1, the error changes by approximately: __________

- Should we increase or decrease w₂ to reduce the error? __________

### Task 3: Exploring w₁ (The Hidden Weight)

**Now try changing w₁:**

| w₁ Value | New h | New y | New Error E | Change in E |
|----------|-------|-------|-------------|-------------|
| 1.0 (original) | | | | baseline |
| 1.1 | | | | |
| 0.9 | | | | |

**Observations:**
- When w₁ increases by 0.1, the error changes by approximately: __________

- When w₁ decreases by 0.1, the error changes by approximately: __________

- Which weight (w₁ or w₂) has a bigger effect on the error? __________

---

## Phase 3: The Calculus Connection - Making It Precise

You've discovered experimentally how weights affect error. Now let's use calculus to find the **exact** relationship.

### Task 4: Direct Derivatives

**Part A: How does y change with w₂?**

Given: y = 2h + w₂ (and h doesn't depend on w₂)

```
dy/dw₂ = __________
```

**Part B: How does the error change with y?**

Given: E = ½(y - 20)²

```
dE/dy = ½ · 2(y - 20) · 1 = (y - 20)
```

At our current y = _____, this equals: dE/dy = __________

### Task 5: The Chain Rule - Connecting the Pieces

**The Big Question:** How does error change with w₂?

We want: **dE/dw₂**

But notice:
- E depends on y
- y depends on w₂

**This is a chain of dependencies! What calculus rule do we use?**

___________________________________________________________________________

**Apply the Chain Rule:**

```
dE/dw₂ = (dE/dy) · (dy/dw₂)

       = (______) · (______)
       
       = __________
```

**Check Your Work:** Does this value match your experimental results from Task 2? 

___________________________________________________________________________

---

## Phase 4: The Harder Case - A Longer Chain

### Task 6: Finding dE/dw₁

This one is trickier! The chain is longer:

```
w₁ affects h, which affects y, which affects E
```

**Part A: Find each piece of the chain**

1. How does h change with w₁?
   - Given: h = 3x + w₁
   ```
   dh/dw₁ = __________
   ```

2. How does y change with h?
   - Given: y = 2h + w₂
   ```
   dy/dh = __________
   ```

3. How does E change with y?
   - We already found this!
   ```
   dE/dy = __________
   ```

**Part B: Chain them together!**

```
dE/dw₁ = (dE/dy) · (dy/dh) · (dh/dw₁)

       = (______) · (______) · (______)
       
       = __________
```

**Check Your Work:** Does this match your experimental results from Task 3?

___________________________________________________________________________

---

## Phase 5: Reflection and Connection

### Task 7: Understanding What You Discovered

**Question 1:** Why was finding dE/dw₁ harder than finding dE/dw₂?

___________________________________________________________________________

___________________________________________________________________________

**Question 2:** What would happen if the network had 10 layers instead of 2? How many derivatives would you need to multiply together to find the gradient of the first weight?

___________________________________________________________________________

___________________________________________________________________________

**Question 3:** Modern neural networks like GPT-4 have billions of weights. How do you think they calculate gradients for all of them?

___________________________________________________________________________

___________________________________________________________________________

---

## The Big Reveal: Backpropagation

What you just discovered is called **backpropagation** - the fundamental algorithm for training neural networks!

**Key Ideas:**
1. The **chain rule** lets us trace how each weight affects the final error
2. We work **backward** through the network (that's why it's called "back" propagation)
3. Once we know dE/dw for each weight, we can adjust weights to reduce error
4. This same process works for networks with millions or billions of weights!

**The Update Rule:**
```
new_weight = old_weight - learning_rate × (dE/dweight)
```

### Task 8: Make It Better

Using your calculated gradients, update the weights to reduce the error:

**Using learning_rate = 0.1:**

```
w₂_new = w₂_old - 0.1 × (dE/dw₂)
       = 3 - 0.1 × (______)
       = __________

w₁_new = w₁_old - 0.1 × (dE/dw₁)
       = 1 - 0.1 × (______)
       = __________
```

**Now calculate the new error with these updated weights:**

```
h_new = 3(2) + w₁_new = __________
y_new = 2(h_new) + w₂_new = __________
E_new = ½(y_new - 20)² = __________
```

**Did the error decrease?** __________

---

## Extension Challenge (If Time Permits)

Real neural networks use **nonlinear activation functions**. Here's a common one:

**Sigmoid function:** σ(z) = 1/(1 + e⁻ᶻ)

**Its derivative:** σ'(z) = σ(z) · (1 - σ(z))

**Modified network:**
- h = σ(3x + w₁)
- y = 2h + w₂
- E = ½(y - 20)²

**Challenge:** Find dE/dw₁ for this network. What's different?

___________________________________________________________________________

___________________________________________________________________________

___________________________________________________________________________

---

## Summary

**What did you learn about:**
- How neural networks adjust their weights?
- How the chain rule connects to machine learning?
- Why calculus is essential for AI?

___________________________________________________________________________

___________________________________________________________________________

___________________________________________________________________________

**Real-World Impact:** Every time you use ChatGPT, Siri, or face recognition on your phone, the chain rule is working behind the scenes!
