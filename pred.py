import os
import json
import torch
from PIL import Image
from torchvision import transforms
from model import resnet34


data_transform = transforms.Compose(
    [transforms.Resize(256),
     transforms.CenterCrop(224),
     transforms.ToTensor(),
     transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])

def predict(img_path):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    img = Image.open(img_path)
    img = img.convert("RGB")
    img = data_transform(img)
    img = torch.unsqueeze(img, dim=0).cuda()

    json_path = './class_indices_sdust.json'
    assert os.path.exists(json_path), "file: '{}' dose not exist.".format(json_path)

    json_file = open(json_path, "r")
    class_indict = json.load(json_file)

    model = resnet34(num_classes=220).to(device)

    weights_path = "./ResNet__sdust.pth"
    assert os.path.exists(weights_path), "file: '{}' dose not exist.".format(weights_path)
    model.load_state_dict(torch.load(weights_path,map_location = 'cuda:0'))

    model.eval()
    with torch.no_grad():
        output = torch.squeeze(model(img)).cpu()

        predict = torch.softmax(output, dim=0)
        predict_cla = torch.argmax(predict).numpy()

    print_res = "预测类别:{} 可能性:{:.3}".format(class_indict[str(predict_cla)], predict[predict_cla].numpy())

    return print_res


