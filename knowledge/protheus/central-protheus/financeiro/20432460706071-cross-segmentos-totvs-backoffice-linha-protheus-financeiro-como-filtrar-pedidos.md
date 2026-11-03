---
article_id: 20432460706071
category: Financeiro
content_hash: 7ebae52a123ec3416e4722f7e7c0af87fc797e2eb1ee186ca64152eb3bfb08f9
fetched_at: '2026-06-28T22:38:04.173868+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - TOTVS BackOffice (Linha Protheus) - Financeiro - Como filtrar
  Pedidos e Titulos que serão exibidos no Novo Gestor Financeiro
type: support-article
updated_at: '2025-01-24T20:50:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20432460706071-Cross-Segmentos-TOTVS-BackOffice-Linha-Protheus-Financeiro-Como-filtrar-Pedidos-e-Titulos-que-ser%C3%A3o-exibidos-no-Novo-Gestor-Financeiro
---

?![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20432448388375) Tempo aproximado para leitura: **00:10:00 min****Dúvida**Como filtrar Pedidos e Titulos que serão exibidos no Novo Gestor Financeiro?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20432448389911)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da release 12.1.2210  
  
**Solução**Foi implementado o ponto de entrada **NGFJOBQRY** que permite criar um filtro para adicionar uma condição de registros para serem levados as tabelas do NGF.

**"F75 - Titulo a Receber /  Pagar"**

**"F76 - Pedidos de Vendas / Compras"**

Ponto de entrada **NGFJOBQR**, adiciona um filtro **SQL** na query que será considerada para atualizar os títulos / pedidos via [JOB](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410339101591) (Pagar, receber, compras e vendas) na tabela de saldos (**F75**) e/ ou de pedidos (**F76**) utilizada no **Fluxo de caixa do Novo Gestor Financeiro**.

**IMPORTANTE:**

Caso a rotina Novo Gestor Financeiro já esteja em uso e se opte pelo uso do ponto de entrada, o cliente deverá limpar a(s) tabela(s) F75 e/ou F76, assim como o parâmetro **MV\_TFCJOBT**, para a base ser alimentada com as novas regras definidas no ponto de entrada.  
  
**Saiba mais:**  
**[NGFJOBQR - Adiciona filtro na query de seleção dos títulos e/ou pedidos no JOB do Novo Gestor Financeiro](https://tdn.totvs.com/pages/releaseview.action?pageId=718423712)**  
**[Novo Gestor Financeiro - (FINA710 - SIGAFIN)](https://tdn.totvs.com/pages/releaseview.action?pageId=611007335)**
