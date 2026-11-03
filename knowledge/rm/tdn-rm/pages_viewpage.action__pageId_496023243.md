---
content_hash: 17671f9b80e012f70f716411ff83d2b35b9b9000ec6d401082ded8aadb9f68a3
fetched_at: '2026-06-29T00:10:22.006565+00:00'
page_id: '496023243'
product: rm
source: tdn-rm
title: 5261240 FISCAL01-8449 - EFD Contribuições - F525 campo3, campo4 e campo10
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=496023243
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Gestão Fiscal |
| Função: | Gerador de Saídas |
| Ticket: | 5261240 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-8449 |

## **02. SITUAÇÃO/REQUISITO**

Na geração do EFD Contribuições o campo 3 do Registro F525 está sendo preenchido conforme campo na tela  
da rotina para lançamento com cliente fornecedor do exterior

## **03. SOLUÇÃO**

Na geração do EFD Contribuições o campo 3 e o campo 10 do Registro F525, foram realizadas alterações no  
Layout, para serem gerados de acordo com o Cliente/Fornecedor do Lançamento (Nacional ou Exterior).

## **04. DEMAIS INFORMAÇÕES**

* Para os registros com Cli/For do Exterior

         Campo 3 será gerado com o valor 99 

         Campo 10 será gerado com a mensagem “Cliente do Exterior”

         Campo 4, se existir CPF/CNPJ será preenchido, caso contrário o campo 4 será gerado vazio

* Para os registros com Cli/For Nacional

         Campo 3 será gerado com valor  “01” para pessoa física e “04” para pessoa jurídica.

         Campo 10 será gerado em branco

        Campo 4, se existir CPF/CNPJ será preenchido, caso contrário o campo 4 será gerado vazio

* Para o registro totalizador de juros e multas:

         Deverá ser gerado no campo 3 com o valor 99

         Campo 10 será gerado vazio.
