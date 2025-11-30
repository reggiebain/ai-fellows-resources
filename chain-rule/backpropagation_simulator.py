"""
Interactive Backpropagation Simulator
For AP Calculus Students Learning Neural Networks

This notebook demonstrates how the chain rule powers neural network learning
through an interactive visualization of backpropagation.
"""

import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# Set style for better-looking plots
try:
    plt.style.use('seaborn-v0_8-darkgrid')
except:
    plt.style.use('seaborn-darkgrid')

print("=" * 70)
print("BACKPROPAGATION: THE CHAIN RULE IN ACTION")
print("=" * 70)
print("\nWelcome! This notebook will show you how neural networks learn")
print("using the chain rule you already know from calculus.\n")

#%% PART 1: THE SIMPLE NETWORK FROM THE WORKSHEET
print("\n" + "=" * 70)
print("PART 1: RECONSTRUCTING YOUR WORKSHEET EXAMPLE")
print("=" * 70)

class SimpleNetwork:
    """
    A simple 2-layer network matching the worksheet:
    h = 3*x + w1
    y = 2*h + w2
    E = 0.5 * (y - target)^2
    """
    
    def __init__(self, w1=1.0, w2=3.0):
        self.w1 = w1
        self.w2 = w2
        self.history = {'w1': [w1], 'w2': [w2], 'error': []}
        
    def forward(self, x, target):
        """Forward pass through the network"""
        # Hidden layer
        self.x = x
        self.h = 3 * x + self.w1
        
        # Output layer
        self.y = 2 * self.h + self.w2
        
        # Calculate error
        self.target = target
        self.error = 0.5 * (self.y - target) ** 2
        
        return self.y, self.error
    
    def backward(self):
        """
        Backward pass: Calculate gradients using the chain rule
        This is where the magic happens!
        """
        # Gradient of error with respect to output
        dE_dy = (self.y - self.target)
        
        # Gradient for w2: dE/dw2 = dE/dy * dy/dw2
        dy_dw2 = 1  # because y = 2*h + w2
        self.dE_dw2 = dE_dy * dy_dw2
        
        # Gradient for w1: dE/dw1 = dE/dy * dy/dh * dh/dw1 (chain rule!)
        dy_dh = 2   # because y = 2*h + w2
        dh_dw1 = 1  # because h = 3*x + w1
        self.dE_dw1 = dE_dy * dy_dh * dh_dw1
        
        return self.dE_dw1, self.dE_dw2
    
    def update_weights(self, learning_rate=0.1):
        """Update weights using gradient descent"""
        self.w1 = self.w1 - learning_rate * self.dE_dw1
        self.w2 = self.w2 - learning_rate * self.dE_dw2
        
        # Store history for visualization
        self.history['w1'].append(self.w1)
        self.history['w2'].append(self.w2)
        self.history['error'].append(self.error)
    
    def train_step(self, x, target, learning_rate=0.1):
        """One complete training step"""
        self.forward(x, target)
        self.backward()
        self.update_weights(learning_rate)
        return self.error

# Create the network with worksheet values
net = SimpleNetwork(w1=1.0, w2=3.0)

# Run forward pass with worksheet values
x_input = 2
target_output = 20
y_pred, initial_error = net.forward(x_input, target_output)

print(f"\nInitial Network State (from your worksheet):")
print(f"  Input x: {x_input}")
print(f"  Target output: {target_output}")
print(f"  Current weights: w1 = {net.w1}, w2 = {net.w2}")
print(f"\nForward Pass:")
print(f"  Hidden layer: h = 3*{x_input} + {net.w1} = {net.h}")
print(f"  Output: y = 2*{net.h} + {net.w2} = {y_pred}")
print(f"  Error: E = 0.5*({y_pred} - {target_output})² = {initial_error:.2f}")

# Calculate gradients
dE_dw1, dE_dw2 = net.backward()

print(f"\nBackward Pass (Using Chain Rule):")
print(f"  dE/dw2 = (y - target) * dy/dw2 = ({y_pred} - {target_output}) * 1 = {dE_dw2:.2f}")
print(f"  dE/dw1 = (y - target) * dy/dh * dh/dw1 = ({y_pred} - {target_output}) * 2 * 1 = {dE_dw1:.2f}")

print(f"\nWeight Updates (learning_rate = 0.1):")
print(f"  w2_new = {net.w2} - 0.1*({dE_dw2:.2f}) = {net.w2 - 0.1*dE_dw2:.2f}")
print(f"  w1_new = {net.w1} - 0.1*({dE_dw1:.2f}) = {net.w1 - 0.1*dE_dw1:.2f}")

# Update weights and check new error
net.update_weights(learning_rate=0.1)
y_new, new_error = net.forward(x_input, target_output)

print(f"\nAfter One Update:")
print(f"  New weights: w1 = {net.w1:.2f}, w2 = {net.w2:.2f}")
print(f"  New output: y = {y_new:.2f}")
print(f"  New error: E = {new_error:.2f}")
print(f"  Error decreased by: {initial_error - new_error:.2f} ✓")

#%% PART 2: WATCH IT LEARN!
print("\n" + "=" * 70)
print("PART 2: WATCHING THE NETWORK LEARN")
print("=" * 70)

# Reset network
net = SimpleNetwork(w1=1.0, w2=3.0)

# Train for multiple steps
print("\nTraining for 20 steps...")
print(f"{'Step':<6} {'w1':<10} {'w2':<10} {'Output':<10} {'Error':<10}")
print("-" * 50)

for step in range(20):
    error = net.train_step(x_input, target_output, learning_rate=0.1)
    y_current, _ = net.forward(x_input, target_output)
    
    if step % 5 == 0 or step == 19:
        print(f"{step:<6} {net.w1:<10.4f} {net.w2:<10.4f} {y_current:<10.4f} {error:<10.4f}")

print(f"\n✓ Final output: {y_current:.4f} (target was {target_output})")
print(f"✓ Final error: {error:.6f}")

# Visualization
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Neural Network Learning via Backpropagation', fontsize=16, fontweight='bold')

# Plot 1: Weight evolution
ax1 = axes[0, 0]
iterations = range(len(net.history['w1']))
ax1.plot(iterations, net.history['w1'], 'b-', linewidth=2, label='w1 (hidden weight)', marker='o')
ax1.plot(iterations, net.history['w2'], 'r-', linewidth=2, label='w2 (output weight)', marker='s')
ax1.set_xlabel('Training Step', fontsize=12)
ax1.set_ylabel('Weight Value', fontsize=12)
ax1.set_title('How Weights Change During Training', fontsize=13, fontweight='bold')
ax1.legend(fontsize=11)
ax1.grid(True, alpha=0.3)

# Plot 2: Error reduction
ax2 = axes[0, 1]
ax2.plot(range(1, len(net.history['error']) + 1), net.history['error'], 'g-', linewidth=2, marker='o')
ax2.set_xlabel('Training Step', fontsize=12)
ax2.set_ylabel('Error', fontsize=12)
ax2.set_title('Error Decreases Over Time', fontsize=13, fontweight='bold')
ax2.grid(True, alpha=0.3)
ax2.set_yscale('log')  # Log scale shows improvement better

# Plot 3: Network diagram
ax3 = axes[1, 0]
ax3.axis('off')
ax3.set_xlim(0, 10)
ax3.set_ylim(0, 10)

# Draw network architecture
# Input
ax3.add_patch(plt.Circle((2, 5), 0.5, color='lightblue', ec='black', linewidth=2))
ax3.text(2, 5, 'x=2', ha='center', va='center', fontsize=11, fontweight='bold')
ax3.text(2, 3.5, 'Input', ha='center', fontsize=10)

# Hidden
ax3.add_patch(plt.Circle((5, 5), 0.5, color='lightgreen', ec='black', linewidth=2))
ax3.text(5, 5, f'h', ha='center', va='center', fontsize=11, fontweight='bold')
ax3.text(5, 3.5, 'Hidden', ha='center', fontsize=10)

# Output
ax3.add_patch(plt.Circle((8, 5), 0.5, color='lightcoral', ec='black', linewidth=2))
ax3.text(8, 5, 'y', ha='center', va='center', fontsize=11, fontweight='bold')
ax3.text(8, 3.5, 'Output', ha='center', fontsize=10)

# Arrows with weights
ax3.annotate('', xy=(4.5, 5), xytext=(2.5, 5),
            arrowprops=dict(arrowstyle='->', lw=2, color='blue'))
ax3.text(3.5, 5.5, f'w1={net.w1:.2f}', ha='center', fontsize=10, color='blue', fontweight='bold')

ax3.annotate('', xy=(7.5, 5), xytext=(5.5, 5),
            arrowprops=dict(arrowstyle='->', lw=2, color='red'))
ax3.text(6.5, 5.5, f'w2={net.w2:.2f}', ha='center', fontsize=10, color='red', fontweight='bold')

ax3.text(5, 8, 'Final Network State', ha='center', fontsize=13, fontweight='bold')
ax3.text(5, 1.5, f'Prediction: {y_current:.2f} → Target: {target_output}', 
         ha='center', fontsize=11, bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# Plot 4: The Chain Rule Visualization
ax4 = axes[1, 1]
ax4.axis('off')
ax4.set_xlim(0, 10)
ax4.set_ylim(0, 10)

ax4.text(5, 9, 'The Chain Rule in Action', ha='center', fontsize=13, fontweight='bold')

# Show the chain for w1
y_pos = 7.5
ax4.text(5, y_pos, 'Finding dE/dw1:', ha='center', fontsize=11, fontweight='bold', color='blue')
y_pos -= 1
ax4.text(5, y_pos, 'w1 → h → y → E', ha='center', fontsize=10, 
         bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
y_pos -= 0.8
ax4.text(5, y_pos, 'dE/dw1 = dE/dy × dy/dh × dh/dw1', ha='center', fontsize=10)
y_pos -= 0.6
ax4.text(5, y_pos, f'= ({y_current-target_output:.1f}) × (2) × (1) = {dE_dw1:.1f}', 
         ha='center', fontsize=9, family='monospace')

y_pos -= 1.5
# Show the chain for w2
ax4.text(5, y_pos, 'Finding dE/dw2:', ha='center', fontsize=11, fontweight='bold', color='red')
y_pos -= 1
ax4.text(5, y_pos, 'w2 → y → E', ha='center', fontsize=10,
         bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.5))
y_pos -= 0.8
ax4.text(5, y_pos, 'dE/dw2 = dE/dy × dy/dw2', ha='center', fontsize=10)
y_pos -= 0.6
ax4.text(5, y_pos, f'= ({y_current-target_output:.1f}) × (1) = {dE_dw2:.1f}', 
         ha='center', fontsize=9, family='monospace')

y_pos -= 1.2
ax4.text(5, y_pos, '✓ Longer chains need more derivatives!', ha='center', 
         fontsize=10, style='italic', color='green')

plt.tight_layout()
plt.savefig('/home/claude/backprop_training.png', dpi=150, bbox_inches='tight')
print("\n✓ Training visualization saved as 'backprop_training.png'")
plt.show()

#%% PART 3: INTERACTIVE EXPLORER
print("\n" + "=" * 70)
print("PART 3: INTERACTIVE WEIGHT EXPLORER")
print("=" * 70)
print("\nUse the interactive controls below to explore how weights affect the output and error.")

def explore_network(w1_value, w2_value, learning_rate):
    """Interactive exploration of weight effects"""
    net_explore = SimpleNetwork(w1=w1_value, w2=w2_value)
    
    # Forward pass
    y_pred, error = net_explore.forward(x_input, target_output)
    
    # Backward pass
    dE_dw1, dE_dw2 = net_explore.backward()
    
    # Create visualization
    fig, axes = plt.subplots(1, 3, figsize=(16, 4))
    
    # Plot 1: Current state
    ax1 = axes[0]
    ax1.bar(['Current\nOutput', 'Target\nOutput'], [y_pred, target_output], 
            color=['orange' if abs(y_pred - target_output) > 1 else 'green', 'blue'],
            alpha=0.7, edgecolor='black', linewidth=2)
    ax1.set_ylabel('Value', fontsize=12)
    ax1.set_title('Network Prediction vs Target', fontsize=13, fontweight='bold')
    ax1.axhline(target_output, color='blue', linestyle='--', linewidth=2, alpha=0.5)
    ax1.set_ylim(0, max(25, y_pred + 2))
    ax1.text(0, y_pred + 1, f'{y_pred:.2f}', ha='center', fontsize=11, fontweight='bold')
    ax1.text(1, target_output + 1, f'{target_output}', ha='center', fontsize=11, fontweight='bold')
    
    # Plot 2: Error surface for w2
    ax2 = axes[1]
    w2_range = np.linspace(w2_value - 5, w2_value + 5, 100)
    errors_w2 = []
    for w2_test in w2_range:
        net_test = SimpleNetwork(w1=w1_value, w2=w2_test)
        _, err = net_test.forward(x_input, target_output)
        errors_w2.append(err)
    
    ax2.plot(w2_range, errors_w2, 'r-', linewidth=2)
    ax2.plot(w2_value, error, 'ro', markersize=12, label='Current position')
    
    # Show gradient arrow
    arrow_length = -learning_rate * dE_dw2 * 10
    ax2.arrow(w2_value, error, arrow_length, 0, 
             head_width=max(errors_w2)*0.05, head_length=0.3,
             fc='green', ec='green', linewidth=2, label='Gradient direction')
    
    ax2.set_xlabel('w2 value', fontsize=12)
    ax2.set_ylabel('Error', fontsize=12)
    ax2.set_title(f'Error Landscape for w2\n(dE/dw2 = {dE_dw2:.2f})', 
                  fontsize=13, fontweight='bold')
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3)
    
    # Plot 3: Error surface for w1
    ax3 = axes[2]
    w1_range = np.linspace(w1_value - 5, w1_value + 5, 100)
    errors_w1 = []
    for w1_test in w1_range:
        net_test = SimpleNetwork(w1=w1_test, w2=w2_value)
        _, err = net_test.forward(x_input, target_output)
        errors_w1.append(err)
    
    ax3.plot(w1_range, errors_w1, 'b-', linewidth=2)
    ax3.plot(w1_value, error, 'bo', markersize=12, label='Current position')
    
    # Show gradient arrow
    arrow_length = -learning_rate * dE_dw1 * 10
    ax3.arrow(w1_value, error, arrow_length, 0,
             head_width=max(errors_w1)*0.05, head_length=0.3,
             fc='green', ec='green', linewidth=2, label='Gradient direction')
    
    ax3.set_xlabel('w1 value', fontsize=12)
    ax3.set_ylabel('Error', fontsize=12)
    ax3.set_title(f'Error Landscape for w1\n(dE/dw1 = {dE_dw1:.2f})', 
                  fontsize=13, fontweight='bold')
    ax3.legend(fontsize=10)
    ax3.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    # Print summary
    print("\n" + "="*60)
    print("CURRENT NETWORK STATE")
    print("="*60)
    print(f"Weights: w1 = {w1_value:.2f}, w2 = {w2_value:.2f}")
    print(f"Hidden layer: h = 3*{x_input} + {w1_value:.2f} = {net_explore.h:.2f}")
    print(f"Output: y = 2*{net_explore.h:.2f} + {w2_value:.2f} = {y_pred:.2f}")
    print(f"Target: {target_output}")
    print(f"Error: {error:.4f}")
    print(f"\nGradients (Chain Rule):")
    print(f"  dE/dw1 = {dE_dw1:.4f} ({'decrease w1' if dE_dw1 > 0 else 'increase w1'} to reduce error)")
    print(f"  dE/dw2 = {dE_dw2:.4f} ({'decrease w2' if dE_dw2 > 0 else 'increase w2'} to reduce error)")
    print(f"\nWith learning_rate = {learning_rate}:")
    print(f"  Next w1 = {w1_value:.2f} - {learning_rate}*{dE_dw1:.2f} = {w1_value - learning_rate*dE_dw1:.2f}")
    print(f"  Next w2 = {w2_value:.2f} - {learning_rate}*{dE_dw2:.2f} = {w2_value - learning_rate*dE_dw2:.2f}")

# Create visualization with default values
print("\nGenerating interactive exploration visualization...")
explore_network(1.0, 3.0, 0.1)

#%% PART 4: NONLINEAR ACTIVATION (EXTENSION)
print("\n" + "=" * 70)
print("PART 4: EXTENSION - NONLINEAR ACTIVATION FUNCTION")
print("=" * 70)

class NonlinearNetwork:
    """
    Network with sigmoid activation:
    h = sigmoid(3*x + w1)
    y = 2*h + w2
    """
    
    def __init__(self, w1=1.0, w2=3.0):
        self.w1 = w1
        self.w2 = w2
        self.history = {'w1': [w1], 'w2': [w2], 'error': []}
    
    @staticmethod
    def sigmoid(z):
        """Sigmoid activation function"""
        return 1 / (1 + np.exp(-z))
    
    @staticmethod
    def sigmoid_derivative(z):
        """Derivative of sigmoid: σ'(z) = σ(z) * (1 - σ(z))"""
        s = NonlinearNetwork.sigmoid(z)
        return s * (1 - s)
    
    def forward(self, x, target):
        """Forward pass with nonlinear activation"""
        self.x = x
        self.z = 3 * x + self.w1  # Pre-activation
        self.h = self.sigmoid(self.z)  # Activation
        self.y = 2 * self.h + self.w2
        self.target = target
        self.error = 0.5 * (self.y - target) ** 2
        return self.y, self.error
    
    def backward(self):
        """Backward pass with chain rule through sigmoid"""
        # dE/dy
        dE_dy = (self.y - self.target)
        
        # dE/dw2 = dE/dy * dy/dw2
        dy_dw2 = 1
        self.dE_dw2 = dE_dy * dy_dw2
        
        # dE/dw1 = dE/dy * dy/dh * dh/dz * dz/dw1
        # This is longer because of the sigmoid!
        dy_dh = 2
        dh_dz = self.sigmoid_derivative(self.z)  # Key difference!
        dz_dw1 = 1
        self.dE_dw1 = dE_dy * dy_dh * dh_dz * dz_dw1
        
        return self.dE_dw1, self.dE_dw2
    
    def update_weights(self, learning_rate=0.1):
        """Update weights"""
        self.w1 = self.w1 - learning_rate * self.dE_dw1
        self.w2 = self.w2 - learning_rate * self.dE_dw2
        self.history['w1'].append(self.w1)
        self.history['w2'].append(self.w2)
        self.history['error'].append(self.error)
    
    def train_step(self, x, target, learning_rate=0.1):
        """One training step"""
        self.forward(x, target)
        self.backward()
        self.update_weights(learning_rate)
        return self.error

print("\nNow with sigmoid activation: h = σ(3x + w1)")
print("The chain rule gets one more link!")
print("\nCompare linear vs nonlinear networks:")

# Train both networks
net_linear = SimpleNetwork(w1=1.0, w2=3.0)
net_nonlinear = NonlinearNetwork(w1=1.0, w2=3.0)

for _ in range(30):
    net_linear.train_step(x_input, target_output, learning_rate=0.5)
    net_nonlinear.train_step(x_input, target_output, learning_rate=0.5)

# Visualize comparison
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
fig.suptitle('Linear vs Nonlinear Activation Functions', fontsize=16, fontweight='bold')

# Error comparison
ax1 = axes[0]
iterations = range(len(net_linear.history['error']))
ax1.plot(iterations, net_linear.history['error'], 'b-', linewidth=2, 
         label='Linear Network', marker='o', markersize=4)
ax1.plot(iterations, net_nonlinear.history['error'], 'r-', linewidth=2,
         label='Nonlinear Network (Sigmoid)', marker='s', markersize=4)
ax1.set_xlabel('Training Step', fontsize=12)
ax1.set_ylabel('Error', fontsize=12)
ax1.set_title('Learning Curves Comparison', fontsize=13, fontweight='bold')
ax1.legend(fontsize=11)
ax1.grid(True, alpha=0.3)
ax1.set_yscale('log')

# Chain rule visualization
ax2 = axes[1]
ax2.axis('off')
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)

ax2.text(5, 9, 'Chain Rule Comparison', ha='center', fontsize=13, fontweight='bold')

# Linear
y_pos = 7.5
ax2.text(5, y_pos, 'Linear Network:', ha='center', fontsize=11, fontweight='bold', color='blue')
y_pos -= 0.8
ax2.text(5, y_pos, 'dE/dw1 = dE/dy × dy/dh × dh/dw1', ha='center', fontsize=9,
         bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
y_pos -= 0.6
ax2.text(5, y_pos, '(3 terms in chain)', ha='center', fontsize=9, style='italic')

y_pos -= 1.5
# Nonlinear
ax2.text(5, y_pos, 'Nonlinear Network:', ha='center', fontsize=11, fontweight='bold', color='red')
y_pos -= 0.8
ax2.text(5, y_pos, 'dE/dw1 = dE/dy × dy/dh × dh/dz × dz/dw1', ha='center', fontsize=9,
         bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.5))
y_pos -= 0.6
ax2.text(5, y_pos, '(4 terms in chain - includes sigmoid derivative!)', 
         ha='center', fontsize=9, style='italic')

y_pos -= 1.5
ax2.text(5, y_pos, 'Key Insight:', ha='center', fontsize=11, fontweight='bold', color='green')
y_pos -= 0.7
ax2.text(5, y_pos, 'More layers = longer chains', ha='center', fontsize=10)
y_pos -= 0.6
ax2.text(5, y_pos, 'But the chain rule still works!', ha='center', fontsize=10)
y_pos -= 0.9
ax2.text(5, y_pos, 'GPT-4 has ~100 layers ≈ 100 terms in the chain', 
         ha='center', fontsize=9, style='italic', color='purple')

plt.tight_layout()
plt.savefig('/home/claude/backprop_nonlinear.png', dpi=150, bbox_inches='tight')
print("\n✓ Nonlinear comparison saved as 'backprop_nonlinear.png'")
plt.show()

#%% PART 5: REAL DATA EXAMPLE
print("\n" + "=" * 70)
print("PART 5: LEARNING FROM REAL DATA")
print("=" * 70)

print("\nNow let's see the network learn from multiple data points!")
print("This is closer to how real neural networks train.\n")

# Generate some simple data: y = 2x + 3 + noise
np.random.seed(42)
x_data = np.linspace(0, 10, 20)
y_data = 2 * x_data + 3 + np.random.normal(0, 1, 20)

print(f"Dataset: 20 points where y ≈ 2x + 3")
print(f"The network will try to learn this relationship!\n")

# Simple network for regression: y = w*x + b
class RegressionNetwork:
    """Simple linear regression network"""
    
    def __init__(self):
        self.w = np.random.randn()
        self.b = np.random.randn()
        self.history = {'w': [self.w], 'b': [self.b], 'loss': []}
    
    def forward(self, x):
        """Forward pass"""
        return self.w * x + self.b
    
    def loss(self, x_batch, y_batch):
        """Mean squared error"""
        predictions = self.forward(x_batch)
        return np.mean((predictions - y_batch) ** 2)
    
    def train_step(self, x_batch, y_batch, learning_rate=0.01):
        """Training step with batch gradient descent"""
        # Forward pass
        predictions = self.forward(x_batch)
        errors = predictions - y_batch
        
        # Backward pass (chain rule!)
        # dL/dw = dL/dy * dy/dw = mean(errors * x)
        # dL/db = dL/dy * dy/db = mean(errors * 1)
        dL_dw = np.mean(errors * x_batch)
        dL_db = np.mean(errors)
        
        # Update
        self.w -= learning_rate * dL_dw
        self.b -= learning_rate * dL_db
        
        # Record
        self.history['w'].append(self.w)
        self.history['b'].append(self.b)
        current_loss = self.loss(x_batch, y_batch)
        self.history['loss'].append(current_loss)
        
        return current_loss

# Train the network
reg_net = RegressionNetwork()
print(f"Initial parameters: w = {reg_net.w:.4f}, b = {reg_net.b:.4f}")

epochs = 100
for epoch in range(epochs):
    loss = reg_net.train_step(x_data, y_data, learning_rate=0.01)
    if epoch % 20 == 0:
        print(f"Epoch {epoch:3d}: w = {reg_net.w:.4f}, b = {reg_net.b:.4f}, Loss = {loss:.4f}")

print(f"\nFinal parameters: w = {reg_net.w:.4f}, b = {reg_net.b:.4f}")
print(f"True relationship: y = 2.0x + 3.0")
print(f"Learned relationship: y = {reg_net.w:.2f}x + {reg_net.b:.2f}")
print(f"\n✓ The network learned the pattern from data!")

# Visualization
fig, axes = plt.subplots(1, 3, figsize=(16, 5))
fig.suptitle('Learning from Real Data', fontsize=16, fontweight='bold')

# Data and fit
ax1 = axes[0]
ax1.scatter(x_data, y_data, color='blue', s=50, alpha=0.6, label='Training data', edgecolors='black')
x_line = np.linspace(0, 10, 100)
y_pred = reg_net.forward(x_line)
ax1.plot(x_line, y_pred, 'r-', linewidth=2, label=f'Learned: y={reg_net.w:.2f}x+{reg_net.b:.2f}')
ax1.plot(x_line, 2*x_line + 3, 'g--', linewidth=2, label='True: y=2x+3')
ax1.set_xlabel('x', fontsize=12)
ax1.set_ylabel('y', fontsize=12)
ax1.set_title('Network Learned the Pattern!', fontsize=13, fontweight='bold')
ax1.legend(fontsize=10)
ax1.grid(True, alpha=0.3)

# Loss curve
ax2 = axes[1]
ax2.plot(range(len(reg_net.history['loss'])), reg_net.history['loss'], 'g-', linewidth=2)
ax2.set_xlabel('Training Step', fontsize=12)
ax2.set_ylabel('Loss (MSE)', fontsize=12)
ax2.set_title('Loss Decreases via Backpropagation', fontsize=13, fontweight='bold')
ax2.grid(True, alpha=0.3)
ax2.set_yscale('log')

# Parameter evolution
ax3 = axes[2]
iterations = range(len(reg_net.history['w']))
ax3.plot(iterations, reg_net.history['w'], 'b-', linewidth=2, label='Weight (w)', marker='o', markersize=3)
ax3.axhline(2.0, color='blue', linestyle='--', alpha=0.5, linewidth=2, label='True w=2.0')
ax3.plot(iterations, reg_net.history['b'], 'r-', linewidth=2, label='Bias (b)', marker='s', markersize=3)
ax3.axhline(3.0, color='red', linestyle='--', alpha=0.5, linewidth=2, label='True b=3.0')
ax3.set_xlabel('Training Step', fontsize=12)
ax3.set_ylabel('Parameter Value', fontsize=12)
ax3.set_title('Parameters Converge to True Values', fontsize=13, fontweight='bold')
ax3.legend(fontsize=10)
ax3.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('/home/claude/backprop_real_data.png', dpi=150, bbox_inches='tight')
print("\n✓ Real data visualization saved as 'backprop_real_data.png'")
plt.show()

#%% FINAL SUMMARY
print("\n" + "=" * 70)
print("SUMMARY: THE CHAIN RULE POWERS ALL OF AI")
print("=" * 70)

print("""
What You've Discovered:

1. BACKPROPAGATION = CHAIN RULE
   - Neural networks learn by adjusting weights to reduce error
   - The chain rule tells us exactly how to adjust each weight
   - Longer networks = longer chains, but same principle

2. THE GRADIENT TELLS US THE DIRECTION
   - dE/dw tells us which direction decreases error
   - Gradient descent: new_weight = old_weight - learning_rate × gradient
   - The network follows these gradients to improve

3. IT SCALES TO MASSIVE NETWORKS
   - Simple network: 2 weights, 3-4 derivatives in chain
   - GPT-4: ~1.8 trillion weights, ~100-layer chains
   - Same math, just repeated billions of times!

4. YOUR CALCULUS HOMEWORK MATTERS
   - Every chain rule problem you solve builds intuition for AI
   - Modern AI wouldn't exist without backpropagation
   - Backpropagation wouldn't exist without the chain rule

The next time you're computing d/dx[f(g(x))], remember:
You're practicing the exact mathematical operation that teaches AI systems
to recognize faces, generate text, drive cars, and solve complex problems.

The chain rule isn't just abstract math—it's the engine of artificial intelligence.
""")

print("=" * 70)
print("END OF INTERACTIVE SIMULATION")
print("=" * 70)
print("\nGenerated visualizations:")
print("  1. backprop_training.png - Complete training visualization")
print("  2. backprop_nonlinear.png - Linear vs nonlinear comparison")
print("  3. backprop_real_data.png - Learning from real data")
print("\nTry modifying the code to:")
print("  - Change the learning rate and see how training speed changes")
print("  - Add more layers to the network")
print("  - Try different activation functions")
print("  - Use your own data!")
