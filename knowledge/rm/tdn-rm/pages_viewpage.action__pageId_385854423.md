---
content_hash: 8a9cbd0a4d454bfde9521017b58a2741626b587066a5b9f30b332a6e3ac3d4ef
fetched_at: '2026-06-29T00:09:07.893411+00:00'
page_id: '385854423'
product: rm
source: tdn-rm
title: FISCAL01-5771 DT Integração RM x TAF - Filtro de lançamentos fiscais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=385854423
version: 2
---

# Filtro de lançamentos fiscais

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | TOTVS Gestão Fiscal |
| **Função:** | Integração RM x TAF |
| **Situação/Requisito:** | Necessidade de filtrar a geração de registros para caso haja necessidade de retificação pontual de alguns lançamentos |
| **Solução/Implementação:** | Inclusão de filtro de Lançamentos Fiscais na tela de geração de registros da integração RM x TAF |

No processo de geração de registros, na tela de integração RM x TAF, foi incluído um filtro de lançamento fiscal:

Nele é possível filtrar os registros para que gerem somente os referentes aos lançamentos filtrados,   
desde que o filtro não contenham parâmetros que tenham que ser informados posteriormente.  
  
  
  
Ao clicar no botão de filtro uma tela será exibida com os filtros já configurados na tela de lançamentos fiscais:

Observações:

* **O filtro de lançamentos funcionará em conjunto com a data inicial e final selecionada, assim como a filial.**
* Ao executar o processo com filtro de lançamento, somente o lançamento filtrado e seus registros correspondentes (filhos) serão gerados.   
  Para geração dos demais registros, é necessária a execução sem o filtro de lançamento.
