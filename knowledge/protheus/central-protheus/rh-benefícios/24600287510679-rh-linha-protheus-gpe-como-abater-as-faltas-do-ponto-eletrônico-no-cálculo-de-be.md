---
article_id: 24600287510679
category: RH - Benefícios
content_hash: 3a386a237379d3efd848090f2500761e262e4bb6e38e45898f330130b29e7e68
fetched_at: '2026-06-28T22:44:03.623431+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Como abater as Faltas do Ponto Eletrônico no cálculo
  de Benefícios
type: support-article
updated_at: '2025-08-21T18:54:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24600287510679-RH-Linha-Protheus-GPE-Como-abater-as-Faltas-do-Ponto-Eletr%C3%B4nico-no-c%C3%A1lculo-de-Benef%C3%ADcios
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24600230364695) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como abater as Faltas do Ponto Eletrônico no cálculo de Benefícios (MV\_USACPER= .F.)?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para busca de **Faltas do Ponto Eletrônico,** o parâmetro **MV\_USACPER** deve estar com conteúdo **.F.,** para que sejam consultadas as tabelas **SPC** e **SPH** (Apontamentos).  
  
Além disso, são utilizados os mnemônicos abaixo:   
  
**• Mnemônico P\_BENBUSFA** - Quantidade de meses utilizados para busca de Faltas.  
- Preenchido com **0**, o sistema irá buscar as Faltas da tabela **SPC do período aberto** no Ponto;  
- Preenchido com **1,** o sistema irá buscar as Faltas da tabela **SPH do período anterior ao aberto** no Ponto;  
- Preenchido com **2,** o sistema irá buscar as Faltas na tabela **SPH do dois períodos anteriores ao aberto** no Ponto.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24959316193559)

**• Mnemônico P\_BENPONEV -** Eventos de Faltas que serão considerados na busca.  
Seu preenchimento deve ser **numérico** e informado entre aspas dupla, como no exemplo abaixo:

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/24960823730967)****Exemplo** de Cálculo de Vale Alimentação para o período 05/2024:  
**- MV\_USACPER** = .F.  
**- P\_BENBUSFA** = 0  
**- P\_BENPONEV** = "009,010"

-Funcionário possui uma Falta apontada no **evento 009:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24959498377495)

- Nos parâmetros de cálculo, a pergunta '**Descontar Faltas?**" = SIM:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24934403227287)

- Na rotina de **Atualização de Vales** (GPEA133), é possível visualizar que:  
**->** A quantidade total de dias referente ao mês 05/2024 foram **23** (Dias Ut. Mês)   
**->** Serão pagos apenas **22** vales em decorrência da Falta descontada (Dias Prop., Qtde. Total)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24959316197015)

**Saiba Mais**[RH - Linha Protheus - GPE - Como abater as Faltas no cálculo de Benefícios](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhoRV%2FTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBlGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyODUyMTgzMi1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1hYmF0ZXItYXMtRmFsdGFzLW5vLWMlQzMlQTFsY3Vsby1kZS1CZW5lZiVDMyVBRGNpb3MGOwhUOg5zZWFyY2hfaWRJIik3NGJkYjkxYS1hZWJkLTRiMTUtYjBjNC1iYTEyNGQ2MWNhMGMGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIlFSSCAtIExpbmhhIFByb3RoZXVzIC0gR1BFIC0gQ29tbyBhYmF0ZXIgYXMgRmFsdGFzIG5vIGPDoWxjdWxvIGRlIEJlbmVmw61jaW9zBjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--6a4d7e67977500520cde2ecccf18c86eb3b37ebf)  
[RH - Linha Protheus - GPE - Rotinas envolvidas nos cálculos de Benefícios - VR/VA/VT](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjp%2B67UUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBnGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MDUyMzExMy1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtUm90aW5hcy1lbnZvbHZpZGFzLW5vcy1jJUMzJUExbGN1bG9zLWRlLUJlbmVmJUMzJUFEY2lvcy1WUi1WQS1WVAY7CFQ6DnNlYXJjaF9pZEkiKTMyM2Y2NTAyLTViNWMtNDM5ZC04NzE5LWEwNDAxOTVjODU4MwY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiW1JIIC0gTGluaGEgUHJvdGhldXMgLSBHUEUgLSBSb3RpbmFzIGVudm9sdmlkYXMgbm9zIGPDoWxjdWxvcyBkZSBCZW5lZsOtY2lvcyAtIFZSL1ZBL1ZUBjsIVDoScmVzdWx0c19jb3VudGkCZwc%3D--1921442cf79d9f852099a99052735ae4c7af4b6b)  
[RH - Linha Protheus - GPE - Quando o parâmetro MV\_USACPER = .F. o campo R0\_FALTAS fica zerado](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgX889WAQQ6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBn2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzQ0MDM3OTc5NDcxNTktUkgtTGluaGEtUHJvdGhldXMtR1BFLVF1YW5kby1vLXBhciVDMyVBMm1ldHJvLU1WLVVTQUNQRVItRi1vLWNhbXBvLVIwLUZBTFRBUy1maWNhLXplcmFkbwY7CFQ6DnNlYXJjaF9pZEkiKWFlZTJjZGE1LTUwMzctNDRhOS1hMTNjLTkwYjE5ODY0MWU4YwY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiY1JIIC0gTGluaGEgUHJvdGhldXMgLSBHUEUgLSBRdWFuZG8gbyBwYXLDom1ldHJvIE1WX1VTQUNQRVIgPSAuRi4gbyBjYW1wbyBSMF9GQUxUQVMgZmljYSB6ZXJhZG8GOwhUOhJyZXN1bHRzX2NvdW50aQLoAw%3D%3D--2bae1731fd4366aa7784eae05d58cc775576b458)
