---
article_id: 360019851752
category: RH - Integração de Titulo
content_hash: 21789f59ee14785404e043d3bd765fbad8488e46210262dcbcb76a42666e288f
fetched_at: '2026-06-28T22:43:36.176565+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus - GPE - Como conferir a geração de títulos de INSS
type: support-article
updated_at: '2025-07-15T20:31:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019851752-RH-Linha-Protheus-GPE-Como-conferir-a-gera%C3%A7%C3%A3o-de-t%C3%ADtulos-de-INSS
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33490659277335)** Tempo aproximado para leitura: 00:00:30 min

**Dúvida**Como conferir a geração de títulos de INSS?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17

**Solução**Abaixo será demonstrada a geração do título de INSS e a conferência dos valores gerados.  
  
**Cadastro de verbas**: Para queas verbas de base sejam apresentadas no resumo da folha, o campo **IMPR. VERBA** deverá estar preenchido igual a sim.

![](http://tdn.totvs.com/download/attachments/438276286/image2018-11-21_10-2-45.png?version=1&modificationDate=1542801978937&api=v2)

**Definição de títulos:**

![](http://tdn.totvs.com/download/attachments/438276286/image2018-11-21_10-4-54.png?version=1&modificationDate=1542801978737&api=v2)

**Fórmula para calculo**

Somatória dos id’s  0064 (INSS SAL) + 0065 (INSS FÉRIAS) + 0070 (INSS SAL 13) + 0148 (INSS EMPR) +0149 (TERCEIROS) + 0150 (ACIDENTE DE TRABALHO).

(ACID TRABALHO) e subtração dos id’s 0040 (MATERNIDADE) e 0034 (SAL FAMILIA) =  GPS DO MÊS

**Observação:** No cadastro de verba o campo RV\_DEDINSS pode ser configurado para abatimento da guia de INSS.

Folha atual de 08/2018:  
  
Contrato Indeterminado:

![](https://totvssuporte.zendesk.com/attachments/token/NiijrHCoyBVJ4O3EGuZiq9UBn/?name=inline-1945655082.png)

Contrato Determinado:

![](https://totvssuporte.zendesk.com/attachments/token/RIKjODlav3xKZQK4roNp9mijH/?name=inline-1450618261.png)

**Geração de título:**![](https://totvssuporte.zendesk.com/attachments/token/L82YgpZbeOxOtnFpn0jEyB6g7/?name=inline545137191.png)  
![](https://totvssuporte.zendesk.com/attachments/token/59hMHr8lVRZD0vSUPthmXOoPV/?name=inline-1317940227.png)  
![](https://totvssuporte.zendesk.com/attachments/token/vYOLOcMN3UqQ06HeqHmvWgYIg/?name=inline-1533017337.png)

**Manutenção de título:**

![](https://totvssuporte.zendesk.com/attachments/token/12GcQ1OnGTUlXGMKiU3mTKkKj/?name=inline-847361037.png)

**Indeterminado:**  
  
Verba 782 (120248,78) + Verba 783 (75881,12) + Verba 401 (7813,25) - Verba 129 (76,71) = Título 000000022/23 (203866,44) corresponde a soma dos títulos 22/23.  
 **Determinado:**  
  
Verba 782 (291,54) + Verba 783 (183,97) + Verba 401 (505,85) = Título 000000024 (981,36).  
  
Após o fechamento mensal da folha de 08/2018 - Folha atual 09/2018 com referência a 08/2018.  
Data Base:  
  
![](https://totvssuporte.zendesk.com/attachments/token/3BFKeMmfIoau6hyhYbPRkKbVf/?name=inline-1283902141.png)

**Geração de título:**![](https://totvssuporte.zendesk.com/attachments/token/L82YgpZbeOxOtnFpn0jEyB6g7/?name=inline545137191.png)  
![](https://totvssuporte.zendesk.com/attachments/token/59hMHr8lVRZD0vSUPthmXOoPV/?name=inline-1317940227.png)  
![](https://totvssuporte.zendesk.com/attachments/token/vYOLOcMN3UqQ06HeqHmvWgYIg/?name=inline-1533017337.png)

**Manutenção de título:**

![](https://totvssuporte.zendesk.com/attachments/token/cJiaT1hvmx6EkS5XqLAArDILq/?name=inline-1085437199.png)

*Default* o sistema buscará as informações tanto da **SRC** como da **SRD**.  
  
**Saiba Mais**  
[Artigos sobre Integração de Títulos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)
