---
article_id: 8452790025623
category: RH - CNAB
content_hash: 6036ff2bcb8350eb207f0567cc92662af1b079d7f6fd84fd3bcbc77b142323d1
fetched_at: '2026-06-28T22:43:39.134080+00:00'
product: protheus
section_id: 360004833653
source: central-protheus
title: RH - Linha Protheus - GPE -  Descontinuidade da Rotina CFGX044 de Configuração
  do SISPAG
type: support-article
updated_at: '2025-09-19T18:52:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8452790025623-RH-Linha-Protheus-GPE-Descontinuidade-da-Rotina-CFGX044-de-Configura%C3%A7%C3%A3o-do-SISPAG
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32853839744535) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Qual será o impacto na Configuração e Geração do SISPAG com a descontinuidade da rotina CFGX044?  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as Versões.  
  
**Solução**

Em 20/08/2022 a rotina **CFGX044** do Configurador (SIGACFG), foi substituída pela rotina **CFGX049**.

Porém, por esta rotina não é possível realizar a configuração do arquivo SISPAG. 

O arquivo com extensão \*.PAG era um layout exclusivo do ITAÚ, e tinha funções limitadas na configuração, já os arquivos \*.2PE , \*.2PR são modelos FEBRABAN, onde é possível desenvolver qualquer layout de qualquer banco. 

Portanto com a descontinuidade da rotina, deverá ser desenvolvido um novo arquivo de configuração com o no layout \*.2PE ou \*.2PR.  
  
 Anexo, para apoio na configuração,  disponibilizamos os modelos CNAB 1, CNAB 2 , SISPAG e um arquivo SISPAG no layout 2.RE

**Saiba Mais:**

<https://tdn.totvs.com/pages/releaseview.action?pageId=666460968>   
[Artigos - CNAB](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833653-RH-CNAB)
