---
article_id: 24652434765719
category: Fiscal Arquivos Magnéticos - Extrator Fiscal
content_hash: 3d15a0adc34d71ac4b81c987b8f9151c27677e669a5a06b8bb182bd84615fea1
fetched_at: '2026-06-28T22:42:07.825128+00:00'
product: protheus
section_id: 1500001535021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Layout T001AE
  -GNRE -  Código  Produto (C0R_CODPRD) não existe na base de dados.
type: support-article
updated_at: '2024-07-04T18:27:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24652434765719-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Layout-T001AE-GNRE-C%C3%B3digo-Produto-C0R-CODPRD-n%C3%A3o-existe-na-base-de-dados
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24652434738199) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Erro 1 - Linha: 1 - **O valor '89' informado na coluna 20 para o campo Cod. Produto (C0R\_CODPRD) não existe na base de dados**.  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TAF – Nova GIA – Todas as versões.  
  
**Causa**Este incidente ocorre, pois **Código de Produto (C0R\_CODPRD)** não existe na base de dados do **TAF**, o erro ocorre ao tentar integrar o *Layout* **T001AE- Documento de Arrecadação**, quando o campo **F6\_CODPROD** é preenchido com o **"Código do Produto"** na **Guia GNRE**, tabela **SF6** no **Protheus**,  é não foi importado para o **TAF**. Este dado populará a tabela **C0R - Documento de Arrecadação.**  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Por favor verifique na Tabela  **C6U** se existe o código "**89** "  verifique a atualização do autocontidas do TAF no Passo 3º **Wizard de Configuração**,  para que possa ser atualizado os cadastros padrão na tabela **C6U** no **TAF**: [Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - GIA-SP - 3º Passo - Wizard de Configuração](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwh%2BPL3TUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBt2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAzNDY3OTkzNC1Dcm9zcy1TZWdtZW50b3MtQmFja29mZmljZS1Qcm90aGV1cy1GSVMtQXJxLU1hZ24lQzMlQTl0aWNvcy1HSUEtU1AtMyVDMiVCQS1QYXNzby1XaXphcmQtZGUtQ29uZmlndXJhJUMzJUE3JUMzJUEzbwY7CFQ6DnNlYXJjaF9pZEkiKWY1Mjg0ZDNiLTVmMTUtNDE1Zi05ODBlLTdiZDIxMGI4ZTJjMAY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkicENyb3NzIFNlZ21lbnRvcyAtIEJhY2tvZmZpY2UgUHJvdGhldXMgLSBGSVMgLSBBcnEuTWFnbsOpdGljb3MgR0lBLVNQIC0gM8K6IFBhc3NvIC0gV2l6YXJkIGRlIENvbmZpZ3VyYcOnw6NvBjsIVDoScmVzdWx0c19jb3VudGkC6AM%3D--0e7403f2bcbb19933243e0f5be98bd302236a4de)

2. Verifique se existe o cadastro do código de Produto na tabela **C6U**, caso o cadastro não exista efetuar a inclusão do cadastro de forma manual na tabela **C6U** do **TAF** através da rotina **Tabela dinâmica**:

3. Para incluir o cadastro de produto no T**AF Acesse o módulo TOTVS Automação Fiscal → Consultas → Tabelas Dinâmicas → Filtre a tabela C6U por código → Abrir Browse → Incluir.**

1) No menu do **TAF**, vá em **Consultas →** **Tabela Dinâmica**.

![IM1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24652450473751)

2) No filtro, selecione a Tabela **C6U**.

![IMG2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24652434738839)

3) Ao selecionar a tabela **C6U**, selecione a opção, "**Abrir Browse**"

![IMG3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24652450478231)

4) Selecione a opção **incluir**.

![inc.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24652434744983)

5) Após seguir os passos acima, realize a integração novamente para o *Layout* **T001AE- Documento de Arrecadação** no **TAF**.

Para mais informações acesse:

[Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Layout T013 GNRE C25\_IDENTI inexistente](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhIpcDSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBqWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAxODEyNjE1Mi1Dcm9zcy1TZWdtZW50b3MtQmFja29mZmljZS1Qcm90aGV1cy1GSVMtQXJxLU1hZ24lQzMlQTl0aWNvcy1MYXlvdXQtVDAxMy1HTlJFLUMyNS1JREVOVEktaW5leGlzdGVudGUGOwhUOg5zZWFyY2hfaWRJIillNjk2NDNlNi04OTRjLTQzNTMtYTMwMi00ZThlOTRiYzMxOGYGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJImxDcm9zcyBTZWdtZW50b3MgLSBCYWNrb2ZmaWNlIFByb3RoZXVzIC0gRklTIC0gQXJxLk1hZ27DqXRpY29zIC0gTGF5b3V0IFQwMTMgR05SRSBDMjVfSURFTlRJIGluZXhpc3RlbnRlBjsIVDoScmVzdWx0c19jb3VudGkCZwI%3D--654a5915d3e5ad0428ab47f436450014d0f8744c)

[Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Procedimento Completo Nova GIA](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXEOLSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBoGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyMDMxNjMxMS1Dcm9zcy1TZWdtZW50b3MtQmFja29mZmljZS1Qcm90aGV1cy1GSVMtQXJxLU1hZ24lQzMlQTl0aWNvcy1Qcm9jZWRpbWVudG8tQ29tcGxldG8tTm92YS1HSUEGOwhUOg5zZWFyY2hfaWRJIik2NmU1ZmQwZi02NDlkLTQ3OTAtYTI1MS0zOGQxZDFiYWQ3NDUGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJImJDcm9zcyBTZWdtZW50b3MgLSBCYWNrb2ZmaWNlIFByb3RoZXVzIC0gRklTIC0gQXJxLk1hZ27DqXRpY29zIC0gUHJvY2VkaW1lbnRvIENvbXBsZXRvIE5vdmEgR0kGOwhUOhJyZXN1bHRzX2NvdW50aQLoAw%3D%3D--5bbd059bac6178beb4116b5646f86d6c7e881d65)
