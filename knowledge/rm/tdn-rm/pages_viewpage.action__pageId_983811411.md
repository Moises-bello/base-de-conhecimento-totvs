---
content_hash: 2c1b3f62d1d8cd3b28c1b25c28a45c5079f2cb2403d979de9cbac4852813343c
fetched_at: '2026-06-29T00:12:16.270592+00:00'
page_id: '983811411'
product: rm
source: tdn-rm
title: FISCAL01-24592 NFE - Status "Denegado" - A nota não pode ser inutilizada
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=983811411
version: 1
---

## **01. DADOS GERAIS**

| Produto: | TOTVS |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | BackOffice |
| Módulo: | Gestão de Estoque, Compras e Faturamento |
| Função: | Consulta Nfe |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-24592 |

## **02. SITUAÇÃO/REQUISITO**

> Desde o dia 1º de agosto, entrou em vigor o ajuste Sinief 43/2023 onde o retorno de uma nota por Denegação passa **a não ser** um evento, mas uma rejeição.  
>    
> Desse modo, as notas rejeitadas poderão ter sua numeração reutilizada ou inutilizada.
>
> No cenário atual, quando uma nota fiscal é denegada o movimento fica travado não sendo possível a reutilização do mesmo ou a inutilização da numeração.  
>    
> Validamos que houve alteração na descrição dos códigos além da criação do código 781 conforme abaixo.
>
> <u>[https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=kIiniiSkpKc=](https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=kIiniiSkpKc= "Follow link")</u>

## **03. SOLUÇÃO**

Foi retirada a validação no método WsConsultarNotas que verificava se o código de retorno da nota fosse (301, 302, 303) o status da Nfe seria alterado para Denegado, com a alteração esse status muda para rejeitada.
