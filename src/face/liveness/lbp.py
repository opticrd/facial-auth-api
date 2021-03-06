from skimage import feature
import numpy as np

class LocalBinaryPatterns:
    def __init__(self, numPoints, radius):
        self.numPoints = numPoints
        self.radius = radius
    
    def _describe(self, image, eps=1e-7) -> np.ndarray:
        lbp = feature.local_binary_pattern(image, self.numPoints,
                self.radius, method="uniform")
        
        hist: np.ndarray
        
        (hist, _) = np.histogram(lbp.ravel(),
            bins=np.arange(0, self.numPoints + 3),
            range=(0, self.numPoints + 2))
        
        hist = hist.astype("float")
        hist /= (hist.sum() + eps)

        return hist

    def get_lbp_max(self, image: np.ndarray, start: int=8, end: int=18, eps: float=1e-7) -> float:
        hist = self._describe(image, eps)
        max_lbp: float = max(hist[start:end])
        return max_lbp