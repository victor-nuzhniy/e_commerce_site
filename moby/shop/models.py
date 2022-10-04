from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


def user_directory_path_1(instance, filename):
    return 'super_category_{0}/{1}'.format(instance.name, filename)


class SuperCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('Общая категория'))
    icon = models.ImageField(upload_to=user_directory_path_1, blank=True, verbose_name=_('Иконка'))

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:super_category', kwargs={'super_category_pk': self.pk})

    class Meta:
        verbose_name = _('Общая категория')
        verbose_name_plural = _('Общие категории')


def user_directory_path_2(instance, filename):
    return 'category_{0}/{1}'.format(instance.name, filename)


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Название категории'))
    slug = models.SlugField(unique=True, verbose_name='URL')
    super_category = models.ForeignKey(SuperCategory, on_delete=models.CASCADE, blank=True, null=True)
    picture = models.ImageField(upload_to=user_directory_path_2, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:category', kwargs={'category_slug': self.slug})

    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')


class CategoryFeatures(models.Model):
    category = models.OneToOneField(Category, on_delete=models.CASCADE)
    feature_name_1 = models.CharField(max_length=100, blank=True, verbose_name='1')
    feature_name_2 = models.CharField(max_length=100, blank=True, verbose_name='2')
    feature_name_3 = models.CharField(max_length=100, blank=True, verbose_name='3')
    feature_name_4 = models.CharField(max_length=100, blank=True, verbose_name='4')
    feature_name_5 = models.CharField(max_length=100, blank=True, verbose_name='5')
    feature_name_6 = models.CharField(max_length=100, blank=True, verbose_name='6')
    feature_name_7 = models.CharField(max_length=100, blank=True, verbose_name='7')
    feature_name_8 = models.CharField(max_length=100, blank=True, verbose_name='8')
    feature_name_9 = models.CharField(max_length=100, blank=True, verbose_name='9')
    feature_name_10 = models.CharField(max_length=100, blank=True, verbose_name='10')
    feature_name_11 = models.CharField(max_length=100, blank=True, verbose_name='11')
    feature_name_12 = models.CharField(max_length=100, blank=True, verbose_name='12')
    feature_name_13 = models.CharField(max_length=100, blank=True, verbose_name='13')
    feature_name_14 = models.CharField(max_length=100, blank=True, verbose_name='14')
    feature_name_15 = models.CharField(max_length=100, blank=True, verbose_name='15')
    feature_name_16 = models.CharField(max_length=100, blank=True, verbose_name='16')
    feature_name_17 = models.CharField(max_length=100, blank=True, verbose_name='17')
    feature_name_18 = models.CharField(max_length=100, blank=True, verbose_name='18')
    feature_name_19 = models.CharField(max_length=100, blank=True, verbose_name='19')
    feature_name_20 = models.CharField(max_length=100, blank=True, verbose_name='20')
    feature_name_21 = models.CharField(max_length=100, blank=True, verbose_name='21')
    feature_name_22 = models.CharField(max_length=100, blank=True, verbose_name='22')
    feature_name_23 = models.CharField(max_length=100, blank=True, verbose_name='23')
    feature_name_24 = models.CharField(max_length=100, blank=True, verbose_name='24')
    feature_name_25 = models.CharField(max_length=100, blank=True, verbose_name='25')
    feature_name_26 = models.CharField(max_length=100, blank=True, verbose_name='26')
    feature_name_27 = models.CharField(max_length=100, blank=True, verbose_name='27')
    feature_name_28 = models.CharField(max_length=100, blank=True, verbose_name='28')
    feature_name_29 = models.CharField(max_length=100, blank=True, verbose_name='29')
    feature_name_30 = models.CharField(max_length=100, blank=True, verbose_name='30')
    feature_name_31 = models.CharField(max_length=100, blank=True, verbose_name='31')
    feature_name_32 = models.CharField(max_length=100, blank=True, verbose_name='32')
    feature_name_33 = models.CharField(max_length=100, blank=True, verbose_name='33')
    feature_name_34 = models.CharField(max_length=100, blank=True, verbose_name='34')
    feature_name_35 = models.CharField(max_length=100, blank=True, verbose_name='35')
    feature_name_36 = models.CharField(max_length=100, blank=True, verbose_name='36')
    feature_name_37 = models.CharField(max_length=100, blank=True, verbose_name='37')
    feature_name_38 = models.CharField(max_length=100, blank=True, verbose_name='38')
    feature_name_39 = models.CharField(max_length=100, blank=True, verbose_name='39')
    feature_name_40 = models.CharField(max_length=100, blank=True, verbose_name='40')

    def __str__(self):
        return 'features name'

    class Meta:
        verbose_name = _('Характеристики категории')
        verbose_name_plural = _('Характеристики категорий')


class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Наименование бренда'))
    slug = models.SlugField(unique=True, verbose_name='URL')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Бренд')
        verbose_name_plural = _('Бренды')


class Supplier(models.Model):
    name = models.CharField(max_length=150, verbose_name=_('Наименование поставщика'))
    inn = models.CharField(max_length=15, blank=True, verbose_name=_('ИНН'))
    pdv = models.CharField(max_length=15, blank=True, verbose_name=_('Номер свидетельства НДС'))
    egrpou = models.CharField(max_length=15, blank=True, verbose_name=_('ЕГРПОУ'))
    bank = models.CharField(max_length=50, blank=True, verbose_name=_('Банк'))
    mfo = models.CharField(max_length=8, blank=True, verbose_name=_('МФО'))
    checking_account = models.CharField(max_length=50, blank=True, verbose_name=_('Расчетный счет'))
    tel = models.CharField(max_length=15, verbose_name=_('Телефон'))
    email = models.EmailField(verbose_name=_('Электронный адрес'))
    person = models.CharField(max_length=20, verbose_name=_('Контактное лицо'))
    date_creation = models.DateField(auto_now_add=True, verbose_name=_('Дата внесения в базу'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Поставщик')
        verbose_name_plural = _('Поставщики')


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name=_('Наименование продукта'))
    model = models.CharField(max_length=50, verbose_name=_('Модель'))
    slug = models.SlugField(unique=True, verbose_name='URL')
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, verbose_name=_('Наименование бренда'))
    description = models.TextField(verbose_name=_('Описание'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('Категория'))
    vendor_code = models.CharField(max_length=50, verbose_name=_('Артикул'))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Цена'))
    supplier = models.ManyToManyField(Supplier, verbose_name=_('Поставщик'))
    sold = models.BooleanField(verbose_name=_('Продан'))
    notes = models.CharField(max_length=200, blank=True, verbose_name=_('Дополнительная информация'))
    last_accessed = models.DateTimeField(blank=True, null=True, verbose_name=_('Дата последнего посещения'))
    access_number = models.PositiveBigIntegerField(blank=True, null=True, verbose_name=_('Количество просмотров'))

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product', kwargs={'product_slug': self.slug})

    class Meta:
        verbose_name = _('Продукт')
        verbose_name_plural = _('Продукты')


class ProductFeature(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    feature_1 = models.CharField(max_length=100, blank=True, verbose_name='1')
    feature_2 = models.CharField(max_length=100, blank=True, verbose_name='2')
    feature_3 = models.CharField(max_length=100, blank=True, verbose_name='3')
    feature_4 = models.CharField(max_length=100, blank=True, verbose_name='4')
    feature_5 = models.CharField(max_length=100, blank=True, verbose_name='5')
    feature_6 = models.CharField(max_length=100, blank=True, verbose_name='6')
    feature_7 = models.CharField(max_length=100, blank=True, verbose_name='7')
    feature_8 = models.CharField(max_length=100, blank=True, verbose_name='8')
    feature_9 = models.CharField(max_length=100, blank=True, verbose_name='9')
    feature_10 = models.CharField(max_length=100, blank=True, verbose_name='10')
    feature_11 = models.CharField(max_length=100, blank=True, verbose_name='11')
    feature_12 = models.CharField(max_length=100, blank=True, verbose_name='12')
    feature_13 = models.CharField(max_length=100, blank=True, verbose_name='13')
    feature_14 = models.CharField(max_length=100, blank=True, verbose_name='14')
    feature_15 = models.CharField(max_length=100, blank=True, verbose_name='15')
    feature_16 = models.CharField(max_length=100, blank=True, verbose_name='16')
    feature_17 = models.CharField(max_length=100, blank=True, verbose_name='17')
    feature_18 = models.CharField(max_length=100, blank=True, verbose_name='18')
    feature_19 = models.CharField(max_length=100, blank=True, verbose_name='19')
    feature_20 = models.CharField(max_length=100, blank=True, verbose_name='20')
    feature_21 = models.CharField(max_length=100, blank=True, verbose_name='21')
    feature_22 = models.CharField(max_length=100, blank=True, verbose_name='22')
    feature_23 = models.CharField(max_length=100, blank=True, verbose_name='23')
    feature_24 = models.CharField(max_length=100, blank=True, verbose_name='24')
    feature_25 = models.CharField(max_length=100, blank=True, verbose_name='25')
    feature_26 = models.CharField(max_length=100, blank=True, verbose_name='26')
    feature_27 = models.CharField(max_length=100, blank=True, verbose_name='27')
    feature_28 = models.CharField(max_length=100, blank=True, verbose_name='28')
    feature_29 = models.CharField(max_length=100, blank=True, verbose_name='29')
    feature_30 = models.CharField(max_length=100, blank=True, verbose_name='30')
    feature_31 = models.CharField(max_length=100, blank=True, verbose_name='31')
    feature_32 = models.CharField(max_length=100, blank=True, verbose_name='32')
    feature_33 = models.CharField(max_length=100, blank=True, verbose_name='33')
    feature_34 = models.CharField(max_length=100, blank=True, verbose_name='34')
    feature_35 = models.CharField(max_length=100, blank=True, verbose_name='35')
    feature_36 = models.CharField(max_length=100, blank=True, verbose_name='36')
    feature_37 = models.CharField(max_length=100, blank=True, verbose_name='37')
    feature_38 = models.CharField(max_length=100, blank=True, verbose_name='38')
    feature_39 = models.CharField(max_length=100, blank=True, verbose_name='39')
    feature_40 = models.CharField(max_length=100, blank=True, verbose_name='40')

    def __str__(self):
        return 'features'

    class Meta:
        verbose_name = _('Характеристики продукта')
        verbose_name_plural = _('Характеристики продуктов')


def user_directory_path(instance, filename):
    return 'product _{0}/{1}'.format(instance.product.slug, filename)


class ProductImage(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    image_1 = models.ImageField(upload_to=user_directory_path, blank=True, verbose_name=_('Изображение 1'))
    image_2 = models.ImageField(upload_to=user_directory_path, blank=True, verbose_name=_('Изображение 2'))
    image_3 = models.ImageField(upload_to=user_directory_path, blank=True, verbose_name=_('Изображение 3'))
    image_4 = models.ImageField(upload_to=user_directory_path, blank=True, verbose_name=_('Изображение 4'))
    image_5 = models.ImageField(upload_to=user_directory_path, blank=True, verbose_name=_('Изображение 5'))

    def __str__(self):
        return 'Image'

    class Meta:
        verbose_name = _('Изображение товара')
        verbose_name_plural = _('Изображения товара')


class Review(models.Model):
    MARKS = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('Отзыв на продукт'))
    grade = models.PositiveSmallIntegerField(blank=True, choices=MARKS, verbose_name=_('Оценка'))
    review_text = models.CharField(max_length=255, blank=True, verbose_name=_('Текст отзыва'))
    review_date = models.DateField(auto_now_add=True, verbose_name=_('Дата создания'))
    review_author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Автор отзыва'), blank=True,
                                      null=True)
    like_num = models.SmallIntegerField(blank=True, null=True, verbose_name='Количество лайков')
    dislike_num = models.SmallIntegerField(blank=True, null=True, verbose_name='Количество дизлайков')

    def __str__(self):
        return self.product.name + '-review'

    class Meta:
        verbose_name = _('Отзыв')
        verbose_name_plural = _('Отзывы')


class Like(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, verbose_name=_('Отзыв'))
    like = models.BooleanField(verbose_name=_('Лайк'))
    dislike = models.BooleanField(verbose_name=_('Дизлайк'), blank=True, null=True)
    like_author = models.ForeignKey(User, on_delete=models.CASCADE,
                                    blank=True, null=True, verbose_name=_('Автор лайка'))

    def __str__(self):
        return 'Likes'

    class Meta:
        verbose_name = _('Лайк')
        verbose_name_plural = _('Лайки')


class Income(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL, verbose_name=_('Наименование продукта'))
    income_quantity = models.PositiveSmallIntegerField(verbose_name=_('Количество'))
    income_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Входящая цена'))
    supplier = models.ForeignKey(Supplier, null=True, on_delete=models.SET_NULL, verbose_name=_('Поставщик'))
    income_date = models.DateField(auto_now_add=True, verbose_name=_('Дата поступления'))

    def __str__(self):
        return str(self.income_date)

    class Meta:
        verbose_name = _('Приход')
        verbose_name_plural = _('Приходы')


class Buyer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE, verbose_name=_('Пользователь'))
    name = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('Имя'))
    email = models.EmailField(null=True, blank=True, verbose_name=_('Почта'))
    tel = models.CharField(max_length=15, blank=True, verbose_name=_('Телефон'))
    address = models.CharField(max_length=30, blank=True, verbose_name=_('Адресс'))

    class Meta:
        verbose_name = _('Покупатель')
        verbose_name_plural = _('Покупатели')

    def __str__(self):
        return str(self.name)


class Order(models.Model):
    buyer = models.ForeignKey(Buyer, null=True, blank=True, on_delete=models.SET_NULL, verbose_name=_('Заказ'))
    date_ordered = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата заказа'))
    complete = models.BooleanField(default=False, verbose_name=_('Выполнение заказа'))

    class Meta:
        verbose_name = _('Заказ')
        verbose_name_plural = _('Заказы')

    def __str__(self):
        return str(self.date_ordered)

    @property
    @admin.display(description=_('Общая сумма'))
    def get_order_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    @admin.display(description=_('Общее количество'))
    def get_order_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL, verbose_name=_('Товар'))
    order = models.ForeignKey(Order, null=True, blank=True, on_delete=models.SET_NULL, verbose_name=_('Заказ'))
    quantity = models.IntegerField(default=0, verbose_name=_('Количество'))
    date_added = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата добавления'))

    class Meta:
        verbose_name = _('Заказанный товар')
        verbose_name_plural = _('Заказанные товары')

    def __str__(self):
        return self.product.name

    @property
    @admin.display(description=_('Сумма заказа'))
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class Sale(models.Model):
    order = models.ForeignKey(Order, null=True, blank=True, on_delete=models.SET_NULL, verbose_name=_('Заказ'))
    sale_date = models.DateField(auto_now_add=True, verbose_name=_('Дата продажи'))
    region = models.CharField(max_length=80, blank=True, verbose_name=_('Регион'))
    city = models.CharField(max_length=80, blank=True, verbose_name=_('Город'))
    department = models.CharField(max_length=6, blank=True, verbose_name=_('Номер отделения'))

    def __str__(self):
        return str(self.sale_date)

    class Meta:
        verbose_name = _('Продажа')
        verbose_name_plural = _('Продажи')


class Stock(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE, verbose_name=_('Продукт'))
    income = models.OneToOneField(Income, null=True, blank=True, on_delete=models.CASCADE, verbose_name=_('Приход'))
    quantity = models.IntegerField(verbose_name=_('Количество'))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Цена'))
    supplier = models.ForeignKey(Supplier, null=True, blank=True, on_delete=models.CASCADE, verbose_name=_('Поставщик'))

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = _('Склад')
        verbose_name_plural = _('Склады')

    @property
    def get_price_total(self):
        total = self.quantity * self.price
        return total
