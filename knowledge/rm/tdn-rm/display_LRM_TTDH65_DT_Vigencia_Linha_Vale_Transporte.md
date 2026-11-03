---
content_hash: 721d47dba32b0b4be26c5623dce91d03f7de1fd18f09981266da18533395a42c
fetched_at: '2026-06-29T00:06:06.276095+00:00'
page_id: '201729610'
product: rm
source: tdn-rm
title: TTDH65_DT_Vigencia_Linha_Vale_Transporte
type: documentation
url: https://tdn.totvs.com/display/LRM/TTDH65_DT_Vigencia_Linha_Vale_Transporte
version: 3
---

# PERIODO DE VIGÊNCIA DAS LINHAS DE VT

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Vale Transporte* |
| **Situação/Requisito:** | *No cálculo do Total Entregue de Vale Transporte, CC 32,  não está considerando corretamente as datas de vigência da Linha que estão iniciando ou terminando durante o mês.* |
| **Solução/Implementação:** | *Ajuste no cálculo do evento de Vale Transporte (CC 32) para efetuar o lançamento do total entregue, considerando o dia correto das datas de vigência que estiverem iniciando e terminando durante o mês competência.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTDH65* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.8* |
