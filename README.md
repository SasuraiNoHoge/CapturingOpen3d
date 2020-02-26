Open3dを使ってスクリプトだけで3D空間のCGを撮影する
==== 

## 動作確認済み環境
python_version 3.6.4

## Install
```bash
pip install open3d
```

## 使い方
 ```executeFolder```内の```capturingImage.py```を実行すると，```output```フォルダ内に出力画像が生成される．  
   
 カメラの位置を指定する場合は```executeFolder```内の```displayMesh.py```を実行し，アプリケーションを起動する．  
 起動したアプリケーションを操作して，望んだカメラの位置で，キーボードのPを押すことで画面キャプチャする．  
 その後，上記フォルダ内に，jsonファイルとpngファイルが生成される．  
 jsonファイルはカメラを撮影した位置が記録されている.  
 ```config```フォルダの```cameraparams.json```を生成されたjsonファイルに変更し，```capturingImage.py```を実行すると変更したカメラの位置が反映されて画像が保存される．

## Licence

[MIT](https://github.com/tcnksm/tool/blob/master/LICENCE)
