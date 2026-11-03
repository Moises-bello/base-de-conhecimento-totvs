---
content_hash: 1a4d7961740981228112a6bc4b38d12f74906d7a629d4d0acbfe130879159603
fetched_at: '2026-06-29T00:11:13.484799+00:00'
page_id: '66126311'
product: rm
source: tdn-rm
title: NFS-e - Parametrizar o sistema para emissão de NFS-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=66126311
version: 3
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | NFS-e                        **Versão:***a partir 11.40* |
| **Processo** | **:** | Parametrizar o sistema para emissão de NFS-e |
| **Subprocesso** | **:** | Parametrizar o sistema para emissão de NFS-e |
| **Data da publicação** | **:** | 09/07/2013 |

**Introdução:**

Este documento tem o objetivo de direcionar a implantação da NFS-e, porem é muito importante que este processo seja acompanhado por um **consultor Totvs** e um responsável de **TI** da empresa para evitar alguns problemas.

Importante: se algum dos passos não for executado com sucesso os passos seguintes apresentaram problemas até que a pendência seja resolvida.

**Passo 1: Instalar e configurar TopConnect**Siga os passos deste link para a correta instalação e configuração do TopConnect:

[NF-e - Configuração Top Connect MSSQL](http://tdn.totvs.com.br/pages/viewpage.action?pageId=65209013)

[NF-e - Configuração Top Connect ORACLE](http://tdn.totvs.com.br/pages/viewpage.action?pageId=65208632)

**Passo 2: Instalar e configurar o TSS**

Siga os passos deste link para a correta instalação e configuração do TSS:

[NF-e - Instalação e Configuração do TSS](http://tdn.totvs.com.br/pages/viewpage.action?pageId=64652506)

**Passo 3: Preparar o certificado**

Siga os passos deste link para a correta preparação do certificado digital:

[Certificado Digital - Preparar Certificado Digital para Emissão de NF-E](http://tdn.totvs.com.br/pages/viewpage.action?pageId=65208525)

**Passo 4: Parametrizar a Filial e os parâmetro da etapa integração | fiscal**

Siga os passos do link abaixo para a correta configuração da Filial.

**Passo 5: Configurar o servidor mashups para atualização de municípios homologados**

Siga os passos do link para configuração do município através do servidor mashups.

[NFS-e - Configuração do servidor mashups para homologação municípios](http://tdn.totvs.com.br/pages/viewpage.action?pageId=64651845)

**Passo 6: Revisar cadastros**

Siga os passos do link abaixo para conferir os cadastros necessários para a emissão de NFS-e.

**Passo 7: Parametrizar o movimento**

Siga os passos do link abaixo para a correta parametrização dos movimentos de emissão de NFS-e.

**Passo 8: Envio da NFS-e**

Após seguir todas as orientações anteriores acesse o seguinte menu: Utilitários SPED NFS-e (Municipal) Processos Enviar NFS-e.

Será apresentada uma tela para informar quais movimentos serão enviados, preencha conforme os dados parametrizados e clique em “Executar”.

Após executar o envio a nota ficará com o status pendente, conforme figura abaixo.

Basta aguardar alguns minutos e executar o processo “Consultar Autorização/Cancelamento” e NFS-e mudará de pendente para autorizada conforme figura abaixo:

Nesta visão ficaram todas as NFS-e que passaram pelo processo descrito acima “Enviar NFS-e” podendo assumir um dos seguintes STATUS:

**Pendente**

Sempre que o processo “Enviar NFS-e” for executado com sucesso a NFS-e ficará aguardando validação da Prefeitura ou seja Pendente.

**Inconsistente**

Sempre que ocorrer um erro no processo “Enviar NFS-e” a NFS-e assumirá este status e isto significa que nota (neste caso o movimento) precisa de algum “ajuste” para ser enviada com sucesso.

**Rejeitada**

Ao executar o Processo “Consultar Autorização/Cancelamento” se a Prefeitura não autorizar uma NFS-e ela assumirá este STATUS, deverá ser verificado a orientação da mensagem de erro para saber o que fazer.

**Autorizada**

Sempre que a Prefeitura autorizar uma NFS-e, ao executar o Processo “Consultar Autorização/Cancelamento” ela assumirá este STATUS e significa que a NFS-e já esta autorizada no site da Prefeitura.

**Cancelada**

Sempre que a Prefeitura autorizar o cancelamento de uma NFS-e, ao executar o Processo “Consultar Autorização/Cancelamento” ela assumirá este STATUS e significa que a nota já esta cancelada no site da Prefeitura.

**Cancelamento Pendente**

Sempre que for solicitado o cancelamento de uma NFS-e ela assumirá este status enquanto aguarda a resposta da Prefeitura.

**Para maiores informações:**

**[Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)**

**COMUNIDADE **R**[@](https://totvs.byyou.com/?space=rnfe)Nfe**

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções: 2 – (Software), 2 – (Suporte Técnico), 3 - (RM), 3 - (Fiscal), 3 - (Nota Fiscal Eletrônica)
