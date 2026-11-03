---
article_id: 19126697004439
category: Evento S-2210
content_hash: e4b7d50526e25223f7698872a826981139bffcb5c4152b2b52c1fd97ac26cf1b
fetched_at: '2026-06-28T22:45:24.483336+00:00'
product: protheus
section_id: 8260521640983
source: central-protheus
title: 'RH - Linha Protheus - MDT - eSocial - S-2210 - Filial: XXX / Acidente: XXX
  /Horas Trabalhadas Antes do Acidente Em Branco'
type: support-article
updated_at: '2023-11-17T10:39:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19126697004439-RH-Linha-Protheus-MDT-eSocial-S-2210-Filial-XXX-Acidente-XXX-Horas-Trabalhadas-Antes-do-Acidente-Em-Branco
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19126741148055) Tempo aproximado para leitura: **00:02:00min** **Dúvida**Filial: XXX / Acidente: XXX /Horas Trabalhadas Antes do Acidente Em Branco, o que avaliar?  
Ao gerar o evento S-2210 o sistema apresenta a seguinte inconsistência:  
  
![erro.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19126696975255)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Essa mensagem de erro ocorre pois na rotina de Acidentes **(MDTA640)**, não foi informado a quantidade de horas trabalhadas antes do acidente acontecer no campo **Horas. Trab (TNC\_HRTRAB).**  
  
![antes.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19126718842391)  
  
Para que a mensagem não apareça novamente, é necessário o preenchimento da quantidade de horas trabalhadas antes da ocorrência do acidente no campo **Horas. Trab**, como no exemplo a seguir:  
  
![depois.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19126741152151)  
  
**Saiba mais**[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)
