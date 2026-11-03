---
article_id: 24590358737431
category: RH - Benefícios
content_hash: 5788809a410392294df690341ec367c2a087b6ad7ac2d2d2deb5476e4b9777d5
fetched_at: '2026-06-28T22:44:03.628328+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Como abater as Faltas lançadas na Folha do cálculo
  de Benefícios
type: support-article
updated_at: '2025-08-29T13:36:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24590358737431-RH-Linha-Protheus-GPE-Como-abater-as-Faltas-lan%C3%A7adas-na-Folha-do-c%C3%A1lculo-de-Benef%C3%ADcios
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24590358684567) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como abater as Faltas lançadas na Folha do cálculo de Benefícios (MV\_USACPER = .T.) ?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para busca de Faltas **lançadas manualmente na folha,** o parâmetro **MV\_USACPER** deve estar com **.T.,** para que seja localizada nas tabelas envolvidas, a existência de verba com o **ID 0054.**Além disso, é utilizado o mnemônico **P\_BENBUSFA** para definir a **quantidade de meses na busca de Faltas.  
  
• Uso do Mnemônico P\_BENBUSFA**- Preenchido com **0**, o sistema irá buscar as Faltas da tabela **RGB do mês de cálculo aberto;**- Preenchido com **1,** o sistema irá buscar primeiro da tabela **SRC** e se não encontrar na SRC aberta, buscará da tabela **SRD do mês anterior ao aberto;**  
- Preenchido com **2,** o sistema irá buscar as Faltas na tabela **SRD de dois meses anteriores ao aberto.****Exemplo de Cálculo** de Vale Alimentação para o período 06/2024:  
- MV\_USACPER = .T.  
- P\_BENBUSFA = 2  
- Funcionário possui duas Faltas lançadas em 04/2024:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24590358688535)

- Nos parâmetros de cálculo, a pergunta '**Descontar Faltas?**" = SIM:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24590352096535)

- Na rotina de **Atualização de Vales** (GPEA133), é possível visualizar que:  
**->** A quantidade total de dias referente ao mês 06/2024 foram **20** (Dias Ut. Mês)   
**->** Serão pagos apenas **18** vales em decorrência das duas Faltas descontadas (Dias Prop., Qtde. Total e Dias Falta)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24590358696215)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24590352105751)

**Saiba Mais**[RH - Linha Protheus - GPE - Como abater as Faltas no cálculo de Benefícios](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhoRV%2FTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBlGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyODUyMTgzMi1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1hYmF0ZXItYXMtRmFsdGFzLW5vLWMlQzMlQTFsY3Vsby1kZS1CZW5lZiVDMyVBRGNpb3MGOwhUOg5zZWFyY2hfaWRJIik3NGJkYjkxYS1hZWJkLTRiMTUtYjBjNC1iYTEyNGQ2MWNhMGMGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIlFSSCAtIExpbmhhIFByb3RoZXVzIC0gR1BFIC0gQ29tbyBhYmF0ZXIgYXMgRmFsdGFzIG5vIGPDoWxjdWxvIGRlIEJlbmVmw61jaW9zBjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--6a4d7e67977500520cde2ecccf18c86eb3b37ebf)  
[RH - Linha Protheus - GPE - Rotinas envolvidas nos cálculos de Benefícios - VR/VA/VT](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjp%2B67UUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBnGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MDUyMzExMy1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtUm90aW5hcy1lbnZvbHZpZGFzLW5vcy1jJUMzJUExbGN1bG9zLWRlLUJlbmVmJUMzJUFEY2lvcy1WUi1WQS1WVAY7CFQ6DnNlYXJjaF9pZEkiKTMyM2Y2NTAyLTViNWMtNDM5ZC04NzE5LWEwNDAxOTVjODU4MwY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiW1JIIC0gTGluaGEgUHJvdGhldXMgLSBHUEUgLSBSb3RpbmFzIGVudm9sdmlkYXMgbm9zIGPDoWxjdWxvcyBkZSBCZW5lZsOtY2lvcyAtIFZSL1ZBL1ZUBjsIVDoScmVzdWx0c19jb3VudGkCZwc%3D--1921442cf79d9f852099a99052735ae4c7af4b6b)  
[Pacote de Expedição Contínua - Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)
