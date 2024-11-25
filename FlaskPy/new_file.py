from aider.coders import Coder
from aider.models import Model
from aider.io import InputOutput

class AiderRunner:
    def __init__(self, user_prompt):
        self.user_prompt = user_prompt
        self.coder = None

    def setup_coder(self) -> Coder:
        model = Model("claude-3-5-sonnet-20240620")
        io = InputOutput(yes=True, chat_history_file="templates/testing_aider.txt")
        self.coder = Coder.create(
                main_model=model,
                io=io,
                stream=False,
                use_git=False,
                edit_format="diff",
            )

        return self.coder

    def run(self):   
        coder = self.setup_coder()
        instruction = f"""Write a python script that is able to {self.user_prompt}. If using input(), first use print(prompt) and then input()."""
        result = coder.run(instruction)
        return result


def main():

    # Create an instance of AiderRunner with the custom input function
    runner = AiderRunner("Write an email to xavier@gmail.com saying Hello. When can we meet over coffee?")
    runner.run()

if __name__ == "__main__":
    main()