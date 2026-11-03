---
content_hash: 8d056caa1e80b2850464dbf2e406b51f99751e1a3f3776c654ca571c29c61dcf
fetched_at: '2026-06-29T00:11:39.029587+00:00'
page_id: '786559317'
product: rm
source: tdn-rm
title: API de Permissões
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=786559317
version: 1
---

# Sumário

---

Sumário

# Objetivo

---

Esse documento tem o objetivo de exemplificar o uso da API utilizando todos os métodos implementados.

Para mais informações sobre consumo de Licença, [veja aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=419548455#APIsdeFrameworkM%C3%B3duloServi%C3%A7osGlobais-5-ConsumodeLicen%C3%A7aspeloLicenseServer).

# 1 - Métodos

---

Serão apresentados 1 método, o qual foi implementado na API de Permissões, sendo ele:

* GET

# 1.1 - GET

---

## 1.1.1 - Get All (Recuperar todas as permissões)

---

false1.1.1 GetAllfalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/sod-matrix/permissions

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Url Utilizada:** <http://localhost:8051/api/framework/v1/sod-matrix/permissions>

falseExemplo de ResultadoVer resultado JSON...

[  
    {

        "value": "9777150e-a405-42bd-8fbf-6966b09045c8",  
        "module": "RM.Glb.Server",  
        "tagMenu": "999999916",  
        "permissionId": 0,  
        "label": "Serviços Globais",  
        "isSelectable": false,  
        "subItems": [  
            {  
                "value": "c4d83bf0-faa6-449f-9fa3-ca5540b59732",  
                "parent": "999999916",  
                "tagMenu": "800000085",  
                "permissionId": 0,  
                "label": "Administração",  
                "isSelectable": false,  
                "subItems": [  
                    {  
                     ...  
                    }  
                ]  
            }  
        ]  
    }  
]
