---
article_id: 7707180320919
category: Gestão de Armazenagem (WMS)
content_hash: 8acd6189696fe2f0428780b365e3dbed6752d43755161c7b93b37c72e0d32b38
fetched_at: '2026-06-28T22:45:48.168986+00:00'
product: protheus
section_id: 206962247
source: central-protheus
title: Logística - Linha Protheus - WMS - Rotina WMSA335 Cadastro de Produtos x Componentes
type: support-article
updated_at: '2024-01-30T00:19:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7707180320919-Log%C3%ADstica-Linha-Protheus-WMS-Rotina-WMSA335-Cadastro-de-Produtos-x-Componentes
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023739612/time.png)***Tempo aproximado para leitura: **00:01:18 min****Dúvida**Funcionamento da rotina **WMSA335** - **Cadastro de Produtos x Componentes****Ambiente**TOTVS Logística - TOTVS WMS (Linha Protheus) - Gestão de Armazenagem (SIGAWMS) -  A partir da versão 12  
  
**Solução**Essa **rotina** tem o objetivo de criar a **tabela** **D11** **Produtos x Componentes**, está tabela armazenará as informações de filial, produto principal, componentes e quantidade múltipla do componente em relação a um produto principal  
  
Esta **tela** vai apresentar as informações dos **Produtos x Componentes** **(D11) e** tem as opção **Incluir**, **Alterar** e **Excluir** nas ações relacionadas.   
  
Quando a opção da ação relacionada no programa for **Incluir**:

* Trata-se da inclusão de um novo componente na estrutura, criando um novo registro nos **Produtos x Componentes (D11)**, validara se o componente ainda não possui cadastro como produto principal, havendo apresentara mensagem e não permitir a inclusão;
* Ao incluir os componentes ira validar se não está associando a outro produto principal, havendo  apresentara mensagem e não permitir a inclusão;
* Se o componente do produto principal não é produto principal o mesmo, apresentara mensagem e não permitir a inclusão.

Quando a opção da ação relacionada no programa for **Alterar**:

* Trata-se de alteração da quantidade múltipla.

Quando a opção da ação relacionada no programa for **Excluir**:

* Trata-se da exclusão do componente na estrutura, se houverem componentes do componente deveram ser excluídos também.

**Importante**Qualquer ação deverá validar se não há **saldo de** **estoque por endereço WMS (D12)**, caso haja saldo não deverá permitir a ação.
