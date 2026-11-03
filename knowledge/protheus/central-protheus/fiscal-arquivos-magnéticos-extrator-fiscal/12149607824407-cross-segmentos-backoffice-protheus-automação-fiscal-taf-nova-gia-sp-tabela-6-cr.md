---
article_id: 12149607824407
category: Fiscal Arquivos Magnéticos - Extrator Fiscal
content_hash: 9052829b887a8a37359b57949f50cf152f8e07d027b6d7b9fee7bd1ea9c0b60a
fetched_at: '2026-06-28T22:42:07.717953+00:00'
product: protheus
section_id: 1500001535021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Automação Fiscal - TAF - Nova GIA-SP
  - Tabela 6 - CR=20 - Campo-CódSubitem
type: support-article
updated_at: '2024-11-11T16:34:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12149607824407-Cross-Segmentos-Backoffice-Protheus-Automa%C3%A7%C3%A3o-Fiscal-TAF-Nova-GIA-SP-Tabela-6-CR-20-Campo-C%C3%B3dSubitem
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:03:00 min****Ocorrência:**Ao validar o arquivo **GIA-SP** é apresentada a seguinte mensagem:  
**Sr(a) usuário(a) entre em contato com a empresa**  
**responsável pela geração do arquivo Pré-Formatado**  
**e informe a mensagem abaixo:**  
**Tabela 6, CR=20, Campo-CódSubitem**  
**Inconsistência, Posição x**  
**Linha nº x**  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) -TAF – Nova GIA –  A partir da versão 12.1.27  
  
**Causa**Esse incidente ocorre devido ao não preenchimento ou preenchimento incorreto do campo **Código de Subitem**, na **Apuração do ICMS.**

**Solução**

O erro ocorre devido ao não preenchimento ou preenchimento incorreto do código de subitem informado na **Apuração do ICMS**.  
Conforme exemplo abaixo, no caso, foi informado o código **006.01**

![Apura__o_CodSubitem.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12148107976471)

Na apuração da **GIA-SP**, ao incluir a **linha 006** na apuração (**Outros Créditos**) deve ser informado o **Código de Subitem** iniciado com **007.XX**.  
  
Na validação do arquivo **Nova GIA** ocorre o alerta **Tabela 06 - CR=20 Campo - CodSubitem Inconsistente**, quando não é informado o código de subitem (segundo campo) na **Apuração de ICMS** ou foi informado código incorreto, de acordo com a **Tabela 13** do *Layout* da **Nova GIA**.  
  
Para correção do problema é necessário que seja refeita a Apuração do **ICMS** e que seja informado os códigos corretos.  
  
*Link* para verificação do *layout* e tabela da **GIA**:  
<http://www.fazenda.sp.gov.br/download/gia0700/pre_formatado_ngia_v0210.pdf>

Diferenças entre *layout* de **Apuração de ICMS** e *layout* da **Nova GIA.**  
O *layout* da **Nova GIA** não contem as linhas **004** e **009**, devido a isso, o sequencial de linhas não confere com o *layout* da **Apuração de ICMS**.  
Ao incluir a **linha 006** na apuração (**Outros Créditos**) deve ser informado o **código 007.XX** correspondente a **tabela 13** da **Nova GIA**, pois refere-se a **Outros Créditos** onde também pode incluir a **linha 007 (Estorno de Débitos)** que deve trazer o código **008.XX**.  
  
**Importante**:   
O preenchimento do **Código de Ajuste** deverá ser realizado de acordo com o **COD SUBITEM GIA-SP**, conforme tabela abaixo: *Link*: [Tabela 5.1.1 – Fundamentação Legal](https://www.fazenda.sp.gov.br/sped/legislacao/Tabela%205.1.1%20da%20Portaria%20CAT%20147_2009%2001012016.pdf)

![Tabela5_1_1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12148267282071)

Preencha com as informações e os valores desejados. Ao incluir um ajuste, preencha a **coluna de código de lançamento** com o **código de ajuste** disponível na tabela de ajustes da **Apuração de ICMS**. 

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Como incluir um ajuste manual na apuração de ICMS?](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiJPCXTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBtmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyNDcxODQ3My1DUk9TUy1TZWdtZW50b3MtVE9UVlMtQmFja29mZmljZS1MaW5oYS1Qcm90aGV1cy1GSVMtQ29tby1pbmNsdWlyLXVtLWFqdXN0ZS1tYW51YWwtbmEtYXB1cmElQzMlQTclQzMlQTNvLWRlLUlDTVMtBjsIVDoOc2VhcmNoX2lkSSIpNDdiYjZhYjctMGZiNC00ZmY0LTlkNWItZDYxZTAxMzM5NmU2BjsIRjoJcmFua2kGOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSJzQ1JPU1MgU2VnbWVudG9zIC0gVE9UVlMgQmFja29mZmljZSBMaW5oYSBQcm90aGV1cyAtIEZJUy0gQ29tbyBpbmNsdWlyIHVtIGFqdXN0ZSBtYW51YWwgbmEgYXB1cmHDp8OjbyBkZSBJQ01TP10GOwhUOhJyZXN1bHRzX2NvdW50aQLpAw%3D%3D--cc4a08700ced6ab57deb9a555e4fafe226af86d7)

[MP - FIS - Como atualizar os códigos de ajuste/lançamentos manuais da apuração de ICMS (tabelas CDO e CC6)?](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwivrPvSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBv2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyMTk5NDY3MS1NUC1GSVMtQ29tby1hdHVhbGl6YXItb3MtYyVDMyVCM2RpZ29zLWRlLWFqdXN0ZS1sYW4lQzMlQTdhbWVudG9zLW1hbnVhaXMtZGEtYXB1cmElQzMlQTclQzMlQTNvLWRlLUlDTVMtdGFiZWxhcy1DRE8tZS1DQzYtBjsIVDoOc2VhcmNoX2lkSSIpYzRmZDJiNjEtNWZlZS00NGI3LWJhYWMtYTRlN2ZjNjIzMzU4BjsIRjoJcmFua2kGOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSJ0TVAgLSBGSVMgLSBDb21vIGF0dWFsaXphciBvcyBjw7NkaWdvcyBkZSBhanVzdGUvbGFuw6dhbWVudG9zIG1hbnVhaXMgZGEgYXB1cmHDp8OjbyBkZSBJQ01TICh0YWJlbGFzIENETyBlIENDNik%2FBjsIVDoScmVzdWx0c19jb3VudGkC6QM%3D--5b54a9a576a68b5bc7cd5e4c189feb5c99d2e9c9)  
  
Após realizar este processo, refaça a **Apuração do ICMS**, extração e integração para o **TAF** e gere novamente o arquivo da **GIA**.
