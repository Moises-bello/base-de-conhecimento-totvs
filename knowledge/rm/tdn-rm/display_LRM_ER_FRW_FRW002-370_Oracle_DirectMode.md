---
content_hash: b9acba7034a150f3443c14a3c51a88efbe0efa3f522a6dfc75a918189ef7be3b
fetched_at: '2026-06-29T00:08:35.353875+00:00'
page_id: '279179695'
product: rm
source: tdn-rm
title: ER_FRW_FRW002-370_Oracle_DirectMode
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_FRW_FRW002-370_Oracle_DirectMode
version: 106
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### (Obrigatório)

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | Lib Data |
| **Segmento Executor** | Framework | | |
| **Projeto1** | Framework BH - 004 | **IRM/EPIC1** |  |
| **Requisito/Story/Issue1** | FRW\_FRW002\_370 | **Subtarefa1** | FRW\_FRW002\_372 |
| **Chamado/Ticket2** |  | | |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### (Obrigatório)

## Objetivo

Permitir que o RM se conecte à bases de dados Oracle através da propriedade Direct disponível pelo provedor (Devart) do componente utilizado. A opção ODM (Oracle Direct Mode) dispensa a necessidade de instalação do Oracle Client em um computador que precisa rodar o RM.exe.

Com o ODM habilitado, o idioma assumido por toda sessão de conexão do RM com uma base Oracle será se torna por padrão en-US. Para não perder a compatibilidade com os clientes, esta definição de idioma é alterada para pt-BR e poderá ser alterada conforme especificação abaixo.

### (Obrigatório)

## Definição da Regra de Negócio

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Configuração para ativar o ODM (Oracle Direct Mode) | [Criação] |  | Para se trabalhar com o RM dispensando a necessidade de instalação do Oracle Client em um computador com RM.exe, é necessário ativar a chave do ODM através da tag de configuração chamara **UseDevartDirect** no arquivo RM.exe.config:  <add key="UseDevartDirect" value="True" />  O valor padrão desta chave é **False**. |
| Configuração para alterar o idioma da sessão de conexão com o Oracle | [Criação] |  | O idioma da sessão de conexão do RM com uma base Oracle pode ser alterar através da tag de configuração chamara **OracleLanguage** no arquivo RM.exe.config:  <add key="OracleLanguage" value="en-US" />  O valor padrão desta chave é **pt-BR**. |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
