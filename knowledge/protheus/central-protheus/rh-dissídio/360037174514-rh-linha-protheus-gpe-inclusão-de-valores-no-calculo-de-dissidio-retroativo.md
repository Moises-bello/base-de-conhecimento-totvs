---
article_id: 360037174514
category: RH - Dissídio
content_hash: 35605169ac7b7d9e551488861276b6c77fdb2edf724a5c1da3e81cf703b870e3
fetched_at: '2026-06-28T22:43:43.600018+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - Inclusão de valores no calculo de dissidio retroativo
type: support-article
updated_at: '2025-08-20T12:43:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037174514-RH-Linha-Protheus-GPE-Inclus%C3%A3o-de-valores-no-calculo-de-dissidio-retroativo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34314210506647) Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**Como incluir valores no calculo de dissídio retroativo?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**

**Criado campo RHH\_VALINF (Valor informado)**

Após efetuar o cálculo do dissídio retroativo, o recálculo poderá ser feito para cada funcionário individualmente, acessando o cálculo através do botão "Manutenção" que foi disponibilizado.

Na rotina de manutenção será possível informar o valor que será utilizado no cálculo no campo "Valor Informado", para todas as verbas, exceto a "000".

A rotina deve ser utilizada da seguinte forma:

Após o cálculo do Dissidio Retroativo, selecionar o funcionário, entrar em Outras Ações, Manutenção.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049575053)

**Exemplo:**

Verba 151 Hora Extra 60%

Valor Original 406,15

Valor Calculado 411,22

Diferença 5,07

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048674394)

Suponhamos que a diferença a ser paga fosse de 25,00, e não foi calculada corretamente devido a mudanças nas incidências das verbas por exemplo. Para que o cálculo seja feito será necessário o seguinte procedimento:

Na coluna **"Valor Informado"** Incluir o valor 431,15 da verba 151, desta forma a diferença entre o calculado e o original será de 25,00 após o recálculo.

Para calcular a diferença, entrar em Outras Ações, Recalculo

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048674694)

A rotina irá carregar os parâmetros de cálculo de acordo com o funcionário e período abertos e irá exibir os dados para conferência, podendo, neste momento, efetuar qualquer alteração.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049575873)![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049575973)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048675534)![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048675554)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048675634)

Após confirmar, o cálculo é refeito, utilizando todas as verbas informadas no recálculo, alterando não só a verba efetivamente alterada, mas todas as demais que ela incidir (Impostos por exemplo).

Após o recálculo a tela é recarregada já com os valores de diferenças corretos.

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049576573)

**Saiba mais:**

<https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109132-RH-Diss%C3%ADdio>
