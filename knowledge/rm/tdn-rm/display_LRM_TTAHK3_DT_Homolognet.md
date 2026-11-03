---
content_hash: b7eefddc1a76768856dc9c026865cefd5304a6c9e3ad7414b6226572bd884bf3
fetched_at: '2026-06-29T00:06:04.064446+00:00'
page_id: '200905141'
product: rm
source: tdn-rm
title: TTAHK3_DT_Homolognet
type: documentation
url: https://tdn.totvs.com/display/LRM/TTAHK3_DT_Homolognet
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
| **Chamados relacionados:** | TTAHK3 |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.7* |
