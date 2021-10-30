#!/usr/bin/env python
# coding: utf-8

# In[1]:


import copy

class Node(object):
    def __init__(self,data):
        data_temp=copy.deepcopy(data)
        self.data=copy.deepcopy(data["data"])
        del data_temp["data"]
        self.left=None
        self.right=None
        self.xdata=data_temp
        self.height=1
        
    def __str__(self):
        return "Data: {0} {1}".format(self.data, str(self.xdata))
        
class AVLTree(object):
    def __init__(self,root=None):
        self.root=root
        
    def __str__(self):
        return "Network: Root is '{0}' and Balance is '{1}'".format(self.root.data, self.get_balance(self.root))

    def insert(self, data):
        self.root=self.insert_helper(self.root, data)
        
    def insert_helper(self, root, data):
     
        # Step 1 - Perform normal insert for BST
        if not root:
            return Node(data)
        elif data["data"] < root.data:
            root.left = self.insert_helper(root.left, data)
        else:
            root.right = self.insert_helper(root.right, data)
 
        # Step 2 - Update the height of the
        # ancestor node
        root.height = 1 + max(self.get_height(root.left),
                           self.get_height(root.right))
 
        # Step 3 - Get the balance factor
        balance = self.get_balance(root)
 
        # Step 4 - If the node is unbalanced,
        # then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and data["data"] < root.left.data:
            return self.right_rotate(root)
 
        # Case 2 - Right Right
        if balance < -1 and data["data"] > root.right.data:
            return self.left_rotate(root)
 
        # Case 3 - Left Right
        if balance > 1 and data["data"] > root.left.data:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
 
        # Case 4 - Right Left
        if balance < -1 and data["data"] < root.right.data:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
 
        return root
 
    def left_rotate(self, z):
 
        y = z.right
        T2 = y.left
 
        # Perform rotation
        y.left = z
        z.right = T2
 
        # Update heights
        z.height = 1 + max(self.get_height(z.left),
                         self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),
                         self.get_height(y.right))
 
        # Return the new root
        return y
 
    def right_rotate(self, z):
 
        y = z.left
        T3 = y.right
 
        # Perform rotation
        y.right = z
        z.left = T3
 
        # Update heights
        z.height = 1 + max(self.get_height(z.left),
                        self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),
                        self.get_height(y.right))
 
        # Return the new root
        return y
 
    def get_height(self, root):
        if not root:
            return 0
 
        return root.height
 
    def get_balance(self, root):
        if not root:
            return 0
 
        return self.get_height(root.left) - self.get_height(root.right)
        
    def inorder(self):
        self.inorder_helper(self.root)
        
        
    def inorder_helper(self, root):
        if root is not None:
            self.inorder_helper(root.left)
            print(root.data)
            self.inorder_helper(root.right)
            
    def preorder(self):
        self.preorder_helper(self.root)
        
        
    def preorder_helper(self, root):
        if root is not None:
            print(root.data)
            self.preorder_helper(root.left)
            self.preorder_helper(root.right)
    
    def postorder(self):
        self.postorder_helper(self.root)
        
        
    def postorder_helper(self, root):
        if root is not None:
            self.postorder_helper(root.left)
            self.postorder_helper(root.right)
            print(root.data)
    
    
def search(root, value):
    if root is None:
        return None
        print("Empty Tree.")
    elif root.data==value:
        return root
    elif root.data>value:
        return search(root.left,value)
    elif root.data<value:
        return search(root.right,value)
    else:
        print("{0} not found in tree.".format(value))
        
def search_IPV4(root, value):
    print("Node: {0:14}   Value: {1:11}".format(root.data, value))
    if not root:
        print("Empty Tree.")
        return None
    elif ipv4_in_to_ipv4_cidr(value,root.data):
        return root
    elif ipv4_compare_to_ipv4_cidr(value,root.data)==-1:
        return search_IPV4(root.left,value)
    elif ipv4_compare_to_ipv4_cidr(value,root.data)==1:
        return search_IPV4(root.right,value)
    else:
        print("{0} not found in tree.".format(value))
        
class IPv4Network:
    def __init__(self,network):
        self.network=network
    def __str__(self):
        return "Network: {0}".format(self.network.data)

def convert_string_ip_to_int(ip):
    powers=[24,16,8,0]
    octets=ip.split(".")
    ip=0
    
    for x in range(len(octets)):
        ip+=int(octets[x])<<powers[x]
    
    return ip

def convert_string_cidr_mask_int(mask):
    return ((1<<int(mask))-1)<<(32-int(mask))

def ipv4_in_to_ipv4_cidr(ip,ipnet):
    ipnet,mask=ipnet.split("/")
    if convert_string_ip_to_int(ip)&convert_string_cidr_mask_int(mask)==convert_string_ip_to_int(ipnet):
        return True
    else:
        return False
    
def ipv4_compare_to_ipv4_cidr(ip,ipnet):
    ipnet,mask=ipnet.split("/")
    if ip<ipnet:
        return -1
    elif ip==ipnet:
        return 0
    else:
        return 1
    
def ipv4_compare_to_ipv4(ip,ip2):
    if ip<ip2:
        return -1
    elif ip==ip2:
        return 0
    else:
        return 1
    
    


# In[2]:


import math as m
import time as t

ip1="10.0.0.81"
ipnet="192.168.0.0/24"


start=t.time()
#t.sleep(0.01)
match="is" if ipv4_in_to_ipv4_cidr(ip1,ipnet) else "is not"
end=t.time()

print("{0} {1} in network({2})".format(ip1,match,ipnet))
elapsed=end-start
print("Time elapsed {0}s".format(elapsed))
print(elapsed*100000)

compare=ipv4_compare_to_ipv4_cidr(ip1, ipnet)
if compare==-1:
    compare="less than"
elif compare==0:
    compare="equals"
else:
    compare="greater than"
    
print("{0} {1} network({2})".format(ip1,compare,ipnet))

ip1=convert_string_ip_to_int(ip1)
print("IP: "+ str(ip1))
print("{0:032b}".format(ip1))

ipnet,mask=ipnet.split("/")
ipnet=convert_string_ip_to_int(ipnet)
print("IP CIDR: "+str(ipnet))
print("{0:032b}".format(ipnet))

print("IP Subnet Mask: "+mask)
mask=convert_string_cidr_mask_int(mask)
print("{0:08b}".format(mask))
print(mask)
print(m.log(mask,2))


networks=AVLTree(Node(dict({"data":"1.1.1.0/24"})))


# In[3]:


networks.insert(dict({"data":"1.0.0.0/24"}))
networks.insert(dict({"data":"8.0.0.0/9"}))
networks.insert(dict({"data":"9.9.9.0/24"}))
networks.insert(dict({"data":"205.251.192.0/18"}))
networks.insert(dict({"data":"176.32.96.0/21"}))
networks.insert(dict({"data":"54.224.0.0/11"}))

myTree=AVLTree(Node(dict({"data":10})))
myTree.insert(dict({"data":20}))
myTree.insert(dict({"data":30}))
myTree.insert(dict({"data":40}))
myTree.insert(dict({"data":50}))
myTree.insert(dict({"data":25}))


# In[4]:


print(str(networks))

networks.inorder()

print("--------")

networks.preorder()

print("--------")

networks.postorder()


# In[5]:


myTree.preorder()


# In[6]:


start=t.time()
magic=search_IPV4(networks.root, "8.8.8.8")
end=t.time()
elapsed=end-start
print("Time elapsed {0}s".format(elapsed))
print(elapsed*100000)


# In[7]:


print(str(magic))


# In[8]:


import csv
import os
import random

maxmindtree=AVLTree()
temp_list=[]

with open(r"Country-Blocks-IPv4.csv") as file:
    print("Number of rows: {0:,}".format(sum(1 for _ in file)))
    
    file.seek(0)
    
    reader=csv.DictReader(file)
    for row in reader:
        temp_list.append(row)
        
    random.shuffle(temp_list)
    
    for row in temp_list:
        maxmindtree.insert(dict({"data":row["network"],"geoname_id":row["geoname_id"],"is_anonymous_proxy":row["is_anonymous_proxy"]}))
        
    del temp_list
        
print(str(maxmindtree))
        


# In[9]:


start=t.time()
magic=search_IPV4(maxmindtree.root, "91.245.222.33")
end=t.time()
elapsed=end-start
print("Time elapsed {0}s".format(elapsed))
print(elapsed*100000)


# In[32]:


print(str(magic))


# In[ ]:




