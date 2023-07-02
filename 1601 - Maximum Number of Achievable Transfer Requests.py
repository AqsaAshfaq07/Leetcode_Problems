#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 1601. Maximum Number of Achievable Transfer Requests

class Solution:
    answer = 0

    def maxRequest(self, requests, indegree, n, index, count):
        if index == len(requests):
            # Check if all buildings have an in-degree of 0.
            for i in range(n):
                if indegree[i]:  # if zero -> false
                    return

            self.answer = max(self.answer, count)
            return

        indegree[requests[index][0]] -= 1
        indegree[requests[index][1]] += 1
       
        self.maxRequest(requests, indegree, n, index + 1, count + 1)
      
        indegree[requests[index][0]] += 1
        indegree[requests[index][1]] -= 1

        self.maxRequest(requests, indegree, n, index + 1, count)

    def maximumRequests(self, n, requests):
        indegree = [0] * n
        self.maxRequest(requests, indegree, n, 0, 0)

        return self.answer

