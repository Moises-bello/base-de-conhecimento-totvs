---
article_id: 360025673672
category: Gestão de Transportes (TMS)
content_hash: 79420a883fc5dd5603b8d144198e2fc4495b8c3eab0d170cecce12cf26a0cea2
fetched_at: '2026-06-28T22:45:27.598234+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Controle de alteração da Configuração da
  Tabela de Frete
type: support-article
updated_at: '2022-07-19T13:11:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025673672-Log%C3%ADstica-Linha-Protheus-TMS-Controle-de-altera%C3%A7%C3%A3o-da-Configura%C3%A7%C3%A3o-da-Tabela-de-Frete
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:01:00 min****Dúvida**É possível controlar se a configuração da tabela de frete pode ser alterada?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**A alteração da **TMSA130 - Configuração da Tabela de Frete** pode ser permitida ou não por meio  do parâmetro **MV\_CONTHIS - Controla alteração da Tabela/Ajuste de Frete**.  
  
Parâmetro **MV\_CONTHIS =  .F.**Permite a alteração dos campos **Descrição - DTL\_DESCRI, Ini. Vigência - DTL\_DATDE, Fim Vigência - DTL\_DATATE, Nº Decimais - DTL\_NUMDEC** e **Moeda - DTL\_MOEDA**:

![Capturar___2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360025009591/Capturar___2.PNG)

Parâmetro **MV\_CONTHIS =  .T.**Não permite a alteração dos campos **Descrição - DTL\_DESCRI, Ini. Vigência - DTL\_DATDE, Fim Vigência - DTL\_DATATE, Nº Decimais - DTL\_NUMDEC** e **Moeda - DTL\_MOEDA**:

![Capturar.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360025001891/Capturar.PNG)

Entretanto, o Sistema possui o ponto de entrada **TMA010HIS**, o qual sobrescreve a regra do parâmetro **MV\_CONTHIS**.  
  
**Saiba mais**Mais informações sobre o ponto de entrada **TMA010HIS**: [Logística - Linha Protheus - TMS - TMA010HIS - Valida Alteração e Exclusão da Tabela de Frete](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052024153-MP-TMS-TMA010HIS-Valida-Altera%C3%A7%C3%A3o-e-Exclus%C3%A3o-da-Tabela-de-Frete)
