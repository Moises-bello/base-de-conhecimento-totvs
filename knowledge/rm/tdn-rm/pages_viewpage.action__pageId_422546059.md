---
content_hash: 15c050d0b2e712968ca5a667b5af3dba82a0e65b451618a680502229af7fd510
fetched_at: '2026-06-29T00:09:23.165859+00:00'
page_id: '422546059'
product: rm
source: tdn-rm
title: Registro 0145 (EFD Contribuições)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422546059
version: 3
---

**Registro 0145 - Regime de Apuração da Contribuição Previdenciária sobre a Receita Bruta**

|  |  |  |
| --- | --- | --- |
| **CAMPO** | **DESCRIÇÃO DO CAMPO** | **ORIGEM DOS DADOS** |
| REG | Texto fixo contendo 0145 | Gerado automaticamente pela rotina |
| COD\_INC\_TRIB | Código indicador da incidência no período:   1 - Contribuição previdenciária apurada no período, exclusivamente com base na receita bruta   2 - Contribuição previdenciária apurada no período com base na receita bruta e com base nas remunerações pagada na forma dos [incisos I e III do art.22 da lei nº 8.212 de 1991](http://www.planalto.gov.br/ccivil_03/LEIS/L8212cons.htm) | Gerado de acordo com o parâmetro: Código indicador de método de apropriação de a créditos da tela de geração da rotina |
| VL\_REC\_TOT | Valor da receita bruta total da pessoa jurídica no período | Valor gravado no campo apresentado na tela de outros dados do período de apuração do tributo Cont. Previdenciárias. Este campo é preenchido manualmente. |
| VL\_REC\_ATIV | Valor da receita bruta total das atividades sujeitas a contribuição previdenciária sobre a receita bruta. | Gerado com a totalização do valor da mercadoria dos itens que possuem o tributo Contr. Previdenciárias:   a) Os lançamentos de saída geram o valor a recolher.   b) Os lançamentos de entrada (Devolução/Vendas Canceladas) irão gerar o valor a ser deduzido da base de cálculo |
| VL\_REC\_DEMAIS\_ATIV | Valor da receita bruta das atividades sujeitas a contribuição previdenciária sobre a remuneração ([incisos I e III do Art. da lei nº 8.212 de 1994](http://www.planalto.gov.br/ccivil_03/LEIS/L8212cons.htm)) | Gerado com a diferença entre o total da receita e o total da receita sujeita a contribuição (VL\_REC\_TOT - VL\_REC\_ATIV) |
| INFO\_COMPL | Informação complementar | Não será gerado |
