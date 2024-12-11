import streamlit as st
import mysql.connector

st.set_page_config(page_title="Basil Energetics Private Ltd - Price Calculator", layout="centered")

# Logo and Title
logo_url = "BEPL_picture.jpg"  
st.image(logo_url, width=200)

st.title("Basil Energetics Private Ltd - Price Calculator")

# User Inputs
st.header("Customer & Sales Details")
customer_name = st.text_input("Customer Name:")
customer_phone = st.text_input("Customer Phone Number:")
salesman_name = st.text_input("Salesman Name:")

st.header("Appliance Quantities")
items = [
    '1-ton AC', '1.5-ton AC', '50L Fridge', '180L Fridge', '300L Fridge', 'Ceiling Fan',
    'Tube Light', '7W Bulb', '9W Bulb', '12W Bulb', '15W Street Light', '24W Street Light', 'Other Loads'
]
power_watts = [900, 1000, 80, 100, 120, 24, 20, 7, 9, 12, 15, 24, 340]
cost_rs = [30000, 33000, 8000, 10000, 16000, 2200, 220, 75, 75, 75, 950, 950, 20500]

qty = []
for item in items:
    qty.append(st.number_input(f"Enter quantity of {item}:", min_value=0, step=1))

# Buttons for Actions
if st.button("Calculate"):
    # Calculations
    tot_load = [qty[i] * power_watts[i] for i in range(len(qty))]
    acp1 = qty[0] * power_watts[0] + qty[1] * power_watts[1]
    tot_app_power = sum(tot_load)
    si = tot_app_power - acp1
    tot_cost = [qty[i] * cost_rs[i] for i in range(len(items))]
    appn_cost = sum(tot_cost) / 100000

    lf = 1
    cal_power = lf * tot_app_power
    panel_power = 450
    sp = 2
    cal_sys_power = tot_app_power * 1.4
    no_of_panel = cal_sys_power / (panel_power * sp)
    round_off = int(no_of_panel)
    if round_off < no_of_panel:
        round_off += 1
    roundoff_panel_no = sp * round_off
    area_reqd = 2.5
    rooftop_area = roundoff_panel_no * area_reqd
    pv_panel_rating = (roundoff_panel_no * panel_power) / 1000
    slave = round(si / 500)
    ms = 1 if tot_app_power > 0 else 0
    pv_panel_cost = pv_panel_rating * 0.24
    master_cost = ms * 0.07
    slave_cost = slave * 0.07
    ac_slave_cost = (qty[0] + qty[1]) * 0.07
    complete_cost = appn_cost + pv_panel_cost + master_cost + slave_cost + ac_slave_cost
    final_cost = 2 * complete_cost

    # Display Results
    st.subheader("Price Calculation Results")
    st.success(f"Rounded-off Panels: **{roundoff_panel_no}**")
    st.success(f"Required Rooftop Area (in sq.m): **{rooftop_area:.2f}**")
    st.success(f"PV Panel Rating (in kW): **{pv_panel_rating:.2f}**")
    st.success(f"Best Price (in Lakhs): **{final_cost:.2f}**")
    # customer details
    st.markdown("---")
    st.info(f"Customer Name: {customer_name}")
    st.info(f"Customer Phone Number: {customer_phone}")
    st.info(f"Salesman Name: {salesman_name}")

# Save to Database Button
if st.button("Load to Database"):
    if customer_name and customer_phone and salesman_name:
        try:
            conn = mysql.connector.connect(
                host="<YOUR_HOST>",
                user="<YOUR_USER>",
                password="<YOUR_PASSWORD>",
                database="basil_energetics"
            )
            cursor = conn.cursor()

            # Insert Data into Database
            cursor.execute("""
                INSERT INTO sales_data (
                    customer_name, customer_phone, salesman_name, 
                    qty_1_ton_ac, qty_1_5_ton_ac, qty_50l_fridge, qty_180l_fridge, 
                    qty_300l_fridge, qty_ceiling_fan, qty_tube_light, qty_7w_bulb, 
                    qty_9w_bulb, qty_12w_bulb, qty_15w_street_light, qty_24w_street_light, 
                    qty_other_loads, roundoff_panel_no, rooftop_area, pv_panel_rating, final_cost
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                customer_name, customer_phone, salesman_name, *qty, roundoff_panel_no, rooftop_area, pv_panel_rating, final_cost
            ))
            conn.commit()
            st.success("Data successfully saved to the database!")
        except mysql.connector.Error as err:
            st.error(f"Error: {err}")
        finally:
            cursor.close()
            conn.close()
    else:
        st.error("Please fill in all Customer & Sales Details.")

st.markdown("---")
st.write("🌍 Powered by **Basil Energetics Private Ltd** - Let's go solar!")
