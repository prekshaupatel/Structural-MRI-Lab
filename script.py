import os
import sys
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

from os import path

default_download_directory = "/Users/prekshapatel/Downloads"
log = open('log.txt', 'w')
output_csv = open('output.csv', 'w')

def process_voi_csv(path_to_upload_file):
    f = open(path.join(default_download_directory, "voidata.csv"), 'r')
    data = [i.split(',') for i in f.read().splitlines()]
    n_data = ','.join([path_to_upload_file, data[1][1], data[1][2]])
    return n_data


def process_request(path_to_upload_file, path_to_output_directory):                    
    # STEP 1

    # using Chrome to access web
    driver = webdriver.Chrome(ChromeDriverManager().install())

    # go to BioImage Suite Web’s Orthogonal Viewer Tool
    browser = driver.get("https://bioimagesuiteweb.github.io/webapp/viewer.html")
    time.sleep(10)

    # close extra tab
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[3]/button[1]').click()
    time.sleep(1)

    # STEP 2

    # navigate the page
    find_button = driver.find_element_by_xpath('//*[@id="bismenuparent"]/li[1]/a')
    find_button.click()
    time.sleep(1)

    load_data_button = driver.find_element_by_xpath('//*[@id="bismenuparent"]/li[1]/ul/li[1]/a')
    load_data_button.click()
    time.sleep(1)

    file_upload = driver.find_element_by_xpath('//input[@type=\"file\"]')
    file_upload.send_keys(path_to_upload_file)
    time.sleep(1)

    # STEP 3

    segmentation_tab = driver.find_element_by_xpath('//*[@id="bismenuparent"]/li[5]/a')
    segmentation_tab.click()
    time.sleep(1)

    segment_image_tab = driver.find_element_by_xpath('//*[@id="bismenuparent"]/li[5]/ul/li[3]/a')
    segment_image_tab.click()
    time.sleep(1)

    segment = driver.find_element_by_xpath('/html/body/div/bisweb-viewerlayoutelement/div[3]/div[2]/div[2]/div[2]/div[2]/div/div/div/div[2]/button[1]')
    segment.click()
    time.sleep(1)

    edit_tab = driver.find_element_by_xpath('//*[@id="bismenuparent"]/li[3]/a')
    try:
        edit_tab.click()
    except:
        print("path to upload file (%s) is not valid" % path_to_upload_file)
        log.write("FAILED: '%s,%s'\n\t(path to upload file (%s) is not valid)\n" % (path_to_upload_file, path_to_output_directory, path_to_upload_file))
        driver.close()
        return
    time.sleep(1)

    copy_viewer_tab = driver.find_element_by_xpath('//*[@id="bismenuparent"]/li[3]/ul/li[1]/a')
    copy_viewer_tab.click()
    time.sleep(1)

    # STEP 4

    browser_2 = driver.get('https://bioimagesuiteweb.github.io/webapp/editor.html')
    time.sleep(1)

    # close extra tab
    driver.find_element_by_xpath('//*[@id="B_8"]/div/div/div/div[3]/button[1]').click()
    time.sleep(1)

    edit_tab = driver.find_element_by_xpath('//*[@id="bismenuparent"]/li[3]/a')
    edit_tab.click()
    time.sleep(1)

    paste_viewer_tab = driver.find_element_by_xpath('//*[@id="bismenuparent"]/li[3]/ul/li[2]/a')
    paste_viewer_tab.click()
    time.sleep(1)

    # STEP 5

    view_snapshot_tab = driver.find_element_by_xpath('//*[@id="headingB_4"]/h4/a')
    view_snapshot_tab.click()
    time.sleep(5)

    viewer_snapshot_tab = driver.find_element_by_xpath('//*[@id="contentsB_4"]/div/div/div/div/form/div[2]/button')
    viewer_snapshot_tab.click()
    time.sleep(10)

    save_to_file = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button')
    save_to_file.click()
    time.sleep(1)

    # STEP 6

    objectmap_tab = driver.find_element_by_xpath('//*[@id="bismenuparent"]/li[2]/a')
    objectmap_tab.click()
    time.sleep(5)

    voi_analysis = driver.find_element_by_xpath('//*[@id="bismenuparent"]/li[2]/ul/li[6]/a')
    voi_analysis.click()
    time.sleep(5)

    plot_voi_volumes = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/div/button[4]')
    plot_voi_volumes.click()
    time.sleep(1)

    # STEP 7

    export_csv = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/div/button[5]')
    export_csv.click()
    time.sleep(10)

    # close the browser
    driver.close()

    output_csv.write(process_voi_csv(path_to_upload_file)+'\n')
    os.rename(path.join(default_download_directory, 'voidata.csv'), path.join(path_to_output_directory, 'voidata.csv'))
    os.rename(path.join(default_download_directory, 'snapshot.png'), path.join(path_to_output_directory, 'snapshot.png'))

    print("SUCCESS: '%s,%s'" % (path_to_upload_file, path_to_output_directory))
    log.write("SUCCESS: '%s,%s'\n" % (path_to_upload_file, path_to_output_directory))

    
def main():
    # check for one argument
    if len(sys.argv) < 2:
        print("Please enter name of .csv file as an argument\n\tUSAGE: python3 script.py [input.csv]")
        log.write("ERROR: Please enter name of .csv file as an argument\n\tUSAGE: python3 script.py [input.csv]\n")
        exit(1)

    # check if default downloads folder had voidata.csv or snapshot.png
    if path.isfile(path.join(default_download_directory, 'voidata.csv')):
        print ("Please remove %s" % path.join(default_download_directory, 'voidata.csv'))
        log.write("ERROR: Please remove %s\n" % path.join(default_download_directory, 'voidata.csv'))
        exit(1)
    if path.isfile(path.join(default_download_directory, 'snapshot.png')):
        print ("Please remove %s" % path.join(default_download_directory, 'snapshot.png'))
        log.write("ERROR: Please remove %s\n" % path.join(default_download_directory, 'snapshot.png'))
        exit(1)
        
    output_csv.write(",Gray_Matter,White_Matter\n")
    f = open(sys.argv[1], 'r')
    data = [i.split(',') for i in f.read().splitlines() if (i != "")]

    for line in data:
        if len(line) != 2:
            log.write("FAILED: '" + ",".join(line) + "'\n\t(line should contain only two values: input_file_path, output_directory_path)\n")
            continue
        if not path.exists(line[1]):
            os.makedirs(line[1])
        elif not path.isdir(line[1]):
            log.write("FAILED: '%s,%s'\n\t(unable to create directory %s, file with path already exists)\n"%(line[0], line[1], line[1]))
            continue
        process_request(line[0], line[1])

main()
