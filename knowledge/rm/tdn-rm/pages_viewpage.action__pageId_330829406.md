---
content_hash: a12bd9951e012e250168271e21ba5e9165773833cb6241b1afbdbc007545a20f
fetched_at: '2026-06-29T00:08:49.419221+00:00'
page_id: '330829406'
product: rm
source: tdn-rm
title: 1986648 DEDUINTEGRACOES-1480 DT Lançamento com 100% Bolsa Não Baixa Automaticamente
  pela Matricula
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=330829406
version: 1
---

# Geração de Lançamento

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Geração de lançamento |
| **Situação/Requisito:** | O aluno possuí um plano de pagamento com seis parcelas e uma bolsa de 100% com o tipo de sacado marcado como outro sacado, e nos parâmetros de matricula no portal está marcado para gerar os lançamentos das seis parcelas, na integração financeira o parâmetro “baixar automaticamente lançamentos com valor liquido igual a zero”, está marcado, após confirmar a matricula no portal, o sistema não está baixando os lançamentos referente ao aluno deixando os mesmos em aberto da parcela 1 até a 5, a parcela 6 o sistema já faz corretamente baixando o lançamento do aluno, mas quando você vai no financeiro aba baixas do lançamento está vindo com 6 "Baixas de lançamento". |
| **Solução/Implementação:** | Ajuste no serviço de baixa de lançamento automaticamente, pois ao realizar a geração de lançamento pelo processo de matricula, por exemplo, parcela de 1 a 6 com 100% bolsa o sistema estava baixando somente a parcela 6 e gerando 6 itens de baixa para esta parcela. |
| **Conversores e Parâmetros:** |  |
| **Tickets relacionados:** |  |
| **Requisito:** |  |
| **Documento de Referência:** |  |
