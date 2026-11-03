---
article_id: 360026666971
category: RH - Folha de Pagamento
content_hash: ed1620da991e882fc711e9773c9062d1080a82dce97aaf34c88895135b70c153
fetched_at: '2026-06-28T22:44:14.988790+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Identificador 0041 e/ou 0042 não está somando o
  adicional que incorpora salário
type: support-article
updated_at: '2024-09-10T20:23:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026666971-RH-Linha-Protheus-GPE-Identificador-0041-e-ou-0042-n%C3%A3o-est%C3%A1-somando-o-adicional-que-incorpora-sal%C3%A1rio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26281077123735) Tempo aproximado para leitura: 00:02:00 min**

**Dúvida**Identificador de calculo 0041 e /ou 0042 não esta somando o adicional (insalubridade e/ou periculosidade - ATS) sendo que este adicional está com sim para incorpora salário.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoas - Todas as versões  
  
**Solução**Para que o sistema considere na verba o adicional que incorpora salário deverá verificar o cadastro de verbas id 0041 e id 0042 aba incidências campo Base de calculo "RV\_BASCAL" para este campo a verba com id 0041 e 0042 deverá ficar com salário incorporado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26281044956823)

Exemplo no caso insalubridade (Calculo pelo salário mínimo)

Salário "RA\_SALARIO" = 2.800,00

insalubridade = 190,80 (954,00\*20%=190,80)

Folha março afastamento 3 dias

Para o id 0041 = 299,08 ( 2800,00/30\*3=280,00) +  (190,80 / 30\* 3 = 19,09) = 280,00+19,09 =299,08

Para o id 0042  299,08 ( 2800,00/30\*3=280,00) +  (190,80 / 30\* 3 = 19,09) = 280,00+19,09 =299,08

Se o campo Base de calculo "RV\_BASCAL" estiver como salario base sistema irá fazer a seguinte conta:

Para o id 0041 = 299,08 ( 2800,00/30\*3=280,00)

Para o id 0042  299,08 ( 2800,00/30\*3=280,00)

**Saiba Mais**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)

[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
