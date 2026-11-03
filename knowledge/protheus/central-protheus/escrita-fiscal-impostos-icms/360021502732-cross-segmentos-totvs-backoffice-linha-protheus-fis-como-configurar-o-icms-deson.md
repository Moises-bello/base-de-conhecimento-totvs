---
article_id: 360021502732
category: Escrita Fiscal - Impostos - ICMS
content_hash: 40ba7b4dc61268e79d5a7756f4e1a2ca7baff7f96221511b63c6d8d484b5048e
fetched_at: '2026-06-28T22:39:24.171067+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: 'CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como configurar
  o ICMS desonerado para órgão público? '
type: support-article
updated_at: '2021-07-28T02:27:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021502732-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-o-ICMS-desonerado-para-%C3%B3rg%C3%A3o-p%C3%BAblico
---

**Dúvida**Como configurar o ICMS desonerado para órgão público?

**Ambiente**Protheus – Livros Fiscais– A partir da versão 11.80  
  
  
**Solução**

No **Cadastro de Clientes (MATA030)**, informe um cliente com os seguintes detalhes:

 Campo **Tipo Pessoa (A1\_TPESSOA) = EP** - Indica que é empresa pública.

No Cadastro de Tipos de **Entrada/Saída (MATA080)**, informe uma TES com os seguintes detalhes:

* Campo **Agrega Valor (F4\_AGREG) = D** – Indica que deve descontar o valor do imposto do valor contábil.
* Campo **Cálculo ICMS (F4\_ICM) = Sim** – Indica que haverá o cálculo do ICMS.
* Campo **L.Fiscal ICMS (F4\_LFICM) = Isento**– Indica que será escriturado como Isento.
* Campo **Sit.Trib.ICMS (F4\_SITTRIB)=40** – Indica que Isento.
* Campo **Mot.Desone. (F4\_MOTICMS) =8** – Indica venda órgão publico.
* Campo **Calc. Difal****(F4\_DIFAL=”1=Sim”)** – Indica venda de Difal

Quando utilizada a configuração para dedução do valor de ICMS do total do documento (F4\_AGREG = D) em uma operação com DIFAL será abatidos os valores de ICMS Próprio e DIFAL. Em alguns casos, como por exemplo uma operação de venda de medicamentos contra o câncer (Convênio 164/94) com origem em São Paulo e destinada a Goiás, que não é um estado signatário do convênio em questão, o recolhimento da parcela do DIFAL (dos dois estados) deverá ser feito normalmente, sem considerar a dedução do ICMS próprio. Desta forma, deve ser deduzido do valor total do documento apenas o valor referente ao ICMS Próprio.

Esta configuração deverá ser feita através do campo **Ded.Difal (****F4\_DEDDIF)**. As opções são:

**1 - Sim:** Serão deduzidos o ICMS Próprio e DIFAL do total do documento. Esta é a configuração padrão deste campo.

**2 - Não:** Será deduzido apenas o ICMS Próprio do total do documento.

**Atenção:** A utilização desta configuração deverá ser em conjunto com a configuração para dedução do ICMS (**F4\_AGREG = D**). Do contrário a mesma não surtirá efeito.
