---
article_id: 23773670362519
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 62be13d3b9d1400cb3edb4850b0073457450beabf810682e89693d91cb77f236
fetched_at: '2026-06-28T22:38:56.867821+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA185 - É possível
  definir o Lote (D3_LOTECTL) automaticamente para evitar a seleção manual?
type: support-article
updated_at: '2025-03-12T12:27:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23773670362519-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA185-%C3%89-poss%C3%ADvel-definir-o-Lote-D3-LOTECTL-automaticamente-para-evitar-a-sele%C3%A7%C3%A3o-manual
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23773670342679) Tempo aproximado para leitura: **00:03:20 min**

**Dúvida**

Na rotina **Baixas das Pre-Requisições (MATA185)**, é possível parametrizar o ambiente de forma que ao Gerar as Pré-Requisições quando o produto controla Lote o Protheus faça a seleção automática do Lote que vence primeiro assim como ocorre em outras rotinas, como por exemplo Liberação de Pedidos de Vendas, entre outras?

![MATA185 LOTE 01.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/23773800857495)

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões

**Solução**

Para a rotina **Baixa de Pré-requisição (MATA185)**, atualmente não tem essa funcionalidade. É necessário definir o Lote que deseja Baixar no momento da Baixa da Pré-requisição.

Dica: no campo Lote (D3\_LOTECTL) pressionar a tecla "Enter" em seguida a tecla "F4" para exibir a consulta "Saldos por Lote". Exemplo abaixo:

![MATA185 LOTE 02.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/23773875026583)

Uma outra alternativa, é a customização da Baixa da Pre-requisição com o **Ponto de Entrada [M185BAIX](https://tdn.totvs.com/x/jhsaDg)**. 

***Saiba Mais:***

[Clique aqui e veja mais artigos sobre MOVIMENTAÇÕES no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)

[SIGAEST - MATA185 - Pontos de Entrada da rotina Baixa de Pré-Requisição ao Armazém](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004530301-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA185-Pontos-de-Entrada-da-rotina-Baixa-de-Pr%C3%A9-Requisi%C3%A7%C3%A3o-ao-Armaz%C3%A9m?source=search)
