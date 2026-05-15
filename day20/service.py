import pandas as pd
import httpx            # HTTP 통신

# 6. 서비스: 비즈니스 로직
class ProductService:
    # 생성자
    def __init__(self):
        self.df = pd.DataFrame([
            {'id':1, 'name':'콜라','price':1000},
            {'id':2, 'name':'사이다','price':1500}
        ])

    # 7. 서비스 함수
    def products(self):
        return self.df.to_dict( orient = 'records' )
    
    # 8. 외부 서버(API나 Spring)와 통신하기
    # httpx.AsyncClient vs. axios
    async def getSpring( self ):
        async with httpx.AsyncClient() as client:
            # 통신할 스프링 주소
            response = await client.get("http://localhost:8080/api/product")
            print( response )
            return response.json()

# 서비스 객체 생성
productService = ProductService()