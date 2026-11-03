---
content_hash: 638253bce7245055bdde8b5efd2bb458d788dca6f70cfd6bfe4973a00106f5cc
fetched_at: '2026-06-29T00:10:16.552393+00:00'
page_id: '471946973'
product: rm
source: tdn-rm
title: Contabilizar Baixa de Crédito de Adiantamento Associado a Baixa de Lançamento
  de Outra Filial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=471946973
version: 5
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Baixa |
| Função: | Contabilização de Baixa de Crédito de Adiantamento |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [FINANCEIRO01-10756](http://jiraproducao.totvs.com.br/browse/FINANCEIRO01-10756) |

## **02. SITUAÇÃO/REQUISITO**

Em uma situação onde o adiantamento recebido de um cliente ocorre em uma determinada filial, mas a baixa do serviço ocorre em outra, constatou-se que a baixa do Crédito de Adiantamento deve ser contabilizada, de modo que fique corretamente indicada a situação de transferência de recursos financeiros entre duas ou mais filiais.

## **03. SOLUÇÃO**

Foi disponibilizado um novo parâmetro "Contabilizar crédito de adiantamento em filiais distintas" no parametrizador, na opção "Contas a Receber | Baixa 3/6", de modo que o comportamento possa ser habilitado e desabilitado. Por default, o comportamento padrão é "desabilitado", de modo a manter a compatibilidade retroativa.

No cadastro da tabela responsável pelo Evento Contábil Default (representada por uma das tabelas opcionais ou pela tabela de tipo de documento), foi disponibilizado novo campo "Evento Contábil para Baixa de Crédito de Adiantamento" na aba "Eventos Contábeis". Este campo deve ser associado a novo evento contábil para contabilização do crédito de adiantamento.

Caso o tipo contábil de um lançamento com classificação Adiantamento seja "Contábil" ou "Baixa Contábil", a sua baixa irá gerar um lançamento de classificação Crédito de Adiantamento, de natureza inversa  e  com tipo contábil "Baixa Contábil".

Em condições convencionais, a baixa de um lançamento vinculado a outro com classificação Crédito de Adiantamento irá gerar uma baixa com tipo Contábil em conformidade com seu próprio tipo contábil, e uma segunda baixa com tipo contábil "Não Contábil" no lançamento de classificação Crédito de Adiantamento associado.

Entretanto, se a baixa do lançamento vinculado atender aos requisitos abaixo, a baixa do lançamento com classificação Crédito de Adiantamento será contabilizado:

* + O parâmetro "Contabilizar crédito de adiantamento em filiais distintas" estiver habilitado.
  + Haver um evento contábil default informado no campo "Evento Contábil para Baixa de Crédito de Adiantamento".
  + O lançamento de Crédito de Adiantamento tenha tipo contábil "Baixa Contábil".
  + O lançamento vinculado e o lançamento de Crédito de Adiantamento sejam de filiais distintas.

## **04. DEMAIS INFORMAÇÕES**

Outras ações/ações relacionadas 

**Ao definir o evento contábil para o item de baixa do lançamento de classificação Crédito de Adiantamento, deve se atentar que este tipo de baixa sempre terá o valor baixado 0 (zero). O item de baixa gerado sempre terá o valor do vínculo informado no campo Valor Original Baixado, fechando com o valor informado no campo Valor Vinculado.IMPORTANTE!**

## **05. ASSUNTOS RELACIONADOS**
