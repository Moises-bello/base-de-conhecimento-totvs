---
content_hash: e28bbd3fc9f4c331a049ebaf713ed92a9489d88c0d4ba3f303319920312509f4
fetched_at: '2026-06-29T00:08:51.974611+00:00'
page_id: '338374593'
product: rm
source: tdn-rm
title: 1176658 FOPROTINAS01-1156 DT Beneficiário Residente ou Domiciliado no Exterior
  Considerado na DIRF Conferência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=338374593
version: 7
---

# CONSIDERAR BENEFICIÁRIO RESIDENTE OU DOMICILIADO NO EXTERIOR PARA A GERAÇÃO DA DIRF CONFERÊNCIA

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | DIRF |
| **Situação/Requisito:** | Os beneficiários residentes ou domiciliados no exterior não são considerados na geração da DIRF Conferência. |
| **Solução/Implementação:** | Os beneficiários residentes ou domiciliados no exterior passaram a ser contemplados também na DIRF Conferência. Para que eles sejam considerados, é necessário:   1. Que o funcionário seja do tipo 'X - Expatriado' (acessando Administração de Pessoal | Cadastros | Funcionários, e editando o funcionário desejado) 2. Acessando o anexo Folha de Pagamento | Dados do Residente ou Domiciliado no Exterior, do cadastro de Funcionários, informar o país onde ele esteve alocado e os dados fiscais referentes aos pagamentos realizados no período em que o funcionário foi residente ou domiciliado no exterior 3. Acessando a ficha financeira do funcionário e editando os períodos correspondentes aos pagamentos efetuados para o residente ou domiciliado no exterior, informe o país onde ele esteva alocado ao receber o pagamento (**Atenção**: Caso o envelope de pagamento seja recalculado após a realização desse passo, ele deverá ser refeito) 4. Ao gerar a DIRF Conferência (acessando Anuais | Rotinas | DIRF/Informe de Rendimentos | DIRF/Informe de Rendimentos), não se esqueça de assinalar que foi realizado pagamento a residentes ou domiciliados no exterior nos parâmetros específicos da coligada em que ele está alocado     Observe que apenas os as linhas INC IRRF e IRRF deverão ser exibidas para os beneficiários residentes ou domiciliados no exterior |
| **Tickets relacionados:** | 1176658 |
