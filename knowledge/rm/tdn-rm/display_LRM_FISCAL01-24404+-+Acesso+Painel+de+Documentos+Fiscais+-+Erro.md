---
content_hash: e549889045a7d6de83cd528491e55f683d35186e8253a87d8ce0bb6eb03c5c41
fetched_at: '2026-06-29T00:12:01.637829+00:00'
page_id: '897290391'
product: rm
source: tdn-rm
title: FISCAL01-24404 - Acesso Painel de Documentos Fiscais - Erro
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-24404+-+Acesso+Painel+de+Documentos+Fiscais+-+Erro
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão de Estoque |
| Função: | Painel de Documentos Eletrônicos |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-24404 |

## **02. SITUAÇÃO/REQUISITO**

Ao tentar acessar o Painel de Documentos Eletrônicos, a tela fica carregando e não conclui o acesso, informando que excedeu o número de licenças ou que não é possível consumir a licença Quarteto.

## **03. SOLUÇÃO**

Foi liberada a permissão para que o movimento pudesse acessar as APIS do fiscal, para isso foi inserido nas controllers das APIS o atributo [RMSLicense(Sistema = CodSistema.Mov)].

Disponível à partir da biblioteca 12.1.2406
