---
article_id: 360028384613
category: Inspeção de Entradas (SIGAQIE)
content_hash: 0ca9e00393ed1c72e932d8461ed0faa8b36fa6ba803b3d251fa493e961381606
fetched_at: '2026-06-28T22:42:27.183791+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIE - Unidades de Skip-lote
type: support-article
updated_at: '2024-06-19T18:33:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028384613-Manufatura-Linha-Protheus-SIGAQIE-Unidades-de-Skip-lote
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24294801463959)***Tempo aproximado para leitura: **00:00:50 min**  
**Dúvida**Qual é a diferença entre as **unidades de Skip-lote** disponíveis no campo **Unid.Sk.Lote - QEF\_UNSKLT** da rotina de **Skip-Lote - QIEA120**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Versão 12  
  
**Solução**A seguir a descrição sobre a aplicação das unidades de **Skip-lote**:

* **L-Documento de Entrada**: Serão consideradas as últimas entradas do mesmo produto, fornecedor e lote, **desconsiderando** a informação do campo **Frequência - QEF\_QTDE** da rotina **QIEA0120**.
* **E-Entradas**: Serão considerados os documentos de entradas do mesmo produto e fornecedor conforme a **quantidade** definida no campo **Frequência**.
* **D-Dias**: Serão consideradas as entradas do mesmo produto e fornecedor, conforme a **quantidade de** **dias** definida no campo **Frequência**.
