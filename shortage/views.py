# Create your views here.
from __future__ import division
from io import StringIO
from django.shortcuts import render
from django.shortcuts import redirect
from django.db.utils import OperationalError
import pandas as pd
import psycopg2
from datetime import datetime
import pathlib
from shortage.forms import Myform,Form


from shortage.models import MB52,SE16N_CEPC,SE16N_T001L,SE16N_T024,ZMM_CARNET_CDE_IS,ZRPFLG13,Core,CoreHistory
#function to upload files
def upload(request):
    # MB52.objects.all().delete()
    # SE16N_CEPC.objects.all().delete()
    # SE16N_T001L.objects.all().delete()
    # SE16N_T024.objects.all().delete()
    # ZMM_CARNET_CDE_IS.objects.all().delete()
    # ZRPFLG13.objects.all().delete()
    uploaded_files()  #call function to upload files
    return render(request,'app/upload.html')

 #Upload Files and check if exist   
def uploaded_files():
    #connection to DB 
        try:
            conn= psycopg2.connect(host='localhost', dbname='latecoere_db', user='postgres', password='sahar',port='5432')
            
        except OperationalError:
           print('Error Establishing a DB connection')
        #
        file_mb52=pathlib.Path(r'C:\Users\bibas\OneDrive\Bureau\PFE\inputSAP\MB52.xlsx')
        file_se16ncepc=pathlib.Path(r'C:\Users\bibas\OneDrive\Bureau\PFE\inputSAP\SE16N_CEPC.xlsx')
        file_se16nt001l=pathlib.Path(r'C:\Users\bibas\OneDrive\Bureau\PFE\inputSAP\SE16N_T001L.xlsx')
        file_se16nt024=pathlib.Path(r'C:\Users\bibas\OneDrive\Bureau\PFE\inputSAP\SE16N_T024.xlsx')
        file_zmm=pathlib.Path( r'C:\Users\bibas\OneDrive\Bureau\PFE\inputSAP\ZMM_CARNET_CDE_IS.xlsx')
        file_zrp=pathlib.Path(r'C:\Users\bibas\OneDrive\Bureau\PFE\inputSAP\ZRPFLG13.txt')
        #User name
        uploded_by = 1
        #Date time for upload files
        uploded_at = datetime.now()
        #control statment to check if files exists    
        if (file_mb52.exists() and file_se16ncepc.exists() and file_se16nt001l.exists() and file_se16nt024.exists() and file_zmm.exists() and file_zrp.exists() ):
            import_file_MB52(conn,file_mb52,uploded_by,uploded_at)
            import_file_SE16N_CEPC(conn,file_se16ncepc,uploded_by,uploded_at)
            import_file_SE16N_T001L(conn,file_se16nt001l,uploded_by,uploded_at)
            import_file_SE16N_T024(conn,file_se16nt024,uploded_by,uploded_at)
            import_file_ZMM_CARNET_CDE_IS(conn,file_zmm,uploded_by,uploded_at)
            import_file_ZRPFLG13(conn,file_zrp,uploded_by,uploded_at)
        else:
            print('files  not found') #To edit as Error MSG
   
#function for import file MB52
def import_file_MB52(con,file,username,uploaded_at):
    #Read file
    df = pd.read_excel(file) # to read file excel
    #insert 2 column created by, created at
    data=MB52.objects.values_list('file_number').distinct().order_by ('file_number')
    if data: 
        file_number=(list(data)[-1][-1]+1)
    else:
        file_number=1
    df.insert(0,'file_number',file_number,True)
    df.insert(1,'uploaded_by',username,True)
    df.insert(2,'uploaded_at',uploaded_at,True)

    df=df.to_csv(index=False,header=None) #To convert to csv
    
    mb=StringIO()
    mb.write(df)
    mb.seek(0)
    with con.cursor() as curs:
        curs.copy_from(
            file=mb,
            table="shortage_mb52",
            columns=[
               'file_number',
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
        data=SE16N_CEPC.objects.values_list('file_number').distinct().order_by ('file_number')
        if data: 
            file_number=(list(data)[-1][-1]+1)
        else:
            file_number=1
               
        df.insert(0,'file_number',file_number,True)
        df.insert(1,'uploaded_by',username,True)
        df.insert(2,'uploaded_at',uploaded_at,True)
        
        print(df)
        df=df.to_csv(index=False,header=None,sep=';') #To convert to csv
        
        se=StringIO()
        se.write(df)
        se.seek(0)
        with con.cursor() as curs:
            curs.copy_from(
                file=se,
                table="shortage_se16n_cepc",
                columns=[
                    'file_number',
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
    data=SE16N_T001L.objects.values_list('file_number').distinct().order_by ('file_number')
    if data: 
        file_number=(list(data)[-1][-1]+1)
    else:
        file_number=1
        
    df.insert(0,'file_number',file_number,True)
    df.insert(1,'uploaded_by',username,True)
    df.insert(2,'uploaded_at',uploaded_at,True)
    #insert 2 column created by, created at
    print(df)
    df=df.to_csv(index=False,header=None) #To convert to csv
        
    se=StringIO()
    se.write(df)
    se.seek(0)
    with con.cursor() as curs:
        curs.copy_from(
            file=se,
            table="shortage_se16n_t001l",
            columns=[
                    'file_number',
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
    data=SE16N_T024.objects.values_list('file_number').distinct().order_by ('file_number')
    if data: 
        file_number=(list(data)[-1][-1]+1)
    else:
        file_number=1
        
    df.insert(0,'file_number',file_number,True)
    df.insert(1,'uploaded_by',username,True)
    df.insert(2,'uploaded_at',uploaded_at,True)
     
    print(df)
    df=df.to_csv(index=False,header=None) #To convert to csv
    
    SE24=StringIO()
    SE24.write(df)
    SE24.seek(0)
    with con.cursor() as curs:
        curs.copy_from(
            file=SE24,
            table="shortage_se16n_t024",
            columns=[
               'file_number',
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
    data=ZMM_CARNET_CDE_IS.objects.values_list('file_number').distinct().order_by ('file_number')
    if data: 
        file_number=(list(data)[-1][-1]+1)
    else:
        file_number=1
        
    df.insert(0,'file_number',file_number,True)
    df.insert(1,'uploaded_by',username,True)
    df.insert(2,'uploaded_at',uploaded_at,True)
     
    print(df)
    df=df.to_csv(index=False,header=None,sep='|') #To convert to csv
    
    zmm=StringIO()
    zmm.write(df)
    zmm.seek(0)
    with con.cursor() as curs:
        curs.copy_from(
            file=zmm,
            table="shortage_zmm_carnet_cde_is",
            columns=[
                'file_number',
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
def  import_file_ZRPFLG13(con,file,username,uploaded_at):
  #Read file
    df = pd.read_csv(file,sep=';',encoding = "ISO-8859-1",index_col=False) # to read file excel
    #insert 2 column created by, created at
    for col in df.columns:
        if df[col].dtypes != 'int64':
            df[col]=df[col].str.strip()
            df[col]=df[col].str.replace(',','.')

   
    data=ZRPFLG13.objects.values_list('file_number').distinct().order_by ('file_number')
    if data: 
        file_number=(list(data)[-1][-1]+1)
    else:
        file_number=1
           
    df.insert(0,'file_number',file_number,True)
    df.insert(1,'uploaded_by',username,True)
    df.insert(2,'uploaded_at',uploaded_at,True)

     
    print(df)
    df=df.to_csv(index=False,header=None,sep=';') #To convert to csv
    
    zrp=StringIO()
    zrp.write(df)
    zrp.seek(0)
    with con.cursor() as curs:
        curs.copy_from(
            file=zrp,
            table="shortage_zrpflg13",
            columns=[
                        'file_number',
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

#CRUD CORE
def core(request):#show list of core
    data=Core.undeleted_objects.all()
    return render(request,r'app\core.html',{'data':data})

def create_core(request):#create new core
    if  (request.method == 'POST') :
        material=request.POST['material']
        division=request.POST['division']
        data=Core.undeleted_objects.all().filter(material=material,division=division).exclude(status='Close').first()

        if data:
            message={'type':'danger','msg':'Core is already created!'}
            return render(request,'app/core_history.html',{'pk':data.id,'message':message})
        else:
            myform = Myform(request.POST)
            if myform.is_valid():
                instance=myform.save(commit=False)
                instance.created_on =datetime.now()
                instance.updated_on =datetime.now()
                instance.created_by='1'
                instance.save()
                message={'type':'success','msg':'Core is  created successfully!'}

                return redirect('core')

    return render(request,'app\create_core.html',{'myform' : Myform})

def update_core(request,pk): #function for update core
    core=Core.objects.get(id=pk)
    myform=Myform(instance=core)
    if (request.method=='POST'):
        myform = Myform(request.POST,instance=core)
        if myform.is_valid():
            myform.save()
            # messages.success(request,"Core updated successfully!")
            return redirect('core')
        # else:
        #     messages.error(request, 'Invalid form submission.') 
    return render(request,'app/updateForm.html',{'core' : core,'myform' : myform}) 

def delete_core(request,pk): #function soft-delete
    core=Core.objects.get(id=pk)
    core.deleted=True
    core.deleted_on=datetime.now()
    core.deleted_by=1
    core.save()
    return redirect('core')

def core_history(request,pk):
    data=CoreHistory.objects.all().filter(core_id=pk).order_by('-id')
    core=Core.objects.get(id=pk)
    if (request.method == 'POST'):
        core.status = request.POST['status']
        if core.status== 'Close':
            core.closing_date=datetime.now()
        core.save()
        form=Form(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.created_on =datetime.now()
            instance.created_by='1'
            instance.core_id=pk
            instance.action=request.POST['status']
            instance.save()
            return redirect('core')
    return render(request,'app/core_history.html',{'form':Form,'pk':pk,'data':data,'core':core})
    

