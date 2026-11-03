---
content_hash: a155991a5a4dfa0a9c22818e6269b3ab84c8d5306bd8b2209dbbb2c14e9c39c5
fetched_at: '2026-06-29T00:11:10.184036+00:00'
page_id: '642386598'
product: rm
source: tdn-rm
title: Ajustar Permissões de Usuários (ExcluiAcessoUsuarios.exe)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=642386598
version: 16
---

## **Visão Geral**

Atualmente existem permissões provenientes do Delphi, permissões que deixaram de existir no sistema, onde não é possível removê-las de dentro da **MDI .Net**.

O aplicativo "Exclui Acesso Usuários" foi desenvolvido para **remover** estas permissões que não pertencem aos **menus** de cada módulo com base nos **menus** da **MDI .Net**.

Atenção

Pelo fato desta ferramenta remover permissões do sistema, **a responsabilidade pelo impacto nas permissões são exclusivamente do usuário que executar a aplicação,** pois não é possível reverter as alterações realizadas pelo sistema.  
Recomendamos que o aplicativo seja executado e validado em base de dados de **homologação** para posteriormente aplicar em produção. 

Permissões de perfis que são utilizados como **MultiPerfil** também serão excluídas, permanecendo somente as permissões do módulo original do perfil. **Voltando com o escopo do perfil somente para aquela aplicação.**

Permissões do **Delphi** que não foram migradas para a **MDI .Net** serão removidas.

Permissões que um dia foram dadas através do **Fluig Identity** que não pertencerem ao módulo original do perfil, serão excluídas.

Atenção

Apesar de existir a validação de base da versão **12.1.31** ou superior, somente a partir dos patches abaixo será possível executar a demanda, pois somente neles estarão presentes algumas rotinas desenvolvidas para executar a aplicação.

| Versão | Patch |
| --- | --- |
| 12.1.31 | 12.1.31.239 |
| 12.1.32 | 12.1.32.167 |
| 12.1.33 | 12.1.33.106 |

Atenção

Permissões que estão sendo excluídas no aplicativo porém existentes no menu da **MDI .NET**devem ser verificadas pela equipe do produto responsável pelo **menu/módulo**.

## **Validações**

A ferramenta possui validações para que somente em determinados cenários a mesma possa ser executada.

**Validação de Usuário Supervisor em Globais (CodSistema G)**: Somente usuários que possuírem a permissão de supervisor no sistema **G** **(Serviços Globais | Integração | Inteligência de Negócios)** poderão executar a funcionalidade. Basta ter acesso de supervisor no sistema **G** **(Serviços Globais | Integração | Inteligência de Negócios)** em **uma** **única****coligada** e a funcionalidade de executar o ajuste de permissões será liberada.

| Usuário Supervisor no sistema G | Usuário sem permissão de Supervisor no sistema G |
| --- | --- |

**Validação da Versão da base em que o sistema será utilizado**: Somente em versões de Banco de dados a partir da 12.1.31 será possível executar a ferramenta.

| Banco de dados em uma versão 12.1.31 ou superior | Banco de Dados em uma versão inferior a 12.1.31 |
| --- | --- |

**Validação da integração RM x Fluig Identity:** Somente será habilitada a funcionalidade se a base de dados não estiver configurada para utilizar a integração **Obrigatória** ou **Opcional** do RM com o Fluig Identity. Esta validação é realizada pois a integração permite que o usuário adicione permissões de qualquer módulo em um único perfil. Para mais informações acesse o TDN [Experiência 3 - Acesso Centralizado](https://tdn.totvs.com/x/VQhgDQ).

| Estas parametrizações podem ser encontradas em Parâmetros Globais | Integração SAML |
| --- |

| Sem utilizar a integração | Utilizando a integração Obrigatória ou Opcional |
| --- | --- |

## **Como Utilizar**

Atenção

Para utilizar a ferramenta é necessário solicitar os arquivos para o Suporte de Framework  e adicioná-los no ambiente RM e excluir o arquivo \_Broker.dat e reiniciar o serviço do RM.Host.

Execute o aplicativo e realize o login no alias desejado

|  |
| --- |

Após efetuar o login e passar pelas validações do Item 2 - Clique em Verificar permissões não contempladas pelo RM.Net

Caso exista algum perfil que possua permissão que não exista no menu do Módulo referente ao **código do sistema** do perfil, estas permissões serão listadas, conforme exemplo abaixo:

| No grid serão exibidas as informações do perfil que a permissão será removida.  **Na coluna relação são exibidas informações relevantes referente à tag de segurança que foi possível encontrá-la em outros módulos.**  **Exemplo:**    CODSISTEMA:G - DESCRIÇÃO:Perfis - Type: routine - Action: GlbPerfilAction ; CODSISTEMA:M - DESCRIÇÃO:Perfis - Type: routine - Action: GlbPerfilAction ;  Significa que a tag de segurança foi encontrada nos sistema G e M, onde o nome da mesma é Perfis e seu tipo é uma Rotina e a action que representa esta tag é a GlbPerfilAction. |
| --- |

Após carregar as informações basta clicar em - Excluir permissões não contempladas pelo RM.Net

| Será exibida uma solicitação de confirmação de exclusão das permissões: |
| --- |
| Ao clicar em Sim todas aquelas permissões exibidas no GRID serão excluídas e os perfis que são utilizados como **MultiPerfil** voltará a ter o **escopo de SinglePerfil. Voltando a ser somente do módulo original do perfil.**     Atenção Ao executar esta rotina, será enviada uma mensagem para o Snowden informando que a rotina de sanitização de permissões foi executada e qual usuário a executou. |

Atenção

É possível exportar as informações do grid para arquivo CSV, utilizando o menu **Exportar.**
