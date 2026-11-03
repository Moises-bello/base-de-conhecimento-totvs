---
article_id: 7008345717527
category: FATURAMENTO - PORTAIS (Cliente, Vendedor)
content_hash: 6a93f5e34e24fc605836789813ec7fcc8bc52658c7de29310d7e51c46331b83d
fetched_at: '2026-06-28T22:38:23.911506+00:00'
product: protheus
section_id: 1500001539321
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Configuração do Appserver
  para utilização TOTVS Gestão de Vendas (PGV)
type: support-article
updated_at: '2024-06-07T20:36:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7008345717527-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Configura%C3%A7%C3%A3o-do-Appserver-para-utiliza%C3%A7%C3%A3o-TOTVS-Gest%C3%A3o-de-Vendas-PGV
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15286101810839) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como realizar a configuração do Appserver para utilização do TOTVS Gestão de Vendas?   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - a partir da release 12.1.33;

**Solução**

Quer um passo a passo, com vídeos, sobre a implementação dessa funcionalidade? [Acesse: Implementação Portal Gestão de Vendas](https://tdn.totvs.com/x/Etk1LQ)

O Portal Gestão de Vendas efetua comunicação com o servidor Protheus através de requisições HTTP. Para que essa comunicação ocorra será necessário efetuar algumas configurações no servidor APPServer.

**Requisitos Mínimos;**

**Chave de Segurança - Importante**

Para o correto funcionamento das APIs do Portão Gestão de Vendas, é de extrema importância que a chave **SECURITY** do APPSERVER esteja **habilitada**.

**Chave PrepareIn**

Caso a chave **PrepareIn** esteja apontando para empresas específicas, na funcionalidade de Troca de Filial, os usuários terão acesso apenas às empresas informadas nesta chave. Caso não seja necessário este tipo de restrição, mantê-la como "**All**".

**Seleção Dbaccess**

Na chave **DATABASE** caso esteja diferente de "MSSQL" realize o ajuste na sua seleção do Dbaccess.

[**DBAccess**]  
DATABASE=MSSQL

**Appserver deve possuir um IP "REST" publico.**

**Exemplo da Configuração do APPSERVER.INI**

**Chave MultiProtocolPort tem que estar configurada igual 1;**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7007621763223)**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7007664765463)**

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7007739390871)**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12291159298967)

**![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7007819034007)**

**![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7007820528023)**

**![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7007822412183)**

**![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7007921937431)**

**Observação:**

Nas chaves com a informação **"ENVIRONMENT"** alterar para o nome do seu Ambiente;

Nas chaves com a informação **"localhost"** alterar para o  IP do servidor;

Na chave **"SECURITY"** tem que estar com o conteúdo igual **1**;

Na chave **"PrepareIn"** tem que estar preenchido com **"ALL"** ou **"Grupo/Empresa e Filial"** Exemplo **"01,010101"**

A chave **"Stateless"** é utilizada para **habilitar** o consumo de **licença por demanda,** é uma solução no Protheus para permitir o serviço REST consumir licenças **somente** quando uma API está em execução, ao invés de manter **permanente** o consumo de uma licença para cada Working Thread em funcionamento no REST.

* **Stateless=1:** Utilizada para habilitar o consumo de licença por demanda na secção da URI de REST caso possua **somente uma chave URI**.
* **Stateless=0 ou sem a chave:** O consumo de licença no inicio da thread será mantido, como a configuração é por URI, é possível ter **URI's diferentes** em uma mesma porta, cada uma trabalhando com um modelo de licenciamento.

**Observação:** A configuração do REST tem que seguir as TAGS do Exemplo, somente criando um REST básico não valida o acesso ao Portal Gestão de Vendas.

**Saiba Mais:**

**[Configurações REST](https://tdn.totvs.com/pages/viewpage.action?pageId=185747842)**

**[REST com ERP Microsiga Protheus](https://tdn.totvs.com/display/framework/02.+REST+com+ERP+Microsiga+Protheus)**

**[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - TOTVS Gestão de Vendas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415437052823)**

**[TOTVS Gestão de Vendas: Guia de Referência](https://tdn.totvs.com/pages/releaseview.action?pageId=579468339#PortalGest%C3%A3odeVendas:GuiadeRefer%C3%AAncia-RELACIONADOS)**

**[Perguntas mais frequentes do Portal Gestão de Vendas](https://tdn.totvs.com/pages/releaseview.action?pageId=649301318)**

**[Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - PGV - Error [SQL Server]Incorrect syntax near '|'](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14339501555351-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-PGV-Error-SQL-Server-Incorrect-syntax-near-)**
