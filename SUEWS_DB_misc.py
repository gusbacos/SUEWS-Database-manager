import pandas as pd

def read_db(db_path):
    # db_path = self.plugin_dir + '/database_copy.xlsx'  
    idx_col = 'ID'
    # Lod 0
    reg = pd.read_excel(db_path, sheet_name = 'Lod0_Region', index_col=  idx_col, engine = 'openpyxl')
    reg.name = 'Lod0_Region'
    # Lod 1
    Type = pd.read_excel(db_path, sheet_name = 'Lod1_Types', index_col=  idx_col, engine = 'openpyxl')
    Type.name = 'Lod1_Types'
    # Lod 2
    veg = pd.read_excel(db_path, sheet_name = 'Lod2_Veg', index_col = idx_col, engine = 'openpyxl')
    veg.name = 'Lod2_Veg'
    nonveg = pd.read_excel(db_path, sheet_name = 'Lod2_NonVeg', index_col = idx_col, engine = 'openpyxl')
    nonveg.name = 'Lod2_NonVeg'
    water = pd.read_excel(db_path, sheet_name = 'Lod2_Water', index_col = idx_col, engine = 'openpyxl')
    water.name = 'Lod2_Water'
    # Ref
    ref = pd.read_excel(db_path, sheet_name = 'References', index_col = idx_col, engine = 'openpyxl')
    ref.name = 'References'
    # Lod 3
    alb =  pd.read_excel(db_path, sheet_name = 'Lod3_Albedo', index_col = idx_col, engine = 'openpyxl')
    alb.name = 'Lod3_Albedo'
    em =  pd.read_excel(db_path, sheet_name = 'Lod3_Emissivity', index_col = idx_col, engine = 'openpyxl')
    em.name = 'Lod3_Emissivity'
    OHM =  pd.read_excel(db_path, sheet_name = 'Lod3_OHM', index_col = idx_col, engine = 'openpyxl') # Away from Veg
    OHM.name = 'Lod3_OHM'
    LAI =  pd.read_excel(db_path, sheet_name = 'Lod3_LAI', index_col = idx_col, engine = 'openpyxl')
    LAI.name = 'Lod3_OHM'
    st = pd.read_excel(db_path, sheet_name = 'Lod3_Storage', index_col = idx_col, engine = 'openpyxl')
    st.name = 'Lod3_Storage'
    cnd = pd.read_excel(db_path, sheet_name = 'Lod3_Conductance', index_col = idx_col, engine = 'openpyxl') # Away from Veg
    cnd.name = 'Lod3_Conductance'
    LGP = pd.read_excel(db_path, sheet_name = 'Lod3_LGP', index_col = idx_col, engine = 'openpyxl')
    LGP.name = 'Lod3_LGP'
    dr = pd.read_excel(db_path, sheet_name = 'Lod3_Drainage', index_col = idx_col, engine = 'openpyxl')
    dr.name = 'Lod3_Drainage'
    VG = pd.read_excel(db_path, sheet_name = 'Lod3_VegetationGrowth', index_col = idx_col, engine = 'openpyxl')
    VG.name = 'Lod3_VegetationGrowth'
    ANOHM = pd.read_excel(db_path, sheet_name = 'Lod3_ANOHM', index_col = idx_col, engine = 'openpyxl')
    ANOHM.name = 'Lod3_ANOHM'
    BIOCO2 = pd.read_excel(db_path, sheet_name = 'Lod3_BiogenCO2',index_col = idx_col, engine = 'openpyxl')
    BIOCO2.name = 'Lod3_BiogenCO2'
    MVCND = pd.read_excel(db_path, sheet_name= 'Lod3_MaxVegetationConductance', index_col = idx_col, engine = 'openpyxl')
    MVCND.name = 'Lod3_MaxVegetationConductance'
    por = pd.read_excel(db_path, sheet_name = 'Lod3_Porosity', index_col = idx_col, engine = 'openpyxl')
    por.name = 'Lod3_Porosity'
    snow = pd.read_excel(db_path, sheet_name = 'Lod3_Snow', index_col = idx_col, engine = 'openpyxl')
    snow.name = 'Lod3_Snow'
    AnEm = pd.read_excel(db_path, sheet_name = 'Lod3_AnthropogenicEmission',index_col = idx_col, engine = 'openpyxl')
    AnEm.name = 'Lod3_AnthropogenicEmission'
    prof = pd.read_excel(db_path, sheet_name= 'Lod3_Profiles', index_col = idx_col, engine = 'openpyxl')
    prof.name = 'Lod3_Profiles'
    ws = pd.read_excel(db_path, sheet_name = 'Lod3_WaterState', index_col = idx_col, engine = 'openpyxl')
    ws.name = 'Lod3_WaterState'
    soil = pd.read_excel(db_path, sheet_name = 'Lod3_Soil', index_col = idx_col, engine = 'openpyxl')
    soil.name = 'Lod3_Soil'
    ESTM = pd.read_excel(db_path, sheet_name = 'Lod3_ESTM', index_col = idx_col, engine = 'openpyxl')
    soil.name = 'Lod3_ESTM'
    irr = pd.read_excel(db_path, sheet_name= 'Lod3_Irrigation', index_col = idx_col, engine = 'openpyxl')
    irr.name = 'Lod3_Irrigation'

    return Type, veg, nonveg, water, ref, alb, em, OHM, LAI, st, cnd, LGP, dr, VG, ANOHM, BIOCO2, MVCND, por, reg, snow, AnEm, prof, ws, soil, ESTM, irr

def read_suews_db(self):

    # set path to our read the docs
    db_path = self.plugin_dir + '/SUEWS_db.xlsx'  
    idx_col = 'ID'
    # Lod 1
    suews_Type = pd.read_excel(db_path, sheet_name = 'Lod1_Types', index_col=  idx_col, engine = 'openpyxl')
    # Lod 2
    suews_veg = pd.read_excel(db_path, sheet_name = 'Lod2_Veg', index_col = idx_col, engine = 'openpyxl')
    suews_veg.name = 'Lod2_Veg'
    suews_nonveg = pd.read_excel(db_path, sheet_name = 'Lod2_NonVeg', index_col = idx_col, engine = 'openpyxl')
    suews_nonveg.name = 'Lod2_NonVeg'
    suews_water = pd.read_excel(db_path, sheet_name = 'Lod2_Water', index_col = idx_col, engine = 'openpyxl')
    suews_water.name = 'Lod2_Water'
    # Ref
    suews_ref = pd.read_excel(db_path, sheet_name = 'References', index_col = idx_col, engine = 'openpyxl')
    # Lod 3
    suews_alb =  pd.read_excel(db_path, sheet_name = 'Lod3_Albedo', index_col = idx_col, engine = 'openpyxl')
    suews_alb.name = 'Lod3_Albedo'
    suews_em =  pd.read_excel(db_path, sheet_name = 'Lod3_Emissivity', index_col = idx_col, engine = 'openpyxl')
    suews_em.name = 'Lod3_Emissivity'
    suews_OHM =  pd.read_excel(db_path, sheet_name = 'Lod3_OHM', index_col = idx_col, engine = 'openpyxl') # Away from Veg
    suews_OHM.name = 'Lod3_OHM'
    suews_LAI =  pd.read_excel(db_path, sheet_name = 'Lod3_LAI', index_col = idx_col, engine = 'openpyxl')
    suews_LAI.name = 'Lod3_OHM'
    suews_st = pd.read_excel(db_path, sheet_name = 'Lod3_Storage', index_col = idx_col, engine = 'openpyxl')
    suews_st.name = 'Lod3_Storage'
    suews_cnd = pd.read_excel(db_path, sheet_name = 'Lod3_Conductance', index_col = idx_col, engine = 'openpyxl') # Away from Veg
    suews_cnd.name = 'Lod3_Conductance'
    suews_LGP = pd.read_excel(db_path, sheet_name = 'Lod3_LGP', index_col = idx_col, engine = 'openpyxl')
    suews_LGP.name = 'Lod3_LGP'
    suews_dr = pd.read_excel(db_path, sheet_name = 'Lod3_Drainage', index_col = idx_col, engine = 'openpyxl')
    suews_dr.name = 'Lod3_Drainage'
    suews_VG = pd.read_excel(db_path, sheet_name = 'Lod3_VegetationGrowth', index_col = idx_col, engine = 'openpyxl')
    suews_VG.name = 'Lod3_VegetationGrowth'
    suews_ANOHM = pd.read_excel(db_path, sheet_name = 'Lod3_ANOHM', index_col = idx_col, engine = 'openpyxl')
    suews_ANOHM.name = 'Lod3_ANOHM'
    suews_BIOCO2 = pd.read_excel(db_path, sheet_name = 'Lod3_BiogenCO2',index_col = idx_col, engine = 'openpyxl')
    suews_BIOCO2.name = 'Lod3_BiogenCO2'
    suews_MVCND = pd.read_excel(db_path, sheet_name= 'Lod3_MaxVegetationConductance', index_col = idx_col, engine = 'openpyxl')
    suews_MVCND.name = 'Lod3_MaxVegetationConductance'
    suews_por = pd.read_excel(db_path, sheet_name = 'Lod3_Porosity', index_col = idx_col, engine = 'openpyxl')
    suews_por.name = 'Lod3_Porosity'
    
    return suews_Type, suews_veg, suews_nonveg, suews_water, suews_ref, suews_alb, suews_em, suews_OHM, suews_LAI, suews_st, suews_cnd, suews_LGP, suews_dr,suews_VG, suews_ANOHM, suews_BIOCO2, suews_MVCND, suews_por

def write_to_db(self,Type, veg, nonveg, water, ref, alb, em, OHM, LAI, st, cnd, LGP, dr, VG, ANOHM, BIOCO2, MVCND, por, reg, snow, AnEm, prof, ws, soil, ESTM, irr):

        db_path = self.plugin_dir + '/database_copy.xlsx'  
        writer = pd.ExcelWriter(db_path)

        reg.to_excel(writer, sheet_name = 'Lod0_Region')
        Type.to_excel(writer, sheet_name = 'Lod1_Types')
        veg.to_excel(writer, sheet_name = 'Lod2_Veg')
        nonveg.to_excel(writer, sheet_name = 'Lod2_NonVeg')
        water.to_excel(writer, sheet_name = 'Lod2_Water')
        ref.to_excel(writer, sheet_name = 'References')
        alb.to_excel(writer, sheet_name = 'Lod3_Albedo')
        em.to_excel(writer, sheet_name = 'Lod3_Emissivity')
        OHM.to_excel(writer, sheet_name = 'Lod3_OHM')
        LAI.to_excel(writer, sheet_name = 'Lod3_LAI')
        st.to_excel(writer, sheet_name = 'Lod3_Storage')
        cnd.to_excel(writer, sheet_name = 'Lod3_Conductance')
        LGP.to_excel(writer, sheet_name = 'Lod3_LGP')
        dr.to_excel(writer, sheet_name = 'Lod3_Drainage')
        VG.to_excel(writer, sheet_name = 'Lod3_VegetationGrowth')
        ANOHM.to_excel(writer, sheet_name = 'Lod3_ANOHM')
        BIOCO2.to_excel(writer, sheet_name = 'Lod3_BiogenCO2')
        MVCND.to_excel(writer, sheet_name = 'Lod3_MaxVegetationConductance')
        por.to_excel(writer, sheet_name = 'Lod3_Porosity')
        snow.to_excel(writer, sheet_name = 'Lod3_Snow')
        AnEm.to_excel(writer, sheet_name = 'Lod3_AnthropogenicEmission')
        prof.to_excel(writer, sheet_name = 'Lod3_Profiles')
        ws.to_excel(writer, sheet_name = 'Lod3_WaterState')
        soil.to_excel(writer, sheet_name = 'Lod3_Soil')
        ESTM.to_excel(writer, sheet_name = 'Lod3_ESTM')
        irr.to_excel(writer, sheet_name = 'Lod3_Irrigation')

        writer.save()