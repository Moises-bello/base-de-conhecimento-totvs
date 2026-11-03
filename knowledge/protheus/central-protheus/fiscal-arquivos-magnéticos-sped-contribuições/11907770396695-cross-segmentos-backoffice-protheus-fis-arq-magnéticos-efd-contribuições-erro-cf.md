---
article_id: 11907770396695
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 058956ce11daad765a95fef419dc66050bc3c7ecc32b8839a02875b850ac35f6
fetched_at: '2026-06-28T22:42:04.859435+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - BackOffice Protheus - FIS - Arq. Magnéticos - EFD Contribuições
  - Erro CF3_VLRCOF Value on SALDODED:GRVSALDO(FISX001.PRW)
type: support-article
updated_at: '2023-01-25T15:07:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11907770396695-Cross-Segmentos-BackOffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-Erro-CF3-VLRCOF-Value-on-SALDODED-GRVSALDO-FISX001-PRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min****Ocorrência**Ao Processar a apuração de PIS/COFINS através da rotina FISA001, ocorre o seguinte erro **CF3\_VLRCOF Value on SALDODED:GRVSALDO(FISX001.PRW).**  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões]  
  
**Causa**

O problema ocorre porque na **Tabela CF3 - Controle Deducao PIS COF** pode haver alguma sujeira.

**Solução**

Para correção do incidente, faça um backup da tabela CF3, em seguida realize a limpeza da tabela  e gere a apuração novamente.

**Importante:**  
É essencial que seja feito backup da tabela antes da realização do procedimento citado acima.

Além do procedimento indicado acima, verifique também a pergunta **Opção Gravação** na ***wizard*** de geração da apuração **(FISA001)**, pois, esta é uma pergunta  interfere na gravação da tabela CF3.

O comportamento da rotina relacionada a pergunta é o seguinte:

1 - Quando a pergunta **Opção Gravação= Individualizada**, as Tabelas CCY,CCW, SFV e SFW devem estar como "Exclusivas".  
  
Quando a pergunta **Opção Gravação** **= Agrupada,** as  Tabelas CCY,CCW, SFV e SFW  devem estar como "Compartilhadas".
