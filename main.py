from manim import *

class DefaultTemplate(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.flip(RIGHT)  # flip horizontally
        square.rotate(-3 * TAU / 8)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen

# lets create a flow chart
class FlowChartExample(Scene):
    def construct(self):
        # Create boxes with smaller dimensions
        start = Rectangle(height=0.4, width=1)
        process1 = Rectangle(height=0.4, width=1)
        process2 = Rectangle(height=0.4, width=1)
        decision = RegularPolygon(n=4, color=WHITE)
        decision.scale(1)
        end = Rectangle(height=0.4, width=1)

        # Add text to boxes
        start_text = Text("Start", font_size=20)
        process1_text = Text("Process 1", font_size=20)
        process2_text = Text("Process 2", font_size=20)
        decision_text = Text("Decision", font_size=20)
        end_text = Text("End", font_size=20)

        # Position the boxes with more space between them
        start.next_to(ORIGIN, LEFT * 4)  # Start more to the left
        process1.next_to(start, RIGHT * 1.5)  # Add more space between boxes
        process2.next_to(process1, RIGHT * 1.5)
        decision.next_to(process2, RIGHT * 1.5)
        end.next_to(decision, RIGHT * 1.5)

        # Add text to boxes
        start_text.move_to(start.get_center())
        process1_text.move_to(process1.get_center())
        process2_text.move_to(process2.get_center())
        decision_text.move_to(decision.get_center())
        end_text.move_to(end.get_center())

        # Create horizontal arrows
        arrow1 = Arrow(start.get_right(), process1.get_left())
        arrow2 = Arrow(process1.get_right(), process2.get_left())
        arrow3 = Arrow(process2.get_right(), decision.get_left())
        arrow4 = Arrow(decision.get_right(), end.get_left())

        # Create the static flowchart
        flowchart = VGroup(start, process1, process2, decision, end,
                          start_text, process1_text, process2_text, decision_text, end_text,
                          arrow1, arrow2, arrow3, arrow4)
        
        # Scale the entire flowchart to fit the screen
        flowchart.scale(0.8)  # Make everything 80% of original size
        
        # Add the flowchart to the scene
        self.add(flowchart)
        
        # Example animations
        self.play(
            start.animate.set_fill(BLUE, opacity=0.3),
            run_time=1
        )
        self.wait(1)
        
        self.play(
            process1.animate.set_fill(GREEN, opacity=0.3),
            run_time=1
        )
        self.wait(1)
        
        self.play(
            process2.animate.set_fill(GREEN, opacity=0.3),
            run_time=1
        )
        self.wait(1)
        
        self.play(
            decision.animate.set_fill(YELLOW, opacity=0.3),
            run_time=1
        )
        self.wait(1)
        
        self.play(
            end.animate.set_fill(RED, opacity=0.3),
            run_time=1
        )
        self.wait(1)

class GraphFlowChart(Scene):
    def construct(self):
        # Create a graph
        vertices = ["A", "B", "C", "D"]
        edges = [("A", "B"), ("B", "C"), ("C", "D")]
        
        graph = Graph(
            vertices,
            edges,
            layout="tree",
            vertex_config={"color": BLUE},
            edge_config={"color": WHITE}
        )
        
        self.add(graph)

