---
article_id: 4411620116247
category: SIGAEST - RELATORIOS
content_hash: 45a286127583ff49f25f61d05b98b722f34135ca34c464376a56c6447128ac05
fetched_at: '2026-06-28T22:39:06.012276+00:00'
product: protheus
section_id: 1500001538841
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Ao fazer uma nota
  de Devolução de Compra o movimento está ficando na coluna de Saída do relatório
  MATR900. Como corrigir?
type: support-article
updated_at: '2025-03-12T12:28:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411620116247-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Ao-fazer-uma-nota-de-Devolu%C3%A7%C3%A3o-de-Compra-o-movimento-est%C3%A1-ficando-na-coluna-de-Sa%C3%ADda-do-relat%C3%B3rio-MATR900-Como-corrigir
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30229570042519) Tempo aproximado para leitura: **00:02:00 min****

**Dúvida**

Ao fazer uma nota de Devolução de Compra está ficando na coluna de Saída do relatório MATR900, como colocar na coluna de Entrada?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

O movimento de nota fiscal de entrada **está na coluna de saída**, por ser tratar de uma nota devolução de um **pedido de venda/saída** e fica entre parênteses e isso é padrão do Sistema.   
  
Em uma simulação efetuando uma Nota Fiscal de devolução independentemente do período, ele sempre irá ficar na coluna de saída e em parêntese.

Nesse cenário temos o **parâmetro MV\_LISTDEV** que poderá auxiliar, segue exemplo abaixo com o **parâmetro MV\_LISTDEV** habilitado:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411608334231)

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411619815959)**

Após isso, alteramos o parâmetro para F e executamos o Recálculo do Custo Médio para esse período:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411606039191)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411606066967)

**Observações importantes:**

**-** Lembrando que somente terá efeito ao executar o custo médio em período aberto. É importante sempre avaliar como será o parâmetro MV\_LISTDEV em sua empresa.

 **-** Para exibir estornos de **Movimentos Internos (tabela SD3)** verifique o parâmetro **MV\_D3ESTOR**, [veja a FAQ](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11471154774935-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Exibir-os-estornos-de-Movimentos-internos-D3-ESTORNO-S-no-Kardex).

**Saiba mais:**

[SIGAEST - Exibir os estornos de Movimentos internos (D3\_ESTORNO=S) no Kardex](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11471154774935-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Exibir-os-estornos-de-Movimentos-internos-D3-ESTORNO-S-no-Kardex)

[Clique aqui e veja mais artigos sobre Relatórios do Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538841-SIGAEST-RELATORIOS)
