---
article_id: 7009044495895
category: FATURAMENTO - PORTAIS (Cliente, Vendedor)
content_hash: 634018a23ecd213b5a854640463b903878c1dedff951e3006aeddc2fecf67567
fetched_at: '2026-06-28T22:38:23.829153+00:00'
product: protheus
section_id: 1500001539321
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Configuração
  TOTVS MINGLE para solicitação do ALIAS para acesso ao Portal Gestão de Vendas (PGV)
type: support-article
updated_at: '2025-04-28T20:19:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7009044495895-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Configura%C3%A7%C3%A3o-TOTVS-MINGLE-para-solicita%C3%A7%C3%A3o-do-ALIAS-para-acesso-ao-Portal-Gest%C3%A3o-de-Vendas-PGV
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30362959687831) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como realizar a configuração do **TOTVS Mingle;**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.1.33;  
  
**Solução**

**Alias TOTVS Mingle**

A plataforma Portal Gestão de Venda é armazenada em uma nuvem TOTVS. Para que a aplicação possa se comunicar com o servidor Protheus é necessário efetuar a configuração do TOTVS Mingle, que executa o papel de um gateway entre a aplicação é o servidor Protheus. Além disso, ao configurar o TOTVS Mingle, a aplicação passa a utilizar os dados de Autenticação padrão do Protheus.

Para configurar o TOTVS Mingle, o servidor Appserver deve possuir um IP publico.

O Administrador do sistema deve solicitar um Alias, através da pagina TOTVS MINGLE e informar o app Portal Gestão de Vendas.

**[Solicitação ALIAS Mingle](https://mingle.totvs.com.br/landpage/)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/31726376168599)**

Por Favor, criar para o REST o acesso ao grupo/empresa, para liberação do ALIAS;

**Exemplo:**

**REST:** localhost:8080/rest

**Grupo/Empresa:** 01

**Filial:** 0101

**Aplicativo:** TOTVS Gestão de Vendas

**Importante:** Na configuração do Appserver tem a chave **PrepareIn,** aconselhamos que a configuração esteja igual a "**PrepareIn=ALL**", ou com **"PrepareIn=01,0101"** passando a empresa e Filial, e esta mesma informação é necessária para a configuração do **Mingle** para o acesso **"Portal Gestão de Vendas"**.

Para visualizar o seu Grupo/Empresa e Filial, pode acessar o Protheus na tela de seleção do modulo ou com apoio do TI através do Select na tabela SYS\_COMPANY

Exemplo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30362990328599)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31726366746391)

**Importante: Caso tenha duvida sobre o MINGLE ou quais ALIAS disponíveis, entrar em contato com a equipe de Framework.**

Saiba Mais:

[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - TOTVS Gestão de Vendas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415437052823)

[TOTVS Gestão de Vendas: Guia de Referência](https://tdn.totvs.com/pages/releaseview.action?pageId=579468339#PortalGest%C3%A3odeVendas:GuiadeRefer%C3%AAncia-RELACIONADOS)

[Perguntas mais frequentes do Portal Gestão de Vendas](https://tdn.totvs.com/pages/releaseview.action?pageId=649301318)
