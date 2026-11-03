---
article_id: 4410629918999
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 172bcaf866863b0ca02aa8bb4da380c1864ce70546955c2d163baaab1ceedbb2
fetched_at: '2026-06-28T22:38:28.533394+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Contabilização
  de impostos via Faturamento
type: support-article
updated_at: '2021-11-26T14:05:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410629918999-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Contabiliza%C3%A7%C3%A3o-de-impostos-via-Faturamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como contabilizar os impostos via módulo de Faturamento?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões  
  
**Solução**

Via  faturamento, pode -se utilizar os **lançamentos padronizados 610 ou 620** para contabilização (**CTBANFS**) de impostos, colocando a instrução de contabilização:

Exemplo: 

* Contabilização de ICMS
  + SD2->D2\_VALICM, se for 610;
  + SF2->F2\_VALICM, se for 620;

Não há um lançamento específico para tratar impostos pelo Faturamento.  
  
No módulo de Livros Fiscais, com o uso da nota fiscal manual de saída (mata920), os lançamento que poderão ser utilizados para esta finalidade são :

* **6B7** - Documento de Saída Manual - Inclusão de Documento Itens;
* **6B8** - Documento de Saída Manual - Exclusão de Documento Itens.

Segue a documentação da equipe Fiscal: **[Contabilização das rotinas MATA910 e MATA920 com Lançamento Padrão](https://tdn.totvs.com/x/WLAXDg)**  
  
Para mais informações de lançamento padrões no faturamento, acesse: **[Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - Contabilização no Modulo Faturamento Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056039034-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Contabiliza%C3%A7%C3%A3o-no-Modulo-Faturamento-Protheus?source=search)**
