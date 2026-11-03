---
content_hash: 719920e04b093b23875aed6f1e42a7a6a2132adc6e2ca09a70e8472d265bd56f
fetched_at: '2026-06-28T21:35:23.840163+00:00'
page_id: '266963098'
product: fluig
source: tdn-fluig
title: DES - É possível realizar uma chamada de API em um dataset customizado?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=266963098
version: 5
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

# Ocorrência

Preciso acessar uma API via dataset customizado: após recuperar os dados e gravar no dataset, esses dados serão utilizados no relatório BIRT.

# Solução

O serviços do SDK estão disponíveis nos datasets via fluigAPI.

Verificar na seção "Consumindo um serviço do componente SDK a partir de eventos de JavaScript" na página

A função de exemplo abaixo é de um evento de processo:

js

Porém a API também pode ser utilizada dentro da função CreateDataset:

js

Consulte a [lista de serviços](http://tdn.totvs.com/pages/viewpage.action?pageId=198934765#ConsumodeServiçosnaAPIPúblicaenocomponenteSDK-ServiçosdisponíveisnocomponenteSDK) que podem ser consumidos.
