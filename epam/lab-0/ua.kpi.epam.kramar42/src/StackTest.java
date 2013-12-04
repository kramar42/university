import org.junit.Rule;
import org.junit.Test;
import org.junit.BeforeClass;
import org.junit.rules.ExpectedException;
import static org.junit.Assert.assertEquals;

public class StackTest {
    private static Stack stack;

    @Rule
    public ExpectedException exception = ExpectedException.none();

    @BeforeClass
    public static void startSetup() {
        stack = new Stack(5);
    }

    @Test
    public void testPush() {
        for (int i = 0; i < 5; i++) {
            stack.push(i);
        }
        exception.expect(IndexOutOfBoundsException.class);
        exception.expectMessage("Stack overflow");
        stack.push(0);
    }

    @Test
    public void testEquals() {
        for (int i = 4; i >= 0; i--) {
            assertEquals(i, stack.pop());
        }
    }

    @Test
    public void testPop() {
        exception.expect(IllegalStateException.class);
        exception.expectMessage("Stack is empty");
        stack.pop();
    }
}
