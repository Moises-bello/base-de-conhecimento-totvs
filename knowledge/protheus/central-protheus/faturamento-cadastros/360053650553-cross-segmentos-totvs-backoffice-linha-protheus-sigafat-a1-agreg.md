---
article_id: 360053650553
category: Faturamento - Cadastros
content_hash: 2fa703f5e93fe3b57621fc6b5ab6655c9f5b9ef5cbe5969e18ff0e3fe6272fcb
fetched_at: '2026-06-28T22:38:35.585126+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGAFAT - A1_AGREG
type: support-article
updated_at: '2022-08-25T11:10:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053650553-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-A1-AGREG
---

**Dúvida**

Qual a finalidade de uso do campo **A1\_AGREG**?

**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGAFAT - todas as versões.  
  
**Solução**

* **Agrega liberados - A1\_AGREG**

Este campo é utilizado para ordenar a geração dos documentos de saída de clientes com alguma característica em comum. Para isto, é necessário indicar alguma informação para sua identificação.

***Observe o exemplo:***

Para facilitar a entrega dos pedidos dos clientes instalados na região norte do município de São Paulo, pode-se preencher o campo **Agre. Lib**. com o conteúdo **NORT** em todos os clientes desta região.

Assim, em Geração do Documento de Saída, o Sistema pode gerar ordenadamente os pedidos por região ou somente da região informada (neste exemplo **NORT).**

|  |
| --- |
| Help_button***Importante:***  O parâmetro **[MV\_AGREG](https://tdn.totvs.com/pages/viewpage.action?pageId=312163752)**indica qual informação deve ser considerada para que os pedidos sejam ordenados. Seu conteúdo padrão é o próprio campo **Agre. Lib,** porém pode ser indicada uma fórmula em sintaxe AdvPl ou um execblock. Se necessário, é possível personalizar a forma de ordenação de pedidos por meio de ponto de entrada. |
