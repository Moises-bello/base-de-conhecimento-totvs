---
article_id: 360062275434
category: SIGAEST - CÁLCULOS
content_hash: 2ca9a7e604b191cb88833bc1d8eb6ce2693bb576a40b238f400bab0e09e29d13
fetched_at: '2026-06-28T22:39:04.174772+00:00'
product: protheus
section_id: 1500001550082
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATC010 - Pontos de
  Entrada da rotina Formação de Preços
type: support-article
updated_at: '2025-03-12T12:23:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062275434-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATC010-Pontos-de-Entrada-da-rotina-Forma%C3%A7%C3%A3o-de-Pre%C3%A7os
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30503265863575) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Quais os Pontos de Entrada da rotina MATC010 - Formação de Preços?

**Ambiente**Microsiga Protheus – Estoque/Custos – A partir da versão 11.80  
  
**Solução**Veja abaixo a lista dos Pontos de Entrada relacionados à rotina MATC010 - Formação de Preços:

|  |  |  |
| --- | --- | --- |
| **Ponto de Entrada:** | **Título:** | **Descrição:** |
| **[MC010NOM](https://tdn.totvs.com/display/public/PROT/MC010NOM+-+Altera+o+tamanho+utilizado+no+nome+do+arquivo)** | Altera o tamanho utilizado no nome do arquivo | LOCALIZAÇÃO : Function GRAVA() - Responsável por gravar o arquivo .PDV da planilha. |
| **[MC010GRV](https://tdn.totvs.com/display/public/PROT/MC010GRV+-+Grava+os+elementos+contidos+no+aArray)** | Grava os elementos contidos no aArray | LOCALIZAÇÃO : Function MC010GRVEX - Função da Consulta de Formação de Preços responsável pela chamada desse ponto de entrada. |
| **[MTC010MNU](https://tdn.totvs.com/pages/releaseview.action?pageId=6087830)** | Adiciona opções em formação de preços | LOCALIZAÇÃO: Function MATC010 - Função principal do programa de formação de preços.  EM QUE PONTO: No início da Função, antes da execução da Mbrowse, utilizado para adicionar mais opções de menu da Mbrowse (no aRotina). |
| **[MC10BGRV](https://tdn.totvs.com/pages/releaseview.action?pageId=6087961)** | Mostrar botão quando variável for igual a 2 | Ponto de entrada utilizado para mostrar o botão de gravação mesmo quando a variável ntipo for igual a 2. LOCALIZAÇÃO: Function BrowPlanW. EM QUE PONTO: Na definição dos botões da tela. |
| **[MC010BUT](https://tdn.totvs.com/pages/releaseview.action?pageId=6087657)** | Adiciona botões na tela de formação de preços e desabilita a ação 'PLANILHA' | LOCALIZAÇÃO : Function BrowPlanW - Função que monta a tela dos Browses. |

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Cálculos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360012199493-SIGAEST-C%C3%81LCULOS)*
