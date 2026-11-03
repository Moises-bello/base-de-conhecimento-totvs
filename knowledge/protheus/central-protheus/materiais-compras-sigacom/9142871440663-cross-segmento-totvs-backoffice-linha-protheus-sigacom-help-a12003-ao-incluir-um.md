---
article_id: 9142871440663
category: Materiais - Compras (SIGACOM)
content_hash: 097fd9d1d355eb453ee0aaae977d52b29bdf6ef1e42b9bae1b770586cb3cf097
fetched_at: '2026-06-28T22:41:11.661751+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Help A12003
  ao Incluir um Pedido de Compras
type: support-article
updated_at: '2026-05-04T19:49:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9142871440663-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGACOM-Help-A12003-ao-Incluir-um-Pedido-de-Compras
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Ao incluir um Pedido de Compras é apresentado o Help A12003

![imagem2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9138053660055/imagem2.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Versão 12  
  
**Solução**O Help A12003 geralmente é exibido quando ocorre o campo C7\_TOTAL teve a quantidade de casas decimais alteradas;

OBS :  Campos de quantidade devem todos possuir mesmo tamanho/ máscara. Campos de valor também devem possuir mesmo tamanho/ máscara.  
Com exceção de campos de Valor Total. CAMPOS TOTAIS NÃO SE ALTERA CASAS DECIMAIS, estes devem permanecer com 2 casas decimais (evitando inclusive erros em arquivos fiscais).

Ou quando há arredondamento do valor total do item do Pedido de Compras.

Para que não ocorra o arredondamento, você pode alterar o parâmetro MV\_ARRPEDC para **NOROUND**, para que não haja o arredondamento.

***Saiba Mais:***

* ***[Aumento de Casas Decimais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9031097398167-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGACOM-Aumento-de-Casas-Decimais?source=search)***
* [Parâmetro MV\_ARRPEDC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026153752-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Par%C3%A2metro-arredondamento-do-Valor-Total-do-Pedido-de-Compras-MV-ARRPEDC)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
