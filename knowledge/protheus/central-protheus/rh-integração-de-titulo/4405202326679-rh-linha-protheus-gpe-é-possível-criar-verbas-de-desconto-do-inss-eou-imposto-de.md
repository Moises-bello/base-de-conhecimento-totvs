---
article_id: 4405202326679
category: RH - Integração de Titulo
content_hash: 1189328d0e81275fd5fd144eb05604072436f3cb2e7824245ee5b20f076625df
fetched_at: '2026-06-28T22:43:36.304351+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus - GPE - É possível criar verbas de desconto do INSS e/ou
  Imposto de Renda dos Autônomos e Pro-laboristas para a Contabilização
type: support-article
updated_at: '2025-07-18T13:38:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405202326679-RH-Linha-Protheus-GPE-%C3%89-poss%C3%ADvel-criar-verbas-de-desconto-do-INSS-e-ou-Imposto-de-Renda-dos-Aut%C3%B4nomos-e-Pro-laboristas-para-a-Contabiliza%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33557946691607) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**É possível criar verbas de desconto do INSS e/ou Imposto de Renda para os Autônomos e Pro-laboristas visando atender o processo de Contabilização?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.  
  
**Solução**

O Produto Padrão não possui identificadores exclusivos para desconto de contribuições de Autônomos e/ou Pro-laboristas. Para atender sua necessidade será necessário criar uma fórmula no **Lançamento Padrão - CTBA080** atribuído aos **Identificadores de Cálculo**  **0009 - I.R. do Adiantamento**, **0064 - INSS** e **0066 I.R.** destas **Verbas - GPEA040**, efetuando um filtro de busca na tabela SRA - Funcionários por aqueles que possuem no campo **Cat. Func. - RA\_CATFUNC** o conteúdo **A - Autônomo** e/ou **P  - Pró-labore** , creditando/debitando em contas diferentes dos demais funcionários.  
  
Caso necessite de apoio para configurar/criar lançamentos padrões utilizando expressões em ADVPL, solicitamos que acione o suporte **Protheus ADVPL**.  
  
**Saiba Mais**  
[Artigos sobre Contabilização](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109092-RH-Contabiliza%C3%A7%C3%A3o)  
[RH - Linha Protheus - GPE - Como configurar Lançamento Padrão para Folha de Pagamento do Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021101152-RH-Linha-Protheus-GPE-Como-configurar-Lan%C3%A7amento-Padr%C3%A3o-para-Folha-de-Pagamento-do-Protheus-)  
[RH - Linha Protheus - GPE - Desconto do INSS de Pro Labore apresenta verba de id.de cálculo 0064 e não na verba de id.de calculo 0222](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052126633-RH-Linha-Protheus-GPE-Desconto-do-INSS-de-Pro-Labore-apresenta-verba-de-id-de-c%C3%A1lculo-0064-e-n%C3%A3o-na-verba-de-id-de-calculo-0222-)
