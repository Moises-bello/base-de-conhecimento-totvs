---
content_hash: a16215690af64432282560098de73b4e8ae906ec132c574b83713e0c11480e94
fetched_at: '2026-06-29T00:06:06.878703+00:00'
page_id: '201732910'
product: rm
source: tdn-rm
title: TSZKB5_DT_Lançamento_Com_Bolsa_Exclusiva_E_De_Crédito
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=201732910
version: 1
---

# GERAÇÃO DE LANÇAMENTOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Gestão Educacional* |
| **Função:** | *Geração de lançamentos com bolsa exclusiva* |
| **Situação/Requisito:** | *Ao gerar um lançamento financeiro para uma parcela associada a um serviço contábil e com duas bolsas, sendo uma delas bolsa de crédito e a outra uma bolsa do tipo exclusiva, o sistema tenta gerar o lançamento para a bolsa de crédito que não possui valor. Com isso, as partidas contábeis do evento não são carregadas, causando falha durante a contabilização de inclusão do lançamento financeiro.* |
| **Solução/Implementação:** | *Foi realizada otimização do processo de geração de lançamentos financeiros, de forma a evitar o processamento de bolsas que estejam aplicadas a uma parcela que já possua uma bolsa do tipo exclusiva.* |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *N/A.* |
| **Requisito (ISSUE):** | *N/A.* |
| **Versões/Release:** | *11.82.41* |
