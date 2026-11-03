---
article_id: 360029070652
category: RH - Férias
content_hash: b3b1aeab43086934b8bf04aee0b625c699c9eb3493596a8f9d47b32fddd4ef7e
fetched_at: '2026-06-28T22:43:58.223893+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Conferência de IRRF de férias quando dois períodos
  de gozo são concedidos com pagamento no mesmo mês
type: support-article
updated_at: '2025-09-12T18:12:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029070652-RH-Linha-Protheus-GPE-Confer%C3%AAncia-de-IRRF-de-f%C3%A9rias-quando-dois-per%C3%ADodos-de-gozo-s%C3%A3o-concedidos-com-pagamento-no-mesmo-m%C3%AAs
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32579177519511)** Tempo aproximado para leitura**: 00:03:00 min**

**Dúvida**Como Conferir o Cálculo do IRRF de Férias quando Dois Períodos de Gozo são concedidos com Pagamento no mesmo mês?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**O fato gerador do Imposto de Renda Retido na Fonte (IRRF) é o **pagamento.** Por isso, quando há o pagamento de dois períodos de gozo de férias dentro do mesmo mês, o sistema **realiza o recálculo do IRRF** com base na soma dos valores recebidos nesses dois períodos, independentemente de o regime de pagamento da empresa ser Caixa ou Competência.

Exemplo:  
**1º Gozo de Férias:**10 dias, de 13 à 22/03 - Data de Pagamento **11/03**:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030672232)

Cálculo do IRRF:

 Férias (Id 0072) + 1/3 de Férias (Id 0077) - INSS (Id 0065) x % Alíquota da Tabela de IRRF - Valor à Deduzir da Tabela de IRRF = Valor do IRRF de Férias.  
3.554,46 + 1184,82 - 521,32 = 4.217,96 x 22,50% = 949,04 - 636,13 = **312,91**

**2º Gozo de Férias:**05 dias, de 01 à 05/04 - Data de Pagamento **28/03**:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030639851)

**Cálculo do IRRF:**

-> Férias (Id 0072) + 1/3 de Férias (Id 0077) + Base IRRF do Outro Período das Férias (Id 0236) - INSS (Id 0065) x % Alíquota da Tabela de IRRF - Valor à Deduzir da Tabela de IRRF - IRRF de Férias do Outro Período (Id 0237) = Valor do IRRF de Férias.  
1.777,23 + 592,41 + 4.217,96 - 213,26 = 6.374,34 x 27,50% = 1.752,94 - 869,36 - 312,91 = **570,67**

Desta forma, as respectivas verbas de cálculo de férias devem conter os seguintes identificadores de cálculo:

**ID    Descrição**  
**0236** - Base de IR de férias de outros períodos de férias.  
**0237** - Valor de IR já descontado em outros períodos de férias.  
**0396** - Base de INSS de férias de outros períodos de férias.  
**0397** - Valor de INSS já descontado em outros períodos de férias.

Sendo que as verbas a serem cadastradas para estes identificadores de cálculo devem, obrigatoriamente, ser do tipo **3 - Base Provento**

**Saiba Mais**[RH - Linha Protheus - GPE - Como calcular dois períodos de férias dentro do mesmo mês](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgOebjUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBpGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MTE0NDk3NC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1jYWxjdWxhci1kb2lzLXBlciVDMyVBRG9kb3MtZGUtZiVDMyVBOXJpYXMtZGVudHJvLWRvLW1lc21vLW0lQzMlQUFzBjsIVDoOc2VhcmNoX2lkSSIpYWZmZWJmNjctNTVkNi00NmE4LThiMGItMjI2MThkMDI1NmEwBjsIRjoJcmFua2kGOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSJdUkggLSBMaW5oYSBQcm90aGV1cyAtIEdQRSAtIENvbW8gY2FsY3VsYXIgZG9pcyBwZXLDrW9kb3MgZGUgZsOpcmlhcyBkZW50cm8gZG8gbWVzbW8gbcOqcwY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--5cb77a777c7c7b7b09196832e652351227d86bc5)
