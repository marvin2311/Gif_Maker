import imageio
import os

clip = os.path.abspath('test.mp4')

def gif_maker(inputPath, targetFormat):
    outputPath = os.path.splitext(inputPath)[0]+targetFormat

    print("converting {0} to {1}".format(inputPath,outputPath))

    reader = imageio.get_reader(inputPath)
    fps = reader.get_meta_data()['fps']
    writer = imageio.get_writer(outputPath, fps=fps)

    for frame in reader:
        writer.append_data(frame)
    print("Done!")
    writer.close()

gif_maker(clip, ".gif")
