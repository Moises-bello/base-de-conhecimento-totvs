---
article_id: 10071074155927
category: RH - Integração de Titulo
content_hash: e91a3e2b1c1635d15da33182248f472785b7266068eb776b6de35531e9872115
fetched_at: '2026-06-28T22:43:36.446530+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus - GPE - Sistema não permite habilitar campo RC1_COMPET
  para edição no browser na inclusão manual de títulos
type: support-article
updated_at: '2025-07-15T19:52:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10071074155927-RH-Linha-Protheus-GPE-Sistema-n%C3%A3o-permite-habilitar-campo-RC1-COMPET-para-edi%C3%A7%C3%A3o-no-browser-na-inclus%C3%A3o-manual-de-t%C3%ADtulos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33490516756119) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Precisamos que o campo RC1\_COMPET seja apresentado na rotina para o usuário preencher quando for inclusão manual de títulos  
**Ambiente**TOTVS RH - TOTVS RH (linha Protheus) - Gestão de Pessoal - Todas as Versões  
  
**Causa**O Sistema não permite que este campo seja habilitado para edição no browser, pois dentro do fonte ele já recebe uma atribuição de valor.  
  
**Solução**O valor gravado na emissão é definido no grupo de perguntas da rotina de geração de títulos:

RC1->RC1\_COMPET   := cCompetTit  
cCompetTit  := mv\_par12

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10070919416855)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10070832781591)

O campo competência também segue a mesma linha de raciocínio, sendo tratada no momento da geração através do campo competência:  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10070934278935)

Para criação de títulos sem a utilização dos filtros, seria necessário customizar a rotina, por exemplo, criando campos e utilizando os pontos de entrada disponíveis na rotina GPEM670 para preenchimento:  
[MP - GPE - Quais os pontos de entrada disponíveis na rotina GPEM670](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018319712-MP-GPE-Quais-os-pontos-de-entrada-dispon%C3%ADveis-na-rotina-GPEM670?source=search)

**Saiba Mais:**

[Artigos sobre Integração de Títulos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)
