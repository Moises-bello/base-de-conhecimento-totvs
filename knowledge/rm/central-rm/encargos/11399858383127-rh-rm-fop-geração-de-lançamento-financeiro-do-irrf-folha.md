---
article_id: 11399858383127
category: Encargos
content_hash: 338a6f7b23cac4393c52277ab322258ef75c93de57788ed1fa6c1cdcceb4f229
fetched_at: '2026-06-28T22:46:52.365858+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RH - RM - FOP - Geração de lançamento financeiro do IRRF Folha
type: support-article
updated_at: '2025-01-24T15:26:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11399858383127-RH-RM-FOP-Gera%C3%A7%C3%A3o-de-lan%C3%A7amento-financeiro-do-IRRF-Folha
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como gerar o lançamento financeiro com o tipo 5- IRRF FOLHA?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Acessar encargos | Cadastros financeiros | Parâmetros:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11399502552599)

Preencha a parametrização conforme necessidade da empresa:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11399503992599)

O parâmetro financeiro precisa está associado a um código de lançamento ativo, para ser utilizado no momento do lançamento:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11399602895127)

Verifique valor lançado em folha no evento com CC04:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11399605910679)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11399657603607)

Esse lançamento considerado IRRF a Pagar :

É a soma dos valores de todos os eventos de código de cálculo de descontos especificados abaixo, subtraindo a soma dos eventos de proventos, que estão na ficha financeira do funcionário para o mês e ano de competência especificados.

Desconto:

 004 - IRRF

 084 - IRRF calculado pelo usuário

127 - IRRF de participação nos lucros

 346 - IRRF Retificação

Provento:

 122 - Restituição de I.R.R.F.

**Importante**: O evento de código de cálculo 127 será considerado na soma apenas se não for criado um lançamento financeiro do tipo **IRRF de Participação nos Lucros**

Geração do lançamento:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11399695878423)

Marcar o parâmetro ativo financeiro conforme a parametrização realizada dentro do cadastro do mesmo:

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11399763203991)

Informar a data da apuração que necessitar:

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11399733505175)

Dessa forma o lançamento será gerado:

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11399739644055)

Saiba mais: [Clique aqui](https://tdn.totvs.com/display/public/LRM/Cadastros+Financeiros)
