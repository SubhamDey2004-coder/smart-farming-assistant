def analyze_irrigation(farmer):

    recommendations = []

    if farmer.water_availability == "Low":
        recommendations.append(
            "Drip irrigation is highly recommended due to low water availability."
        )

    if farmer.soil_moisture < 40:
        recommendations.append(
            "Soil moisture is low. Frequent light irrigation is recommended."
        )

    if farmer.soil_type.lower() == "sandy":
        recommendations.append(
            "Sandy soil loses water quickly. Moisture conservation is important."
        )

    return recommendations


def analyze_soil_health(farmer):

    recommendations = []

    if farmer.soil_ph < 6:
        recommendations.append(
            "Soil is acidic. Lime treatment may help balance pH."
        )

    elif farmer.soil_ph > 7.5:
        recommendations.append(
            "Soil is alkaline. Organic compost can help improve soil condition."
        )

    if farmer.organic_carbon < 0.5:
        recommendations.append(
            "Organic carbon is low. Add compost or organic manure."
        )

    return recommendations


def analyze_fertilizer(farmer):

    recommendations = []

    if farmer.nitrogen < 50:
        recommendations.append(
            "Nitrogen level is low. Nitrogen-rich fertilizers may be needed."
        )

    if farmer.phosphorus < 30:
        recommendations.append(
            "Phosphorus is low. DAP fertilizer can improve root development."
        )

    if farmer.potassium < 40:
        recommendations.append(
            "Potassium is low. Potash fertilizers may improve crop resistance."
        )

    return recommendations


def analyze_crop_suitability(farmer):

    recommendations = []

    if farmer.crop_type.lower() == "paddy":

        if farmer.water_availability == "Low":
            recommendations.append(
                "Paddy cultivation may face water stress due to low water availability."
            )

    if farmer.crop_type.lower() == "bajra":

        recommendations.append(
            "Bajra is suitable for dry and sandy soil conditions."
        )

    if farmer.crop_type.lower() == "banana":

        if farmer.soil_moisture < 60:
            recommendations.append(
                "Banana cultivation requires higher moisture levels."
            )

    return recommendations


def analyze_pest_risk(farmer):

    recommendations = []

    if farmer.pest_history:

        recommendations.append(
            f"Monitor crop carefully due to previous pest issue: {farmer.pest_history}."
        )

    if farmer.humidity_percent > 80:

        recommendations.append(
            "High humidity may increase fungal disease risk."
        )

    return recommendations