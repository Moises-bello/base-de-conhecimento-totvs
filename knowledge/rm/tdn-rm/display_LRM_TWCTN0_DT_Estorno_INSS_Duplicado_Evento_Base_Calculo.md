---
content_hash: 3b1e232cc9b66b3ae24c40e7b0b797614a1498ff3337f48f933ea992d0f48c66
fetched_at: '2026-06-29T00:08:21.039704+00:00'
page_id: '268809510'
product: rm
source: tdn-rm
title: TWCTN0_DT_Estorno_INSS_Duplicado_Evento_Base_Calculo
type: documentation
url: https://tdn.totvs.com/display/LRM/TWCTN0_DT_Estorno_INSS_Duplicado_Evento_Base_Calculo
version: 1
---

# ESTORNO DE INSS DUPLICADO DE EVENTO DO TIPO BASE DE CÁLCULO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *INSS* |
| **Situação/Requisito:** | *No cálculo de rescisão, quando existe um evento do tipo Base de Cálculo, estornando INSS, que tem o seu valor alterado após o cálculo das médias, o valor do estorno na Base de INSS, no CC 3, estava sendo duplicado.* |
| **Solução/Implementação:** | *Ajuste no cálculo do desconto de INSS, evento de CC 3**.* |
| **Chamados   relacionados:** | *TWCTN0* |
| **Versões/Release:** | *12.1.14* |
