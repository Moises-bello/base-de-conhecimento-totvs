---
article_id: 360007019991
category: RH - CNAB
content_hash: bd1d02520ededcde928454eabb61698f8fde71f4d65aad8b0739bdf725ad0137
fetched_at: '2026-06-28T22:43:39.170480+00:00'
product: protheus
section_id: 360004833653
source: central-protheus
title: RH - Linha Protheus - GPE - Como configurar as fórmulas para parametrizar o
  CNAB em layout específico
type: support-article
updated_at: '2025-06-17T12:34:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007019991-RH-Linha-Protheus-GPE-Como-configurar-as-f%C3%B3rmulas-para-parametrizar-o-CNAB-em-layout-espec%C3%ADfico
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32867064794775)** Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**CNAB Modelo 2 - Geração de Líquido - Como configurar as fórmulas para parametrizar o CNAB em *layout* específico?  
  
 **Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
**Solução**1. Verifique o artigo referente ao CNAB - Centro Nacional de Informação Bancária, pré-definido (Modelo 1) e identifique se algum dos modelos descritos atende a sua necessidade: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006726112>  
  
2 - Caso não utilize nenhum destes bancos/modelos mencionados no artigo indicada no item 1, recomendamos que seja realizado o *download* do modelo do banco desejado, através do Portal do Cliente e após, que seja verificado, conforme abaixo, a fórmula que poderá ser utilizada para adequação do seu *layout*.  
  
Exemplo: Abrir um dos *Layouts* e verificar as fórmulas utilizadas para cada variável, assim poderá adequar a sua necessidade.  
  
Exemplo para encontrar a fórmula para o dígito da Agência:  
StrZero(Val( cDigAgenc ),1)   
  
![](http://tdn.totvs.com/download/attachments/286721565/image2017-8-31%2019%3A9%3A11.png?version=1&modificationDate=1504217661000&api=v2 "Linha Microsiga Protheus > PSIGABD0088 - CNAB Modelo 2 - Geração de Líquido - Como configurar as fórmulas para parametrizar o CNAB em layout específico? > image2017-8-31 19:9:11.png")   
  
Nestes modelos pré-definidos, poderá encontrar fórmulas prontas para vários campos utilizados no CNAB.  
  
3 - Para mais detalhes sobre o processo, verifique todo o passo a passo descrito no artigo indicado no item 1.

**Saiba Mais**

[MP - BD0088 - CNAB Modelo 2 - Geração de Líquido - Como configurar as fórmulas para parametrizar o CNAB em layout específico](http://tdn.totvs.com/pages/viewpage.action?pageId=286721565)

[Artigos - CNAB](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833653-RH-CNAB)
