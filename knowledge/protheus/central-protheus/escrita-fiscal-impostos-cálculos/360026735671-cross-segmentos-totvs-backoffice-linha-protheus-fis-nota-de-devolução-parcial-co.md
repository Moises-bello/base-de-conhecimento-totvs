---
article_id: 360026735671
category: Escrita Fiscal - Impostos - Cálculos
content_hash: 10e96f8dfa7a540ee19518627ef5b26e855b96dec8786abc1058cf52c2fecda8
fetched_at: '2026-06-28T22:39:31.092607+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Nota de Devolução
  Parcial com Impostos
type: support-article
updated_at: '2026-05-29T14:15:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026735671-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Nota-de-Devolu%C3%A7%C3%A3o-Parcial-com-Impostos
---

**Dúvida**

Como devo proceder para escriturar uma nota fiscal do tipo devolução parcial?

**Ambiente**

Protheus – Compras e/ou Faturamento – A partir da versão 11.80

**Solução**

Quando se trata de nota de devolução é necessário que a nota devolvida seja um espelho da nota fiscal de origem, contudo, em alguns casos, o cliente precisa escriturar uma nota de devolução parcial. Para isso é preciso utilizar a configuração abaixo no cadastro do TES:  
  
O Sistema olha o campo **F4\_DEVPARC (**DEV. Par Prop.)

**Help do campo:**

Indica se ao realizar devolução parcial a base de ICMS deve ser proporcionalizada de acordo com a NF original.

1= Sim (o calculo será refeito de acordo com os cálculos da Nf de origem)  
2= Não (o calculo será refeito de acordo com os cadastros e parâmetros atuais).
