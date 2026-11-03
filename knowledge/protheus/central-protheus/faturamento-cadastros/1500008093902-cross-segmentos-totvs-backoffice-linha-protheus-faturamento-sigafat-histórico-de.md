---
article_id: 1500008093902
category: Faturamento - Cadastros
content_hash: f1a42a5a5ebed20ae248eda064909b291a278c39179df4b03b7401ea53d8cf07
fetched_at: '2026-06-28T22:38:35.502363+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT)
  - Histórico de alterações do Cadastro de Clientes
type: support-article
updated_at: '2024-09-26T18:08:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008093902-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Hist%C3%B3rico-de-altera%C3%A7%C3%B5es-do-Cadastro-de-Clientes
---

**Dúvida**Como gerar um log de alterações do Cadastro de Clientes   
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

Basta configurar o Parâmetro **MV\_HISTTAB:**Habilita (T) ou desabilita (F) histórico das alterações do cadastro de clientes/fornecedores.

Caso não existir o parâmetro, é possível cria-lo conforme a imagem de exemplo abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500011755742)

O sistema vai gravar registros na tabela **AIF (histórico de Alterações Cliente e Fornecedor)** informando o código do cliente, campo, data e hora.  
A tabela **AIF** é de uso interno, sendo somente possível de visualizar via banco de dados, não existindo uma rotina específica para visualização do histórico.
