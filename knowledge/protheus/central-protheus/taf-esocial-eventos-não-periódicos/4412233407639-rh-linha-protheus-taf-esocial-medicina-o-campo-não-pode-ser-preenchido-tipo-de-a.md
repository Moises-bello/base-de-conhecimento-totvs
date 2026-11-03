---
article_id: 4412233407639
category: TAF - eSocial - Eventos Não Periódicos
content_hash: d253869765070f4fb7dff5875433e54534eab9501d45f5d5632115f32139ddeb
fetched_at: '2026-06-28T22:45:18.035272+00:00'
product: protheus
section_id: 1500001548002
source: central-protheus
title: 'RH - Linha Protheus - TAF - eSocial - Medicina - O campo não pode ser preenchido:
  Tipo de avaliação do agente nocivo (S-2240 - TAF).'
type: support-article
updated_at: '2024-05-24T17:38:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412233407639-RH-Linha-Protheus-TAF-eSocial-Medicina-O-campo-n%C3%A3o-pode-ser-preenchido-Tipo-de-avalia%C3%A7%C3%A3o-do-agente-nocivo-S-2240-TAF
---

**Ocorrência**

**Sequência**: *000* - Tipo: Erro - Codigo da Ocorrência: 2 - **Descrição** : *O campo nao pode ser preenchido: Tipo de avaliacao do agente nocivo. - Localização : /eSocial/evtExpRisco/infoExpRisco/agNoc/tpAval*

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Eventos - Tipo de avaliação do agente nocivo - Todas as versões.  
  
**Solução**

1 - Verifique o XML se existe a mesma informação abaixo:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412233397527)

2 - O problema ocorre devido a tag tpAval está preenchida no cadastro do evento S-2240;

3 - A validação que o Governo efetua é que quando o codAgNoc for igual 09.01.001 não deve ser gerado a tag tpAval:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412240647319)

4 - O Governo também aponta que a TAG epcEpi não deve ser preenchida.

**Como corrigir dentro do TAF:**

5 - Acesse a rotina do evento S-2240:  
[TAF - Medicina - S-2240 - Como acessar a Rotina de Condições Ambientais do Trabalho - Agentes Nocivos no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008664741-TAF-Medicina-S-2240-Como-acessar-a-Rotina-de-Condi%C3%A7%C3%B5es-Ambientais-do-Trabalho-Agentes-Nocivos-no-TAF)

6 - Deverá ser retirada a informações dos campos grifados abaixo:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412250160919)

7 - Após isso realize novamente o envio ao Governo através do Monitoramento TAF.

OBS: Caso não queira ajustar o evento direto no TAF, deverá excluir o registro no TAF e integrar novamente do sistema de origem.
