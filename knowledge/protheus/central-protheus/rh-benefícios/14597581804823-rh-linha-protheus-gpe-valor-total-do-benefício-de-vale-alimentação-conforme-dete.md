---
article_id: 14597581804823
category: RH - Benefícios
content_hash: b10ff41382e878377f86dcaac46968d9c916a135cf8147326bd98084b91d7e67
fetched_at: '2026-06-28T22:44:04.830242+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Valor total do benefício de vale alimentação conforme
  determinação do MOS da versão S-1.0
type: support-article
updated_at: '2025-09-30T02:07:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14597581804823-RH-Linha-Protheus-GPE-Valor-total-do-benef%C3%ADcio-de-vale-alimenta%C3%A7%C3%A3o-conforme-determina%C3%A7%C3%A3o-do-MOS-da-vers%C3%A3o-S-1-0
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31927598056599) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como informar o valor total do benefício de vale alimentação conforme determinação do MOS da versão S-1.0?   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**No **MOS da versão S-1.0**, determina que os valores de parcelas salariais in natura devem ser informados pelo valor total e não apenas em relação à parte custeada pelo empregador.   
  
**Exemplo:** Se o declarante cadastrado no PAT fornece cartão alimentação de R$ 200,00 e desconta o correspondente a R$ 30,00 do empregado, deve informar o valor de R$ 200,00 em rubrica atrelada a natureza 1806 e o desconto de R$ 30,00 em rubrica atrelada a natureza 9241.  
  
Para o benefício de **vale alimentação** foi criado o **mnemônico P\_PDVAVAL,** onde deve ser informado a verba para gerar o valor total do benefício ao **efetuar a integração do roteiro VAL**:  
  
**Mnemônico P\_PDVAVAL - Informar a verba de Valor Total**Mnemônico P\_PDVADES - Informar a verba de Desconto funcionárioMnemônico P\_PDVAEMP - Informar a verba de Parte empresa  
  
**Obs.:** As verbas relacionadas ao roteiro VAL, **não devem possuir ID de cálculo.**  
Se a empresa aderiu ao PAT deve cadastrar a natureza de rubrica correspondente ao vínculo com o PAT, que é a natureza 1806. Caso contrário, deve cadastrar a natureza de rubrica correspondente a quando não há vínculo com o PAT, que é a natureza 1807.

**Saiba Mais**[Boletim Ténico](https://tdn.totvs.com/pages/releaseview.action?pageId=630365963#beneficios-BEN)  
[MOS da versão S-1.0](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-0-consolidada-ate-a-no-s-1-0-04-2021.pdf)  
[RH - Linha Protheus - GPE - Cadastro e Cálculo do Vale Alimentação](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhIMmXTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBkWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyODkxMDE1Mi1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ2FkYXN0cm8tZS1DJUMzJUExbGN1bG8tZG8tVmFsZS1BbGltZW50YSVDMyVBNyVDMyVBM28GOwhUOg5zZWFyY2hfaWRJIiliN2I0MmJlMC01NTY1LTQ0MWQtYmQ0Yi0xMmYwNjA3Nzk3OTUGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhd2YWxlIGFsaW1lbnRhw6fDo28GOwhUOhJyZXN1bHRzX2NvdW50aQJgAQ%3D%3D--47fe097a462f3e637b21cafc9ea7288b00b3b0bb)
