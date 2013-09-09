class Stack {
    private Object stack[];
    private int capacity;

    public Stack(int capacity) {
        this.capacity = 0;
        this.stack = new Object[capacity];
    }

    public void push(Object element) {
        if (capacity == stack.length) {
            throw new IndexOutOfBoundsException("Stack overflow");
        } else {
            stack[capacity++] = element;
        }
    }

    public Object pop() {
        if (capacity == 0) {
            throw new IllegalStateException("Stack is empty");
        } else {
            return stack[--capacity];
        }
    }

    public static void main(String[] args) {
        Stack stack = new Stack(5);
        stack.push(42);
        System.out.println("Answer to The Ultimate Question of Life, the Universe, and Everything is " + stack.pop());
    }
}
