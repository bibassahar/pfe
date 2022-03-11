from datetime import  datetime
from django.db import models

# Create your models here.


class MB52(models.Model): #Model MB52
    file_number=models.IntegerField(null=True)
    uploaded_by=models.IntegerField(null=True)
    uploaded_at=models.DateTimeField(null=True)
    material = models.CharField(max_length=30,null=True) #Numéro d'article	
    division = models.CharField(max_length=20,null=True) #Division
    store = models.CharField(max_length=10,null=True) #Magasin
    store_level_deletion_indicator =models.CharField(max_length=15,null=True) #Tém.suppr.:niv. mag	
    unit=models.CharField(max_length=5,null=True) #Unité de qté base
    for_free_use= models.FloatField(null=True) #A utilisation libre	
    currency=models.CharField(max_length=5,null=True) #Devise	
    value_free_use=models.FloatField(null=True)#Val. utilis. libre
    transit_transfer=models.FloatField(null=True) #Transit et transfert
    transit_transfer_value = models.FloatField(null=True) #Val. en Trnst&Tsft	
    in_quality_control = models.FloatField(null=True) #En contrôle qualité	
    value_quality_control = models.FloatField(null=True) #Val. ds ctrl.qual.	
    non_free_stock=models.FloatField(null=True) #Stock non libre	
    non_free_value =models.FloatField(null=True) #Valeur non libre
    blocked=models.FloatField(null=True) #Bloqué	
    blocked_stock_value=models.FloatField(null=True) #Val. stock bloqué	
    returns=models.FloatField(null=True) #Retours	
    blocked_return_stock_value=models.FloatField(null=True) #Val.stk ret.bloq.   



class SE16N_CEPC(models.Model): #Model SE16N_CEPC
    file_number=models.IntegerField(null=True)
    uploaded_by = models.IntegerField()
    uploaded_at= models.DateTimeField()
    profit_center = models.CharField(max_length=30,null=True) #Centre de profit
    valid_to = models.DateTimeField(null=True) #Fin de validité
    controlling_area = models.CharField(max_length=30,null=True) #Périmètre analytique
    valid_from =models.DateTimeField(null=True) #Début de validité  
    created_on=models.DateTimeField(null=True) #Saisi le  
    created_by= models.CharField(max_length=30,null=True) #Saisi par      
    field_name_of_CO_PA_characteristic=models.CharField(max_length=30,null=True) #Nom de zone de caractér. ds CO-PA  
    department=models.CharField(max_length=30,null=True) #Département  
    person_responsible_for_profit_center=models.CharField(max_length=30,null=True) #Responsable centre de profit
    user_responsible=models.CharField(max_length=30,null=True) #Utilisateur responsable
    currency = models.CharField(null=True , max_length=10) #Devise    
    successor_profit_center = models.CharField(max_length=30,null=True) #Centre de profit suivant    
    country_key = models.CharField(max_length=10,null=True) #Clé de pays
    title = models.CharField(max_length=30,null=True) #Titre de civilité  
    name1 = models.CharField(max_length=30,null=True)  #Nom 1  
    name2 = models.CharField(max_length=30,null=True)  #Nom 2  
    name3 = models.CharField(max_length=30,null=True)  #Nom 3
    name4 = models.CharField(max_length=30,null=True)  #Nom 4  
    city = models.CharField(max_length=10,null=True)  #ville  
    district = models.CharField(max_length=30,null=True)  #Arrondissement        
    street = models.CharField(max_length=30,null=True)  #Rue    
    po_box = models.CharField(max_length=10,null=True)  #Boîte postale
    postal_code = models.CharField(max_length=30,null=True) #Code postal
    p_o_box_costal_code = models.CharField(max_length=30,null=True) #CdP-Boîte postale  
    language_key = models.CharField(max_length=10,null=True) #Code langue    
    telebox_number = models.CharField(max_length=30,null=True) #Nº boîte électroniq.    
    telephone1 = models.CharField(max_length=30,null=True) #Téléphone 1
    telephone2 = models.CharField(max_length=30,null=True) #Téléphone 2
    fax_number = models.CharField(max_length=30,null=True) #Numéro de télécopie
    teletex_number = models.CharField(max_length=30,null=True) #Numéro de télétex  
    telex_number = models.CharField(max_length=30,null=True) #Numéro de télex
    data_line = models.CharField(max_length=30,null=True) #Ligne transmission  
    printer_name = models.CharField(max_length=30,null=True) #Nom imprimante  
    hierarchy_area = models.CharField(max_length=30,null=True) #Dom. hiérarchie
    company_code = models.CharField(max_length=30,null=True) #Société
    joint_venture = models.CharField(max_length=30,null=True) #Joint venture  
    recovery_indicator = models.CharField(max_length=30,null=True) #Catégorie de coûts  
    equity_type = models.CharField(max_length=30,null=True) #Classe participation
    tax_jurisdiction = models.CharField(max_length=30,null=True) #Juridiction fiscale
    region = models.CharField(max_length=30,null=True)  # Région    
    usage = models.CharField(max_length=30,null=True) #Emploi  
    application = models.CharField(max_length=30,null=True) #Application
    procedure = models.CharField(max_length=30,null=True) #schéma  
    logical_system = models.CharField(max_length=30,null=True) #Système logique
    lock_indicator = models.CharField(max_length=30,null=True) #code de blocage
    prctr_formula_planning_template = models.CharField(max_length=30,null=True) #Sch. type p-budg. form. ctre profit
    segment = models.CharField(max_length=30,null=True) #Segment
    name = models.CharField(max_length=30,null=True) #Désignation
    long_text = models.CharField(max_length=100,null=True) #Texte descriptif  
    profit_center_short_text_for_matchcode = models.CharField(max_length=100,null=True) #Désing. centre de pro
   

class SE16N_T001L(models.Model):
    file_number=models.IntegerField(null=True)
    uploaded_by = models.IntegerField()
    uploaded_at= models.DateTimeField()
    plant = models.CharField(null=True,max_length=20) #Division
    storage_location = models.CharField(max_length=20,null=True)  #Magasin		
    descr_of_storage_loc = models.CharField(max_length=100,null=True) #Désignation magasin	
    store_level_deletion_indicator =models.CharField(max_length=20,null=True) #Secteur d'activité	
    division=models.CharField(max_length=20,null=True) #Stks négatifs magas.	
    neg_stocks_in_sloc= models.CharField(max_length=20,null=True) #Fixer stk théo. mag.	    
    freeze_book_inv_sLoc = models.FloatField(null=True) #Code MRP		
    sloc_MRP_indicator = models.CharField(max_length=20,null=True) #Contrôle autorisat.	
    authorization_check = models.CharField(max_length=20,null=True) #Ressource magasin		
    stor_resource = models.CharField(max_length=20,null=True)  #Gest. unités manut.	
    hu_reqmnt = models.CharField(max_length=20,null=True)  #Magasin partenaire		
    sales_organization = models.CharField(max_length=20,null=True)  #Organis. commerciale	
    distribution_channel = models.CharField(max_length=20,null=True)  #cannal de distrution		
    shipping_point_receiving_pt = models.CharField(max_length=20,null=True)  # Point expédition/réception		    
    vendor = models.CharField(max_length=20,null=True)  #fornisseur	
    customer = models.CharField(max_length=20,null=True)  #client	  
    business_system_of_mes = models.CharField(max_length=20,null=True) #Système de gestion du MES	
    inventory_management_type = models.CharField(max_length=20,null=True) # Tpe de gestion des stocks	
    license_number = models.CharField(max_length=20,null=True) #Numéro licence
    in_transit_assignment = models.CharField(max_length=20,null=True) # Affectation transit		
    tank_assgn = models.CharField(max_length=20,null=True) #Affectat. bac


class SE16N_T024(models.Model): #Model SE16N_T024
    file_number=models.IntegerField(null=True)
    uploaded_by = models.IntegerField()
    uploaded_at= models.DateTimeField()
    purchasing_group = models.CharField(max_length=20,null=True) #Groupe d'acheteurs	
    description_p_group = models.CharField(max_length=20,null=True) #Désignat.grpe achet.	
    tel_no_purch_group = models.CharField(max_length=20,null=True) #N° tél.grpe achet.		
    output_device = models.CharField(max_length=20,null=True) #Unité de sortie	
    fax_number = models.CharField(max_length=20,null=True) #Numéro de télécopie	
    telephone = models.CharField(max_length=20,null=True) #Téléphone		
    extension = models.CharField(max_length=20,null=True) #Numéro de poste		
    e_mail_address = models.CharField(max_length=50,null=True) #Adresse e-mail	
    user_name = models.CharField(max_length=20,null=True) #Utilisateur	

class ZMM_CARNET_CDE_IS(models.Model): #Model ZMM_CARNET_CDE_IS
     file_number=models.IntegerField(null=True)
     uploaded_by = models.IntegerField(null=True)
     uploaded_at= models.DateTimeField()
     request_no = models.CharField(max_length=30,null=True) #N° Demande		
     plant = models.CharField(null=True,max_length=30)              #Division	
     storage_location = models.CharField(max_length=30,null=True) #Magasin		
     purchase_document = models.CharField(null=True,max_length=30)              #Document d'achat	  
     poste1 = models.CharField(null=True,max_length=30)              #Poste			
     due_date = models.CharField(null=True,max_length=20)              #Echéance		     
     vendor = models.CharField(max_length=50,null=True) #Fournisseur		
     vendor_name = models.CharField(max_length=50,null=True) #Nom Fournisseur		
     material = models.CharField(max_length=50,null=True) #Article			      
     designation_add_material = models.CharField(max_length=50,null=True) #Désignation add. art.			
     name = models.CharField(max_length=50,null=True) #Désignation			       
     transmission_info = models.DateTimeField(null=True)               #Info Transmission			
     validated_by = models.CharField(max_length=50,null=True) #Validé par			      
     priority = models.CharField(max_length=50,null=True) #Priorité de l'ordre			
     quantity = models.FloatField(null=True)              #Quantité de commande			       
     quantity_to_receive = models.FloatField(null=True)              #Quantité à réceptionner			
     date_of_purchase = models.DateTimeField(null=True)               #Date d'achat			       
     desired_date = models.DateTimeField(null=True)               #date souhaitée	
     original_delivery_date = models.DateTimeField(null=True)               #Date de livraison initiale				
     contractual_delivery_date = models.DateTimeField(null=True)               #Date de livraison contractulle	
     validated_delivery_date = models.DateTimeField(null=True)               #Date de livraison validée	
     confirmed_quantity = models.FloatField(null=True)              #Quantité confirmée
     comment = models.CharField(max_length=500,null=True) #Commentaire Appros				           
     expected_stock_week_w = models.FloatField(null=True)              #Stock Prévu Semaine S		
     expected_stock_week_w_1 = models.FloatField(null=True)              #Stock Prévu Semaine S+1		
     expected_stock_week_w_2 = models.FloatField(null=True)              #Stock Prévu Semaine S+2		
     expected_stock_week_w_3 = models.FloatField(null=True)              #Stock Prévu Semaine S+3		
     expected_stock_week_w_4 = models.FloatField(null=True)              #Stock Prévu Semaine S+4		
     expected_stock_week_w_5 = models.FloatField(null=True)              #Stock Prévu Semaine S+5		
     expected_stock_week_w_6 = models.FloatField(null=True)              #Stock Prévu Semaine S+6	
     expected_stock_week_w_7 = models.FloatField(null=True)              #Stock Prévu Semaine S+7	
     expected_stock_week_w_8 = models.FloatField(null=True)              #Stock Prévu Semaine S+8		
     expected_stock_week_w_9 = models.FloatField(null=True)              #Stock Prévu Semaine S+9		
     expected_stock_week_w_10 = models.FloatField(null=True)              #Stock Prévu Semaine S+10	
     expected_stock_week_w_11 = models.FloatField(null=True)              #Stock Prévu Semaine S+11	
     expected_stock_week_w_12 = models.FloatField(null=True)              #Stock Prévu Semaine S+12
     confirmation = models.CharField(max_length=30,null=True) #Confirmation ordre					
     estimated_delivery_time = models.CharField(null=True,max_length=20)              #Délai prévisionnel de livraison (en jrs)
     comment_vendor = models.CharField(max_length=500,null=True) #Commentaires fournisseur	
     element_otp = models.CharField(max_length=30,null=True) #Elément d'OTP		
     business_document = models.CharField(max_length=10,null=True) #Document commercial							
     poste2 = models.CharField(null=True,max_length=20)              #Poste			
     need_number= models.CharField(max_length=30,null=True)             # N° de besoin	
     net_price = models.FloatField(null=True)              #Prix net de la cde
     currency = models.CharField(max_length=10,null=True) #Devise
     price_basis = models.CharField(null=True,max_length=20)              #Base de prix	
     price_unit = models.CharField(max_length=10,null=True) #Unité de prix	
     net_order_value = models.FloatField(null=True)              #Valeur nette de cde	
     purchasing_document_type = models.CharField(max_length=10,null=True) # Type document achat	
     exception_message_number = models.CharField(null=True,max_length=20)              #Exception message numér
     exception_message = models.CharField(max_length=50,null=True) #Exception message	
     purchasing_group = models.CharField(max_length=50,null=True) #Groupe d'acheteurs	




class ZRPFLG13(models.Model): #Model ZRPFLG13 
    file_number=models.IntegerField(null=True)
    uploaded_by=models.IntegerField(null=True)
    uploaded_at=models.DateTimeField(null=True)
    period = models.FloatField(null=True)              #Période	
    plant= models.FloatField(null=True)              #Division	
    ctr_pft = models.CharField(max_length=10,null=True) #Ctr Pft	
    administrator = models.CharField(max_length=10,null=True) #Gestionnaire	
    tech_desc = models.CharField(max_length=10,null=True) #Desc. Tech.
    customer_grp = models.CharField(max_length=10,null=True) #Grp acheteurs	
    material = models.CharField(max_length=10,null=True) #Référence article	
    ty = models.CharField(max_length=10,null=True) #Ty	
    st = models.FloatField(null=True)              #St	
    gv = models.CharField(max_length=10,null=True) #Gv	
    needs = models.CharField(null=True,max_length=30)              #Besoins	
    stock = models.FloatField(null=True)              #Stock	
    consign_stock = models.FloatField(null=True)              #Consign. Stock	
    lot_qm = models.FloatField(null=True)              #Lot QM	
    of = models.FloatField(null=True)              #OF	
    cde = models.FloatField(null=True)              #CDE	
    op = models.FloatField(null=True)              #OP
    da = models.FloatField(null=True)              #DA	
    key = models.CharField(max_length=10,null=True) #Clé	
    fixed_lot = models.FloatField(null=True)              #Lot fixe		
    security = models.FloatField(null=True)              #Sécurité	
    surpluses = models.FloatField(null=True)              #Exédents	
    valuation = models.FloatField(null=True)              #Valorisation		
    time_limit_of_secu = models.FloatField(null=True)              #Délai sécu		
    pmp_ps = models.FloatField(null=True)              #PMP-PS	
    abc = models.CharField(max_length=10,null=True) #ABC	
    mini_lot = models.FloatField(null=True)              #Lot mini		
    rounds = models.FloatField(null=True)              #Cycle		
    tps_recept = models.FloatField(null=True)              #Tps récept.		
    maxi_lot = models.FloatField(null=True)              #Taille de lot maxi		
    storage_loc = models.FloatField(null=True)              #Storage loc.	
    desc_material = models.CharField(max_length=50,null=True) #Désignation article		
    curency = models.CharField(max_length=10,null=True) #Unité		
    material_type = models.CharField(max_length=10,null=True) #Type article		
    appro_spe = models.CharField(max_length=10,null=True) #Appro Spe		
    vrac = models.CharField(max_length=10,null=True) #Vrac		
    planif_type = models.CharField(max_length=10,null=True) #Type planif.	
    vendor1 = models.CharField(max_length=10,null=True) #Fournisseur 1		
    desc_vendor1 = models.CharField(max_length=200,null=True) #Désignation Fournisseur 1		
    vendor2 = models.CharField(max_length=10,null=True) #Fournisseur 2		
    desc_vendor2 = models.CharField(max_length=20,null=True) #Désignation Fournisseur 2		
    stock_in_transit = models.FloatField(null=True)              #Stock en Transit		
    required_quantity_1000 = models.FloatField(null=True)              #Quantité requise (1000)		
    required_quantity_1010 = models.FloatField(null=True)              #Quantité requise (1010)		
    required_quantity_1900 = models.FloatField(null=True)              #Quantité requise (1900)		
    required_quantity_3000 = models.FloatField(null=True)              #Quantité requise (3000)	.	
    required_quantity_3100 = models.FloatField(null=True)              #Quantité requise (3100)		
    required_quantity_4000 = models.FloatField(null=True)              #Quantité requise (4000)	
    required_quantity_5000 = models.FloatField(null=True)               #Quantité requise (5000)		
    decoupling_point=models.CharField(max_length=20,null=True)  #Pt découplage
    vmi_stock = models.FloatField(null=True)              #Stock VMI		
    item_order = models.FloatField(null=True)              #Point Commande		
    planif_device = models.CharField(max_length=10,null=True) #Unité Planif	


class SoftDeleteManager(models.Manager):
    # def deleted_object(self):
    #     return super().get_queryset().filter(deleted=True)
    # def nodeleted_object(self):
    #     return super().get_queryset().filter(deleted=False)
       def get_queryset(self):
           return super().get_queryset().filter(deleted=False)

class Soft_delete(models.Model): #model info 
    # uploaded_by= models.IntegerField(null=True, default='1')
    # uploaded_at= models.DateTimeField(null=True, auto_now_add=True)
    deleted=models.BooleanField(default=False)
    deleted_by=models.IntegerField(null=True)
    deleted_on=models.DateTimeField(null=True)
    objects=models.Manager()
    undeleted_objects=SoftDeleteManager()
    def soft_delete(self):
        self.deleted = True
        self.save()
    def soft_delete(self):
        self.deleted_on = datetime.now()
        self.save()
    def soft_delete(self):
        self.deleted_by = 1
        self.save()
    class Meta:
        abstract=True



class Core(Soft_delete):
    created_on=models.DateTimeField()
    created_by=models.IntegerField(default=1)
    updated_by=models.IntegerField(default=1)
    updated_on=models.DateTimeField()
    plant=models.CharField(max_length=30,null=True)
    program=models.CharField(max_length=30,null=True)
    supplier=models.CharField(max_length=30,null=True)
    part_number=models.FloatField(null=True)
    create=models.CharField(max_length=30,null=True)
    type_of_alert=models.CharField(max_length=30,null=True)
    requested_date=models.DateTimeField()
    needed_quantity=models.FloatField(null=True)
    production_comments=models.TextField(null=True)
    status=models.CharField(max_length=30,null=True)
    procurement_comments=models.TextField(null=True)
    closing_date=models.DateTimeField()
    duration_of_the_event=models.CharField(max_length=30,null=True)

class CoreHistory(models.Model):
    core=models.ForeignKey(Core,on_delete=models.CASCADE)
    created_on=models.DateTimeField()
    created_by=models.IntegerField(default=1)
    comment=models.TextField(null=True)
   

        


        