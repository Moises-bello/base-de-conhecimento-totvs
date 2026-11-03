---
content_hash: 35dc1ec80c598650804e5233cb0311beca3242a4b6963cf08398bd7f2186ca96
fetched_at: '2026-06-29T00:08:18.874474+00:00'
page_id: '266972608'
product: rm
source: tdn-rm
title: TOTVS Console - Authorization Server - Persistência Identity Server 4
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=266972608
version: 119
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | FRAMEWORK | **Módulo** |  |
| **Segmento Executor** |  | | |
| **Projeto1** | [TOTVS Console - Fase 1](http://jiraproducao.totvs.com.br/secure/RapidBoard.jspa?rapidView=359&projectKey=FRW_FRW003&view=planning&selectedIssue=FRW_FRW003-2) | **IRM1** | [FRW\_FRW003-1](http://jiraproducao.totvs.com.br/browse/FRW_FRW003-1) |
| **Requisito1** | [FRW\_FRW003-3](http://jiraproducao.totvs.com.br/browse/FRW_FRW003-3) | **Subtarefa1** | [FRW\_FRW003-21](http://jiraproducao.totvs.com.br/browse/FRW_FRW003-21) |
| **Chamado2** |  | | |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *[Documentação do Identity Server 4](https://identityserver4.readthedocs.io/en/dev/index.html)*  *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

 Criar camada de persistência para os dados de Configuração e dados Operacionais do servidor de autorização do TOTVSConsole (Identity Server 4) utilizando o banco MongoDB.

## Definição da Regra de Negócio

Conforme, determinado na especificação OAuth 2.0, um STS necessita de alguns dados de Configuração (Clients e Scopes) e gera dados operacionais (Tokens de Referência, Consentimentos de Autorização).

Para fins de desenvolvimento e testes, o Identity Server 4, fornece mecanismos de armazenamentos dessas informações em memória. Em um ambiente de produção, necessitamos criar mecanismos para armazenamento físico destas informações.

A comunidade open source já fornece uma [camada de persistência baseada no Entity Framework Core](https://github.com/IdentityServer/IdentityServer4.EntityFramework) para armazenamento destas informações em bancos de dados SQL Server. Entretanto, como estratégia para disponibilização do TOTVS Console em ambientes multiplataforma, será criada uma camada de pesistência utilizando MongoDB.

O Identity Server 4 disponibiliza contratos para as suas camadas de persistência, assim, as implementações padrões (em memória) podem ser substituídas por implementações específicas através de injeção de dependência.

Esses contratos são:

c#Confluence1IClientStoretrue
/// Retrieval of client configuration
///
public interface IClientStore
{
/// 
/// Finds a client by id
/// 
/// The client id
/// The client
Task FindClientByIdAsync(string clientId);
}
}]]>c#Confluence1IScopeStoretrue
/// Scope retrieval
///
public interface IScopeStore
{
/// 
/// Gets all scopes.
/// 
/// List of scopes
Task> FindScopesAsync(IEnumerable scopeNames);
/// 
/// Gets all defined scopes.
/// 
/// if set to true only public scopes are returned.
/// 
Task> GetScopesAsync(bool publicOnly = true);
}
}]]>c#Confluence1IPersistedGrantStoretrue
/// Store interface for persisting grants.
///
public interface IPersistedGrantStore
{
Task StoreAsync(PersistedGrant grant);
Task GetAsync(string key);
Task> GetAllAsync(string subjectId);
Task RemoveAsync(string key);
Task RemoveAllAsync(string subjectId, string clientId);
Task RemoveAllAsync(string subjectId, string clientId, string type);
}
}]]>

Para que também contribuamos com a evolução deste framework e também fácil reutilização, esta biblioteca será disponibilidada como um projeto open source no GitHub e distribuída via Nuget (Gerenciador de Pacotes .NET).

Projeto no GitHub: <https://github.com/diogodamiani/IdentityServer4.MongoDB>

Pacote Nuget: <https://www.nuget.org/packages/IdentityServer4.MongoDB>

### Opcional

## Fluxo do Processo

*<Nesta etapa incluir representações gráficas que descrevam o problema a ser resolvido e o sistema a ser desenvolvido. Exemplo: Diagrama - Caso de Uso, Diagrama de Atividades, Diagrama de Classes, Diagrama de Entidade e Relacionamento e Diagrama de Sequência>.*

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
