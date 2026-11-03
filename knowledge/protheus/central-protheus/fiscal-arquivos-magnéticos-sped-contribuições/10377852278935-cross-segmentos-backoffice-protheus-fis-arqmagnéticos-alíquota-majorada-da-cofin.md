---
article_id: 10377852278935
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 6cbafcca8b22a2ca9e259f7b2abe8af75c55691bab57bbe5c4c08152a73ad560
fetched_at: '2026-06-28T22:42:04.899956+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Alíquota Majorada
  da COFINS no EFD Contribuições
type: support-article
updated_at: '2025-05-21T20:08:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10377852278935-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Al%C3%ADquota-Majorada-da-COFINS-no-EFD-Contribui%C3%A7%C3%B5es
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:02:00 min**Dúvida**Tratamento do sistema em relação a **alíquota majorada da COFINS no EFD Contribuições.**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

Por padrão as alíquotas de uma **operação de Importação** são:

**PIS**: **2,10%**

**COFINS**: **10,65%**

Estas alíquotas podem ser definidas através do **Cadastro do Produto** ou pela **rotina de** **Exceção Fiscal**, já que os parâmetros **MV\_TXPIS** e **MV\_TXCOFIN,** são definidos as alíquotas do **PIS e COFINS Cumulativo (0,65% e 3,00%) ou Não Cumulativo (1,65% e 7,60%).**

A **Majoração é 1% na COFINS**, este **1%** é configurado no **Cadastro de TES**, que é o **adicional da despesa/ custo, e que não dá direito ao crédito da COFINS**.

Segue processo de **Majoração da COFINS**, para solucionar essa dúvida, realize os seguintes passos:

1. No **cadastro da TES**, configure os campos **Aliq. Cof M (F4\_MALQCOF)** e **Aliq. Pis M (F4\_MALQPIS).** Informe o **percentual de aumento da Alíquota da PIS e COFINS de Importação**. Estes valores acrescentado **não geram créditos a serem recuperados**.  
  
2. Após o lançamento da **Nota Fiscal**, observe como foram gravados os campos da tabela **SFT** **FT\_MVALCOF** e **FT\_MVALPIS**, neles **são gravados separadamente os valores do PIS e COFINS Majorado**, já os campos **FT\_ALIQPIS** e **FT\_ALIQCOF são gravados as alíquotas da operação**.  
  
3. Acesse a rotina e **processe a Apuração EFD Contribuições** e gere o **relatório de Conferência EFD,** verifique se os valores estão corretos.  
  
4. Ao gerar o **arquivo txt do EFD Contribuições**, o sistema busca a alíquota padrão no campo **FT\_ALIQCOF** e subtrai a alíquota que está no campo **FT\_MALQCOF** para gerar o **registro C170** com a informação da **alíquota 9,65% para COFINS,** visto que **1% não dá direito ao crédito**.

Configuração para a **Nota Fiscal** de Importação:  
<https://tdn.totvs.com/pages/releaseview.action?pageId=6076840>
