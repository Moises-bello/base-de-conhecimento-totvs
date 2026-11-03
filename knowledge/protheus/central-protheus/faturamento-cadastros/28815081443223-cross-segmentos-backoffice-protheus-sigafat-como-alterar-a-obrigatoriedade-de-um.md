---
article_id: 28815081443223
category: Faturamento - Cadastros
content_hash: 3c9ac72f25cb97a88c490edd3d634d45033efae0b2ad46fd1ccad2206b7a7aba
fetched_at: '2026-06-28T22:38:36.744503+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - BackOffice Protheus - SIGAFAT - Como alterar a obrigatoriedade
  de um campo no Cadastro de Clientes (CRMA980)
type: support-article
updated_at: '2024-12-27T19:11:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28815081443223-Cross-Segmentos-BackOffice-Protheus-SIGAFAT-Como-alterar-a-obrigatoriedade-de-um-campo-no-Cadastro-de-Clientes-CRMA980
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28815090079255) Tempo aproximado para leitura: **00:02:00** **min** **Dúvida**Como alterar a obrigatoriedade de um campo no Cadastro de Clientes (CRMA980)?  
  
**Ambiente**Cross Segmentos - BackOffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

É possível alterar a obrigatoriedade de um campo dentro do Cadastro de Clientes (**CRMA980**) através do **SIGACFG** (Configurador).

*Exemplo:*

* No **SIGACFG**, acesse a tabela de Clientes (**SA1)**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28815081424151)

* Selecione a opção **Campos**, clique no campo desejado e em **Editar**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28815090089367)

* Selecione a aba **Uso**, marque/desmarque a opção **Obrigat. Usuário**e clique em **Salvar:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28815090090775)

* Clique em Salvar a alteração no disquete para **Atualizar base de dados.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/28815090091415)**

**Observação**

Para evitar inconsistências, o Configurador possui uma **trava** que **impede alterações** no uso de alguns campos. Essa configuração é essencial para garantir o correto funcionamento do sistema e a consistência dos dados:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28815090092055)

**Saiba mais:**

[Pasta Uso (CFGX034 - SIGACFG)](https://tdn.totvs.com/pages/releaseview.action?pageId=312157843)

[Cadastro de Clientes (MATA030/CRMA980)](https://tdn.totvs.com/pages/releaseview.action?pageId=789989987)
