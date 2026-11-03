---
article_id: 360036440753
category: RH - Funcionários
content_hash: 6436aff1fda5411796723f484d9b8b2ef249f7975cce48beae36986e1f2219a1
fetched_at: '2026-06-28T22:43:28.724837+00:00'
product: protheus
section_id: 360011909593
source: central-protheus
title: RH - Linha Protheus - GPE - Como funciona a aposentadoria especial para  funcionário
  exposto ao agente nocivo
type: support-article
updated_at: '2025-06-12T20:12:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036440753-RH-Linha-Protheus-GPE-Como-funciona-a-aposentadoria-especial-para-funcion%C3%A1rio-exposto-ao-agente-nocivo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19194760324887) Tempo aproximado para leitura: 00:02:00 min**

**Dúvida**Como funciona a aposentadoria especial para funcionário exposto ao agente nocivo?  
  
**Ambiente**

TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**As ocorrências referem-se aos códigos dos agentes nocivos aos quais o funcionário seja exposto na lida de sua função, conforme Tabela de Ocorrências disponível no manual da SEFIP.  
  
Os códigos são:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046991674)

Este campo deve ser informado em conformidade com o campo %Acid. Trab. A partir da informação do percentual e do código, o sistema efetua automaticamente o cálculo do valor da aposentadoria especial, gerando a verba de base provento cadastrada com o identificador de cálculo **0150**.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046991914)  
  
Cabe salientar que o campo ocorrência pode ser deixado em branco. Deixe em branco quando o trabalhador **nunca foi exposto a agente nocivo.**  
  
Considerando a tabela acima, caso ocorra a informação de ocorrência 02, haverá um acréscimo de 12%  no valor devido ao INSS, assim como se o código for 03 o percentual sobre para 9%, e se for 04 o percentual sobre para 6%. O cálculo é realizado pela SEFIP e é direcionado para o campo 6 da GPS (valor do INSS).  
  
No Protheus deve ser informado a Ocorrência na **SRA** (Cadastro do funcionário) e informar o percentual diferenciado no campo **%Acid. Trab.**, ou através do **Centro de Custo** amarrado na matrícula.  
  
**Observação:** Para os funcionários que terão o percentual diferenciado de acidente de trabalho no cadastro do funcionário, deve ser cadastrado o percentual final de cálculo, pois não será feita com o percentual da Tabela S037.  
  
**-Cadastro de Funcionário (GPEA010):**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19194779342231)

**-Cadastro de Centro de Custo (CTBA030):**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19194826284823)  
  
Assim, no cálculo da folha levará o valor do percentual devido na verba com Id 0150 para as matrículas cujo campo %Acid. Trab esteja preenchido em seu cadastro e para os demais funcionários que não se enquadram na ocorrência continuará carregando o percentual informado na tabela S037.  
  
Para que os encargos sejam calculados corretamente pelo eSocial, deve ser enviado o grau de exposição no evento S-1200 - remuneração mensal. Essa informação é gerada de acordo com os dados preenchidos no cadastro do funcionário preenchida no campo Ocorrência (RA\_OCORREN) com a informação de exposição e o Governo vai calcular o GILRAT ajustado.   
  
Segue a documentação de apoio com as orientações relacionadas ao eSocial:   
[RH - Linha Protheus - GPE - eSocial - S-1200/S-2299 - Para que serve a informação de Exposição a Agentes Nocivos e como é apurado os encargos no eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033742313-RH-Linha-Protheus-GPE-eSocial-S-1200-S-2299-Para-que-serve-a-informa%C3%A7%C3%A3o-de-Exposi%C3%A7%C3%A3o-a-Agentes-Nocivos-e-como-%C3%A9-apurado-os-encargos-no-eSocial) 

**Saiba Mais:**[RH - Linha Protheus - GPE - Cadastro Pré Aposentadoria](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXVSbPYhA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBfWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzE4MDE2NTY4MjM1NDE1LVJILUxpbmhhLVByb3RoZXVzLUdQRS1DYWRhc3Ryby1QciVDMyVBOS1BcG9zZW50YWRvcmlhBjsIVDoOc2VhcmNoX2lkSSIpMDU5YmEzZGYtYmEwZC00Yzc5LWJjNzQtMDc3MDNkZTc2ZGFiBjsIRjoJcmFua2kGOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSI8UkggLSBMaW5oYSBQcm90aGV1cyAtIEdQRSAtIENhZGFzdHJvIFByw6kgQXBvc2VudGFkb3JpYQY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--6378437a9935bb023b342a5dd837e0076ee48a36)  
[RH - Linha Protheus - GPE- Onde alterar o % do FAP e como informar o RAT (acidente de trabalho) no sistema](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgLR1rTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBp2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyODE5NDU3MS1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtT25kZS1hbHRlcmFyLW8tZG8tRkFQLWUtY29tby1pbmZvcm1hci1vLVJBVC1hY2lkZW50ZS1kZS10cmFiYWxoby1uby1zaXN0ZW1hBjsIVDoOc2VhcmNoX2lkSSIpYmY4MDJjODItNmZkNC00MGVjLWI1OTktZDI2YmZmYzI3NDY5BjsIRjoJcmFua2kGOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIJUzAzNwY7CFQ6EnJlc3VsdHNfY291bnRpfg%3D%3D--543200e44382c67bf2da405447cbf985d2cc054a)   
[RH - Linha Protheus - GPE - Como cadastrar % INSS acidente de trabalho quando o percentual é diferente por filial](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgX8UQj4ww6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBtmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzE0MTY5Njg4ODMwMjMxLVJILUxpbmhhLVByb3RoZXVzLUdQRS1Db21vLWNhZGFzdHJhci1JTlNTLWFjaWRlbnRlLWRlLXRyYWJhbGhvLXF1YW5kby1vLXBlcmNlbnR1YWwtJUMzJUE5LWRpZmVyZW50ZS1wb3ItZmlsaWFsBjsIVDoOc2VhcmNoX2lkSSIpYmY4MDJjODItNmZkNC00MGVjLWI1OTktZDI2YmZmYzI3NDY5BjsIRjoJcmFua2kHOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIJUzAzNwY7CFQ6EnJlc3VsdHNfY291bnRpfg%3D%3D--94ff85ced8251baf388e316f65d1376fa049db89)
