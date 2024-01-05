from sqlalchemy import BigInteger, ForeignKey, select,delete
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy.orm import relationship, Mapped, mapped_column, DeclarativeBase

engine = create_async_engine('sqlite+aiosqlite:///example.db', echo=True)

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    user_id: Mapped[int] = mapped_column()
    purchases = relationship("Purchase", back_populates="user")


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    products = relationship("Product", back_populates="category")


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    price: Mapped[int] = mapped_column()
    category_id: Mapped[str] = mapped_column(ForeignKey("categories.id"))
    category = relationship("Category", back_populates="products")
    purchases = relationship("Purchase", back_populates="product")


class Color(Base):
    __tablename__ = "color"

    id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[str] = mapped_column(ForeignKey("products.id"))
    name: Mapped[str] = mapped_column()
    link: Mapped[str] = mapped_column()
    purchases = relationship("Purchase", back_populates="color")


class Purchase(Base):
    __tablename__ = "purchases"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    product_id: Mapped[str] = mapped_column(ForeignKey("products.id"))
    color_id: Mapped[str] = mapped_column(ForeignKey("color.id"))
    memory_id: Mapped[str] = mapped_column(ForeignKey("memory.id"))
    city: Mapped[str] = mapped_column()
    adress: Mapped[str] = mapped_column()
    index_city: Mapped[int] = mapped_column()
    email: Mapped[str] = mapped_column()
    tp_number: Mapped[int] = mapped_column()

    user = relationship("User", back_populates="purchases")
    product = relationship("Product", back_populates="purchases")
    color = relationship("Color", back_populates="purchases")
    memory = relationship("Memory", back_populates="purchases")


class Memory(Base):
    __tablename__ = "memory"

    id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[str] = mapped_column(ForeignKey("products.id"))
    memory: Mapped[str] = mapped_column()
    purchases = relationship("Purchase", back_populates="memory")
    price: Mapped[int] = mapped_column()




async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


# from .models import User, Category,Product,async_session

async def add_category(value):
    async with async_session() as session:
        new_categor = Category(name=value)
        session.add(new_categor)
        await session.commit()

async def add_product2(name,price,description,category_id):
    async with async_session() as session:
        new_product = Product(
            name=name,
            price = price,
            description=description,
            category_id=category_id
        )
        session.add(new_product)
        await session.commit()


async def delete_category(value):
    async with async_session() as session:
  
        await session.execute(delete(Category).where(Category.name == value))
        await session.commit()


        


async def delete_product(value):
    async with async_session() as session:
  
        await session.execute(delete(Color).where(Color.product_id == value))
        await session.execute(delete(Memory).where(Memory.product_id == value))
        await session.execute(delete(Product).where(Product.id == value))
        await session.commit()

async def add_memory(memory,price,product_id):
    async with async_session() as session:
        new_memory = Memory(
            product_id = product_id,
            price = price,
            memory = memory
        )
        session.add(new_memory)
        await session.commit()


async def add_user_and_purchases(user_id, product_id, color_id,memory_id,adress,city,index_city,phone_number,email):
    async with async_session() as session:
        new_user = User(user_id=user_id)
        session.add(new_user)
        await session.commit()

        new_purchase = Purchase(
            user_id=user_id,
            product_id=product_id,
            color_id=color_id,
            memory_id=memory_id,
            tp_number=phone_number,
            email=email,
            adress = adress,
            city = city,
            index_city = index_city,
     
        )
        session.add(new_purchase)
        await session.commit()



async def add_color_and_link(color,link,product_id):
    async with async_session() as session:
        new_data_color = Color(name= color,link=link,product_id=product_id)
        session.add(new_data_color)
        await session.commit()



async def get_categories():
    async with async_session() as session:
        result = await session.scalars(select(Category))
        return result 
    

async def get_idcategory(category_name):
    async with async_session() as session:
        result = await session.scalar(select(Category).where(Category.name == category_name))
        return result 
    
async def get_namecategory(category_id):
    async with async_session() as session:
        result = await session.scalar(select(Category).where(Category.id == category_id))
        return result 

async def get_models(category_id):
    async with async_session() as session:
        result = await session.scalars(select(Product).where(Product.category_id== category_id))
        return result 
    

async def get_name_product(name_product):
    async with async_session() as session:
        result = await session.scalar(select(Product).where(Product.name== name_product))
        return result


async def get_description(desc_id):
    async with async_session() as session:
        result = await session.scalar(select(Product).where(Product.id== desc_id))
        return result 
    
async def get_color_id(color_id):
    async with async_session() as session:
        result = await session.scalar(select(Color).where(Color.id== color_id))
        return result
    


async def get_color_link(color_id):
    async with async_session() as session:
        result = await session.scalar(select(Color.link).where(Color.id== color_id))
        return result

async def get_memory_id(memory_id):
    async with async_session() as session:
        result = await session.scalar(select(Memory).where(Memory.id== memory_id))
        return result



async def get_color_id(color_id):
    async with async_session() as session:
        result = await session.scalar(select(Color).where(Color.id== color_id))
        return result
    

async def get_colors(product_id):
    async with async_session() as session:
        result = await session.scalars(select(Color).where(Color.product_id == product_id))
        return result

async def get_memory(product_id):
    async with async_session() as session:
        result = await session.scalars(select(Memory).where(Memory.product_id == product_id))
        return result



