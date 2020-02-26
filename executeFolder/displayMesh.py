import open3d as o3d

if __name__ == "__main__":
  mesh = o3d.io.read_triangle_mesh("../CGData/monky.obj")
  # 法線の計算
  mesh.compute_vertex_normals()
  
  vis = o3d.visualization.Visualizer()
  # ウィンドウのサイズを指定する場合
  # vis.create_window(width = 1200, height = 1600)
  vis.create_window()
  vis.add_geometry(mesh)
  vis.run()
  vis.destroy_window()