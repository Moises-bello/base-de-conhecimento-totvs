---
content_hash: ce1e08cf36f92bab54708c954526db935a930281094ce7ca2bd4bba368e1685a
fetched_at: '2026-06-29T00:08:28.933619+00:00'
page_id: '271869601'
product: rm
source: tdn-rm
title: DT Controle de Acesso para Utilitário de Atualização de Valores
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271869601
version: 115
---

# Controle de Acesso para Utilitário de Atualização de Valores (Delphi e .NET)

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Atualização de Valores (RM Saude.exe e RM.exe) |  |  | | --- | | **Rotinas envolvidas** | | Segurança / Perfis (RM Saude.exe e RM.exe) | | Parâmetros Gerais, parâmetro Utiliza Controle de Acesso em Atualização de Valores | |
| **Parâmetro(s):** | Utiliza Controle de Acesso em Atualização de Valores |
| **Tickets relacionados** | #406534 |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | SAUHRM02-743 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER® e Oracle® |
| **Tabelas Utilizadas:** | SZPARAM |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Implementado controle de acesso para definir quais perfis de usuários podem utilizar o utilitário de **Atualização de Valores**. A segurança será aplicada somente após ativação de parâmetro nos **Parâmetros Gerais** do sistema.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):

   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.16 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.16.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:

   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).

   2. Faça o login, com seu E-mail e Senha.

   3. Na barra de menu superior, clique em DOWNLOAD.

   4. No boxe Central de Downloads aplique os filtros:

   a. Linha: RM

   b. Versão: RM 12.1.16

   c. Tipo: Patch

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.

**Importante**: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. O controle de segurança somente será aplicado às rotinas somente se o parâmetro em **Opções / Parâmetros / Parâmetros Gerais**, aba **Geral**, campo **Utiliza Controle de Acesso em Atualização de Valores** for marcado:.

## Procedimento para Utilização

1. Pela nova MDI (RM.exe) acesse **Serviços Globais / Segurança*.***
2. Selecione um perfil e a aba **Acesso a Menus** para configurar o acesso deste perfil para a rotina de **Atualização de valores**.
3. Após configurar as permissões de acesso do perfil do usuário, acesse **Gestão Hospitalar / Utilitários / Atualização de Valores**.
4. Verifique que as opções que **não** foram dadas permissões estarão desabilitadas ao exibir a tela. 

   Observação

   Materiais e Medicamentos ficará habilitado se ao menos uma das opções (Atualizar valores de MAT/MED ou Atualizar Códigos de MAT/MED) estiver selecionada.
5. Informe todos os dados necessários para executar a rotina.
6. Por **RMSaude.exe** acesse **Cadastros / Segurança / Perfis*.***
7. Selecione um perfil e selecione a aba **Acesso a Menus** para configurar o acesso deste perfil para a rotina de **Atualização de valores**.
8. Acesse **Utilitários / Utilitários do RM Saúde / Atualização de Valores*.***
9. Verifique que as opções que **não** foram dadas permissões estarão desabilitadas ao exibir a tela. 

   Observação

   Materiais e Medicamentos ficará habilitado se ao menos uma das opções (Atualizar valores de MAT/MED ou Atualizar Códigos de MAT/MED) estiver selecionada.
10. Informe todos os dados necessários para executar a rotina.

divs
