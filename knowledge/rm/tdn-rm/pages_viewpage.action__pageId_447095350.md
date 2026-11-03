---
content_hash: bfdbb45f2e08e21743f2f3c05d80122b400d6b891f92bbc8e52564ba84a1930d
fetched_at: '2026-06-29T00:09:55.550424+00:00'
page_id: '447095350'
product: rm
source: tdn-rm
title: PORTALMOBILE01-6523 DT 4736872 Tags de valor ficando em branco no contrato
  de matrícula
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=447095350
version: 1
---

# Tags de valor ficando em branco no contrato de matrícula

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Gestão Educacional |
| **Módulo:** | Educacional |
| **Função:** | Contrato durante o processo de matrícula online |
| **Situação/Requisito:** | Ao utilizar as tags [VALOR P], [VALOR LIQUIDO P], [VALOR PARC P] e [NUM PARC P] no texto de contrato financeiro que é exibido durante o processo de matrícula online, os valores não eram atualizados de acordo com o plano de pagamento correto. |
| **Solução/Implementação:** | O plano de pagamento utilizado para substituir os valores das tags citadas acima é seguida nesta ordem:  1) Se o aluno possuir algum contrato financeiro, é utilizado o plano de pagamento do contrato do aluno.  2) Se o aluno não possuir contrato, utiliza o plano de pagamento default da parametrização por curso.  Caso esteja parametrizado na matrícula online para exibir os planos de pagamentos, as TAGs de valores do plano de pagamento serão substituídas de acordo com o plano de pagamento selecionado pelo aluno durante o processo de matrícula. Portanto, se este parâmetro estiver marcado é imprescindível que possua ao menos um plano de pagamento cadastrado no anexo "Séries do plano de pagamento" para o ensino básico, ou "Habilitações do plano de pagamento" para o ensino superior. E os valores deste plano selecionado é que será utilizado prioritariamente para substituir as TAGs no contrato. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
| **Pacote:** | N/A |
