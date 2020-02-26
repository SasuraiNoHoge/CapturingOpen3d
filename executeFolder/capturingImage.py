
import open3d as o3d

if __name__ == "__main__":
  mesh = o3d.io.read_triangle_mesh("../CGData/monky.obj")
  # 法線の計算
  mesh.compute_vertex_normals()

  vis = o3d.visualization.Visualizer()
  # ウィンドウのサイズを指定する場合
  # vis.create_window(width = 1200, height = 1600, visible = False)
  vis.create_window(visible = False)
  vis.add_geometry(mesh)

  # カメラの撮影位置を指定
  param = o3d.io.read_pinhole_camera_parameters('../config/cameraparams.json')
  ctr = vis.get_view_control()
  ctr.convert_from_pinhole_camera_parameters(param)

  vis.capture_screen_image('../output/output.png', True)
  vis.destroy_window()