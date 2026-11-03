---
article_id: 41259435394967
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 65b5c5860d1abc3b7a94d921a1686fcd679a0e987c0c11233142aa6695111403
fetched_at: '2026-06-28T22:37:22.929310+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Help CNTA300OPNPERM
  ao usar opção "Excluir Cronograma Financeiro" em uma Revisão de Contrato
type: support-article
updated_at: '2026-06-16T12:09:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41259435394967-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Help-CNTA300OPNPERM-ao-usar-op%C3%A7%C3%A3o-Excluir-Cronograma-Financeiro-em-uma-Revis%C3%A3o-de-Contrato
---

O Help CNTA300OPNPERM ocorre ao tentar excluir o Cronograma Financeiro em revisão de contrato vigente no TOTVS Gestão de Contratos, pois essa exclusão não é permitida após o contrato estar vigente. Para utilizar a opção de excluir o cronograma, o contrato deve ser retornado ao status "Em Elaboração". A exclusão só é permitida na revisão quando o cronograma foi incluído na mesma revisão.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41259443342103) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**

Help CNTA300OPNPERM ao usar opção "Excluir Cronograma Financeiro" em uma revisão de Contrato.

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões

**Solução**

O  help CNTA300OPNPERM, ocorre quando se esta tentando executar uma "operação não permitida" pela rotina.

Para um contrato que foi incluído com Cronograma Financeiro, após o contrato se tornar Vigente, pelo conceito do módulo, no processo de Revisão não é permitida a exclusão do Cronograma Financeiro que foi incluído na inclusão do contrato, mesmo que o cronograma não tenha tido nenhuma movimentação.

Neste caso, como não ouve movimentação para a planilha/contrato, para se excluir o cronograma a possibilidade é retornando o contrato para o status "Em Elaboração", e estando o Contrato neste status, utilizar a opção "Alterar" e assim é permitida a utilização da opção para se "excluir" o Cronograma Financeiro.

No processo de Revisão, a opção de "Excluir Cronograma Financeiro" tem sua utilização permitida apenas quando é incluída uma nova planilha em que acabou de ter sido incluído um cronograma financeiro, e assim nessa mesma revisão que está sendo realizada, a rotina permite a exclusão do cronograma que acabou de ser incluído.

***Saiba Mais:***

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
