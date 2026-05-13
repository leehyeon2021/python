
import pandas as pd


# 서비스 클래스
class ItemService:
    # 생성자
    def __init__(self):
        self.df = pd.DataFrame([
            { 'id': 1 , 'name': '콜라' , 'price':1500 },
            { 'id': 2 , 'name': '사이다' , 'price':1000 }
        ])

    # 함수
    # 1. 개별 조회 서비스
    def item( self , id ):
        result = self.df[ self.df['id'] == id ]  # 출력호출용df[ 조건식용df['특정열']==값 ]
        if result.empty:    # `.empty`: 비어있으면
            return '해당 상품이 없습니다.'
        # df타입 대신에 `.to_dict()`: df조회 결과는 항상 리스트형식이다.(pandas)
        print(result)
        return result.to_dict( orient= 'records' )[0]
    
    # 2. 전체 조회 서비스
    def items( self ):
        return self.df.to_dict( orient='records' )
    
    # 3. 저장 서비스
    def save( self , item ):
        # 1) 저장할 객체를 데이터프레임으로 만든다.
        saveDf = pd.DataFrame( [item] )
        print( saveDf )
        # 2) 기존 데이터프레임에 연결한다.
        self.df = pd.concat( [self.df , saveDf] , ignore_index=True )
        return True
    
    # 4. 수정 서비스
    def update( self , item ):
        # 1) 수정할 id가 존재 여부 확인
        update_id = item.get( 'id' )
        if update_id not in self.df['id'].values:
            return '수정할 상품이 없습니다.'
        # 2) 해당 수정할 id에 index찾기
        idx = self.df[self.df['id'] == update_id].index
        # 3) 찾은 index에 값 수정
        self.df.loc[ idx , item.keys() ] = item.values()
        # 4) 
        return True
    
    # 5. 삭제 서비스
    def delete( self , id ):
        # 1) 삭제할 id 존재 여부 확인
        if id not in self.df['id'].values:
            return '삭제할 상품이 없습니다.'
        # 2) 삭제할 아이디를 제외한 df 재구성
        self.df = self.df[ self.df['id'] != id ]
        # 3) 
        return True
       
    
# ⭐ **서비스 객체 생성**: 위 ItemService() 서비스 클래스를 객체로 생성
item_service = ItemService()