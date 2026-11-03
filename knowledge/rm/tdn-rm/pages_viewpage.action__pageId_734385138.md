---
content_hash: c64f4e1e4b26246a60976843599a077ca8ec4ab1e4d771c149c60dbf09903988
fetched_at: '2026-06-29T00:11:29.229619+00:00'
page_id: '734385138'
product: rm
source: tdn-rm
title: DT - Férias - Cancelamento de Férias Pagas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=734385138
version: 4
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Férias |
| País: | Brasil |
| Releases: | a partir da 12.1.2302 |
| Issue: | [DRHCALCRM-2826](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-2826) |

## **02. SITUAÇÃO/REQUISITO**

Ao realizar o cancelamento de férias, cujo pagamento já foi efetuado, é necessário lançar manualmente o desconto do liquido de férias na folha de pagamento do funcionário. O cliente deseja que quando houver o cancelamento de férias, cujo pagamento já tenha ocorrido, o sistema armazene o valor do líquido de férias e realize o lançamento automaticamente na próxima folha mensal do funcionário.

## **03. SOLUÇÃO**

Foi criado no processo de cancelamento global de férias o parâmetro '**Armazena líquido como Evento Programado**'. Ao marcar este parâmetro, o sistema irá gravar na tabela de 'Eventos Programados' do funcionário, um evento para ser lançado no envelope de pagamento, com o valor do desconto de líquido de férias canceladas.

## **04. DEMAIS INFORMAÇÕES**

[Cancelamento de Férias Pagas](https://tdn.totvs.com/pages/viewpage.action?pageId=734385195)
