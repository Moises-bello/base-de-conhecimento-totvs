---
article_id: 18496695290647
category: Escrita Fiscal - Impostos - ISS
content_hash: f3681ac254bf97b1c0ec09b26cdc32e50682c180ae206544cec917e4c7191b06
fetched_at: '2026-06-28T22:39:35.274775+00:00'
product: protheus
section_id: 1500001549762
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS – Registro de Apuração
  de ISS Modelo 56 (MATR912).
type: support-article
updated_at: '2025-01-29T13:06:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18496695290647-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Registro-de-Apura%C3%A7%C3%A3o-de-ISS-Modelo-56-MATR912
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18496701308183) Tempo aproximado para leitura: **00:05:00 min****Dúvida**

Como configurar corretamente para que conste os valores retidos do ISS no relatório Registro de Apuração de ISS Modelo 56 (MATR912)?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**

Para que seja apresentado os valores retidos do ISS, é necessário a seguinte configuração:

Ajuste o parâmetro “MV\_F3RECIS = .T.”.

**PRODUTO**

Cód. Serv. ISS(B1\_CODISS) = Informe o código de serviço do ISS - Caso não haja o código referente ao serviço deve ser incluído na tabela 60 do Configurador.

**TES**  
Calculo ISS (F4\_ISS) = Sim

L. Fiscal ISS (F4\_LFISS) = Tributado

**Observação**

Caso no cadastro da TES esteja com o campo L. Fiscal ISS (F4\_LFISS) = Outros ou Isento, o valor do ISS retido, o código de retenção, base de cálculo e alíquota não irá constar. Exemplo:

![](https://totvssuporte.zendesk.com/attachments/token/Nk1VX06LUY79ewqBOSlQrI54h/?name=inlineImage.png)

- A nota 01 foi criada com o campo L. Fiscal ISS (F4\_LFISS) = Tributado no cadastro da TES.

- A nota 02 foi criada com o campo L. Fiscal ISS (F4\_LFISS) = Isento no cadastro da TES.

- A nota 03 foi criada com o campo L. Fiscal ISS (F4\_LFISS) = Outros no cadastro da TES.
