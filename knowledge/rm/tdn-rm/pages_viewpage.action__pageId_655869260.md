---
content_hash: 37e60ea009c7c5511089e859fae66be7584f6468982639a9f545e25018dd842b
fetched_at: '2026-06-29T00:11:12.631327+00:00'
page_id: '655869260'
product: rm
source: tdn-rm
title: DT FISCAL01-17170 - NFS-e Bento Gonçalve Rejeição - 0000 - 00180 - A Hora da
  geração do recibo de prestação do serviço (RPS)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=655869260
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Envio NFSe |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-17170 |

## **02. SITUAÇÃO/REQUISITO**

Ao consultar a autorização da NFS-e para o município de Bento Gonçalves/RS a seguinte mensagem abaixo está sendo apresentada.

0000 - 00180 - A Hora da geração do recibo de prestação do serviço (RPS) está indefinida ou foi declarada incorretamente

*Obs. O tag dthremissao do XML gerado pelo layout único no RM está sendo gerado fora do padrão especifico da Prefeitura sem a informação do horário.*\_  
<dthremissao>2021-12-14T00:00:00</dthremissao>

*Layout único*  
\_[https://tdn.totvs.com/display/public/LRM/Identificacao](https://tdn.totvs.com/display/public/LRM/Identificacao "Follow link")

Data e hora da emissão do documento. Formato AAAA-MM-DDTHH:mm:ss

## **03. SOLUÇÃO**

**Ajuste na tag dthremissao do XML da NFSE, a hora de emissão, ao invés de zerada, irá vir preenchida de acordo com o registrado no movimento.**
