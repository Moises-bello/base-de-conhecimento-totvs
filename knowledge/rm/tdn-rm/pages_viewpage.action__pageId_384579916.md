---
content_hash: f301087473811e9b29ca45b4f3fc167fb6224dfb1238bc3d47a01efcd0c6e109
fetched_at: '2026-06-29T00:09:07.583611+00:00'
page_id: '384579916'
product: rm
source: tdn-rm
title: CONTROLADORIA01-1809 DT Lançamento Financeiro - Contabilidade com diferença
  entre Débito e Crédito
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=384579916
version: 4
---

# Lançamento Financeiro - Contabilidade com diferença entre Débito e Crédito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Totvs Gestão Financeira. |
| **Função:** | Inclusão de Lançamento com tipo contábil = Contábil |
| **Situação/Requisito:** | Caso esteja sendo gerado um lançamento financeiro, com valor líquido igual a zero, para uma parcela do contrato de um aluno do TOTVS Educacional e o sistema esteja parametrizado para realizar a baixa automática do lançamento, pode ocorrer de existir um evento contábil parametrizado para ser executado na baixa. Caso o lançamento financeiro gerado seja contábil (contabilização na inclusão) e o evento da contabilização de baixa falhe por uma diferença entre débito e crédito, uma mensagem do TOTVS Gestão Contábil é encaminhada para o Educacional que por sua vez, é apresentada ao usuário. Como a mensagem informada diz apenas que "Não foi possível salvar o lançamento contábil, pois a existe uma diferença entre o valor de débito e o valor de crédito.", não é imediata a conclusão de qual evento que está sendo processado e qual operação está sendo realizada. Com isso, pode existir uma demora significativa no diagnóstico do problema pelo suporte e desgaste com o cliente. Por isso, demandamos que mais informações sejam acrescentadas a mensagem como o código do evento que está sendo processado e se é uma operação de inclusão ou baixa do lançamento financeiro. |
| **Solução/Implementação:** | Melhoria na mensagem e aviso do Gestão Contábil para que sejam informados o produto, o processo e o código do Evento Contábil que originaram a contabilização que apresentou aviso de diferença entre débitos e créditos. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A. |
