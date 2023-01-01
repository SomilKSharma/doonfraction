class doonfraction:
    
    
    def __init__(self, num, den):
        
        """Constructor to initializes the numerator and denominator.

        Args:
            num (int): The numerator of the fraction.
            den (int): The denominator of the fraction.
        """
        self.numerator = num
        self.denominator = den    
    
    
    def __str__(self):
       
        """Prints the fraction. When print() function is called.

        Returns:
            The string representation of the fraction in the form "numerator/denominator".
        """
        return f"{self.numerator}/{self.denominator}"
    
    
    def __add__(self, other):
       
        """To add two fractions.

        Args:
            The other fraction to be added

        Returns:
            Fraction: The result of the addition as a new Fraction instance.
        """
        num = self.numerator * other.denominator + self.denominator * other.numerator
        den = self.denominator * other.denominator
        
        m=min(num,den)
        
        for i in range(m,0,-1):
            
            if num%i==0 and den%i==0:
                break
       
        return doonfraction(num//i, den//i)
    
    
    def __sub__(self, other):
        
        """To substract two fractions

        Args:
            The other fraction to be substracted.

        Returns:
            Fraction: The result of the subtraction as a new Fraction instance.
        """
        num = self.numerator * other.denominator - self.denominator * other.numerator
        den = self.denominator * other.denominator
        
        return doonfraction(num, den)
    
    
    def __mul__(self, other):
        
        """To multiply two fractions.

        Args:
            The other fraction to be multiplied.

        Returns:
            Fraction: The result of the multiplication as a new Fraction instance.
        """
        num = self.numerator * other.numerator
        den = self.denominator * other.denominator
        
        return doonfraction(num, den)
    
    
    def __truediv__(self, other):
        
        """To divide two fractions.

        Args:
           The other fraction to divide the current fraction.

        Returns:
            Fraction: The result of the division as a new Fraction instance.
        """
        num = self.numerator * other.denominator
        den = self.denominator * other.numerator
        
        m=min(num,den)
        
        for i in range(m,0,-1):
            
            if num%i==0 and den%i==0:
                break
       
        return doonfraction(num//i, den//i)
        
    
    def __float__(self):
        
        """Converts the fraction to a floating point number.

        Returns:
            float: The floating point representation of the fraction.
        """
        return self.numerator / self.denominator


    def mixf(self):
        
        """Convert any fraction to a mixed fraction
        
        Returns:
        str: With the string containing the mixed fraction
        """
        return (str(self.numerator//self.denominator)+" "+str(self.numerator%self.denominator)+'/'+str(self.denominator))