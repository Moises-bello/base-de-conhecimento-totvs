---
article_id: 360057720614
category: RH - Rescisão
content_hash: 4178b6df09c7f7edd85a1757437b965c1268239e60f8cb49bc2c0607afd96646
fetched_at: '2026-06-28T22:43:49.737794+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Identificador de cálculo 1415 - 1ª Parcela 13º
  Antecipada mesmo mês rescisão
type: support-article
updated_at: '2026-03-16T13:23:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057720614-RH-Linha-Protheus-GPE-Identificador-de-c%C3%A1lculo-1415-1%C2%AA-Parcela-13%C2%BA-Antecipada-mesmo-m%C3%AAs-rescis%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15862019870231) Tempo aproximado para leitura: **00:01:00 min**  
**Dúvida**Identificador de cálculo 1415 - 1ª Parcela 13º Antecipada mesmo mês rescisão  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Criado novo Identificador **1415** - 1ª Parcela 13º Antecipada mesmo mês rescisão, utilizado quando a rescisão é no mesmo mês do pagamento da primeira parcela.   
Com isso a base do FGTS é calculada de forma integral na rescisão e informada na GRRF, na Sefip ela não será considerada.   
A verba com esse novo identificador **não deve ter incidência de FGTS** e deve ser uma verba de desconto. 

 1. No Gestão de Pessoal (SIGAGPE), acesse Atualizações / Definições de Cálculos / Verbas (GPEA040);

 2. Clique em incluir;

 3. Crie uma nova Verba com os seguintes dados principais:

* Tipo do Cod (RV\_TIPOCOD) = 2-Desconto
* Tipo Verba(RV\_TIPO) = V- Valor
* Id p/Calculo(RV\_CODFOL = 1415
* **FGTS (RV\_FGTS) = N - não**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15861735544855)

**Observação:** A configuração eSocial das Verbas/Rubricas com relação a Natureza e as Incidências Tributárias é algo particular de cada Empresa e que deve ser analisado em conjunto com o departamento Jurídico e Contábil. **Porém a incidência FGTS eSocial (RV\_INCFGTS) é necessário que esteja = 12 para que seja deduzido da base do FGTS calculada na rescisão.**  
  
4. No Gestão de Pessoal (SIGAGPE), acesse Miscelânea /Cálculos / Rescisão (GPEM040)  
Calcule a Rescisão do funcionário desejado

**Saiba Mais:**[RH - Linha Protheus - GPE - Como conferir cálculo de 13º e Férias Sobre Aviso na Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016799471-RH-Linha-Protheus-GPE-Como-conferir-c%C3%A1lculo-de-13%C2%BA-e-F%C3%A9rias-Sobre-Aviso-na-Rescis%C3%A3o)[RH - Linha Protheus - GPE - Como conferir valor do ID 1672-INSS 13º Devolução calculado em rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXoSx6NQo6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBuWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzExMjI0Nzk5Mjg5NzUxLVJILUxpbmhhLVByb3RoZXVzLUdQRS1Db21vLWNvbmZlcmlyLXZhbG9yLWRvLUlELTE2NzItSU5TUy0xMyVDMiVCQS1EZXZvbHUlQzMlQTclQzMlQTNvLWNhbGN1bGFkby1lbS1yZXNjaXMlQzMlQTNvBjsIVDoOc2VhcmNoX2lkSSIpZjkzZWZkZjktNTRhZC00ZmE0LTk3ZDYtMzU0ZTk4OGI0NWMxBjsIRjoJcmFua2kMOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSITcmVzY2lzw6NvIDEzwroGOwhUOhJyZXN1bHRzX2NvdW50aQLJBA%3D%3D--03ab7457b5dc0a876a1a05e748ece117cd5adc20)  
[RH - Linha Protheus - GPE - Como conferir valor do ID 1676-FGTS 13º Devolução calculado em rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11269726795031-RH-Linha-Protheus-GPE-Como-conferir-valor-do-ID-1676-FGTS-13%C2%BA-Devolu%C3%A7%C3%A3o-calculado-em-rescis%C3%A3o)  
[RH - Linha Protheus - GPE - Valor INSS 13º salário não é deduzido para a base de IR 13º salário em rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051550714-RH-Linha-Protheus-GPE-Valor-INSS-13%C2%BA-sal%C3%A1rio-n%C3%A3o-%C3%A9-deduzido-para-a-base-de-IR-13%C2%BA-sal%C3%A1rio-em-rescis%C3%A3o)  
[RH - Linha Protheus - GPE - Por que rescisão gera id 1672 indevidamente quando a data de demissão contabiliza 12/12 avos de 13º salário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11062854403095-RH-Linha-Protheus-GPE-Por-que-rescis%C3%A3o-gera-id-1672-indevidamente-quando-a-data-de-demiss%C3%A3o-contabiliza-12-12-avos-de-13%C2%BA-sal%C3%A1rio)
