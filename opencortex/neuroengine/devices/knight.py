import time
import logging
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds


class KnightBoard:
    def __init__(self, board_shim: BoardShim = None, num_channels: int = 8):
        """Initialize and configure the Knight Board."""
        self.num_channels = num_channels
        self.board_shim = board_shim


        # Initialize board
        self.board_id = self.board_shim.get_board_id()
        self.eeg_channels = self.board_shim.get_exg_channels(self.board_id)
        self.sampling_rate = self.board_shim.get_sampling_rate(self.board_id)

    def start_stream(self, buffer_size: int = 450000, streamer_params: str = None):
        """Start the data stream from the board."""
        self.board_shim.start_stream(buffer_size, streamer_params=streamer_params)
        time.sleep(2)
        for x in range(1, self.num_channels + 1):
            time.sleep(0.5)
            cmd = f"chon_{x}_12"
            self.board_shim.config_board(cmd)
            logging.info(f"sending {cmd}")
            time.sleep(1)
            rld = f"rldadd_{x}"
            self.board_shim.config_board(rld)
            logging.info(f"sending {rld}")
            time.sleep(0.5)

    def stop_stream(self):
        """Stop the data stream and release resources."""
        self.board_shim.stop_stream()

    def release_session(self):
        self.board_shim.release_session()
