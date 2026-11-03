---
content_hash: 2fcfbf6807746c0a3050d7e6404c535f5e445e20e1e2f0780930f4182f4990fa
fetched_at: '2026-06-29T00:09:19.459334+00:00'
page_id: '421393783'
product: rm
source: tdn-rm
title: 4125752 FISCAL01-6853 DT NFC-e - Envio NFC-e - DHEMI
type: documentation
url: https://tdn.totvs.com/display/LRM/4125752+FISCAL01-6853+DT+NFC-e+-+Envio+NFC-e+-+DHEMI
version: 1
---

Tempo aproximado para leitura:**02 min**

****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | Gestão Fiscal |
| Função: | Envio NFC-e 4.00 |

**02. SITUAÇÃO/REQUISITO**

Ao realizar o envio de uma NFC-e, versão 4.00, está apresentando a seguinte mensagem de inconsistência:

"Mensagem de erro: invalid property \_DHEMI"

**03. SOLUÇÃO**

Ajuste no Processo de Envio da NFC-e para que quando estiver parametrizado na Filial para enviar a Nota Fiscal na versão 4.00 o sistema não verifique o Parâmetro HABILITANFESEFAZ,

e faça o envio no Modelo "SEFAZ" conforme já e realizado no Envio de NF-e.
