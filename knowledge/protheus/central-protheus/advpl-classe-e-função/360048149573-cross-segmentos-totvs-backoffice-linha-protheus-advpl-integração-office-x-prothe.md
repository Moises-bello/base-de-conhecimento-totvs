---
article_id: 360048149573
category: ADVPL - Classe e Função
content_hash: 2f7d269b451dff68c56f301ebd1b8aa152610db87698e70eea64db04ad73ed70
fetched_at: '2026-06-28T22:40:20.465513+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - Integração Office
  x Protheus
type: support-article
updated_at: '2022-01-11T22:22:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048149573-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Integra%C3%A7%C3%A3o-Office-x-Protheus
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**O que preciso saber sobre integrações Office x Protheus ?  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.8  
  
**Solução**No **Protheus**, existe a possibilidade de realizar integração com **Office** (Word e Excel), porém é necessário se atentar as versões homologadas para essa integração.   
  
**Versões da suite Office**Não são homologadas versões limitadas e tipicamente classificadas como "básicas" por se tratarem de distribuições compactas e que apresentam a falta ou incompatibilidade de componentes.  
  
**Versões 64 bits do Office com binário SmartClient 32 bits**A partir da **build 170117A** o **SmartClient** passa a contar também com uma versão **64bits** (ou x64), sendo necessário atentar para a arquitetura dos programas de terceiros utilizados em conjunto com ele.

Assim, ao utilizar o **SmartClient x86** (ou 32 bits) somente será possível integrá-lo a ferramentas desta arquitetura, o mesmo vai acontecer ao utilizar o **SmartClient x64**,  
  
**Integração com os pacotes Office 32/64 bits:**  
Ao utilizar o **Office** **x86** não conseguirá integra-lo ao **SmartClient x64** **e vice e versa**, sendo importante atentar também para arquitetura das **DLLs** de integração distribuídas pela **TOTVS**, sendo:  
**· mpexcel.dll**  
**· mpproject.dll**  
**· mpword.dll  
  
Office 365**Muitas empresas optaram por utilizar o **Office 365**, porém esse recurso não está homologado para integrações com o **Protheus**.  
  
**Saiba mais**[Office descontinuados](https://tdn.totvs.com/display/tec/SmartClient+-+Office+descontinuados)  
[Office homologado para uso em integrações](https://tdn.totvs.com/display/tec/SmartClient+-+Office)  
[Plataforma homologada dos produtos](https://tdn.totvs.com/display/tec/Plataforma+homologada+dos+produtos)

**Documentações uteis**[Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - APAPI64 e APAPI](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360008266192)  
[Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - Identificar se a integração Excel está funcionando no protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019481732)  
[Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - TOII Integração com Office](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042562774)  
[Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Validar funções advpl na integração Excel](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018993631)
