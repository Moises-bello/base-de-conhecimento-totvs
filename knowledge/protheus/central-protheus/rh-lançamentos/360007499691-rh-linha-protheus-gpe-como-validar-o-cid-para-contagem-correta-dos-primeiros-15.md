---
article_id: 360007499691
category: RH - Lançamentos
content_hash: d0a45de4bb4239fd7379a5c9a255d6bc30289be19c25260ba3bc86e2c64ccc23
fetched_at: '2026-06-28T22:43:31.438836+00:00'
product: protheus
section_id: 360010781734
source: central-protheus
title: RH - Linha Protheus - GPE - Como validar o CID para contagem correta dos primeiros
  15 dias de Atestado pagos pela Empresa
type: support-article
updated_at: '2025-08-18T19:45:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007499691-RH-Linha-Protheus-GPE-Como-validar-o-CID-para-contagem-correta-dos-primeiros-15-dias-de-Atestado-pagos-pela-Empresa
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22514767738135) Tempo aproximado para leitura: 00:02:00 min**

**Dúvida**Como validar o campo **CID** - Código Internacional de Doença, para contagem correta dos primeiros 15 dias de Atestado pagos pela Empresa?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Embasamento Teórico - Legislação:  
A inserção do número do CID - Código Internacional de Doença no atestado do trabalhador **não é obrigatória**. Segundo o Código de Ética Médica, é vedado ao profissional revelar o fato de que tenha conhecimento em virtude do exercício de sua profissão, salvo por justa causa, dever legal ou autorização expressa do paciente.  
  
Sendo assim, as normas trabalhistas e previdenciárias vinculam esta questão em decorrência de mesma doença e não mesmo CID - Código Internacional de Doença.  
  
Posto isto, segue-se as disposições do artigo 75 do Decreto 3.048/1999 e artigo 60 da Lei 8.213/1991 para esclarecer que são de responsabilidade da empresa o pagamento dos primeiros quinze dias não trabalhados, remetendo o empregado para pagamento do auxílio-doença, feito pelo INSS - Instituto Nacional do Seguro Social , apenas após o décimo sexto dia.  
  
As disposições previdenciárias também permitem que todo o afastamento no período de 60 dias seja considerado para efeito de auxílio-doença.  
  
Portanto, com base no dispositivo acima, o sistema Protheus está parametrizado corretamente para efetuar a contagem da quantidade de dias de atestado, **sem considerar o CID**, uma vez que o mesmo não é obrigatório, contudo, caberá à Previdência Social a avaliação da concessão do benefício previdenciário ou não.

Além disso, o sistema possui tratamento para **informar que um novo afastamento é sequencia de um afastamento anterior** e contabilizar os 15 dias pago pela empresa corretamente. Para mais detalhes, acesse [esta documentação.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049659234-RH-Linha-Protheus-GPE-Como-informar-para-o-sistema-que-o-novo-afastamento-%C3%A9-sequencia-do-anterior)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34272418351127)  
  
Para que os afastamento sequencias sejam validados no prazo de 60 dias habilite o parâmetro **MV\_NDIAEMP,** conforme [esta documentação.](https://tdn.totvs.com/pages/releaseview.action?pageId=910009761)  
 **Saiba Mais**[Documento Técnico](https://tdn.totvs.com/pages/releaseview.action?pageId=221547575)  
[RH - Linha Protheus - GPE - Como incluir novo C.I.D. no Cadastro de Ausências](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhxBMTUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBkWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MTkwMTU1My1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1pbmNsdWlyLW5vdm8tQy1JLUQtbm8tQ2FkYXN0cm8tZGUtQXVzJUMzJUFBbmNpYXMGOwhUOg5zZWFyY2hfaWRJIikwY2I5ODUwNC0zOWZjLTQ3M2UtOWNiNS04YjJlODcyZDcxYzkGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIlNSSCAtIExpbmhhIFByb3RoZXVzIC0gR1BFIC0gQ29tbyBpbmNsdWlyIG5vdm8gQy5JLkQuIG5vIENhZGFzdHJvIGRlIEF1c8OqbmNpYXMGOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--4d8b297f301db8ba48533b04c7185742278087e6)  
[RH - Linha Protheus - GPE - Como configurar o sistema para afastamento superior a 15 dias](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgu8T8%2FXQE6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBmmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzE1MDAwMDQ3NDE0MjItUkgtTGluaGEtUHJvdGhldXMtR1BFLUNvbW8tY29uZmlndXJhci1vLXNpc3RlbWEtcGFyYS1hZmFzdGFtZW50by1zdXBlcmlvci1hLTE1LWRpYXMGOwhUOg5zZWFyY2hfaWRJIikyZjBiY2RiOS00NDc1LTRjZmEtOGM2Ni0wZTI2N2VjMjY3NjUGOwhGOglyYW5raQ46C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIgGKUkggLSBMaW5oYSBQcm90aGV1cyAtIEdQRSAtIENvbW8gdmFsaWRhciBvIGNhbXBvIENvZC4gSW50LiBEb2VuIHBhcmEgY29udGFnZW0gY29ycmV0YSBkb3MgcHJpbWVpcm9zIDE1IGRpYXMgZGUgYXRlc3RhZG8gcGFnb3MgcGVsYSBlbXByZXNhBjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--2f40b266974f721dadc8b6c9145bfd7dcb00c743)  
[RH - Linha Protheus - GPE - Quando o funcionário perde direito ao Período Aquisitivo após o retorno do Afastamento](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwht9CnTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBwWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyNTAyNzY5My1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtUXVhbmRvLW8tZnVuY2lvbiVDMyVBMXJpby1wZXJkZS1kaXJlaXRvLWFvLVBlciVDMyVBRG9kby1BcXVpc2l0aXZvLWFwJUMzJUIzcy1vLXJldG9ybm8tZG8tQWZhc3RhbWVudG8GOwhUOg5zZWFyY2hfaWRJIiliMDBhYjE2MC1lNDgxLTQ3YmItOTEwNi1lY2RmZjEyNDM2ZTkGOwhGOglyYW5raQ86C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhVhdXNlbmNpYSBkb2Vuw6dhBjsIVDoScmVzdWx0c19jb3VudGkCRgM%3D--40dbbb90deb15119fe5018cc7abcb6f9eee67a31)
