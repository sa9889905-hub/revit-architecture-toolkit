# -*- coding: utf-8 -*-
# Revit Architecture Toolkit
# Room Area Summary - Revit 2024 / pyRevit

from pyrevit import revit, DB

doc = revit.doc

rooms = DB.FilteredElementCollector(doc)\
    .OfCategory(DB.BuiltInCategory.OST_Rooms)\
    .WhereElementIsNotElementType()

total_area = 0.0
room_count = 0

print("REVIT ROOM AREA SUMMARY")
print("-" * 40)

for room in rooms:
    if room.Area > 0:
        area = DB.UnitUtils.ConvertFromInternalUnits(
            room.Area,
            DB.UnitTypeId.SquareMeters
        )

        name = room.get_Parameter(
            DB.BuiltInParameter.ROOM_NAME
        ).AsString()

        total_area += area
        room_count += 1

        print("{} - {}: {:.2f} m2".format(
            room.Number, name, area
        ))

print("-" * 40)
print("Total Rooms: {}".format(room_count))
print("Total Area: {:.2f} m2".format(total_area))
