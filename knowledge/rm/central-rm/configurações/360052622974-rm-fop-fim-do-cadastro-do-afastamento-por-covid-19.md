---
article_id: 360052622974
category: Configurações
content_hash: 861a0ec1595a31ac0da8400891aad8b109c24a68299b48cb116f193e8c2f219f
fetched_at: '2026-06-28T22:46:49.609916+00:00'
product: rm
section_id: 1500000834621
source: central-rm
title: RM - FOP - Fim do cadastro do Afastamento por COVID 19
type: support-article
updated_at: '2021-07-01T22:09:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052622974-RM-FOP-Fim-do-cadastro-do-Afastamento-por-COVID-19
---

**Dúvida**

Como proceder com o fim do cadastro do Afastamento por COVID 19?  
  
 **Ambiente**

RM - Totvs Folha de Pagamento - Versões:

* 12.1.25.271 ou superior
* 12.1.26.217 ou superior
* 12.1.27.173 ou superior
* 12.1.28.107 ou superior

**Solução**

Os colaboradores que estavam nesta situação antes da nota ser emitida pelo governo terão que reduzir a duração do cadastro feito para a data fim de 21/07/2020 para ser deduzido até esta data. Portanto, a partir da data 21/07/2020, não é permitido que seja cadastrado novos colaboradores nesta situação, pois não terão o direito a dedução. Para que novos cadastros não entrem nesta situação, é necessário somente cadastrar um afastamento com o motivo diferente do que está salvo em **Configurações | Parametrizador | Folha Normal | Afastamento.****Para não haver deduções na Guia referente aos 15 primeiros dias de Atestado Médico:**

Acesse **Administração de Pessoal | Cadastros Globais | Tabelas Dinâmicas**e selecione o sistema **Folha de Pagamento.** Localize a tabela **INT28.**

É possível utilizar qualquer motivo cadastrado na tabela INT28, exceto o código CV - Afastamento por Covid19, ou criar um novo tipo de afastamento para que não seja levado para dedução na guia.

**Obs.:** Não se deve retirar o cadastro que já está no parametrizador, conforme consta na imagem abaixo, pois se optar por remover remove-lo, não haverá dedução na guia e impactará o cálculo dos funcionários que estiverem com atestado já cadastrado.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360085858514/mceclip0.png)
