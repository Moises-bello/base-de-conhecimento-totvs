---
article_id: 1500011503642
category: Administração de Pessoal
content_hash: 1263d441d96b1fb015ec97cb9afe4ddb848f318279f3dcfce58e770b0a2b8e49
fetched_at: '2026-06-28T22:47:02.150024+00:00'
product: rm
section_id: 1500000861042
source: central-rm
title: RH - RM - FOP - Alteração global dos campos do cadastro para atender ao B.E.M
  MP 1.045/2021
type: support-article
updated_at: '2025-03-13T11:21:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011503642-RH-RM-FOP-Altera%C3%A7%C3%A3o-global-dos-campos-do-cadastro-para-atender-ao-B-E-M-MP-1-045-2021
---

**Dúvida**

Existe uma forma de alterar os campos do B.E.M de forma global?  
  
**Ambiente**

TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir das versões:

* 12.1.29.250
* 12.1.31.154
* 12.1.32.101 e superiores.

**Solução**

Os campos acima podem ser preenchidos de forma global através do processo de Alteração Global de Cadastro, usando fórmulas:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500018552082/mceclip0.png)  
  
Abaixo exemplificaremos algumas sugestões de fórmulas, porém as mesmas devem ser desenvolvidas/adaptadas pelo usuário de forma a atender a sua necessidade:

Data da mudança: Deverá ser informada ao executar a alteração global de dados do funcionário ou preenchida manualmente.  
  
![](https://tdn.totvs.com/download/attachments/617174252/image2021-5-14_16-20-41.png?version=1&modificationDate=1621020041673&api=v2)  
  
Tipo de adesão:

* Fórmula: **1 /\* TIPO DE ADESÃO  1 - REDUÇÃO DE JORNADA ACORDADO ENTRE EMPREGADO E EMPRESA\*/**
* Fórmula:**0 /\* TIPO DE ADESÃO  0 - SUSPENSÃO DE CONTRATO DE TRABALHO ACORDADO ENTRE EMPREGADO E EMPRESA\*/**

Data do acordo:

* Fórmula:  **"17/05/2021" /\*INFORME UMA DATA REDUÇÃO JORNADA ACORDADO ENTRE EMPREGADO E EMPRESA\*/**

Percentual de Redução da Jornada:

* Fórmula: **25,00 /\*INFORME O PERCENTUAL DE REDUÇÃO JORNADA ACORDADO ENTRE EMPREGADO E EMPRESA\*/**

Dias de duração do acordo:

* Fórmula: **30 /\*TEMPO DE DURAÇÃO DA REDUÇÃO DE CONTRATO ACORDADO ENTRE EMPREGADO E EMPRESA\*/**

Valor Reduzido:  Exemplo de fórmula para redução de jornada/salário em até 25%. Para demais reduções deverá ser adequado para contemplar o percentual. A fórmula respeita a redução não deixando o salário pago no mês menor que o salário mínimo

* Fórmula:

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500018534782/mceclip0.png)**

Data da Antecipação:

* Fórmula:  **"26/06/2021" /\* INFORME UMA DATA DE ANTECIPAÇÃO DO TÉRMINO DO CONTRATO ACORDADO ENTRE EMPREGADO E EMPRESA \*/**

Data do Cancelamento:

* Fórmula:  **"26/06/2021" /\* INFORME A DATA DE CANCELAMENTO DO CONTRATO ACORDADO ENTRE EMPREGADO E EMPRESA \*/**

Dias de Prorrogação:

* Fórmula:  **30 /\* QUANTIDADE DE DIAS DE PRORROGAÇÃO DO CONTRATO ACORDADO ENTRE EMPREGADO E EMPRESA \*/****![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500018806921/mceclip1.png)**

****Histórico****

Quando é feito o preenchimento dos campos acima, seja direto no Cadastro de Funcionário ou pelo processo Alteração Global de Campos do Cadastro, o sistema armazena a cada alteração de qualquer campo da aba B.E.M, um registro no histórico de Adesão ao Benefício Extraordinário Mensal B.E.M. Caso a data de mudança seja a mesma de um registro já existente, será feito somente a atualização dos dados, mesmo se o tipo de acordo, data do acordo sejam o mesmo.

Este histórico é necessário estar preenchido corretamente para os devidos cálculos referente a MP 1045, como o desconto do complemento da redução de Jornada, dias de estabilidade, verba indenizatória, etc.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500018535022/mceclip2.png)

Saiba mais: [Alteração Global Campos do Cadastro](https://tdn.totvs.com/pages/releaseview.action?pageId=617174252)
