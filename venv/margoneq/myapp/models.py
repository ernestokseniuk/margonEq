from django.db import models
from django.contrib.auth.models import User

class itemClass(models.Model):
    typ = models.CharField(max_length=32)
    def __str__(self):
        return self.typ
class itemLvl(models.Model):
    typ = models.CharField(max_length=32)
    color = models.CharField(max_length=7)
    def __str__(self):
        return self.typ
class legendaryBonus(models.Model):
    bonusName = models.CharField(max_length=32)
    bonusescription = models.CharField(max_length=255)
    def __str__(self):
        return self.bonusName
class verifyCodes(models.Model):
    code = models.CharField(max_length=32)
    inUse = models.BooleanField()
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    mprofile = models.URLField(max_length=256, unique=True)
    verifCode = models.ForeignKey(verifyCodes,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

class customItem(models.Model):
    itemname = models.CharField(max_length=64)
    typ = models.ForeignKey(itemClass,on_delete=models.CASCADE)
    lvl = models.IntegerField(null=True)
    klasa = models.ForeignKey(itemLvl,on_delete=models.CASCADE)
    bonus = models.ForeignKey(legendaryBonus,on_delete=models.CASCADE, null=True, blank=True)
    img = models.URLField(max_length=255)

    atakfizmin = models.IntegerField(blank=True, null=True)
    atakFizMax = models.IntegerField(blank=True, null=True)
    atakOg = models.IntegerField(blank=True, null=True)
    atakZim = models.IntegerField(blank=True, null=True)
    atakBlysk = models.IntegerField(blank=True, null=True)
    grsil = models.IntegerField(blank=True, null=True)
    grprc = models.IntegerField(blank=True, null=True)
    ck = models.IntegerField(blank=True, null=True)
    niszMan = models.IntegerField(blank=True, null=True)
    niszEne = models.IntegerField(blank=True, null=True)
    niszPan = models.IntegerField(blank=True, null=True)
    niszAbs = models.IntegerField(blank=True, null=True)
    fizycznyck = models.IntegerField(blank=True, null=True)
    magicznyck= models.IntegerField(blank=True, null=True)
    trucizna = models.IntegerField(blank=True, null=True)
    przebicie = models.IntegerField(blank=True, null=True)
    spowalniaCel = models.IntegerField(blank=True, null=True)
    niszczOdporn = models.IntegerField(blank=True, null=True)
    kontra = models.IntegerField(blank=True, null=True)
    panc = models.IntegerField(blank=True, null=True)
    absFiz = models.IntegerField(blank=True, null=True)
    absMag = models.IntegerField(blank=True, null=True)
    blok = models.IntegerField(blank=True, null=True)
    blokprze = models.IntegerField(blank=True, null=True)
    odpOg = models.IntegerField(blank=True, null=True)
    odpZim = models.IntegerField(blank=True, null=True)
    odpBlysk = models.IntegerField(blank=True, null=True)
    odpTrut = models.IntegerField(blank=True, null=True)
    obnUniku = models.IntegerField(blank=True, null=True)
    obnCk = models.IntegerField(blank=True, null=True)
    SA = models.IntegerField(blank=True, null=True)
    obnSA = models.IntegerField(blank=True, null=True)
    hp = models.IntegerField(blank=True, null=True)
    sil = models.IntegerField(blank=True, null=True)
    zren = models.IntegerField(blank=True, null=True)
    inte = models.IntegerField(blank=True, null=True)
    wszystkieCechy = models.IntegerField(blank=True, null=True)
    unik = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True)
    mana = models.IntegerField(blank=True, null=True)
    energia = models.IntegerField(blank=True, null=True)
    przywr = models.IntegerField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    pub_date = models.DateField(auto_now_add=True)


    pal = models.BooleanField()
    mag = models.BooleanField()
    woj = models.BooleanField()
    low = models.BooleanField()
    tro = models.BooleanField()
    tan = models.BooleanField()
    def __str__(self):
        return self.itemname
class votes(models.Model):
    voteItem = models.ForeignKey(customItem, on_delete=models.CASCADE)
    voted = models.BooleanField(default=False)
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    vot_date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.voter,self.voted
class Comments(models.Model):
     topic = models.ForeignKey(customItem, on_delete=models.CASCADE)
     text = models.TextField(max_length=512,)
     author = models.ForeignKey(User, on_delete=models.CASCADE)
     deleted = models.BooleanField(default=False)
     pub_date = models.DateField(auto_now_add=True)
     def __str__(self):
         return self.topic.itemname





