# Generated by Django 4.0.2 on 2022-03-02 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Core',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False)),
                ('deleted_by', models.IntegerField(null=True)),
                ('deleted_on', models.DateTimeField(null=True)),
                ('created_on', models.DateTimeField()),
                ('created_by', models.IntegerField(default=1)),
                ('updated_by', models.IntegerField(default=1)),
                ('updated_on', models.DateTimeField()),
                ('plant', models.CharField(max_length=30, null=True)),
                ('program', models.CharField(max_length=30, null=True)),
                ('supplier', models.CharField(max_length=30, null=True)),
                ('part_number', models.FloatField(null=True)),
                ('create', models.CharField(max_length=30, null=True)),
                ('type_of_alert', models.CharField(max_length=30, null=True)),
                ('requested_date', models.DateField()),
                ('needed_quantity', models.FloatField(null=True)),
                ('production_comments', models.TextField(null=True)),
                ('status', models.CharField(max_length=30, null=True)),
                ('procurement_comments', models.TextField(null=True)),
                ('closing_date', models.DateField()),
                ('duration_of_the_event', models.CharField(max_length=30, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MB52',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_number', models.IntegerField(null=True)),
                ('uploaded_by', models.IntegerField(null=True)),
                ('uploaded_at', models.DateTimeField(null=True)),
                ('material', models.CharField(max_length=30, null=True)),
                ('division', models.CharField(max_length=20, null=True)),
                ('store', models.CharField(max_length=10, null=True)),
                ('store_level_deletion_indicator', models.CharField(max_length=15, null=True)),
                ('unit', models.CharField(max_length=5, null=True)),
                ('for_free_use', models.FloatField(null=True)),
                ('currency', models.CharField(max_length=5, null=True)),
                ('value_free_use', models.FloatField(null=True)),
                ('transit_transfer', models.FloatField(null=True)),
                ('transit_transfer_value', models.FloatField(null=True)),
                ('in_quality_control', models.FloatField(null=True)),
                ('value_quality_control', models.FloatField(null=True)),
                ('non_free_stock', models.FloatField(null=True)),
                ('non_free_value', models.FloatField(null=True)),
                ('blocked', models.FloatField(null=True)),
                ('blocked_stock_value', models.FloatField(null=True)),
                ('returns', models.FloatField(null=True)),
                ('blocked_return_stock_value', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SE16N_CEPC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_number', models.IntegerField(null=True)),
                ('uploaded_by', models.IntegerField()),
                ('uploaded_at', models.DateTimeField()),
                ('profit_center', models.CharField(max_length=30, null=True)),
                ('valid_to', models.DateField(null=True)),
                ('controlling_area', models.CharField(max_length=30, null=True)),
                ('valid_from', models.DateField(null=True)),
                ('created_on', models.DateField(null=True)),
                ('created_by', models.CharField(max_length=30, null=True)),
                ('field_name_of_CO_PA_characteristic', models.CharField(max_length=30, null=True)),
                ('department', models.CharField(max_length=30, null=True)),
                ('person_responsible_for_profit_center', models.CharField(max_length=30, null=True)),
                ('user_responsible', models.CharField(max_length=30, null=True)),
                ('currency', models.CharField(max_length=10, null=True)),
                ('successor_profit_center', models.CharField(max_length=30, null=True)),
                ('country_key', models.CharField(max_length=10, null=True)),
                ('title', models.CharField(max_length=30, null=True)),
                ('name1', models.CharField(max_length=30, null=True)),
                ('name2', models.CharField(max_length=30, null=True)),
                ('name3', models.CharField(max_length=30, null=True)),
                ('name4', models.CharField(max_length=30, null=True)),
                ('city', models.CharField(max_length=10, null=True)),
                ('district', models.CharField(max_length=30, null=True)),
                ('street', models.CharField(max_length=30, null=True)),
                ('po_box', models.CharField(max_length=10, null=True)),
                ('postal_code', models.CharField(max_length=30, null=True)),
                ('p_o_box_costal_code', models.CharField(max_length=30, null=True)),
                ('language_key', models.CharField(max_length=10, null=True)),
                ('telebox_number', models.CharField(max_length=30, null=True)),
                ('telephone1', models.CharField(max_length=30, null=True)),
                ('telephone2', models.CharField(max_length=30, null=True)),
                ('fax_number', models.CharField(max_length=30, null=True)),
                ('teletex_number', models.CharField(max_length=30, null=True)),
                ('telex_number', models.CharField(max_length=30, null=True)),
                ('data_line', models.CharField(max_length=30, null=True)),
                ('printer_name', models.CharField(max_length=30, null=True)),
                ('hierarchy_area', models.CharField(max_length=30, null=True)),
                ('company_code', models.CharField(max_length=30, null=True)),
                ('joint_venture', models.CharField(max_length=30, null=True)),
                ('recovery_indicator', models.CharField(max_length=30, null=True)),
                ('equity_type', models.CharField(max_length=30, null=True)),
                ('tax_jurisdiction', models.CharField(max_length=30, null=True)),
                ('region', models.CharField(max_length=30, null=True)),
                ('usage', models.CharField(max_length=30, null=True)),
                ('application', models.CharField(max_length=30, null=True)),
                ('procedure', models.CharField(max_length=30, null=True)),
                ('logical_system', models.CharField(max_length=30, null=True)),
                ('lock_indicator', models.CharField(max_length=30, null=True)),
                ('prctr_formula_planning_template', models.CharField(max_length=30, null=True)),
                ('segment', models.CharField(max_length=30, null=True)),
                ('name', models.CharField(max_length=30, null=True)),
                ('long_text', models.CharField(max_length=100, null=True)),
                ('profit_center_short_text_for_matchcode', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SE16N_T001L',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_number', models.IntegerField(null=True)),
                ('uploaded_by', models.IntegerField()),
                ('uploaded_at', models.DateTimeField()),
                ('plant', models.CharField(max_length=20, null=True)),
                ('storage_location', models.CharField(max_length=20, null=True)),
                ('descr_of_storage_loc', models.CharField(max_length=100, null=True)),
                ('store_level_deletion_indicator', models.CharField(max_length=20, null=True)),
                ('division', models.CharField(max_length=20, null=True)),
                ('neg_stocks_in_sloc', models.CharField(max_length=20, null=True)),
                ('freeze_book_inv_sLoc', models.FloatField(null=True)),
                ('sloc_MRP_indicator', models.CharField(max_length=20, null=True)),
                ('authorization_check', models.CharField(max_length=20, null=True)),
                ('stor_resource', models.CharField(max_length=20, null=True)),
                ('hu_reqmnt', models.CharField(max_length=20, null=True)),
                ('sales_organization', models.CharField(max_length=20, null=True)),
                ('distribution_channel', models.CharField(max_length=20, null=True)),
                ('shipping_point_receiving_pt', models.CharField(max_length=20, null=True)),
                ('vendor', models.CharField(max_length=20, null=True)),
                ('customer', models.CharField(max_length=20, null=True)),
                ('business_system_of_mes', models.CharField(max_length=20, null=True)),
                ('inventory_management_type', models.CharField(max_length=20, null=True)),
                ('license_number', models.CharField(max_length=20, null=True)),
                ('in_transit_assignment', models.CharField(max_length=20, null=True)),
                ('tank_assgn', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SE16N_T024',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_number', models.IntegerField(null=True)),
                ('uploaded_by', models.IntegerField()),
                ('uploaded_at', models.DateTimeField()),
                ('purchasing_group', models.CharField(max_length=20, null=True)),
                ('description_p_group', models.CharField(max_length=20, null=True)),
                ('tel_no_purch_group', models.CharField(max_length=20, null=True)),
                ('output_device', models.CharField(max_length=20, null=True)),
                ('fax_number', models.CharField(max_length=20, null=True)),
                ('telephone', models.CharField(max_length=20, null=True)),
                ('extension', models.CharField(max_length=20, null=True)),
                ('e_mail_address', models.CharField(max_length=50, null=True)),
                ('user_name', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ZMM_CARNET_CDE_IS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_number', models.IntegerField(null=True)),
                ('uploaded_by', models.IntegerField(null=True)),
                ('uploaded_at', models.DateTimeField()),
                ('request_no', models.CharField(max_length=30, null=True)),
                ('plant', models.CharField(max_length=30, null=True)),
                ('storage_location', models.CharField(max_length=30, null=True)),
                ('purchase_document', models.CharField(max_length=30, null=True)),
                ('poste1', models.CharField(max_length=30, null=True)),
                ('due_date', models.CharField(max_length=20, null=True)),
                ('vendor', models.CharField(max_length=50, null=True)),
                ('vendor_name', models.CharField(max_length=50, null=True)),
                ('material', models.CharField(max_length=50, null=True)),
                ('designation_add_material', models.CharField(max_length=50, null=True)),
                ('name', models.CharField(max_length=50, null=True)),
                ('transmission_info', models.DateField(null=True)),
                ('validated_by', models.CharField(max_length=50, null=True)),
                ('priority', models.CharField(max_length=50, null=True)),
                ('quantity', models.FloatField(null=True)),
                ('quantity_to_receive', models.FloatField(null=True)),
                ('date_of_purchase', models.DateField(null=True)),
                ('desired_date', models.DateField(null=True)),
                ('original_delivery_date', models.DateField(null=True)),
                ('contractual_delivery_date', models.DateField(null=True)),
                ('validated_delivery_date', models.DateField(null=True)),
                ('confirmed_quantity', models.FloatField(null=True)),
                ('comment', models.CharField(max_length=500, null=True)),
                ('expected_stock_week_w', models.FloatField(null=True)),
                ('expected_stock_week_w_1', models.FloatField(null=True)),
                ('expected_stock_week_w_2', models.FloatField(null=True)),
                ('expected_stock_week_w_3', models.FloatField(null=True)),
                ('expected_stock_week_w_4', models.FloatField(null=True)),
                ('expected_stock_week_w_5', models.FloatField(null=True)),
                ('expected_stock_week_w_6', models.FloatField(null=True)),
                ('expected_stock_week_w_7', models.FloatField(null=True)),
                ('expected_stock_week_w_8', models.FloatField(null=True)),
                ('expected_stock_week_w_9', models.FloatField(null=True)),
                ('expected_stock_week_w_10', models.FloatField(null=True)),
                ('expected_stock_week_w_11', models.FloatField(null=True)),
                ('expected_stock_week_w_12', models.FloatField(null=True)),
                ('confirmation', models.CharField(max_length=30, null=True)),
                ('estimated_delivery_time', models.CharField(max_length=20, null=True)),
                ('comment_vendor', models.CharField(max_length=500, null=True)),
                ('element_otp', models.CharField(max_length=30, null=True)),
                ('business_document', models.CharField(max_length=10, null=True)),
                ('poste2', models.CharField(max_length=20, null=True)),
                ('need_number', models.CharField(max_length=30, null=True)),
                ('net_price', models.FloatField(null=True)),
                ('currency', models.CharField(max_length=10, null=True)),
                ('price_basis', models.CharField(max_length=20, null=True)),
                ('price_unit', models.CharField(max_length=10, null=True)),
                ('net_order_value', models.FloatField(null=True)),
                ('purchasing_document_type', models.CharField(max_length=10, null=True)),
                ('exception_message_number', models.CharField(max_length=20, null=True)),
                ('exception_message', models.CharField(max_length=50, null=True)),
                ('purchasing_group', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ZRPFLG13',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_number', models.IntegerField(null=True)),
                ('uploaded_by', models.IntegerField(null=True)),
                ('uploaded_at', models.DateTimeField(null=True)),
                ('period', models.FloatField(null=True)),
                ('plant', models.FloatField(null=True)),
                ('ctr_pft', models.CharField(max_length=10, null=True)),
                ('administrator', models.CharField(max_length=10, null=True)),
                ('tech_desc', models.CharField(max_length=10, null=True)),
                ('customer_grp', models.CharField(max_length=10, null=True)),
                ('material', models.CharField(max_length=10, null=True)),
                ('ty', models.CharField(max_length=10, null=True)),
                ('st', models.FloatField(null=True)),
                ('gv', models.CharField(max_length=10, null=True)),
                ('needs', models.CharField(max_length=30, null=True)),
                ('stock', models.FloatField(null=True)),
                ('consign_stock', models.FloatField(null=True)),
                ('lot_qm', models.FloatField(null=True)),
                ('of', models.FloatField(null=True)),
                ('cde', models.FloatField(null=True)),
                ('op', models.FloatField(null=True)),
                ('da', models.FloatField(null=True)),
                ('key', models.CharField(max_length=10, null=True)),
                ('fixed_lot', models.FloatField(null=True)),
                ('security', models.FloatField(null=True)),
                ('surpluses', models.FloatField(null=True)),
                ('valuation', models.FloatField(null=True)),
                ('time_limit_of_secu', models.FloatField(null=True)),
                ('pmp_ps', models.FloatField(null=True)),
                ('abc', models.CharField(max_length=10, null=True)),
                ('mini_lot', models.FloatField(null=True)),
                ('rounds', models.FloatField(null=True)),
                ('tps_recept', models.FloatField(null=True)),
                ('maxi_lot', models.FloatField(null=True)),
                ('storage_loc', models.FloatField(null=True)),
                ('desc_material', models.CharField(max_length=50, null=True)),
                ('curency', models.CharField(max_length=10, null=True)),
                ('material_type', models.CharField(max_length=10, null=True)),
                ('appro_spe', models.CharField(max_length=10, null=True)),
                ('vrac', models.CharField(max_length=10, null=True)),
                ('planif_type', models.CharField(max_length=10, null=True)),
                ('vendor1', models.CharField(max_length=10, null=True)),
                ('desc_vendor1', models.CharField(max_length=200, null=True)),
                ('vendor2', models.CharField(max_length=10, null=True)),
                ('desc_vendor2', models.CharField(max_length=20, null=True)),
                ('stock_in_transit', models.FloatField(null=True)),
                ('required_quantity_1000', models.FloatField(null=True)),
                ('required_quantity_1010', models.FloatField(null=True)),
                ('required_quantity_1900', models.FloatField(null=True)),
                ('required_quantity_3000', models.FloatField(null=True)),
                ('required_quantity_3100', models.FloatField(null=True)),
                ('required_quantity_4000', models.FloatField(null=True)),
                ('required_quantity_5000', models.FloatField(null=True)),
                ('decoupling_point', models.CharField(max_length=20, null=True)),
                ('vmi_stock', models.FloatField(null=True)),
                ('item_order', models.FloatField(null=True)),
                ('planif_device', models.CharField(max_length=10, null=True)),
            ],
        ),
    ]