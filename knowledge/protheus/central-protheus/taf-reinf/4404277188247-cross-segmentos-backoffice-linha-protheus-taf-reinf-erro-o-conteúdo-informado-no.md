---
article_id: 4404277188247
category: TAF - REINF
content_hash: b8bfe2a01dcc350fdc504ca4220ea5258b3f2ef3ac1ede77c3d5a999337b0c24
fetched_at: '2026-06-28T22:41:33.423071+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: CROSS Segmentos - Backoffice Linha Protheus - TAF - REINF - Erro O Conteúdo
  Informado no Parâmetro SourceBranch Não Está Cadastrado no Complemento de Empresas.
  '803'.
type: support-article
updated_at: '2023-03-30T16:49:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404277188247-CROSS-Segmentos-Backoffice-Linha-Protheus-TAF-REINF-Erro-O-Conte%C3%BAdo-Informado-no-Par%C3%A2metro-SourceBranch-N%C3%A3o-Est%C3%A1-Cadastrado-no-Complemento-de-Empresas-803
---

**Dúvida**  
Como corrigir o erro "O Conteúdo Informado no Parâmetro SourceBranch Não Está Cadastrado no Complemento de Empresas. '803'", no painel do reinf?  
  
**Ambiente**  
Cross Segmento - TAF – Painel Reinf – A partir da versão 12.1.17.

**Solução**  
Para corrigir o erro abaixo é necessário conferir os seguintes cadastros;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404276648343/mceclip0.png)

1. Conferir no **complemento de empresa** do **TAF** se esta correto as configurações dos campos **C1E\_FILTAF** e **C1E\_CODFIL**;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404276742167/mceclip1.png)

2. Conferir no appserver.ini a configuração na seção **[TAF\_CFGJOB]**, no campo **PrepareIn =** "Tem que informar todas as empresas Ex: "**01,02,03"** ou informar **"ALL"** para o sistema buscar todas as empresas de forma automática ;

**[TAF\_CFGJOB]**  
MAIN=TAF\_CFGJOB  
Instances=5,30,5,1  
**PrepareIn=01,02,03** ->  Código da empresa, para grupos com mais de uma empresa conteúdo **ALL**

Environment=IPFIS229  
RefreshRate=120

Mais informações no link abaixo;

https://tdn.totvs.com/display/public/TAF/Painel+REINF
