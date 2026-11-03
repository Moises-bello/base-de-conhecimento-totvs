---
article_id: 4403897652119
category: RH - Cálculos
content_hash: d80654ddfe0e0e54300e706bfdca6340f5236a9de8e3033b1e13e583250de7fe
fetched_at: '2026-06-28T22:44:51.654286+00:00'
product: protheus
section_id: 32419138773655
source: central-protheus
title: RH - Linha Protheus - PON - Mensagem de Eventos sobrepostos no Cálculo Mensal
type: support-article
updated_at: '2026-02-10T18:32:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403897652119-RH-Linha-Protheus-PON-Mensagem-de-Eventos-sobrepostos-no-C%C3%A1lculo-Mensal
---

**Dúvida**  
Quando é acessado o SIGAPON, em Miscelânea > Cálculos > Cálculo Mensal, o sistema traz a seguinte mensagem de aviso:  
"**Ao realizar o cálculo mensal os eventos serão sobrepostos, principalmente a data de pagamento. Ela será utilizada para a data base do sistema caso já existam eventos nos resultados dentro do período selecionado"**  
  
**Conforme tela abaixo:**  
**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403903424023)**  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Esta mensagem se refere ao alerta que ocorre ao calcular funcionários intermitentes que recebem mais de um pagamento no mesmo mês. Caso o funcionário não se enquadre nesse cenário, não é necessário se preocupar.

Esse alerta acontece porque, no contrato intermitente, o sistema utiliza a data base para referência, que, neste caso, corresponde à data de pagamento da verba ao funcionário nos resultados do Ponto.

**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[RH - Linha Protheus - PON - Como fazer e qual a finalidade do Cálculo Mensal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051550453-RH-Linha-Protheus-PON-Como-fazer-e-qual-a-finalidade-do-C%C3%A1lculo-Mensal)  
[RH - Linha Protheus - PON - PONM070 - Como configurar o Schedule para automação do Cálculo Mensal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035556074-RH-Linha-Protheus-PON-PONM070-Como-configurar-o-Schedule-para-automa%C3%A7%C3%A3o-do-C%C3%A1lculo-Mensal)
