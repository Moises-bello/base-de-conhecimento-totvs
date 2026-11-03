---
article_id: 360023594412
category: Escrita Fiscal - Impostos - ICMS
content_hash: 93107a1bf9bf0f7d65610787676ae0cfb90718e358734b1390b0e0ead4d211ad
fetched_at: '2026-06-28T22:39:24.233822+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - MATR930 - Conceito
  da pergunta - CONSIDERA LACUNAS?
type: support-article
updated_at: '2024-04-16T18:11:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023594412-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-MATR930-Conceito-da-pergunta-CONSIDERA-LACUNAS
---

**Dúvida**

MATR930 - Conceito da pergunta - CONSIDERA LACUNAS?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Livros Fiscais - a partir da versão 12  
  
  
**Solução**

Veja as explicações sobre este parâmetro:

**Conceito da pergunta - CONSIDERA LACUNAS?:**

* **SIM =** Lista as notas fiscais que foram excluídas através da rotina exclusão de **Documento de Saída** (se a nota fiscal foi gerada pelo Faturamento), ou através da exclusão da nota fiscal manual de saída (se a nota fiscal foi gerada através dos Livros Fiscais).

Também são impressas as notas fiscais que não foram utilizadas, mas estão na sequência numérica lógica.  
  
Ex: dia 19/04/21 foram emitidas as notas fiscais 15,16,17 e por qualquer motivo a nota fiscal seguinte foi a 34, o sistema considera como lacuna imprimindo no relatório da nota fiscal 18 até a 33 como cancelada.

* **NÃO =** Não lista notas fiscais canceladas e nem as notas fiscais fora da sequência.

* **CANCELADA =**Lista as notas fiscais que foram excluídas através da rotina exclusão de Documento de Saída (se a nota fiscal foi gerada pelo Faturamento), ou através da exclusão da nota fiscal manual de saída (se a nota fiscal foi gerada através dos Livros Fiscais).

Para identificar na tabela Livros Fiscais (SF3) se as notas são realmente canceladas, o sistema grava automático o **Data do cancelamento (F3\_DTCANC)** e **Observações (F3\_OSERV) = NF CANCELADA**

**Informações adicionais:**

Manual do relatório Regime de Processamento de Dados (MATR930)

<https://tdn.totvs.com/pages/releaseview.action?pageId=708115006>
