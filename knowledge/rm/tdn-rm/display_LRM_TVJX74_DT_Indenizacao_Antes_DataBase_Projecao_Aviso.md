---
content_hash: 9fce442ecb7b517c57b27a1d54c34063f4ba42a167ae30fa53e52613db7af027
fetched_at: '2026-06-29T00:08:19.215986+00:00'
page_id: '266981117'
product: rm
source: tdn-rm
title: TVJX74_DT_Indenizacao_Antes_DataBase_Projecao_Aviso
type: documentation
url: https://tdn.totvs.com/display/LRM/TVJX74_DT_Indenizacao_Antes_DataBase_Projecao_Aviso
version: 114
---

# INDENIZAÇÃO ANTES DA DATA BASE NÃO CONSIDERA PROJEÇÃO DO AVISO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Rescisão* |
| **Situação/Requisito:** | O parâmetro do Sindicato "Lança indenização adicional na dispensa sem justa causa, no período de 30 dias antes da data base" não estava levando em consideração a projeção do aviso prévio indenizado, e não lançava o evento de código de cálculo 344 - INDENIZAÇÃO ADICIONAL NA DISPENSA ANTES DATA BASE. |
| **Solução/Implementação:** | Foi ajustado no tratamento do CC 344 para efetuar o lançamento sempre que a data com a projeção do aviso prévio indenizado for até 30 dias antes da data base informada no Sindicato. |
| **Chamados relacionados:** | *TVJX74, TWCTKC* |

divs
