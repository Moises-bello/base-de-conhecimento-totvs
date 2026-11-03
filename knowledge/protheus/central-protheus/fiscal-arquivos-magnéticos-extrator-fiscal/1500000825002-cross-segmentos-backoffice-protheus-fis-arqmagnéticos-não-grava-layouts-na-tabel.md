---
article_id: 1500000825002
category: Fiscal Arquivos Magnéticos - Extrator Fiscal
content_hash: ff889283cd61e82fc450b57e9c6657413007dd610d5e4cee05af82dcf7081eac
fetched_at: '2026-06-28T22:42:07.926616+00:00'
product: protheus
section_id: 1500001535021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Não Grava Layouts
  na Tabela TAFST2
type: support-article
updated_at: '2022-08-18T17:45:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000825002-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-N%C3%A3o-Grava-Layouts-na-Tabela-TAFST2
---

**Dúvida**  
Após executar o Extrator Fiscal, não foram gravados registros na tabela TAFST2 referente os layouts para processamento no TAF.   
  
**Ambiente**  
Microsiga Protheus – TAF – A partir da versão 12  
  
**Solução**  
O problema de não gravar registros referente os layouts na tabela TAFST2 para processamento no TAF, ocorre quando os parâmetros abaixo não estão configurados corretamente:   
  
MV\_TAFTALI = "Deve ser informado no nome do TOPALIAS do seu ambiente dentro do appserver.ini"  
  
MV\_TAFTDB = "Deve ser informado nome do banco do seu ambiente Exemplo MSSQL ou MSSQL7 informado no seu TOPBASE dentro do appserver.ini"  
  
MV\_TAFPORT = Indica o número da porta do serviço do TopConnect (porta do DBAccess)  
  
MV\_TAFINT = .T.
