---
article_id: 4421899347095
category: Escrita Fiscal - Impostos - ICMS - Regime de Processamento
content_hash: 26180e30f71b751455512fe342e2737d954e3679d34babffafef9a2ce745a101
fetched_at: '2026-06-28T22:39:22.844942+00:00'
product: protheus
section_id: 1500001549862
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - MATR930 - Conceito
  da pergunta - CONSIDERA LACUNAS?
type: support-article
updated_at: '2024-10-08T21:32:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4421899347095-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-MATR930-Conceito-da-pergunta-CONSIDERA-LACUNAS
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

Manual do relatório Regime de Processamento de Dados (MATR930

<https://tdn.totvs.com/pages/releaseview.action?pageId=189303671>
