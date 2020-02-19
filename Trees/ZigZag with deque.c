// C++ program to print level order traversal 
// in spiral form using a single dequeue 
#include <bits/stdc++.h> 

struct Node { 
	int data; 
	struct Node *left, *right; 
}; 

// A utility function to create a new node 
struct Node* newNode(int data) 
{ 
	struct Node* node = new struct Node; 
	node->data = data; 
	node->left = node->right = NULL; 
	return (node); 
} 

// function to print the level order traversal 
void levelOrder(struct Node* root, int n) 
{ 
  if(root == NULL)
    return;
	
	std::deque<Node*> dq;
  	dq.push_front(root);
  
  	bool rightToLeft = true;
  	while(!dq.empty())
    {
      int numberOfNodesInThisLevel = dq.size();
      
      for(int i = 0;i<numberOfNodesInThisLevel;i++)
      {
        	Node* p = NULL;
        
        	if(rightToLeft)
            {
              p = dq.back();
              dq.pop_back();
              
              if(p->right)
                dq.push_front(p->right);
               if(p->left)
                dq.push_front(p->left);
            }
        	else
            {
              p = dq.front();
              dq.pop_front();
              
                if(p->left)
                dq.push_back(p->left);
                if(p->right)
                dq.push_back(p->right);

            }
        
        	printf("%d ", p->data); 
      }
      
      rightToLeft = !rightToLeft;
      printf("\n");
    }
} 

// Driver code 
int main() 
{ 
	struct Node* root = newNode(1); 
	root->left = newNode(2); 
	root->right = newNode(3); 
	root->left->left = newNode(4); 
	root->left->right = newNode(5); 
	root->right->left = newNode(6); 
	root->right->right = newNode(7); 
	levelOrder(root, 7); 

	return 0; 
} 
