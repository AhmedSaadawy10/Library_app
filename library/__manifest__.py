{
    "name": "library app",
    "author": "Ahmed Saadawy",
    "summary": "The Library Module by Ahmed Saadawy is an essential tool for managing library resources efficiently.",
    "description": """
                   This is a dynamic application designed to streamline library operations and enhance user experience.
                   Developed by Ahmed Saadawy,
                   this module offers a sophisticated yet intuitive platform for librarians to manage their collections effectively.
                   With features tailored to meet the diverse needs of libraries,
                   it allows for easy cataloging, indexing, and tracking of library materials.
                   """,
    "category": "Productivity",
    "application": True,
    "data": [
        "security/ir.model.access.csv",
        "views/main_menu.xml",
        "views/book_view.xml",
        "views/publisher_view.xml",
        "wizard/add_publisher_wizard.xml"
    ],
    "depends": ["base", "web"],
}
