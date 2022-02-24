# Create your views here.
from io import StringIO
from django.shortcuts import render
import pandas as pd
import psycopg2
from datetime import datetime
import pathlib
import time
from app.forms import Myform



from app.models import MB52,SE16N_CEPC,SE16N_T001L,SE16N_T024,ZMM_CARNET_CDE_IS,ZRPFLG13

def coreform(request):
    if  (request.method == 'POST') :
        myform = Myform(request.POST)
        myform.save(commit=False)
        instance=myform
        instance.created_on='2022-02-24 00:00:00'
        instance.created_by='1'
        print(instance)
        instance.save()
        
    return render(request,'app\corform.html',{'myform' : Myform} )
def home(request):
    MB52.objects.all().delete()
    SE16N_CEPC.objects.all().delete()
    SE16N_T001L.objects.all().delete()
    SE16N_T024.objects.all().delete()
    ZMM_CARNET_CDE_IS.objects.all().delete()
    ZRPFLG13.objects.all().delete()
    uploaded_files()
    return render(request,'app\index.html')
def uploaded_files():
        #connection to DB 
    conn= psycopg2.connect(host='localhost', dbname='shortagemanquant_db', user='postgres', password='sahar',port='5432')
    
    file1=pathlib.Path(r'C:\Users\bibas\OneDrive\Bureau\PFE\inputSAP\MB52.xlsx')
    file2=pathlib.Path(r'C:\Users\bibas\OneDrive\Bureau\PFE\inputSAP\SE16N_CEPC.xlsx')
    file3=pathlib.Path(r'C:\Users\bibas\OneDrive\Bureau\PFE\inputSAP\SE16N_T001L.xlsx')
    file4=pathlib.Path(r'C:\Users\bibas\OneDrive\Bureau\PFE\inputSAP\SE16N_T024.xlsx')
    file5=pathlib.Path( r'C:\Users\bibas\OneDrive\Bureau\PFE\inputSAP\ZMM_CARNET_CDE_IS.xlsx')
    file6=pathlib.Path(r'C:\Users\bibas\OneDrive\Bureau\PFE\inputSAP\ZRPFLG13.txt')

    #User name
    uploded_by = 1
    #Date time for upload files
    uploded_at = datetime.now()

    #control statment to check if files exists    
    if (file1.exists() and file2.exists() and file3.exists() and file4.exists() and file5.exists() and file6.exists() ):
    
        start=time.time()
        s1=time.time()
        import_file_MB52(conn,file1,uploded_by,uploded_at)
        e1=time.time()
        print('*'*50 )
        print('MB52')
        print(e1-s1)
        print(MB52.objects.all().count())
        print('*'*50 )

        s2=time.time()
        import_file_SE16N_CEPC(conn,file2,uploded_by,uploded_at)
        e2=time.time()
        print('*'*50)
        print('SE16N_CEPC')
        print(e2-s2)
        print('*'*50 )
        print(SE16N_CEPC.objects.all().count())
        print('*'*50 )

        
        s3=time.time()
        import_file_SE16N_T001L(conn,file3,uploded_by,uploded_at)
        e3=time.time()
        print('*'*50 )
        print('SE16N_T001L')
        print(e3-s3)
        print('*'*50 )
        print(SE16N_T001L.objects.all().count())
        
        print('*'*50 )

        s4=time.time()
        import_file_SE16N_T024(conn,file4,uploded_by,uploded_at)
        e4=time.time()
        print('*'*50 )
        print('SE16N_T024')
        print(e4-s4)
        print('*'*50 )
        print(SE16N_T024.objects.all().count())
        print('*'*50 )

        s5=time.time()
        import_file_ZMM_CARNET_CDE_IS(conn,file5,uploded_by,uploded_at)
        e5=time.time()
        print('*'*50 )
        print('ZMM_CARNET_CDE_IS')
        print(e5-s5)
        print('*'*50 )
        print(ZMM_CARNET_CDE_IS.objects.all().count())
        print('*'*50 )
        

        s6=time.time()
        import_file_ZRPFLG13(conn,file6,uploded_by,uploded_at)
        e6=time.time()
        print('*'*50 )
        print('ZRPFLG13')
        print(e6-s6)
        print('*'*50 )
        print(ZRPFLG13.objects.all().count())
        print('*'*50 )
        end=time.time()
        total=end-start
        print('#'*50)
        print('total')
        print('#'*50)
        print(total)
    else:
        print("files  not found")

#function for import file MB52
def import_file_MB52(con,file,username,uploaded_at):
    #Read file
    df = pd.read_excel(file) # to read file excel
    #insert 2 column created by, created at
  
    df.insert(0,'uploaded_by',username,True)
    df.insert(1,'uploaded_at',uploaded_at,True)
     
    
    print(df)
    df=df.to_csv(index=False,header=None) #To convert to csv
    
    mb=StringIO()
    mb.write(df)
    mb.seek(0)
    with con.cursor() as curs:
        curs.copy_from(
            file=mb,
            table="app_mb52",
            columns=[
              'uploaded_by',
               'uploaded_at',
               'material',
               'division',
               'store', 
               'store_level_deletion_indicator',
               'unit',
               'for_free_use',	
               'currency',
               'value_free_use',
               'transit_transfer',
               'transit_transfer_value', 	
               'in_quality_control',
               'value_quality_control', 	
               'non_free_stock',	
               'non_free_value', 
               'blocked',
               'blocked_stock_value',
               'returns',	
               'blocked_return_stock_value',
            ],
            null='',
            sep=','
        )
    con.commit()
#function for Import file SE16N_CEPC
def import_file_SE16N_CEPC(con,file,username,uploaded_at):

        #Read file
        df = pd.read_excel(file,index_col=False) # to read file excel
        #insert 2 column created by, created at
    
        df.insert(0,'uploaded_by',username,True)
        df.insert(1,'uploaded_at',uploaded_at,True)
        
        print(df)
        df=df.to_csv(index=False,header=None,sep=';') #To convert to csv
        
        mb=StringIO()
        mb.write(df)
        mb.seek(0)
        with con.cursor() as curs:
            curs.copy_from(
                file=mb,
                table="app_se16n_cepc",
                columns=[
                    'uploaded_by',
                    'uploaded_at',
                    'profit_center',
                    'valid_to',
                    'controlling_area', 
                    'valid_from',
                    'created_on',
                    'created_by',	
                    'field_name_of_CO_PA_characteristic',
                    'department',
                    'person_responsible_for_profit_center',
                    'user_responsible', 	
                    'currency',
                    'successor_profit_center', 	
                    'country_key',	
                    'title', 
                    'name1',
                    'name2',
                    'name3',	
                    'name4',
                    'city',
                    'district',
                    'street',
                    'po_box',	
                    'postal_code',
                    'p_o_box_costal_code',
                    'language_key',
                    'telebox_number',
                    'telephone1',
                    'telephone2',
                    'fax_number',	
                    'teletex_number',
                    'telex_number',
                    'data_line',
                    'printer_name',
                    'hierarchy_area',
                    'company_code',	
                    'joint_venture',
                    'recovery_indicator',
                    'equity_type',
                    'tax_jurisdiction',
                    'region',
                    'usage',
                    'application',
                    'procedure',	
                    'logical_system',
                    'lock_indicator',
                    'prctr_formula_planning_template',
                    'segment',
                    'name',
                    'long_text',	
                    'profit_center_short_text_for_matchcode',
                 ],
                null='',
                sep=';'
            )
        con.commit()
#function for Import file SE16N_T001L
def import_file_SE16N_T001L(con,file,username,uploaded_at):
    #     #Read file
    df = pd.read_excel(file,index_col=False) # to read file excel
    #insert 2 column created by, created at
    
    df.insert(0,'uploaded_by',username,True)
    df.insert(1,'uploaded_at',uploaded_at,True)
        
    print(df)
    df=df.to_csv(index=False,header=None) #To convert to csv
        
    mb=StringIO()
    mb.write(df)
    mb.seek(0)
    with con.cursor() as curs:
        curs.copy_from(
            file=mb,
            table="app_se16n_t001l",
            columns=[
                    'uploaded_by',
                    'uploaded_at',
                    'plant',
                    'storage_location',
                    'descr_of_storage_loc', 
                    'store_level_deletion_indicator',
                    'division',
                    'neg_stocks_in_sloc',	
                    'freeze_book_inv_sLoc',
                    'sloc_MRP_indicator',
                    'authorization_check',
                    'stor_resource', 	
                    'hu_reqmnt',
                    'sales_organization', 	
                    'distribution_channel',	
                    'shipping_point_receiving_pt', 
                    'vendor',
                    'customer',	
                    'business_system_of_mes',
                    'inventory_management_type',
                    'license_number',
                    'in_transit_assignment',
                    'tank_assgn',

                ],
            null='',
            sep=','
            )
    con.commit()
#function for Import file SE16N_T024
def import_file_SE16N_T024(con,file,username,uploaded_at):
      #Read file
    df = pd.read_excel(file) # to read file excel
    #insert 2 column created by, created at
  
    df.insert(0,'uploaded_by',username,True)
    df.insert(1,'uploaded_at',uploaded_at,True)
     
    print(df)
    df=df.to_csv(index=False,header=None) #To convert to csv
    
    SE24=StringIO()
    SE24.write(df)
    SE24.seek(0)
    with con.cursor() as curs:
        curs.copy_from(
            file=SE24,
            table="app_se16n_t024",
            columns=[
              'uploaded_by',
               'uploaded_at',
               'purchasing_group',
               'description_p_group',
               'tel_no_purch_group', 
               'output_device',
               'fax_number',	
               'telephone',
               'extension',
               'e_mail_address',
               'user_name', 	
            ],
            null='',
            sep=','
        )
    con.commit() 
#function for Import file ZMM_CARNET_CDE_IS
def import_file_ZMM_CARNET_CDE_IS(con,file,username,uploaded_at):
     #Read file
    df = pd.read_excel(file) # to read file excel
    #insert 2 column created by, created at
  
    df.insert(0,'uploaded_by',username,True)
    df.insert(1,'uploaded_at',uploaded_at,True)
     
    print(df)
    df=df.to_csv(index=False,header=None,sep='|') #To convert to csv
    
    mb=StringIO()
    mb.write(df)
    mb.seek(0)
    with con.cursor() as curs:
        curs.copy_from(
            file=mb,
            table="app_zmm_carnet_cde_is",
            columns=[
                'uploaded_by',
                'uploaded_at',
                'request_no',
                'plant',
                'storage_location', 
                'purchase_document',
                'poste1',	
                'due_date',
                'vendor',
                'vendor_name',
                'material', 	
                'designation_add_material',
                'name',
                'transmission_info',
                'validated_by',
                'priority', 
                'quantity',
                'quantity_to_receive',	
                'date_of_purchase',
                'desired_date',
                'original_delivery_date',
                'contractual_delivery_date', 	
                'validated_delivery_date',
                'confirmed_quantity',
                'comment',
                'expected_stock_week_w',
                'expected_stock_week_w_1',
                'expected_stock_week_w_2',
                'expected_stock_week_w_3',
                'expected_stock_week_w_4',
                'expected_stock_week_w_5',
                'expected_stock_week_w_6',
                'expected_stock_week_w_7',
                'expected_stock_week_w_8',
                'expected_stock_week_w_9',
                'expected_stock_week_w_10',
                'expected_stock_week_w_11',
                'expected_stock_week_w_12',
                'confirmation',
                'estimated_delivery_time',
                'comment_vendor',
                'element_otp',
                'business_document',
                'poste2',
                'need_number',
                'net_price',
                'currency',
                'price_basis',
                'price_unit',
                'net_order_value',
                'purchasing_document_type',
                'exception_message_number',
                'exception_message',
                'purchasing_group',
            ],
            null='',
            sep='|'
        )
    con.commit() 
#function for Import file ZRPFLG13
def  import_file_ZRPFLG13(con,file,username,uploded_at):
  #Read file
    df = pd.read_csv(file,sep=';',encoding = "ISO-8859-1",index_col=False) # to read file excel
    #insert 2 column created by, created at
    # print(df.head(10))
    print(df.dtypes)
    for col in df.columns:
        if df[col].dtypes != 'int64':
            #print(col)
            df[col]=df[col].str.strip()
            df[col]=df[col].str.replace(',','.')

    df.insert(0,'uploaded_by',username,True)
    df.insert(1,'uploaded_at',uploded_at,True)

     
    print(df)
    df=df.to_csv(index=False,header=None,sep=';') #To convert to csv
    
    zrp=StringIO()
    zrp.write(df)
    zrp.seek(0)
    with con.cursor() as curs:
        curs.copy_from(
            file=zrp,
            table="app_zrpflg13",
            columns=[
                        'uploaded_by',
                        'uploaded_at',
                        'period',           	
                        'plant',            	
                        'ctr_pft', 	
                        'administrator', 	
                        'tech_desc', 
                        'customer_grp', 	
                        'material', 	
                        'ty', 	
                        'st',            	
                        'gv', 	
                        'needs',            	
                        'stock',            	
                        'consign_stock',            	
                        'lot_qm',             	
                        'of',            	
                        'cde',            
                        'op',            
                        'da',            	
                        'key', 	
                        'fixed_lot',            		
                        'security',            	
                        'surpluses',            	
                        'valuation',            		
                        'time_limit_of_secu',           		
                        'pmp_ps',          	
                        'abc',
                        'mini_lot', 
                        'rounds', 
                        'tps_recept',
                        'maxi_lot', 
                        'storage_loc',
                        'desc_material',
                        'curency', 		
                        'material_type', 		
                        'appro_spe',		
                        'vrac', 		
                        'planif_type',	
                        'vendor1', 		
                        'desc_vendor1',		
                        'vendor2',		
                        'desc_vendor2',		
                        'stock_in_transit', 	
                        'required_quantity_1000', 		
                        'required_quantity_1010', 		
                        'required_quantity_1900', 		
                        'required_quantity_3000',
                        'required_quantity_3100', 		
                        'required_quantity_4000', 	
                        'required_quantity_5000',  		
                        'decoupling_point',
                        'vmi_stock',
                        'item_order',            
                        'planif_device', 
            ],
            null='',
            sep=';'
        )
    con.commit() 

