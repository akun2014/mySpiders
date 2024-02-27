from lxml import etree

data1 = """
<div class="block-content expand-content block-expanded">
                <div class="tab-cnt">                    <strong>Description:</strong><br><div>	<strong>Material: chrome vanadium alloy steel</strong></div><div>	<strong>Length: 200 mm</strong></div><div>	<strong>Opening expand: 0-44mm</strong></div><div>	<strong>Color: blue, silver</strong></div><div>	<strong>Weight: 450g</strong></div><br><strong>Features:</strong><br><div>	<strong>Made of Chrome Vanadium Steel material,durable and solid,never rust.</strong></div><div>	<strong>Mirror polished,Fixed head ratchet spanner.</strong></div><div>	<strong>This spanner for the professional or the home mechanic.</strong></div><div>	<strong>Ideal for applications where space is limited.</strong></div><br><strong>Package Included:<br>1pcs 0-44mm&nbsp;Spanner<br><br>More Details: </strong><br><br><br><img src="image/catalog/Wrenches/0-44mm-Metric-Chromium-Vanadium-Steel-Multi-function-Spanner-Wrench-1107781-descriptionImage0.jpg" alt="0-44mm-Metric-Chromium-Vanadium-Steel-Multi-function-Spanner-Wrench-1107781"><br><br><img src="image/catalog/Wrenches/0-44mm-Metric-Chromium-Vanadium-Steel-Multi-function-Spanner-Wrench-1107781-descriptionImage1.jpg" alt="0-44mm-Metric-Chromium-Vanadium-Steel-Multi-function-Spanner-Wrench-1107781"><br><br><img src="image/catalog/Wrenches/0-44mm-Metric-Chromium-Vanadium-Steel-Multi-function-Spanner-Wrench-1107781-descriptionImage2.jpg" alt="0-44mm-Metric-Chromium-Vanadium-Steel-Multi-function-Spanner-Wrench-1107781"><br><br><img src="image/catalog/Wrenches/0-44mm-Metric-Chromium-Vanadium-Steel-Multi-function-Spanner-Wrench-1107781-descriptionImage3.jpg" alt="0-44mm-Metric-Chromium-Vanadium-Steel-Multi-function-Spanner-Wrench-1107781"><br><br><img src="image/catalog/Wrenches/0-44mm-Metric-Chromium-Vanadium-Steel-Multi-function-Spanner-Wrench-1107781-descriptionImage4.jpg" alt="0-44mm-Metric-Chromium-Vanadium-Steel-Multi-function-Spanner-Wrench-1107781"><br><br><img src="image/catalog/Wrenches/0-44mm-Metric-Chromium-Vanadium-Steel-Multi-function-Spanner-Wrench-1107781-descriptionImage5.jpg" alt="0-44mm-Metric-Chromium-Vanadium-Steel-Multi-function-Spanner-Wrench-1107781"><br><br><img src="image/catalog/Wrenches/0-44mm-Metric-Chromium-Vanadium-Steel-Multi-function-Spanner-Wrench-1107781-descriptionImage6.jpg" alt="0-44mm-Metric-Chromium-Vanadium-Steel-Multi-function-Spanner-Wrench-1107781"><br><br><img src="image/catalog/Wrenches/0-44mm-Metric-Chromium-Vanadium-Steel-Multi-function-Spanner-Wrench-1107781-descriptionImage7.jpg" alt="0-44mm-Metric-Chromium-Vanadium-Steel-Multi-function-Spanner-Wrench-1107781"><br><br><img src="image/catalog/Wrenches/0-44mm-Metric-Chromium-Vanadium-Steel-Multi-function-Spanner-Wrench-1107781-descriptionImage8.jpg" alt="0-44mm-Metric-Chromium-Vanadium-Steel-Multi-function-Spanner-Wrench-1107781"><br><img src="image/catalog/Wrenches/0-44mm-Metric-Chromium-Vanadium-Steel-Multi-function-Spanner-Wrench-1107781-descriptionImage9.jpg" alt="0-44mm-Metric-Chromium-Vanadium-Steel-Multi-function-Spanner-Wrench-1107781"><br><br><div id="imgBox">    </div>                </div>
                                  <div class="block-expand-overlay"><a class="block-expand btn"></a></div>
                              </div>
        """

data2 = """
<div class="block-content expand-content block-expanded">
                <div>	<strong><span style="font-size: 16px;">Features:</span></strong></div><div>	&nbsp;</div><div>	<span style="font-size: 14px;">High hardness, no damage to the screen, not easy to pull off, no rust.<br>	Length: 150m<br>	Type:&nbsp;0.035mm</span></div><div>	&nbsp;</div><div>	<strong><span style="font-size: 16px;">Package included:</span></strong><br><br><span style="font-size: 14px;">1 x Wire</span></div><div>	&nbsp;</div><div>	<strong><span style="font-size: 16px;">Details pictures:</span></strong></div><br><div id="imgBox">            <br><div style="text-align: center;">	<img alt="0035mm-150m-Tungsten-Alloy-Steel-Wire-LCD-Separation-Line-Repair-Tool-for-Mobile-Screen-1546789" src="image/catalog/Prying-Opening-Tools/0035mm-150m-Tungsten-Alloy-Steel-Wire-LCD-Separation-Line-Repair-Tool-for-Mobile-Screen-1546789-descriptionImage0.jpeg"></div><br><div style="text-align: center;">	<img alt="0035mm-150m-Tungsten-Alloy-Steel-Wire-LCD-Separation-Line-Repair-Tool-for-Mobile-Screen-1546789" src="image/catalog/Prying-Opening-Tools/0035mm-150m-Tungsten-Alloy-Steel-Wire-LCD-Separation-Line-Repair-Tool-for-Mobile-Screen-1546789-descriptionImage1.jpeg"></div><br><div style="text-align: center;">	<img alt="0035mm-150m-Tungsten-Alloy-Steel-Wire-LCD-Separation-Line-Repair-Tool-for-Mobile-Screen-1546789" src="image/catalog/Prying-Opening-Tools/0035mm-150m-Tungsten-Alloy-Steel-Wire-LCD-Separation-Line-Repair-Tool-for-Mobile-Screen-1546789-descriptionImage2.jpeg"></div><br><div style="text-align: center;">	<img alt="0035mm-150m-Tungsten-Alloy-Steel-Wire-LCD-Separation-Line-Repair-Tool-for-Mobile-Screen-1546789" src="image/catalog/Prying-Opening-Tools/0035mm-150m-Tungsten-Alloy-Steel-Wire-LCD-Separation-Line-Repair-Tool-for-Mobile-Screen-1546789-descriptionImage3.jpeg"></div><br><div style="text-align: center;">	<img alt="0035mm-150m-Tungsten-Alloy-Steel-Wire-LCD-Separation-Line-Repair-Tool-for-Mobile-Screen-1546789" src="image/catalog/Prying-Opening-Tools/0035mm-150m-Tungsten-Alloy-Steel-Wire-LCD-Separation-Line-Repair-Tool-for-Mobile-Screen-1546789-descriptionImage4.jpeg"></div><br><div style="text-align: center;">	<img alt="0035mm-150m-Tungsten-Alloy-Steel-Wire-LCD-Separation-Line-Repair-Tool-for-Mobile-Screen-1546789" src="image/catalog/Prying-Opening-Tools/0035mm-150m-Tungsten-Alloy-Steel-Wire-LCD-Separation-Line-Repair-Tool-for-Mobile-Screen-1546789-descriptionImage5.jpeg"></div><br><div style="text-align: center;">	<img alt="0035mm-150m-Tungsten-Alloy-Steel-Wire-LCD-Separation-Line-Repair-Tool-for-Mobile-Screen-1546789" src="image/catalog/Prying-Opening-Tools/0035mm-150m-Tungsten-Alloy-Steel-Wire-LCD-Separation-Line-Repair-Tool-for-Mobile-Screen-1546789-descriptionImage6.jpeg"></div><br><div style="text-align: center;">	<img alt="0035mm-150m-Tungsten-Alloy-Steel-Wire-LCD-Separation-Line-Repair-Tool-for-Mobile-Screen-1546789" src="image/catalog/Prying-Opening-Tools/0035mm-150m-Tungsten-Alloy-Steel-Wire-LCD-Separation-Line-Repair-Tool-for-Mobile-Screen-1546789-descriptionImage7.jpeg"></div><br></div>
                                  <div class="block-expand-overlay"><a class="block-expand btn"></a></div>
                              </div>
"""

data3 = """
<div class="block-content expand-content block-expanded">
                <div>	<strong><span style="font-size: 16px;">Features:</span></strong><br><br><div>		<span style="font-size: 14px;">Fine silver flying wire, wire diameter as fine as hair, automatic placement of filling points, tin-silver alloy composition.</span></div>	<div>		<span style="font-size: 14px;">Solve the main board screw hole short line, CPU chip breakpoint break line.</span></div></div><div>	&nbsp;</div><div>	<strong><span style="font-size: 16px;">Specification:</span></strong><br><br><span style="font-size: 14px;">Size: 5000 x 0.02mm</span></div><div>	&nbsp;</div><div>	<strong><span style="font-size: 16px;">Package included:</span></strong><br><br><span style="font-size: 14px;">1 x Flying Line</span></div><div>	&nbsp;</div><div>	<strong><span style="font-size: 16px;">Details pictures:</span></strong></div><br><div id="imgBox">            <br><div style="text-align: center;">	<img alt="002mm-Fine-Maintenance-Connecting-Line-Flying-Line-for-Phone-Fingerprint-Repair-Line-1441797" src="image/catalog/Precise-BGA-Rework-Tools/002mm-Fine-Maintenance-Connecting-Line-Flying-Line-for-Phone-Fingerprint-Repair-Line-1441797-descriptionImage0.jpeg"></div><br><div style="text-align: center;">	<img alt="002mm-Fine-Maintenance-Connecting-Line-Flying-Line-for-Phone-Fingerprint-Repair-Line-1441797" src="image/catalog/Precise-BGA-Rework-Tools/002mm-Fine-Maintenance-Connecting-Line-Flying-Line-for-Phone-Fingerprint-Repair-Line-1441797-descriptionImage1.jpeg"></div><br><div style="text-align: center;">	<img alt="002mm-Fine-Maintenance-Connecting-Line-Flying-Line-for-Phone-Fingerprint-Repair-Line-1441797" src="image/catalog/Precise-BGA-Rework-Tools/002mm-Fine-Maintenance-Connecting-Line-Flying-Line-for-Phone-Fingerprint-Repair-Line-1441797-descriptionImage2.jpeg"></div><br><div style="text-align: center;">	<img alt="002mm-Fine-Maintenance-Connecting-Line-Flying-Line-for-Phone-Fingerprint-Repair-Line-1441797" src="image/catalog/Precise-BGA-Rework-Tools/002mm-Fine-Maintenance-Connecting-Line-Flying-Line-for-Phone-Fingerprint-Repair-Line-1441797-descriptionImage3.jpeg"></div><br><div style="text-align: center;">	<img alt="002mm-Fine-Maintenance-Connecting-Line-Flying-Line-for-Phone-Fingerprint-Repair-Line-1441797" src="image/catalog/Precise-BGA-Rework-Tools/002mm-Fine-Maintenance-Connecting-Line-Flying-Line-for-Phone-Fingerprint-Repair-Line-1441797-descriptionImage4.jpeg"></div><br><div style="text-align: center;">	<img alt="002mm-Fine-Maintenance-Connecting-Line-Flying-Line-for-Phone-Fingerprint-Repair-Line-1441797" src="image/catalog/Precise-BGA-Rework-Tools/002mm-Fine-Maintenance-Connecting-Line-Flying-Line-for-Phone-Fingerprint-Repair-Line-1441797-descriptionImage5.jpeg"></div><br><div style="text-align: center;">	<img alt="002mm-Fine-Maintenance-Connecting-Line-Flying-Line-for-Phone-Fingerprint-Repair-Line-1441797" src="image/catalog/Precise-BGA-Rework-Tools/002mm-Fine-Maintenance-Connecting-Line-Flying-Line-for-Phone-Fingerprint-Repair-Line-1441797-descriptionImage6.jpeg"></div><br><div style="text-align: center;">	<img alt="002mm-Fine-Maintenance-Connecting-Line-Flying-Line-for-Phone-Fingerprint-Repair-Line-1441797" src="image/catalog/Precise-BGA-Rework-Tools/002mm-Fine-Maintenance-Connecting-Line-Flying-Line-for-Phone-Fingerprint-Repair-Line-1441797-descriptionImage7.jpeg"></div><br><div style="text-align: center;">	<img alt="002mm-Fine-Maintenance-Connecting-Line-Flying-Line-for-Phone-Fingerprint-Repair-Line-1441797" src="image/catalog/Precise-BGA-Rework-Tools/002mm-Fine-Maintenance-Connecting-Line-Flying-Line-for-Phone-Fingerprint-Repair-Line-1441797-descriptionImage8.jpeg"></div><br></div>
                                  <div class="block-expand-overlay"><a class="block-expand btn"></a></div>
                              </div>
"""

data4 = """
<div class="block-content expand-content block-expanded">
                <div class="tab-cnt">                    <div>	<strong>Description:</strong></div><div>	<strong>0.6-6.5mm Drill Chuck Drill Adapter 3/8-24UNF Changed Impact Wrench Into Eletric Drill</strong></div><div>	&nbsp;</div><div>	<strong>Specification:</strong></div><div>	Clamping Range: 0.6-6.5mm</div><div>	Thread: 3/8-24 UNF</div><div>	<strong>Quantity: 5pcs/set</strong></div><div>	10mm electric wrench conversion head +</div><div>	10mm hex post +</div><div>	10mm round handle post +</div><div>	6.5mm manual chuck (with wrench)</div><div>	&nbsp;</div><div>	<strong>Features:</strong></div><div>	- Changed Impact Wrench Into Eletric Drill</div><div>	- High precision screw thread and tapered hole.</div><div>	- Strong impact resistance.</div><div>	- The shank with screw can be tight and flex for you.&nbsp;&nbsp;</div><div>	- For milling machine, lathe, drilling machine, wood working machine.</div><div>	&nbsp;</div><div>	<strong>Package Included:</strong></div><div>	<strong>1 set x Drill Chuck Adapter</strong></div><div>	&nbsp;</div><div>	<strong>More Details:&nbsp;</strong></div><br><div id="imgBox">            <br><br><img src="image/catalog/Woodworking-and-Handmade-Tools/Drillpro-06-65mm-Drill-Chuck-Drill-Adapter-Thread-38-24UNF-Changed-Impact-Wrench-Into-Eletric-Drill-1597106-descriptionImage0.jpg" alt="Drillpro-06-65mm-Drill-Chuck-Drill-Adapter-Thread-38-24UNF-Changed-Impact-Wrench-Into-Eletric-Drill-1597106"><br><br><img src="image/catalog/Woodworking-and-Handmade-Tools/Drillpro-06-65mm-Drill-Chuck-Drill-Adapter-Thread-38-24UNF-Changed-Impact-Wrench-Into-Eletric-Drill-1597106-descriptionImage1.jpg" alt="Drillpro-06-65mm-Drill-Chuck-Drill-Adapter-Thread-38-24UNF-Changed-Impact-Wrench-Into-Eletric-Drill-1597106"><br><br><img src="image/catalog/Woodworking-and-Handmade-Tools/Drillpro-06-65mm-Drill-Chuck-Drill-Adapter-Thread-38-24UNF-Changed-Impact-Wrench-Into-Eletric-Drill-1597106-descriptionImage2.jpg" alt="Drillpro-06-65mm-Drill-Chuck-Drill-Adapter-Thread-38-24UNF-Changed-Impact-Wrench-Into-Eletric-Drill-1597106"><br><br><img src="image/catalog/Woodworking-and-Handmade-Tools/Drillpro-06-65mm-Drill-Chuck-Drill-Adapter-Thread-38-24UNF-Changed-Impact-Wrench-Into-Eletric-Drill-1597106-descriptionImage3.jpg" alt="Drillpro-06-65mm-Drill-Chuck-Drill-Adapter-Thread-38-24UNF-Changed-Impact-Wrench-Into-Eletric-Drill-1597106"><br><br><img src="image/catalog/Woodworking-and-Handmade-Tools/Drillpro-06-65mm-Drill-Chuck-Drill-Adapter-Thread-38-24UNF-Changed-Impact-Wrench-Into-Eletric-Drill-1597106-descriptionImage4.jpg" alt="Drillpro-06-65mm-Drill-Chuck-Drill-Adapter-Thread-38-24UNF-Changed-Impact-Wrench-Into-Eletric-Drill-1597106"><br><br><img src="image/catalog/Woodworking-and-Handmade-Tools/Drillpro-06-65mm-Drill-Chuck-Drill-Adapter-Thread-38-24UNF-Changed-Impact-Wrench-Into-Eletric-Drill-1597106-descriptionImage5.jpg" alt="Drillpro-06-65mm-Drill-Chuck-Drill-Adapter-Thread-38-24UNF-Changed-Impact-Wrench-Into-Eletric-Drill-1597106"><br><br><img src="image/catalog/Woodworking-and-Handmade-Tools/Drillpro-06-65mm-Drill-Chuck-Drill-Adapter-Thread-38-24UNF-Changed-Impact-Wrench-Into-Eletric-Drill-1597106-descriptionImage6.jpg" alt="Drillpro-06-65mm-Drill-Chuck-Drill-Adapter-Thread-38-24UNF-Changed-Impact-Wrench-Into-Eletric-Drill-1597106"><br><br><img src="image/catalog/Woodworking-and-Handmade-Tools/Drillpro-06-65mm-Drill-Chuck-Drill-Adapter-Thread-38-24UNF-Changed-Impact-Wrench-Into-Eletric-Drill-1597106-descriptionImage7.jpg" alt="Drillpro-06-65mm-Drill-Chuck-Drill-Adapter-Thread-38-24UNF-Changed-Impact-Wrench-Into-Eletric-Drill-1597106"><br><br><img src="image/catalog/Woodworking-and-Handmade-Tools/Drillpro-06-65mm-Drill-Chuck-Drill-Adapter-Thread-38-24UNF-Changed-Impact-Wrench-Into-Eletric-Drill-1597106-descriptionImage8.jpg" alt="Drillpro-06-65mm-Drill-Chuck-Drill-Adapter-Thread-38-24UNF-Changed-Impact-Wrench-Into-Eletric-Drill-1597106"><br><br><img src="image/catalog/Woodworking-and-Handmade-Tools/Drillpro-06-65mm-Drill-Chuck-Drill-Adapter-Thread-38-24UNF-Changed-Impact-Wrench-Into-Eletric-Drill-1597106-descriptionImage9.jpg" alt="Drillpro-06-65mm-Drill-Chuck-Drill-Adapter-Thread-38-24UNF-Changed-Impact-Wrench-Into-Eletric-Drill-1597106"><br></div>                </div>
                                  <div class="block-expand-overlay"><a class="block-expand btn"></a></div>
                              </div>
"""

data5 = """
<div class="block-content expand-content block-expanded">
                <div class="tab-cnt">                    <span style="font-size:14px;"><span style="font-size:16px;">Description:</span><br>0-10cm ABS Black Universal Pitch Gauge is suitable for most models like<br>Esky Belt CP V2 KING 3 Replace EK1-0348<br><br><span style="font-size:16px;">Specification:</span><br>Material:ABS<br>Size:14cm x 4.8cm<br>Color:Black<br>Weight:About 25g<br><br><span style="font-size:16px;">Features:</span><br>1.Simple pitch gauge to set main blade angles on your RC helicopter<br>2.Be suitable for most blade sizes in the range 400-600 series, e.g. E,sky HB king 2,<br>&nbsp;&nbsp; Belt-CP, CP2 Eflite Blade 400 Walkera&nbsp; 22 36 60 etc.<br>3.Along with blade tracking and balancing, correct pitch will ensure good lift and keep<br>&nbsp;&nbsp; your helicopter running sweetly.<br>4.Automatic spring slide clip attaches to blade leaving hands free to make adjustments.<br><br><span style="font-size:16px;">Package Include:</span><br>1 x Pitch Gauge</span><br><br><br><div style="text-align: center;">	<img src="image/catalog/Woodworking-and-Handmade-Tools/0-10cm-ABS-Black-Universal-Pitch-Gauge-For-Esky-Belt-CP-V2-KING-3-Replace-EK1-0348-1110257-descriptionImage0.jpg" alt="0-10cm-ABS-Black-Universal-Pitch-Gauge-For-Esky-Belt-CP-V2-KING-3-Replace-EK1-0348-1110257"><br><br><div style="text-align: center;">		<img src="image/catalog/Woodworking-and-Handmade-Tools/0-10cm-ABS-Black-Universal-Pitch-Gauge-For-Esky-Belt-CP-V2-KING-3-Replace-EK1-0348-1110257-descriptionImage1.jpg" alt="0-10cm-ABS-Black-Universal-Pitch-Gauge-For-Esky-Belt-CP-V2-KING-3-Replace-EK1-0348-1110257"><br><br><div style="text-align: center;">			<img src="image/catalog/Woodworking-and-Handmade-Tools/0-10cm-ABS-Black-Universal-Pitch-Gauge-For-Esky-Belt-CP-V2-KING-3-Replace-EK1-0348-1110257-descriptionImage2.jpg" alt="0-10cm-ABS-Black-Universal-Pitch-Gauge-For-Esky-Belt-CP-V2-KING-3-Replace-EK1-0348-1110257"><br><br><div style="text-align: center;">				<img src="image/catalog/Woodworking-and-Handmade-Tools/0-10cm-ABS-Black-Universal-Pitch-Gauge-For-Esky-Belt-CP-V2-KING-3-Replace-EK1-0348-1110257-descriptionImage3.jpg" alt="0-10cm-ABS-Black-Universal-Pitch-Gauge-For-Esky-Belt-CP-V2-KING-3-Replace-EK1-0348-1110257"><br><br><div style="text-align: center;">					<img src="image/catalog/Woodworking-and-Handmade-Tools/0-10cm-ABS-Black-Universal-Pitch-Gauge-For-Esky-Belt-CP-V2-KING-3-Replace-EK1-0348-1110257-descriptionImage4.jpg" alt="0-10cm-ABS-Black-Universal-Pitch-Gauge-For-Esky-Belt-CP-V2-KING-3-Replace-EK1-0348-1110257"><br><br><div style="text-align: center;">						<img src="image/catalog/Woodworking-and-Handmade-Tools/0-10cm-ABS-Black-Universal-Pitch-Gauge-For-Esky-Belt-CP-V2-KING-3-Replace-EK1-0348-1110257-descriptionImage5.jpg" alt="0-10cm-ABS-Black-Universal-Pitch-Gauge-For-Esky-Belt-CP-V2-KING-3-Replace-EK1-0348-1110257"><br><br><div style="text-align: center;">							<img src="image/catalog/Woodworking-and-Handmade-Tools/0-10cm-ABS-Black-Universal-Pitch-Gauge-For-Esky-Belt-CP-V2-KING-3-Replace-EK1-0348-1110257-descriptionImage6.jpg" alt="0-10cm-ABS-Black-Universal-Pitch-Gauge-For-Esky-Belt-CP-V2-KING-3-Replace-EK1-0348-1110257"><br><br><div style="text-align: center;">								<img src="image/catalog/Woodworking-and-Handmade-Tools/0-10cm-ABS-Black-Universal-Pitch-Gauge-For-Esky-Belt-CP-V2-KING-3-Replace-EK1-0348-1110257-descriptionImage7.jpg" alt="0-10cm-ABS-Black-Universal-Pitch-Gauge-For-Esky-Belt-CP-V2-KING-3-Replace-EK1-0348-1110257"></div>						</div>					</div>				</div>			</div>		</div>	</div></div><br><div id="imgBox">    </div>                </div>
                                  <div class="block-expand-overlay"><a class="block-expand btn"></a></div>
                              </div>
"""

html = etree.HTML(data5)

img_list = html.xpath('//div[contains(@class,"block-content expand-content")]//img//@src')

imgs = []
for img in img_list:
    imgs.append("www.cyberebee.com/" + img)


# print(imgs)


def get_features(elms, title, others):
    if title in {'Details pictures:'}: return None;
    print(title)
    features = []
    features_find = False
    other_find = False
    for elm in elms:
        tag = elm.tag

        if tag == 'br':
            continue
        # print("tag=", tag)
        if (tag == 'span' or tag == 'strong') and elm.text is not None and elm.text.startswith(
                title) and elm.text.strip() != 'Package Included:':
            # print("====Features txt founded====")
            features_find = True
            continue

        if (tag == 'span' or tag == 'strong') and elm.text is not None and elm.text.strip() in others and features_find:
            # print("====Other txt founded====1")
            other_find = True
            break

        if tag == 'div':
            for e in elm.xpath('.//text()'):
                if e.strip() in others and features_find:
                    # print("====Other txt founded====2")
                    other_find = True
                    break

        if tag == 'img':
            # print("====Img txt founded====3")
            break

        if tag == 'strong' and elm.text is not None and elm.text.strip() == 'Package Included:':
            x_elm = elm.xpath('.//text()')
            for e in x_elm:
                if len(e.strip()) == 0 or e.strip() == 'Package Included:' or e.strip() == 'More Details:':
                    other_find = True
                    continue
                if e.strip() not in features:
                    features.append(e.strip())
            break

        if features_find and (not other_find):
            x_elm = elm.xpath('.//text()')
            for e in x_elm:
                if len(e.strip()) == 0:
                    continue
                if e.strip() not in features:
                    features.append(e.strip())
    return features


e_tmp = html.xpath('//div[contains(@class,"block-content expand-content")]//*')

# others_el = {'Package included', 'Details pictures', 'Package Included', 'Specification', 'Description','Features'}
others_el = {'Package included:', 'Details pictures:', 'Package Included:',
             'Specification:', 'Description:', 'Features:', 'More Details:'}

if __name__ == '__main__':
    # for el in others_el:
    #     f_set = get_features(e_tmp, el, others_el)
    #     # print("====", el, "====")
    #     print(f_set)

    features = get_features(e_tmp, 'Features:', others_el)

    desc = get_features(e_tmp, 'Description:', others_el)
    pkg_inc1 = get_features(e_tmp, 'Package Included:', others_el)
    pkg_inc2 = get_features(e_tmp, 'Package included:', others_el)
    spec = get_features(e_tmp, 'Specification:', others_el)

    print(desc)
    print(pkg_inc1)
    print(pkg_inc2)
    print(spec)

    description = "<b>Description</b><br>"
    if len(desc) > 0:
        for d in desc:
            description += d + "<br>"

    if len(spec) > 0:
        description += "<b>Specification</b><br>"
        for d in spec:
            description += d + "<br>"

    description += "<b>Package Included:</b><br>"
    if len(pkg_inc1) > 0:
        for d in pkg_inc1:
            description += d + "<br>"
    if len(pkg_inc2) > 0:
        for d in pkg_inc2:
            description += d + "<br>"
    # f_set = get_features(e_tmp, "Package Included:", others_el)
    print(description)
    print(features)
