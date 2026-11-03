---
article_id: 360048709534
category: Gestão de Transportes (TMS)
content_hash: 136e1ead70f156822f7906c3f413b4bb5c60b74468653579395304869acafd84
fetched_at: '2026-06-28T22:45:33.335163+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Rejeição 786  Grupo de informações da partilha
  com a UF de fim da prestação deve estar preenchido
type: support-article
updated_at: '2022-06-14T20:14:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048709534-Log%C3%ADstica-Linha-Protheus-TMS-Rejei%C3%A7%C3%A3o-786-Grupo-de-informa%C3%A7%C3%B5es-da-partilha-com-a-UF-de-fim-da-presta%C3%A7%C3%A3o-deve-estar-preenchido
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:05 min****Ocorrência** **Rejeição 786** na transmissão do **CT-e** - Grupo de informações da **partilha com a UF de fim da prestação** deve estar preenchido  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Causa**Se Tipo do **CT-e** = **0 - Normal, 3 - Substituição ou 1 - Complemento de Valores**, na Operação interestadual com **Tipo de Serviço Normal**, Destinatário não contribuinte *tag* **IE** do destinatário não informada e Tomador diferente de remetente e não contribuinte *tag* **indIEToma = 9**  
  
**Solução**1. No cadastro do Destinatário o campo **Contribuinte** não poderá estar em branco, devendo constar preenchido como **2-Não** e ocampo **Tipo** deverá ser igual **F - Consumidor Final.**

**![Capturar.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360073691753/Capturar.PNG)  
  
![2Capturar.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360073691953/2Capturar.PNG)**

2. A configuração da **TES** para o calculo do **DIFAL** deve ter os campos:  
**L.Fisc. ICMS = T - Tributado**  
**Calc. Dif. ICM = S - Sim**  
**Mat. Consumo = S - Sim**  
**Calc. Difal = 1 - Sim**

![3Capturar.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360073692333/3Capturar.PNG)  
  
![4Capturar.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360072517314/4Capturar.PNG)

Após o calculo do **CT-e** no **xml** será apresentado a *tag* **ICMSUFFim**

![5Capturar.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360072517694/5Capturar.PNG)

**Glossário  
CT-e**- Conhecimento de transporte eletrônico  
**UF** - Unidade Federativa  
**ICMS** -  Imposto sobre Operações relativas à Circulação de Mercadorias e Prestação de Serviços de Transporte Interestadual e Intermunicipal e de Comunicação  
**TES** - Tipo de Entradas e Saídas  
**DIFAL** - Diferencial de Alíquota  
**XML** - Extensible Markup Language
