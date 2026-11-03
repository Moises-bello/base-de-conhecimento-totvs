---
article_id: 34313933199895
category: SIGAEST - CUSTOS
content_hash: 6b3ba0201fa448b89793489d00c7a07e833c593a9fcdae9773c8d4569b3ed37f
fetched_at: '2026-06-28T22:39:02.276146+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Nota de entrada com
  TES que não atualiza estoque – Como gerar valor no Custo Standard
type: support-article
updated_at: '2025-08-20T13:50:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34313933199895-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Nota-de-entrada-com-TES-que-n%C3%A3o-atualiza-estoque-Como-gerar-valor-no-Custo-Standard
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34313917747607) Tempo aproximado para leitura: 00**:01:00 min**  
  
**Dúvida**  
Se a nota de entrada utiliza um TES configurado para não atualizar estoque, como o sistema gera valor no Custo Standard do produto?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Conforme documentação oficial TOTVS [Custo de Reposição MATA320](https://tdn.totvs.com/pages/releaseview.action?pageId=448601697), para que o **Custo Standard** seja atualizado a partir de uma nota de entrada, o TES utilizado precisa estar configurado corretamente.

O campo **"Atualiza Preço de Compra" (F4\_UPRC)** é determinante nesse processo. Após a entrada do documento com TES configurado, a atualização do custo deve ser processada pela rotina **MATA320** (Geração do Custo Standard).

Mesmo que o TES esteja definido para **não atualizar estoque (F4\_ESTOQUE = N)**, o sistema poderá gerar valor no **Custo Standard**, desde que o campo **F4\_UPRC** esteja configurado como **“Sim”**.

### Exemplo prático

Documento de entrada com produtos a **10,00**:

* **Produto A** – TES: F4\_ESTOQUE = N, F4\_UPRC = N
* **Produto B** – TES: F4\_ESTOQUE = N, F4\_UPRC = S
* **Produto C** – TES: F4\_ESTOQUE = S, F4\_UPRC = N
* **Produto D** – TES: F4\_ESTOQUE = S, F4\_UPRC = S

#### Após inclusão da nota:

* Produto A → B1\_CUSTD = 0, B1\_UPRC = 0
* Produto B → B1\_CUSTD = 0, B1\_UPRC = 10
* Produto C → B1\_CUSTD = 0, B1\_UPRC = 0
* Produto D → B1\_CUSTD = 0, B1\_UPRC = 10

#### Após processamento do MATA320 – Parâmetro **"Último Custo de Compra"**:

* Produto A → B1\_CUSTD = 0, B1\_UPRC = 0
* Produto B → B1\_CUSTD = 0, B1\_UPRC = 10
* Produto C → B1\_CUSTD = 0, B1\_UPRC = 0
* Produto D → B1\_CUSTD = 10, B1\_UPRC = 10

👉 Nesse cenário, apenas o **Produto D** atualizou simultaneamente **B1\_CUSTD** e **B1\_UPRC**, pois o TES estava com **F4\_ESTOQUE = S** e **F4\_UPRC = S**.

#### Após processamento do MATA320 – Parâmetro **"Último Preço de Compra"**:

* Produto A → B1\_CUSTD = 0, B1\_UPRC = 0
* Produto B → B1\_CUSTD = 10, B1\_UPRC = 10
* Produto C → B1\_CUSTD = 0, B1\_UPRC = 0
* Produto D → B1\_CUSTD = 10, B1\_UPRC = 10

👉 Nesse caso, o **F4\_UPRC** é suficiente para atualizar **B1\_CUSTD** e **B1\_UPRC**, mesmo que o TES não atualize estoque.

### Conclusão

* Quando configurado para **"Último Custo de Compra"**, o sistema depende da combinação dos campos **F4\_ESTOQUE = Sim** e **F4\_UPRC = Sim** para gerar valor no **Custo Standard**.
* Quando configurado para **"Último Preço de Compra"**, basta que o TES tenha **F4\_UPRC = Sim**, mesmo que **F4\_ESTOQUE = Não**.

Assim, mesmo em notas de entrada com TES que **não atualizam estoque**, é possível gerar valor no Custo Standard desde que o TES esteja configurado corretamente no campo **F4\_UPRC**.

[*Clique aqui e veja mais artigos sobre Cálculos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360012199493-SIGAEST-C%C3%81LCULOS)

[*Cross Segmentos - Backoffice (Linha Protheus) - SIGAEST - Conceito de utilização da rotina Custo Standard/Custo de Reposição MATA320 - B1\_CUSTD*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013572791-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAEST-Conceito-de-utiliza%C3%A7%C3%A3o-da-rotina-Custo-Standard-Custo-de-Reposi%C3%A7%C3%A3o-MATA320-B1-CUSTD)
