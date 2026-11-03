---
article_id: 1500004367962
category: SIGAEST - CUSTOS
content_hash: cae330390f7e56d02a8dd8c7a376b57e8b3adbf3269aff93d86d02cec45ebcd2
fetched_at: '2026-06-28T22:39:02.061064+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA320 - Pontos de
  Entrada da rotina Custo Standard (Custo de Reposição)
type: support-article
updated_at: '2025-08-07T20:27:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004367962-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA320-Pontos-de-Entrada-da-rotina-Custo-Standard-Custo-de-Reposi%C3%A7%C3%A3o
---

**Dúvida**Quais os Pontos de Entrada da rotina MATA320 - Custo Standard?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Veja abaixo os pontos de entrada relacionados à rotina MATA320 - Custo Standard (Custo de Reposição)

|  |  |  |
| --- | --- | --- |
| **Ponto de Entrada** | **Título:** | **Descrição:** |
| **[M320FIM](https://tdn.totvs.com/pages/releaseview.action?pageId=6087585)** | Customizações no final da rotina de custo de reposição | LOCALIZAÇÃO : Function MA320Process() - Função utilizada para processar o calculo do custo de reposição.  EM QUE PONTO : Executada após a calculo do custo de reposição, ponto de entrada utilizado para realizar customizações no final da rotina de custo de reposição.  Eventos |
| **[M320FILPR](https://tdn.totvs.com/display/public/PROT/M320FILPR)** | Customização do Filtro no Recálculo do Custo | Este ponto de entrada tem o objetivo customizar o filtro no Recálculo do Custo de Reposição para o último preço de compra. |
| **[M320ESTRU](https://tdn.totvs.com/pages/releaseview.action?pageId=6087986)** | Customização do Filtro no Recálculo do Custo (Estrutura) | Localização: Está localizado na função MA320Estru que tem o Objetivo de Atualizar o custo standard (B1\_CUSTD) dos PA's e PI's baseado na estrutura dos mesmos, buscando o custo standard dos filhos e o índice técnico de cada item.  Finalidade: Este Ponto de Entrada tem o objetivo de customizar o filtro no Recálculo do Custo de Reposição, quando o custo for calculado pela estrutura. |
| **[A320CUST](https://tdn.totvs.com/display/public/PROT/TTGFXH_EST_DT_Ponto_de_Entrada_A320CUST)** | Gravação e Atualização do Custo de Reposição | O ponto de entrada A320CUST foi desenvolvido para realização de dois tratamentos:   * MA320Estru(): Executado após o cálculo e gravação do custo standard para cada produto calculado pela estrutura permitindo customizações do usuário. * MA320LCust(): Função utilizada para atualizar o custo standard (B1\_CUSTD) baseado no ultimo custo de NF de compra. |
| **[A320CUSM](https://tdn.totvs.com/pages/releaseview.action?pageId=236427350)** | Novo Custo Standard para o produto | Este ponto de entrada permite ao usuário obter um novo custo standard para o produto através de uma fórmula ou outra regra desejada. Por exemplo, se o custo standard da matéria-prima estiver em moeda diferente do produto acabado, será possível obter a taxa referente à moeda da MP e converter o custo para a moeda do PA. |
| **[A320LOOP](https://tdn.totvs.com/pages/releaseview.action?pageId=236427370)** | Permite manipular o arquivo de trabalho no SG1 | Descrição: LOCALIZAÇÃO : Function MostraProc() - Função utilizada para realizar o acertos dos niveis do SG1  EM QUE PONTO : Este ponto de Entrada permite manipular o arquivo de trabalho do SG1. |
| **[M320FILNF](https://tdn.totvs.com/display/public/PROT/M320FILNF)** | Customização do Filtro no Recálculo do Custo | Este ponto de entrada tem o objetivo de customizar o filtro no Recálculo do Custo de Reposição para o último custo da compra. |

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Cálculos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360012199493-SIGAEST-C%C3%81LCULOS)*
