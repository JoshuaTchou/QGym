import rclpy
from rclpy.node import Node
# from unitree_go.msg import LowState
# from unitree_api.msg import Request
# import torch, time

# from custom_controller.state_machine import State
# from learning.modules import Actor


class CustomController(Node):
    def __init__(self):
        super().__init__(
            "custom_controller", automatically_declare_parameters_from_overrides=True
        )

        # watchdog_timeout = self.get_parameter_or("watchdog_timeout_s", 0.5).value
        # self.sm = StateMachine()
        self.model = None  # figure out how to load policy
        self.last_sensor_time = None


def main():
    rclpy.init()
    custom_controller_node = CustomController()
    rclpy.spin(custom_controller_node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
