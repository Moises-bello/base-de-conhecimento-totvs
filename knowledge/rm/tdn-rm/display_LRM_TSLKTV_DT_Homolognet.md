---
content_hash: 258073d1cf05667e84d3ce3ed15e88a93b7f1bf41d598737c41b3a74ac444129
fetched_at: '2026-06-29T00:06:04.044122+00:00'
page_id: '200904967'
product: rm
source: tdn-rm
title: TSLKTV_DT_Homolognet
type: documentation
url: https://tdn.totvs.com/display/LRM/TSLKTV_DT_Homolognet
version: 1
---

# Homolognet

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de pagamento* |
| **Função:** | *Homolognet* |
| **Situação/Requisito:** | Atualmente ao gerar o Homolognet sempre leva na tag <NRCnpjCeiTomadorObra> a mesma informação que está na tag <NRCnpjCei>.  Cliente solicita que seja possível levar informações do tomador de serviço vinculado ao funcionário.  *.* |
| **Solução/Implementação:** | Como o layout do homolognet só prevê informações de 1 tomador, foi criada nova aba na geração do homolognet para que as informações do tomador em questão possam ser informadas. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TSLKTV |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.40* |
