---
content_hash: 2b7a5cec41f4c1726db53ff217d7b310aa0957b68f3ecb63e1f8e41af45bf8c3
fetched_at: '2026-06-29T00:09:38.468448+00:00'
page_id: '425919697'
product: rm
source: tdn-rm
title: 3767384 FISCAL01-6751 DT EFD - Contribuições Registro 1900
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425919697
version: 1
---

Tempo aproximado para leitura:**02 min**

****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | Gestão Fiscal |
| Função: | EFD - Contribuições |

**02. SITUAÇÃO/REQUISITO**

Ao gerar o arquivo da EFD Contribuições, identificou que os valores contidos nos registros F500 e F525,   
não bate com o computado no único registro 1900, o registro 1900 é gerado, porém com o valor zerado.

**03. SOLUÇÃO**

Ajuste na Geração do Registro 1900 da EFD - Contribuições para que os Lançamentos Financeiros que sejam gerados direto do Movimento sejam contemplados  
no registro.
