int dziel(int n)
{
	if (n>2)
  	{
  		int k=1,l=0;
		while (k<n)
		{
			if(n%k==0) l=k;
			k++;
		}
		return l;
  	}
}
