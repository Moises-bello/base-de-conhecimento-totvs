---
article_id: 11471154774935
category: SIGAEST - RELATORIOS
content_hash: 27204286dd4a4662f8a3e1031ef0b9121f6748e666b9f37420678619da8799ad
fetched_at: '2026-06-28T22:39:06.037583+00:00'
product: protheus
section_id: 1500001538841
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Exibir os estornos
  de Movimentos internos (D3_ESTORNO=S) no Kardex
type: support-article
updated_at: '2025-03-12T12:25:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11471154774935-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Exibir-os-estornos-de-Movimentos-internos-D3-ESTORNO-S-no-Kardex
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30229035793815) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como exibir os estornos de movimentações internas no Kardex (MATR900 / MATR910) e Consulta Kardex (MATC030 / MATC050)?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**Habilitar o parâmetro **MV\_D3ESTOR** para **S**. Esse parâmetro indica se deve exibir os movimentos internos estornados nas consultas e relatórios.

*Exemplo simulado abaixo com um movimento interno de Entrada estornado:*

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11471265983383)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11471383150231)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11471577793431)

***Observação importante:*** Caso processar a rotina Recálculo do CUSTO MÉDIO (MATA330) com o parâmetro **Apagar Estornos** igual a **Sim** Perde-se o registro e não serão exibidos. Atentar-se a necessidade de manter ou não os registros de estornos no ambiente.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11471485829911)

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11471694709015)

***Saiba Mais:***

[SIGAEST - Ao fazer uma nota de Devolução de Compra o movimento está ficando na coluna de Saída do relatório MATR900. Como corrigir?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411620116247--Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Ao-fazer-uma-nota-de-Devolu%C3%A7%C3%A3o-de-Compra-o-movimento-est%C3%A1-ficando-na-coluna-de-Sa%C3%ADda-do-relat%C3%B3rio-MATR900-Como-corrigir?source=search)

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538841-SIGAEST-RELATORIOS)
