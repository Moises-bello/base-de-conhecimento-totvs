---
article_id: 360034789134
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: bf8922baa8f85c343f09555eef3b840a982349a60f612d7c5bccb96664363640
fetched_at: '2026-06-28T22:40:48.756978+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECF - Y600 Como gerar
type: support-article
updated_at: '2024-07-04T18:22:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034789134-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-Y600-Como-gerar
---

**Dúvida**

Como gerar o Y600 ?  
  
**Ambiente**Microsiga Protheus – contabilidade – A partir da versão 11.80  
  
**Solução**

## **01. VISÃO GERAL**

O registro **Y600 - IDENTIFICAÇÃO DOS SÓCIOS OU TITULAR**  deverá ser cadastrado diretamente no módulo de **TAF,**através da rotina TAFA346, sendo possível inserir os dados dos sócios através de uma rotina mais amigável, com descrição e help de campos que auxiliam no preenchimento das informações.

## **02. EXEMPLO DE UTILIZAÇÃO**

Para cadastrar um ou mais sócios que irão compor o Y600 do ECF, entre na rotina TAFA346 e clique em incluir, será apresentado uma tela com os campos para informação, segue abaixo exemplo de preenchimento:

![](https://tdn.totvs.com/download/attachments/235586519/image-2024-4-9_14-1-26.png?version=1&modificationDate=1712682147260&api=v2)

Para mais detalhes:

## [**Registro Y600 - Remoção do parâmetro MV\_REGSOC**](https://tdn.totvs.com/pages/releaseview.action?pageId=821186345)

* O parâmetro MV\_REGSOC foi criado para a rotina DIPJ (MATA975) para sanar um problema de que não havia um cadastro para informações dos sócios. Com a migração da DIPJ para a ECF, realizamos a descontinuação do parâmetro MV\_REGSOC e essas informações devem ser cadastradas diretamente no TAF, através da rotina TAFA346. Saiba mais: [ECF0005\_Exportação\_para\_TAF\_do\_Registro\_Y600\_Sócios - Linha Microsiga Protheus - TDN (totvs.com)](https://tdn.totvs.com/pages/viewpage.action?pageId=235586519)

Saiba mais :

[MP - SIGACTB - ECF - X320 - UNIDADE DE MEDIDA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020084511-MP-SIGACTB-ECF-X320-UNIDADE-DE-MEDIDA-?source=search)

[MP - SIGACTB - ECF -Como realizar a geração dos blocos X e Y?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006827952-MP-SIGACTB-ECF-Como-realizar-a-gera%C3%A7%C3%A3o-dos-blocos-X-e-Y-?source=search)

[Relatório Transfer Pricing - Preço de Transferência](http://tdn.totvs.com/pages/releaseview.action?pageId=6076191)

[MP - SIGACTB - ECF - Tabelas ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006861411-MP-SIGACTB-ECF-Tabelas-ECF?source=search)
