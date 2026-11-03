---
content_hash: c210a80175b5c3f4175f84ac207672d0d1e7a712f806405210b04154560d9d73
fetched_at: '2026-06-29T00:12:06.888708+00:00'
page_id: '917129381'
product: rm
source: tdn-rm
title: DT - Integração RM X Ahgora - Disponibilização da Localização
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=917129381
version: 8
---

## **1. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Integração RM X Ahgora - Disponibilização da Localização |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-11997](https://jiraproducao.totvs.com.br/browse/DRHROTRM-11997) |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2402.271
* 12.1.2406.229
* 12.1.2410.160 e superiores

## **03. SITUAÇÃO/REQUISITO**

Criação de um campo para enviar a localização do funcionário para o produto Ponto Web (Ahgora).

## **04. SOLUÇÃO**

Para possibilitar o envio deste campo foi criada a aba **Fórmula para Localizações** no menu  RH | Folha de pagamento | Configurações | Parametrizador | 06.02 - Integrações | 06.02.11 - Ahgora.

Nesta aba será realizada a vinculação de fórmulas onde pode ser usada funções padrão do produto para retornar a informação ou a criação de novos campos.

Exemplo de criação de Fórmula:

Após a vinculação das fórmulas no parametrizador, sempre que houver integração de um funcionário (Inclusão/Alteração) as localizações serão enviadas.

## **05. DEMAIS INFORMAÇÕES**
