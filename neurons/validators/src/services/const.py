MIN_JOB_TAKEN_TIME = 20

GPU_MAX_SCORES = {
    # Latest Gen NVIDIA GPUs (Averaged if applicable)
    "NVIDIA H100 80GB HBM3": 3.49,
    "NVIDIA H100 NVL": 2.79,
    "NVIDIA H100 PCIe": 2.69,
    "NVIDIA GeForce RTX 4090": 0.69,
    "NVIDIA RTX 4000 Ada Generation": 0.38,
    "NVIDIA RTX 6000 Ada Generation": 1.03,
    "NVIDIA L4": 0.43,
    "NVIDIA L40S": 1.03,
    "NVIDIA L40": 0.99,
    "NVIDIA RTX 2000 Ada Generation": 0.28,
    # Previous Gen NVIDIA GPUs (Averaged if applicable)
    "NVIDIA A100 80GB PCIe": 1.64,
    "NVIDIA A100-SXM4-80GB": 1.89,
    "NVIDIA RTX A6000": 0.76,
    "NVIDIA RTX A5000": 0.43,
    "NVIDIA RTX A4500": 0.35,
    "NVIDIA RTX A4000": 0.32,
    "NVIDIA A40": 0.39,
    "NVIDIA A30": 0.35,
    "NVIDIA GeForce RTX 3090": 0.43,
}

MAX_UPLOAD_SPEED = 1000
MAX_DOWNLOAD_SPEED = 1000

JOB_TAKEN_TIME_WEIGHT = 0.9
UPLOAD_SPEED_WEIGHT = 0.05
DOWNLOAD_SPEED_WEIGHT = 0.05

MAX_GPU_COUNT = 14

UNRENTED_MULTIPLIER = 0.25

HASHCAT_CONFIGS = {
    "NVIDIA RTX A5000": {
        "digits": 11,
        "average_time": [
            24.251156330108643,
            24.459399509429932,
            25.07683423360189,
            26.078879714012146,
            27.233995351791386,
            27.801182564099634,
            29.58513449941363,
            30.492227721214295,
        ],
    },
    "NVIDIA RTX A6000": {
        "digits": 11,
        "average_time": [
            24.251156330108643,
            24.459399509429932,
            25.07683423360189,
            26.078879714012146,
            27.233995351791386,
            27.801182564099634,
            29.58513449941363,
            30.492227721214295,
        ],
    },
    "NVIDIA RTX A4500": {
        "digits": 11,
        "average_time": [
            24.251156330108643,
            24.459399509429932,
            25.07683423360189,
            26.078879714012146,
            27.233995351791386,
            27.801182564099634,
            29.58513449941363,
            30.492227721214295,
        ],
    },
    "NVIDIA RTX A4000": {
        "digits": 11,
        "average_time": [
            32.62807669639587,
            33.436131143569945,
            33.88327717781067,
            34.187138891220094,
            35.52240489006042,
            37.14521159331004,
            39.016253103528705,
            40.42734135985374,
        ],
    },
    "NVIDIA GeForce RTX 3090": {
        "digits": 11,
        "average_time": [
            22.13358383178711,
            24.477075362205504,
            26.968040720621747,
            29.163842380046844,
            31.934904451370237,
            34.341850678126015,
            37.18430421011789,
            39.15856931209564,
        ],
    },
    "NVIDIA RTX 6000 Ada Generation": {
        "digits": 11,
        "average_time": [
            12.016858005523682,
            13.232668924331666,
            14.015261713663739,
            14.904895508289338,
            15.89838502883911,
            16.701006396611533,
            18.079130056926182,
            19.553341883420945,
        ],
    },
    "NVIDIA L40S": {
        "digits": 11,
        "average_time": [
            10.906689882278442,
            9.32911479473114,
            12.892356348037719,
            13.338897478580474,
            14.28122389793396,
            15.280945293108621,
            15.630833080836705,
            17.76026642918587,
        ],
    },
    "NVIDIA L40": {
        "digits": 11,
        "average_time": [
            10.906689882278442,
            9.32911479473114,
            12.892356348037719,
            13.338897478580474,
            14.28122389793396,
            15.280945293108621,
            15.630833080836705,
            17.76026642918587,
        ],
    },
    "NVIDIA L4": {
        "digits": 11,
        "average_time": [
            27.768908500671387,
            27.90283513069153,
            27.773880004882812,
            27.653605222702026,
            27.88539433479309,
            27.88539433479309,
            27.88539433479309,
            27.88539433479309,
        ],
    },
    "NVIDIA RTX 4000 Ada Generation": {
        "digits": 11,
        "average_time": [
            23.84185085296631,
            25.37116765975952,
            25.933285299936934,
            27.255381512641907,
            28.95430653572082,
            30.480634721120204,
            32.16756559780665,
            33.507733607292174,
        ],
    },
    "NVIDIA H100 PCIe": {
        "digits": 11,
        "average_time": [
            18.3540611743927,
            17.581688284873962,
            19.558610963821412,
            23.779386079311372,
            25.929840545654294,
            28.815886704126996,
            29.60572577885219,
            33.850944715738294,
        ],
    },
    "NVIDIA H100 NVL": {
        "digits": 11,
        "average_time": [
            18.3540611743927,
            17.581688284873962,
            19.558610963821412,
            23.779386079311372,
            25.929840545654294,
            28.815886704126996,
            29.60572577885219,
            33.850944715738294,
        ],
    },
    "NVIDIA H100 80GB HBM3": {
        "digits": 11,
        "average_time": [
            18.3540611743927,
            17.581688284873962,
            19.558610963821412,
            23.779386079311372,
            25.929840545654294,
            28.815886704126996,
            29.60572577885219,
            33.850944715738294,
        ],
    },
    "NVIDIA A100 80GB PCIe": {
        "digits": 11,
        "average_time": [
            18.69497232437134,
            20.42860324382782,
            22.53571968078613,
            25.373827075958253,
            26.749426555633544,
            31.196198654174804,
            32.80575948442732,
            37.11309432387352,
        ],
    },
    "NVIDIA A100-SXM4-80GB": {
        "digits": 11,
        "average_time": [
            18.69497232437134,
            20.42860324382782,
            22.53571968078613,
            25.373827075958253,
            26.749426555633544,
            31.196198654174804,
            32.80575948442732,
            37.11309432387352,
        ],
    },
    "NVIDIA A40": {
        "digits": 11,
        "average_time": [
            22.828101253509523,
            23.189609861373903,
            21.3694882551829,
            23.657343721389772,
            28.178246479034424,
            27.75535701115926,
            30.86851720128741,
            34.388632106781,
        ],
    },
    "NVIDIA A30": {
        "digits": 11,
        "average_time": [
            22.828101253509523,
            23.189609861373903,
            21.3694882551829,
            23.657343721389772,
            28.178246479034424,
            27.75535701115926,
            30.86851720128741,
            34.388632106781,
        ],
    },
    "NVIDIA RTX 2000 Ada Generation": {
        "digits": 11,
        "average_time": [
            22.828101253509523,
            23.189609861373903,
            21.3694882551829,
            23.657343721389772,
            28.178246479034424,
            27.75535701115926,
            30.86851720128741,
            34.388632106781,
        ],
    },
    "NVIDIA GeForce RTX 4090": {
        "digits": 11,
        "average_time": [
            11.02204384803772,
            11.871551060676575,
            12.621799103418986,
            13.46524715423584,
            14.425264406204224,
            12.915648317337036,
            16.706109033312117,
            17.858580154180526,
        ],
    },
}

LIB_NVIDIA_ML_DIGESTS = {
    "535.183.01": "58fc46eefa8ebb265293556951a75a39",
    "535.183.06": "03ed7fa2134095b32f9d0d24a774c6ba",
    "535.216.01": "96479a06139fc5261d06f432970d6a7b",
    "535.216.03": "189634bf960b9a2efe1af8011d27ccf7",
    "545.23.06": "5ad33588e91af67139efb54fe9fefc68",
    "545.29.06": "85ad949d7553ab96cce5c811e229c7c7",
    "550.120": "48be49d0e792b5ee76f73857c0bef35a",
    "550.127.05": "bfa2733eee442016792bcbf130156e3d",
    "550.54.15": "9625642dcf8765f52e332c8e38fbef73",
    "550.78": "1f335d1f068931fe7f2ce13117d1602b",
    "550.90.07": "c95828f8a8ab7f17743b40561b812c96",
    "550.90.12": "d7702d394ab213a725abeb345185a072",
    "555.42.02": "0262f396e80847dccefc8ccf52cff1ae",
    "555.42.06": "69774adffa76471490e6d8fac9067725",
    "560.28.03": "6d6e0122cff1ac777a9e37ba09b886cb",
    "560.35.03": "93a3f8ef77af86b79314c00b0788aeed",
    "560.35.05": "1eec299b50e33a6cfa5155ded53495ab",
    "565.57.01": "c801dd3fc4660f3a8ddf977cfdffe113",
    "550.127.08": "ac925f2cd192ad971c5466d55945a243",
}

DOCKER_DIGESTS = {
    "26.1.3": "52d8fcc2c4370bf324cdf17cbc586784",
    "27.3.1": "40f1f7724fa0432ea6878692a05b998c",
}
