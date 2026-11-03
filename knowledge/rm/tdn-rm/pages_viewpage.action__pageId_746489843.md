---
content_hash: 53be0a6ad9b69673e5286332033a9d1fdecc6215dd11aae62fa9a571f27e9b96
fetched_at: '2026-06-29T00:11:32.329215+00:00'
page_id: '746489843'
product: rm
source: tdn-rm
title: FISCAL01-19127 DT -  Emissão de NF-e tag refNFeSig
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=746489843
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Emissão de NF-e |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-19127 |

## **02. SITUAÇÃO/REQUISITO**

Após as alterações na cópia por referência podemos afirmar que todas as chaves de acessos referenciadas estão gravadas na tela do Movimento, de forma que o processo sempre irá gerar as referências informadas nesta tela.

Devemos tratar no processo a geração da NF-e os campos **refNFe** e **refNFeSig**.

## **03. SOLUÇÃO**

Ajuste no Envio da NF-e para gerar a tag refNFeSig  quando a Chave de Acesso da NF-e referenciada tiver sido anonimizada no Movimento.

Disponível a partir da biblioteca 12.1.2205
