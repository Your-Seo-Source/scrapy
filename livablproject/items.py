import scrapy

class LivablprojectItem(scrapy.Item):
    # Basic project information
    name = scrapy.Field()
    status = scrapy.Field()  # This should be 'selling_status' if you want to maintain consistency with other fields
    price = scrapy.Field()
    incentives = scrapy.Field()
    address = scrapy.Field()
    developer = scrapy.Field()
    project_url = scrapy.Field()  # Use snake_case for consistency
    
    # Detailed project specifications
    building_type = scrapy.Field()  # Use snake_case for consistency
    units_stories = scrapy.Field()  # Use snake_case for consistency
    bedrooms = scrapy.Field()
    size_sq_ft = scrapy.Field()  # Use snake_case for consistency
    estimated_completion = scrapy.Field()  # Use snake_case for consistency

    # Additional project details
    ownership = scrapy.Field()
    selling_status = scrapy.Field()
    sales_started = scrapy.Field()
    construction_status = scrapy.Field()
    construction_start_date = scrapy.Field()
    builders = scrapy.Field()
    ceilings = scrapy.Field()
    
    # Detailed unit information
    unit_details = scrapy.Field()  # Store list of dictionaries for unit details here

    # Gallery Data from script tag's JSON
    gallery_data = scrapy.Field()  # Store gallery data here
    
    # Raw Development Units JSON Data
    hd_development_latitude = scrapy.Field()  # Use snake_case for consistency
    hd_development_longitude = scrapy.Field()  # Use snake_case for consistency

# Remove PropertyListingItem unless it's actually being used as a separate class elsewhere in your spider
    # Remove PropertyListingItem unless it's actually being used as a separate class elsewhere in your spider
    # Note: The 'units' field has been replaced by 'unit_details' for structured unit information.