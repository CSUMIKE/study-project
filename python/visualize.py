import vtk

def main():
	# read stl file
	reader = vtk.vtkSTLReader()
	reader.SetFileName("C:/Users/Suca/Desktop//vtk_visualize/surface-2.stl")
	reader.Update()

	# mapper
	mapper = vtk.vtkPolyDataMapper()
	mapper.SetInputData(reader.GetOutput())

	# actor
	actor = vtk.vtkActor()
	actor.SetMapper(mapper)

	# renderer
	ren = vtk.vtkRenderer()
	ren.AddActor(actor)

	# render window
	renWin = vtk.vtkRenderWindow()
	renWin.AddRenderer(ren)

	# interactor style
	iren = vtk.vtkRenderWindowInteractor()
	# iren.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())
	iren.SetRenderWindow(renWin)

	# initalize and render
	iren.Initialize()
	# ren.ResetCamera()
	renWin.Render()

	iren.Start()

if __name__=="__main__":
	main()