---
article_id: 360018463012
category: SIGAEST - RELATORIOS
content_hash: 98b781bbe4d829473bc696f61fdd81af2716ac8866021f5fa8e1f67aab1afb71
fetched_at: '2026-06-28T22:39:05.968043+00:00'
product: protheus
section_id: 1500001538841
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR282 - Parametrização
  para validar divergência de saldos SB2 x SB8 x SBF
type: support-article
updated_at: '2025-07-29T17:05:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018463012-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR282-Parametriza%C3%A7%C3%A3o-para-validar-diverg%C3%AAncia-de-saldos-SB2-x-SB8-x-SBF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18366465470999) Tempo aproximado para leitura: **00:03:00 min**

**Duvida**  
**Qual a parametrização CORRETA** do relatório de ***Conferência de Saldos (MATR282)*** para identificarmos desbalanceamento de saldos entre tabelas **SB2** x **SB8** x **SBF**?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**  
**Conceito do Relatório:** O relatório de **Conferência de Saldos (MATR282)** efetua comparativo entre os seguintes saldos disponíveis:   
---***Saldo Físico (******SB2******)***  
---***Saldo por Endereço(******SBF******)***  
---***Saldo por Rastreabilidade (******SB8******)**.*

É muito importante revisar a pergunta **Saldo a Considerar** que traz diferentes perspectivas de análise, listaremos abaixo:  
**- "Saldo a Considerar?"** opções = ***Atual, Movimento e Fechamento***  
***- Atual -***Considera o último saldo gravado nas tabelas SB2, SB8 e SBF;  
***- Movimento -***Considera o saldo pela data informada na pergunta ***Data de referência***, utiliza as tabelas de movimentos para compor o saldo ate a data desejada. Considera B2\_QATU (Saldo Atual) como saldo físico do produto.  
***- Fechamento -***Considera o saldo pela data informada na pergunta ***Data de referência***, utiliza as tabelas de movimentos para compor o saldo até a data desejada. Considera B2\_QFIM (Saldo de fechamento) como saldo físico do produto. Utiliza-se esta opção no processo de fechamento de estoque para realizar a conferência de saldos a serem virados para o próximo período.

|  |
| --- |
| **Para correta validação dos saldos,** **efetuar a parametrização****, conforme a seguir:** |

***Primeiramente uma dica importante nesse cenário******:*** Como o relatório efetua cálculo de todas as movimentações no período indicado, na seleção de código do produto, indique **apenas um código que esteja com divergência e que você esteja analisando**. Ao listar todos os itens, pode ter uma demora além do normal na impressão do relatório (Baixa performance).

**Para identificar saldos desbalanceados é necessário estar parametrizado da seguinte forma:**

***SALDO A CONSIDERAR =*** ***Movimento***

***DATA DE REFERÊNCIA =*** ***Data Atual (Data-base do sistema)***

***LISTAR PRODUTOS =*** ***Ambas***

![Screenshot_1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30558622901655)

Desta forma, na impressão do relatório apresentará se tiver divergência na coluna **STATUS***.* Veja um exemplo abaixo apresentando saldo desbalanceado de um produto e de outro produto correto:

![Screenshot_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30558651006743)

***Obs: Caso não tenha esse relatório no menu,*** [***veja no artigo.***](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000317301-SIGAEST-MATR282-Como-incluir-o-relat%C3%B3rio-MATR282-no-menu?source=search)  
***Sugestão*****:** Assista também o Webinar sobre o conceito de Lote e Endereço, acesse o vídeo [***clicando aqui***](https://www.youtube.com/watch?v=gnVIMBPaYo4).

**Também podera validar através do modelo smartview:**  
[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - SmartView ESTSV009 - Conferência de Saldos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/29621804434071-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-SmartView-ESTSV009-Confer%C3%AAncia-de-Saldos)

Por se tratar de um relatorio descontinuado, o fonte podera ser obtido na central de downloads.  
<https://centraldeatendimento.totvs.com/hc/pt-br/article_attachments/23352944116631>

**Saiba mais:**

[*SIGAEST - MATR282 - Como incluir o relatório MATR282 no menu*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000317301-SIGAEST-MATR282-Como-incluir-o-relat%C3%B3rio-MATR282-no-menu)

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Tratamento correto de desbalanceamento de tabelas de Lote e Endereço em todos os cenários*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402491211159)

[*Clique aqui e veja mais artigos sobre Relatórios do Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360012224673-SIGAEST-RELATORIOS)
