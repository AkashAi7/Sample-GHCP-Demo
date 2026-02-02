# 🟡 Intermediate Challenge 3: Performance Optimization

**Difficulty**: Intermediate  
**Time Estimate**: 60 minutes  
**Skills Practiced**: Profiling, optimization, `@workspace`, code analysis

---

## 🎯 Challenge Overview

The Smart Home Energy Monitor is slow when processing large datasets (100,000+ readings). Your mission: profile the code, identify bottlenecks, and optimize performance by **10x or more**.

## 📋 Requirements

### Task 1: Generate Performance Test Data (10 min)
Create a script to generate large datasets:
- 1,000 devices
- 100,000 readings
- Multiple CSV files

**Ask Copilot**: "Create a script to generate 100,000 sample energy readings across 1,000 devices"

### Task 2: Baseline Performance Measurement (10 min)
1. Install profiling tools: `pip install cProfile memory_profiler line_profiler`
2. Create `benchmark.py` to measure:
   - CSV loading time
   - Analytics calculation time
   - Memory usage
   - Total processing time
3. Run baseline and document results

### Task 3: Identify Bottlenecks (10 min)
Use profiling to find slow code:
```python
python -m cProfile -o profile.stats benchmark.py
python -m pstats profile.stats
```

**Ask Copilot**: "Analyze this profiling output and identify the top 5 bottlenecks"

### Task 4: Optimize Code (25 min)

#### Optimization 1: Vectorize Calculations
Replace loops with NumPy/Pandas operations:
- Install: `pip install numpy pandas`
- Convert calculations to vectorized operations
- Use DataFrame operations instead of row-by-row processing

#### Optimization 2: Efficient Data Structures
- Use generators instead of lists where possible
- Implement lazy loading for CSV files
- Use `defaultdict` and `Counter` from collections

#### Optimization 3: Caching
- Cache efficiency calculations with `@lru_cache`
- Memoize expensive operations
- Consider using `functools.cache` (Python 3.9+)

#### Optimization 4: Parallel Processing
- Use `multiprocessing` for CPU-bound tasks
- Process multiple devices in parallel
- Use `concurrent.futures.ProcessPoolExecutor`

#### Optimization 5: Algorithm Improvements
- Optimize the efficiency score calculation
- Reduce redundant calculations
- Use better data structures (sets vs lists for lookups)

### Task 5: Measure Improvements (5 min)
1. Re-run benchmarks
2. Document performance improvements
3. Create comparison charts

---

## ✅ Success Criteria

- [ ] Achieved 10x+ performance improvement
- [ ] Memory usage reduced or stable
- [ ] All optimizations documented
- [ ] No functionality broken
- [ ] Created `PERFORMANCE.md` report with before/after metrics

---

## 💡 Copilot Tips

- **Generate test data**: "Create a function to generate 100K random readings"
- **Optimize function**: Highlight slow function + "Optimize this for performance"
- **Vectorize**: "Convert this loop to use NumPy vectorization"
- **Parallelize**: "Refactor this to use multiprocessing"
- **Cache**: "Add caching to this expensive calculation"

---

## 🏆 Bonus Challenges

1. **Database Indexing**: If using a database, add proper indexes
2. **Batch Processing**: Process data in chunks instead of all at once
3. **Compiled Extensions**: Use Cython or Numba for hot paths
4. **Async I/O**: Use async/await for I/O operations
5. **Profiling Dashboard**: Create a visualization of profiling results
6. **Load Testing**: Create load tests to validate improvements

---

## 🔍 Evaluation Rubric

| Criteria | Points |
|----------|--------|
| Performance improvement (10x+) | 40 |
| Multiple optimization techniques used | 30 |
| No broken functionality | 15 |
| Documentation and analysis | 10 |
| Bonus optimizations | 5 |
| **Total** | **100** |

---

## 📚 Related Exercises

This challenge builds on skills from:
- [Exercise 04: Refactoring](../../exercises/04_refactoring_and_modernization.py)
- [Exercise 06: Terminal](../../exercises/06_terminal_and_cli.py)

---

## 🧪 Example: Optimization

**Before (Slow)**:
```python
def calculate_total_consumption(readings: List[Reading]) -> float:
    total = 0.0
    for reading in readings:
        total += reading.value
    return total

def calculate_average_per_device(readings: List[Reading]) -> Dict[str, float]:
    device_sums = {}
    device_counts = {}
    for reading in readings:
        if reading.device_id not in device_sums:
            device_sums[reading.device_id] = 0
            device_counts[reading.device_id] = 0
        device_sums[reading.device_id] += reading.value
        device_counts[reading.device_id] += 1
    
    return {
        device_id: device_sums[device_id] / device_counts[device_id]
        for device_id in device_sums
    }
```

**After (Fast)**:
```python
import pandas as pd
from functools import lru_cache

@lru_cache(maxsize=128)
def calculate_total_consumption(readings_tuple: tuple) -> float:
    """Vectorized calculation with caching."""
    df = pd.DataFrame([r.__dict__ for r in readings_tuple])
    return df['value'].sum()

def calculate_average_per_device(readings: List[Reading]) -> Dict[str, float]:
    """Vectorized groupby operation."""
    df = pd.DataFrame([r.__dict__ for r in readings])
    return df.groupby('device_id')['value'].mean().to_dict()
```

---

## 📝 PERFORMANCE.md Template

```markdown
# Performance Optimization Report

## Baseline Performance
- Dataset: 100,000 readings, 1,000 devices
- CSV Loading: 45.2 seconds
- Analytics Calculation: 123.7 seconds
- Total Time: 168.9 seconds
- Memory Usage: 2.3 GB

## Optimizations Applied

### 1. Vectorization with Pandas
- Replaced loops with DataFrame operations
- Impact: 15x faster calculations

### 2. Caching with LRU
- Cached efficiency score calculations
- Impact: 80% cache hit rate, 5x speedup on repeated queries

### 3. Parallel Processing
- Process devices in parallel using multiprocessing
- Impact: 4x speedup on 8-core machine

### 4. Generator-based CSV Reading
- Use lazy loading instead of loading all data
- Impact: 60% memory reduction

## Final Performance
- CSV Loading: 5.3 seconds ⚡ **8.5x faster**
- Analytics Calculation: 8.2 seconds ⚡ **15x faster**
- Total Time: 13.5 seconds ⚡ **12.5x faster**
- Memory Usage: 0.9 GB ⚡ **61% reduction**

## Code Changes
- Modified files: analytics.py, data_ingestion.py
- Lines changed: 247 additions, 156 deletions
- New dependencies: pandas, numpy

## Profiling Evidence
[Include screenshots or profiling output]

## Recommendations
- Consider moving to a database for datasets > 1M readings
- Implement incremental processing for real-time data
- Add monitoring for production performance tracking
```

---

**Good luck optimizing! Make it fast! ⚡🚀**
