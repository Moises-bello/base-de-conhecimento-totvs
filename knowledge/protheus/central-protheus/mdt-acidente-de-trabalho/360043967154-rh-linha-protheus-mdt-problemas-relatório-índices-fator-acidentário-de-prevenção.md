---
article_id: 360043967154
category: MDT - Acidente de Trabalho
content_hash: bc5b444e6a689cb759a556990db81b6ebb29447f95bd737981976749362befc9
fetched_at: '2026-06-28T22:44:24.008039+00:00'
product: protheus
section_id: 360012070513
source: central-protheus
title: RH - Linha Protheus - MDT - Problemas relatório índices  Fator Acidentário
  de Prevenção (FAP)
type: support-article
updated_at: '2025-10-02T19:06:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043967154-RH-Linha-Protheus-MDT-Problemas-relat%C3%B3rio-%C3%ADndices-Fator-Acident%C3%A1rio-de-Preven%C3%A7%C3%A3o-FAP
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20007820021783)** Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**No módulo  35 (SIGAMDT), ao tentar extrair o relatório de índices Fator Acidentário de Prevenção (FAP)  rotina **(MDTR780),** o resultado apresentado na impressão não coincide com a quantidade de acidentes no período cadastrados na rotina de acidentes **(MDTA640).** O que verificar?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**O **relatório de índices FAP** levará em consideração para gerar a impressão das informações um conjunto de informações em conformidade com a portaria do FAP divulgada pelo **INSS**.  
  
Assim sendo, o relatório irá considerar além dos acidentes do período, algumas movimentações que se enquadrem nas condições citadas na portaria do **INSS,** como por exemplo as demissões ocorridas no período.   
  
Dentro do modulo **SIGAMDT,** por exemplo, serão considerados além dos acidentes as demissões que ocorreram dentro do período e estiverem no cadastro do funcionário, com o campo situação folha (Sit. Folha) igual a 'D' (demitido) e o campo código de rescisão RAIS ( cd.resc..RAIS) igual a '**62**', '**64**','**73**' ,'**74**'.  
  
Em relação as ausências são considerados o campo de duração ( Num. Dias) maior que **15**e o campo tipo de afastamento (Tipo Afast.) igual a **'003'**(afastamento temporário por acidente de trabalho) ou **'004'** (afastamento temporário por doença).  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20027572218519)  
  
**Saiba Mais**  
[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)  
[Portaria referente as regras do FAP para o ano de 2020 divulgado pelo INSS](http://www.previdencia.gov.br/2019/09/publicada-portaria-do-fap-com-vigencia-para-2020/)
