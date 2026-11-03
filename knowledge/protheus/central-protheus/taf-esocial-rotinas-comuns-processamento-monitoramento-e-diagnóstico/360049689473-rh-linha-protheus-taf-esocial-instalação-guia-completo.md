---
article_id: 360049689473
category: TAF - eSocial - Rotinas comuns (Processamento, Monitoramento e Diagnóstico)
content_hash: 7ccb257401e590a9cbf0da6949deff31d8ae5edc2d8abea94c92a2a94b6de139
fetched_at: '2026-06-28T22:45:21.165088+00:00'
product: protheus
section_id: 1500001536781
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - INSTALAÇÃO - Guia completo
type: support-article
updated_at: '2024-08-20T17:53:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049689473-RH-Linha-Protheus-TAF-eSocial-INSTALA%C3%87%C3%83O-Guia-completo
---

**Dúvida**

Como realizar a instalação completa do sistema TAF e TSS (Segregado)

**Ambiente**

TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - INSTALAÇÃO - Todas as versões

**Solução**

**PRÉ REQUISITOS DE INSTALAÇÃO:**

1 - Verifique os pré requisitos mínimos que o seu servidor precisa ter para instalar o TAF acessando o artigo abaixo:

[RH - Linha Protheus - TAF - eSocial - Instalação- INSTALADOR - Pré-requisitos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034038393)

**BANCO DE DADOS:**

2 - Verifique se seu banco de dados é homologado para o sistema TAF e TSS acessando o artigo abaixo:

<https://tdn.totvs.com/display/tec/DBAccess+-+Banco+de+dados>

***Obs.:*** *Verifique no site do suporte do seu banco de dados, as datas das atualizações (Upgrades). Podem existir versões que não serão compatíveis após o término do suporte do seu banco de dados, de acordo com o tempo de vida útil. Veja com seu DBA os upgrades necessários do seu banco de dados e procure manter compatível com as versões mais recentes.*

3 -Antes de qualquer processo da instalação do TAF e do TSS, devem ser criadas duas bases no banco de dados. Dêem preferência com o nome igual ao do sistema que estão instalando:

**Exemplo:**

Veja o exemplo abaixo no *SQL Server*:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23692634135959)

4 - Veja a *collation* padrões utilizados pelos bancos de dados homologados pela Totvs:

[Framework - Linha Protheus - Qual Collation utilizar na criação do Banco de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000513567-MP-FRAME-Qual-Collation-utilizar-na-cria%C3%A7%C3%A3o-do-Banco-de-Dados)

**SQL SERVER - Configurando conexão:**

5 - Para configurar as conexões ODBC para o sistema TAF e TSS para comunicação com o banco de dados SQL Server, verifique o artigo abaixo:

[RH - Linha Protheus - TAF - eSocial - Cofiguração - Como criar uma fonte de dados (ODBC 64 bits) para uso com Microsoft SQL Server](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034281974)

**ORACLE - Configuração conexão:**

6 - Para configurar as conexões para o sistema TAF e TSS para comunicação com o banco de dados Oracle, verifique o artigo abaixo:

[RH - Linha Protheus - TAF - eSocial - CONFIGURAÇÃO - Criando conexão com banco Oracle](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035186814)

**DOWNLOAD:**

7 - Segue documentação abaixo para realizar o download do TAF e TSS (Segregado):

[RH - Linha Protheus - TAF - eSocial - Como baixar o instalador do TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033541434)

**INSTALAÇÃO:**

8 - Segue documentação que orienta como realizar os procedimentos de instalação do TAF:

[TAF - INSTALADOR - Como instalar o TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034116973)
