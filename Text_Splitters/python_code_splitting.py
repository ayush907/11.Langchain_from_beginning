from langchain.text_splitter import RecursiveCharacterTextSplitter, Language

python_text = """
class Greeting:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return f"Hello, {self.name}!"

# Object creation
user = Greeting("Amit")

# Function call and if-else logic
message = user.say_hello()
if "Hello" in message:
    print("Greeting received!")
else:
    print("No greeting found.")
"""

java_text = """
public class Greeting {
    private String name;

    public Greeting(String name) {
        this.name = name;
    }

    public String sayHello() {
        return "Hello, " + name + "!";
    }

    public static void main(String[] args) {
        Greeting user = new Greeting("Amit");
        String message = user.sayHello();

        if (message.contains("Hello")) {
            System.out.println("Greeting received!");
        } else {
            System.out.println("No greeting found.");
        }
    }
}
"""


splitter1 = RecursiveCharacterTextSplitter.from_language(
    language = Language.PYTHON,
    chunk_size = 170,
    chunk_overlap = 0
)

result1 = splitter1.split_text(python_text)

# print(result1)

# for chunk in result1:
#     print(chunk)
#     print("-" * 30)

splitter2 = RecursiveCharacterTextSplitter.from_language(
    language = Language.JAVA,
    chunk_size = 200,
    chunk_overlap = 0
)

result2 = splitter2.split_text(java_text)

print(len(result2))

for chunk in result2:
    print(chunk)
    print('-' * 40)