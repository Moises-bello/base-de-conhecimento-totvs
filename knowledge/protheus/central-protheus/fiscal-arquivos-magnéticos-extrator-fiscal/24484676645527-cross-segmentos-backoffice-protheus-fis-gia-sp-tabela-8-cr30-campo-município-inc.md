---
article_id: 24484676645527
category: Fiscal Arquivos Magnéticos - Extrator Fiscal
content_hash: 7050a77ca6a3b8bc1b5db63883f007c613b1a53d27df3b6a7c39c1e2fac8b89b
fetched_at: '2026-06-28T22:42:07.961758+00:00'
product: protheus
section_id: 1500001535021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - GIA-SP - Tabela 8, CR=30, Campo
  Município Inconsistentes, Posição 5, linha Nº XX
type: support-article
updated_at: '2024-06-28T12:28:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24484676645527-Cross-Segmentos-Backoffice-Protheus-FIS-GIA-SP-Tabela-8-CR-30-Campo-Munic%C3%ADpio-Inconsistentes-Posi%C3%A7%C3%A3o-5-linha-N%C2%BA-XX
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24484737095319) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**Erro de validação no arquivo da **GIA-SP**:

**Tabela 8, CR=30, Campo Município Inconsistentes, Posição 5, linha Nºxx.**  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TAF – Nova GIA – Todas as versões.  
  
**Causa**O erro de validação ocorre, pois o **Município** gerado no arquivo da **GIA-SP**, não pertence a tabela 15-Relação de Municípios Paulistas válidos.  
  
**Solução**Para solucionar essa ocorrência, no registro **CR=30**, siga os passos abaixo, para corrigir o erro de validação na **GIA-SP** :  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Verifique se o Fornecedor ou Cliente é participante da **DIPAM-B**  
- Inclua a **UF** para o qual será gerado o **CR=30**;  
-  Informe no **Cadastro de Cliente** ou **Fornecedor** a **UF (SP)** e **Código do Município**, preencher  os campos: **A1/A2\_EST** "Estado" e **A2/A1\_COD\_MUN** **"Cod. Municipio"**:  
- Se for cadastro de cliente preencher **A1\_EST "Estado" e A1\_COD\_MUN "Cod. Municipio"**:

![A1_COD_MUN.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24484737103767)

Se cadastro de fornecedor preencher **A2\_EST** **"Estado" e A2\_COD\_MUN "Cod. Municipio"**:

![A2_EST.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24484737106327)  
  
2. Para os participantes da **DIPAM-B,** é necessário parametrizar o código da cidade que pertence a **Tabela 15-Relação de Municípios Paulistas Válidos**

- Informe no parâmetro **MV\_UFIPM = SP** (se a nota for gerada para essa UF);

3. Após seguir os passos acima, realize a escrituração da nota novamente, e realize a integração no **TAF**.

4. Acesse a rotina Central de Obrigações (**TAFOBRIG**), e gere um novo arquivo **GIA** e valide-o.

Para mais informações acesse:

[Cross Segmentos - Backoffice Protheus - FIS - GIA-SP - Tabela 8, CR=30, Campos - CódDIP ou CFOP inválidos](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjNkZnUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBrWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA0OTExOTY5My1Dcm9zcy1TZWdtZW50b3MtQmFja29mZmljZS1Qcm90aGV1cy1GSVMtR0lBLVNQLVRhYmVsYS04LUNSLTMwLUNhbXBvcy1DJUMzJUIzZERJUC1vdS1DRk9QLWludiVDMyVBMWxpZG9zBjsIVDoOc2VhcmNoX2lkSSIpMTlkOTUyZmItZjYxMy00ZjFiLWEwZmItNWE2ZmE2M2I2YjU0BjsIRjoJcmFua2kGOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSJwQ3Jvc3MgU2VnbWVudG9zIC0gQmFja29mZmljZSBQcm90aGV1cyAtIEZJUyAtIEdJQS1TUCAtIFRhYmVsYSA4LCBDUj0zMCwgQ2FtcG9zIC0gQ8OzZERJUCBvdSBDRk9QIGludsOhbGlkb3MGOwhUOhJyZXN1bHRzX2NvdW50aQLoAw%3D%3D--75beecac9aafee28301448a151810fe3b0b5bd13)

[Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Procedimento Completo Nova GIA](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXEOLSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBoGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyMDMxNjMxMS1Dcm9zcy1TZWdtZW50b3MtQmFja29mZmljZS1Qcm90aGV1cy1GSVMtQXJxLU1hZ24lQzMlQTl0aWNvcy1Qcm9jZWRpbWVudG8tQ29tcGxldG8tTm92YS1HSUEGOwhUOg5zZWFyY2hfaWRJIik2NmU1ZmQwZi02NDlkLTQ3OTAtYTI1MS0zOGQxZDFiYWQ3NDUGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJImJDcm9zcyBTZWdtZW50b3MgLSBCYWNrb2ZmaWNlIFByb3RoZXVzIC0gRklTIC0gQXJxLk1hZ27DqXRpY29zIC0gUHJvY2VkaW1lbnRvIENvbXBsZXRvIE5vdmEgR0kGOwhUOhJyZXN1bHRzX2NvdW50aQLoAw%3D%3D--5bbd059bac6178beb4116b5646f86d6c7e881d65)

*Link* **Manual da Nova GIA-SP - Pré-formatado-NG.** <https://portal.fazenda.sp.gov.br/servicos/gia/Downloads/pre_formatado_ngia_v0210_gia0801.pdf>
