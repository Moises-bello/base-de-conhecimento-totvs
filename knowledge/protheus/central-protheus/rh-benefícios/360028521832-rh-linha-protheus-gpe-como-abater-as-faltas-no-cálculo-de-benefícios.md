---
article_id: 360028521832
category: RH - Benefícios
content_hash: e302659f6d2d92984ff599bb568f61caabd7a73eedf9c6a35569ee77af59a223
fetched_at: '2026-06-28T22:44:03.637167+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Como abater as Faltas no cálculo de Benefícios
type: support-article
updated_at: '2025-09-05T10:22:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028521832-RH-Linha-Protheus-GPE-Como-abater-as-Faltas-no-c%C3%A1lculo-de-Benef%C3%ADcios
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24413073268887) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como **abater as Faltas** no cálculo de **Benefícios?**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões   
  
**Solução**Atualmente o Sistema utiliza para busca de faltas:  
  
- Parâmetro **MV\_USACPER**  
- Mnemônico **P\_BENBUSFA** - Mnemônico **P\_BENPONEV**

**MV\_USACPER**O parâmetro indicará se o Sistema utilizará o Cadastro de **Períodos da folha** ou a **Escala do ponto** para realizar o cálculo do benefício. Este parametro definirá a utilização dos mnemônicos P\_BENBUSFA e P\_BENPONEV.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11299831734039)

Ele possui preenchimento lógico onde:

* Quando preenchido com **.T.**, o Sistema utilizará como busca o **Período da Folha,** então irá buscar a existência de verbas com o **ID 0054** na tabelas **RGB, SRC e SRD.**
* Quando preenchido com **.F.**, o Sistema usa a Escala do Funcionário do **Ponto Eletrônico,** buscando os eventos apontados como falta nas tabelas **SPC e SPH.**

**P\_BENBUSFA**É configurado com valor numérico da **q****uantidade de meses** para buscar faltas. A busca das tabelas irá depender de como está configurado o Parâmetro **MV\_USACPER.**   
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409306208023)

* Preenchido com **0**, o Sistema irá buscar as faltas da tabela **SPC** do **período aberto** no Ponto **caso o MV\_USACPER estiver com conteúdo .F.** ou da tabela **RGB no Gestão de Pessoal caso o parâmetro estiver com .T.**
* Preenchido com **1,** o Sistema irá buscar as faltas na tabela **SPH** do **período anterior** ao aberto no Ponto **caso o MV\_USACPER estiver com conteúdo .F.** ou das tabelas **SRC** (caso esteja aberta) e **SRD** (quando SRC estiver fechada)**, no Gestão de Pessoal caso o parâmetro estiver com .T.**
* Preenchido com **2,** o Sistema irá buscar as faltas na tabela **SPH** de **dois períodos anteriores** ao aberto no Ponto **caso o MV\_USACPER estiver com conteúdo .F.** ou da tabela **SRD de dois meses anteriores ao aberto no Gestão de Pessoal caso o parâmetro estiver com .T.**

**P\_BENPONEV**Este mnemônico será preenchido com o código dos eventos de Falta a serem considerados no cálculo quando a origem da busca de faltas forem **geradas** por **eventos cadastrados no Ponto,** portanto o mnemônico **só será utilizando quando o parâmetro MV\_USACPER estiver com conteúdo .F.**

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11308183387415)**Seu preenchimento deve ser numérico e informado **entre aspas duplas.**  **Exemplo:** "513,540"  
  
Verifique um exemplo de cálculo com abatimento de faltas, conforme definição do parâmetro **MV\_USACPER.**

* [Cálculo com faltas da folha (MV\_USACPER=.T.)](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgX8phjXRY6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBrWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzI0NTkwMzU4NzM3NDMxLVJILUxpbmhhLVByb3RoZXVzLUdQRS1Db21vLWFiYXRlci1hcy1GYWx0YXMtbGFuJUMzJUE3YWRhcy1uYS1Gb2xoYS1kby1jJUMzJUExbGN1bG8tZGUtQmVuZWYlQzMlQURjaW9zBjsIVDoOc2VhcmNoX2lkSSIpOTJjNjc4NjctOTVmZi00NTUzLTgwYzctN2NmODIyNTI3MzBmBjsIRjoJcmFua2kJOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSJRUkggLSBMaW5oYSBQcm90aGV1cyAtIEdQRSAtIENvbW8gYWJhdGVyIGFzIEZhbHRhcyBubyBjw6FsY3VsbyBkZSBCZW5lZsOtY2lvcwY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--23c398f025ac893de054c486a6bf80cd689c9538)
* [Cálculo com faltas do ponto (MV\_USACPER=.F.)](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXAGazXxY6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBr2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzI0NjAwMjg3NTEwNjc5LVJILUxpbmhhLVByb3RoZXVzLUdQRS1Db21vLWFiYXRlci1hcy1GYWx0YXMtZG8tUG9udG8tRWxldHIlQzMlQjRuaWNvLW5vLWMlQzMlQTFsY3Vsby1kZS1CZW5lZiVDMyVBRGNpb3MGOwhUOg5zZWFyY2hfaWRJIik5MmM2Nzg2Ny05NWZmLTQ1NTMtODBjNy03Y2Y4MjI1MjczMGYGOwhGOglyYW5raQc6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIlFSSCAtIExpbmhhIFByb3RoZXVzIC0gR1BFIC0gQ29tbyBhYmF0ZXIgYXMgRmFsdGFzIG5vIGPDoWxjdWxvIGRlIEJlbmVmw61jaW9zBjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--bf5da041a5be8479d535380a949925b027fad890)

**Observação:**

Quando houver **vínculos** de Vale Refeição/Vale Alimentação relacionados à **entidades de Gestão de Serviços (ABS, TDX ou SA1)**, a quantidade de dias do benefício será obtida a partir da alocação do funcionário em determinado **local de trabalho**. Esta informação será retornada pelo módulo de **Gestão de Serviços**, com as informações: **Filial, Matrícula, Data Início, Data Fim.**

Para a execução do cálculo de **Vale Refeição/Vale Alimentação** é verificado o conteúdo das perguntas referentes à proporcionalidade em casos de férias, afastamentos, férias programadas e faltas, que terão um tratamento específico quando houver integração com Gestão de Serviços:

* **Faltas**: o pagamento ou não das faltas será de acordo com o que foi informado no campo **Pg Faltas**, no lançamento dos vínculos.

**Saiba Mais**[RH - Linha Protheus - GPE - Como utilizar parâmetro MV\_CVTPROP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014665512-RH-Linha-Protheus-GPE-Como-utilizar-par%C3%A2metro-MV-CVTPROP?source=search)  
[RH - Linha Protheus - GPE - Rotinas envolvidas nos cálculos de Benefícios - VR/VA/VT](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050523113-RH-Linha-Protheus-GPE-Rotinas-envolvidas-nos-c%C3%A1lculos-de-Benef%C3%ADcios-VR-VA-VT?source=search)  
[RH - Linha Protheus - GPE - Cálculo de Benefícios para Funcionários com Contrato Intermitente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028891312-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-Benef%C3%ADcios-para-Funcion%C3%A1rios-com-Contrato-Intermitente?source=search)  
[RH - Linha Protheus - GPE - Como calcular benefício VT/VR/VA apenas para dias Não trabalhados - Não úteis](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054064254-RH-Linha-Protheus-GPE-Como-calcular-benef%C3%ADcio-VT-VR-VA-apenas-para-dias-N%C3%A3o-trabalhados-N%C3%A3o-%C3%BAteis?source=search)
