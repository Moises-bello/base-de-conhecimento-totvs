---
article_id: 41435533244055
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 9cdcb18b534a03ba7a84025cd8536324966251fa56b0386b3a1cdf1b5953658c
fetched_at: '2026-06-28T22:40:48.802082+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECF : Reg. 0010 "13
  - IND_REC_RECEITA - O campo possui uma valor diferente de seus valores válidos"'
type: support-article
updated_at: '2026-06-23T20:19:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41435533244055-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-Reg-0010-13-IND-REC-RECEITA-O-campo-possui-uma-valor-diferente-de-seus-valores-v%C3%A1lidos
---

O erro "13 - IND\_REC\_RECEITA com valor inválido" ocorre porque o campo deve ser "1" ou "2", mas está sendo gerado como "0". A solução envolve verificar parâmetros na rotina CTBS001, confirmar o registro na tabela CSZ\_REGIME, validar dados no TAF e usar a rotina TAFA372 para garantir a geração correta do campo. Atualizações do sistema podem ser necessárias.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41435549682839) Tempo aproximado para leitura: **15:00 min**  
  
**Dúvida**

"13 - IND\_REC\_RECEITA O campo possui uma valor diferente de seus valores válidos."

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41435533209111)

**Ambiente**  
Cross Segmento - Backoffice Linha Protheus - Contabilidade – A partir da versão 12  
  
  
**Ocorrência**

Erro está sendo apresentado, pois no manual o campo 13 - IND\_REC\_RECEITA deve ser gerado como "1" ou "2", e o arquivo está sendo gerado como "0"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41435533210775)

**Requisitos:**

* Regime tributário: Lucro presumido;
* Apuração trimestral;
* Plano referencial amarrado do Lucro presumido;
* [Como realizar a exportação no Regime tributário Lucro Presumido](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004838052-MP-SIGACTB-ECF-Como-realizar-a-exporta%C3%A7%C3%A3o-no-Regime-tribut%C3%A1rio-Lucro-Presumido?source=search);
* [É permitido utilizar o mesmo modelo de Visão Gerencial já usado no Sped Contábil (ECD)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006823491-MP-SIGACTB-ECF-%C3%89-permitido-utilizar-o-mesmo-modelo-de-Vis%C3%A3o-Gerencial-j%C3%A1-usado-no-Sped-Cont%C3%A1bil-ECD-?source=search);
* [Reg 0010 COMO GERAR OS REGISTRO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050634994-MP-SIGACTB-ECF-Reg-0010-COMO-GERAR-OS-REGISTRO?source=search).

**Solução**

Ao gerar a revisão por meio da rotina de escrituração (CTBS001), verifique os parâmetros abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41435533217687)

Critério de reconhecimento de receitas (IND\_REC\_RECEITA ):

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41435533218711)

Verifique se o registro foi gerado na tabela da contabilidade, no campo "CSZ\_REGIME"

|  |  |  |
| --- | --- | --- |
| **Registro** | **Tabela/CTB** | **TAFST1/TAFST2** |
| Reg. 0010 | CSZ | T127 |

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41435533219863)

Por meio do registro da conta, verifique T127 – Tabela TAFST1 e TAFST2, ou gerenciador de integração, veja se o registro:

[**Blocos/Registros**](http://tdn.totvs.com/pages/viewpage.action?pageId=192094180)**– geração no TAF ou na integração :**[**MP - SIGACTB - ECF - Tabelas ECF**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006861411-MP-SIGACTB-ECF-Tabelas-ECF?source=search)

|T127|20250101|20251231|0|0|00000||0||2|2|5|1|01|PPPP||2||||||1|000|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2||**1**|2|||||||||||||||||2|2|||||||||||2||

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41435549688599)

Através do [Layout do TAF](https://tdn.totvs.com/pages/releaseview.action?pageId=187534666) veja se os dados foram gerados corretamente:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41435533222167)

Através da rotina abaixo, [TAFA372](https://tdn.totvs.com/pages/releaseview.action?pageId=192089512) verifique se o registro foi gerado:

[**Registro 0010 - Parâmetros de Tributação**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006861411-MP-SIGACTB-ECF-Tabelas-ECF)

* Tabela - CHD (Parâmetros de abertura ECF)
* Registro do Layout TOTVS - T127
* Rotina - TAFA372 (Cadastro de Parâmetros de Abertura ECF)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41435533226519)

Ao gerar o arquivo por meio da rotina do TAF, Central de Obrigações (TAFOBRIG)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41435533227159)

Veja se o sistema gerou no registro 0010 o campo 13 - IND\_REC\_RECEITA, corretamente. 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41435549697943)

Caso não esteja sendo gerado, analise se está com as atualizações:

[Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBS001 - Pacote de atualização da ECF 2026, leiaute 12](https://centraldeatendimento.totvs.com/hc/pt-br/articles/41005548608919-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-Pacote-de-atualiza%C3%A7%C3%A3o-da-ECF-2026-leiaute-12)
