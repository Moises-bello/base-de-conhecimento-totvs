---
content_hash: ccbaec681296f8d8a58398b3af0ed2690ffd845706e7e38a9984472a52f04200
fetched_at: '2026-06-29T00:10:51.475044+00:00'
page_id: '568919493'
product: rm
source: tdn-rm
title: 9309666 FISCAL01-13752 DT EFD-CONTRIBUICOES Carregamento dados conta Dispensa
  de ECD - IN RFB nº 1.774/2017
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=568919493
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: |  |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Geração de arquivo EFD-Contribuições |
| Ticket: | 9309666 |
| Requisito/Story/Issue (informe o requisito relacionado) : |  |

## **02. SITUAÇÃO/REQUISITO**

No momento da geração do EFD Contribuições ocorre o seguinte erro:  
"Erro: Erro durante carregamento dos dados do lançamento. Ident. Lançamento: 347394.  
Erro: Erro ao carregar dados dos itens - Ident. Lançamento: 347394.  
Erro: Erro ao Carregar os dados da conta Dispensa de ECD - IN RFB nº 1.774/2017. Motivo: Object reference not set to an instance of an object."

## **03. SOLUÇÃO**

Foram feitas alterações para que sejam carregados os dados da conta contábil "Dispensa de ECD - IN RFB nº 1.774/2017" a fim de impedir que ocorram erros durante a geração da EFD-Contribuições.
