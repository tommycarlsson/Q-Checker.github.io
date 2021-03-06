import json


config_data = {
  'dz_aprx': r'C:/QAQC_contract/nantucket/nantucket_qaqc_arcpro_project/nantucket_qaqc_arcpro_project.aprx',
  'mosaics_to_make': {
    'Hillshade': [ False, 'C:/QAQC_contract/nantucket/qaqc_nantucket.gdb' ],
    'Dz': [ False, 'C:/QAQC_contract/nantucket/qaqc_nantucket.gdb' ]
  },
  'project_name': 'select a project',
  'check_keys': {
    'gps_time': 'Satellite GPS Time',
    'pdrf': '3',
    'version': '1.4',
    'hdatum': 'NAD_1983_2011_UTM_Zone_19N',
    'naming': 'yyyy_[easting]e_[northing]n_las',
    'exp_cls': '07,28,27,26,25,01',
    'vdatum': 'Ellipsoid (Meters)',
    'pt_src_ids': 'Verify Unique Flight Line IDs'
  },
  'surfaces_to_make': {
    'Hillshade': [ False, 'C:/QAQC_contract/nantucket/hillshade' ],
    'Dz': [ False, 'C:/QAQC_contract/nantucket/dz' ]
  },
  'qaqc_dir': 'C:\\QAQC_contract',
  'dz_export_settings': 'Z:\\QChecker\\QChecker_GITHUB\\assets\\config_files\\dz_export_settings.xml',
  'make_contact_centroids': False,
  'checks_to_do': {
    'gps_time': True,
    'pdrf': True,
    'version': True,
    'hdatum': True,
    'naming': True,
    'exp_cls': True,
    'vdatum': False,
    'pt_src_ids': True
  },
  'las_tile_dir': 'C:\\QAQC_contract\\nantucket\\CLASSIFIED_LAS',
  'qaqc_gdb': 'C:\\QAQC_contract\\nantucket\\qaqc_nantucket.gdb',
  'dz_classes_template': 'C:\\QAQC_contract\\dz_classes.lyr',
  'to_pyramid': True,
  'make_tile_centroids_shp': True
  'tile_size': '500',
  'contractor_shp': 'C:\\QAQC_contract\\nantucket\\EXTENTS\\final\\Nantucket_TileGrid.shp',
  'supp_las_domain': 'Topo-Bathy Lidar Domain Profile',
  'epsg_json': 'Z:\QChecker\QChecker_GITHUB\epsg_lut.json',
  'lp360_ldexport_exe': r'C:\Program Files\Common Files\LP360\LDExport.exe',
  'las_classes_json': r'.\assets\config_files\las_classes.json',
  'qchecker_icon':  r'.\assets\images\qaqc.ico',
  'qchecker_splash_image': r'.\assets\images\SplashScreen.gif',
  'project_list': r'.\assets\project_list.txt',
  'srs_wkts': r'.\assets\wkts_NAD83_2011_UTM.csv',  
}

with open(r'Z:\QChecker\QChecker_GITHUB\assets\config_files\qaqc_config.json', 'w') as f:
    json.dump(config_data, f)
