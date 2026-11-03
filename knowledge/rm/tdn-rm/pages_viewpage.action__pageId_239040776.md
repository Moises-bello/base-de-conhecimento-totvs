---
content_hash: 0a337c14e22c418f5cc8b3f6aba93ad9bf9f38d21ac6b7fef4a3f7d96307f1b4
fetched_at: '2026-06-29T00:08:09.750940+00:00'
page_id: '239040776'
product: rm
source: tdn-rm
title: DT_Integração_Responsável_X_Cadastro_de_Visitantes
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=239040776
version: 114
---

# Integração Responsável X Cadastro de Visitantes

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Registro de Internações | |
| **Cadastros Iniciais:** | Registro de internações, Responsável |
| **Parâmetro(s):** | psaIntegraRespVisitante |
| **Requisito (ISSUE):** | SAUHRM01-9 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | MSSQL® |
| **Tabelas Utilizadas:** | SZCADVISITANTE |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Implementada rotina que insere os dados do responsável informados no Registro de Internação diretamente no Cadastro de Visitantes. Foi realizada a criação do parâmetro " **Integrar responsável no cadastro de visitante**" que habilita este comportamento.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. Acesse o menu **Opções / Parâmetros / Parâmetros Gerais**, aba Registro e Controle II.
2. Marque o checkbox **Integrar responsável no cadastro de visitante**para que após o cadastro de um responsável, ele seja inserido no cadastro de visitantes.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):

   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.12 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.12.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:

   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).

   2. Faça o login, com seu E-mail e Senha.

   3. Na barra de menu superior, clique em DOWNLOAD.

   4. No boxe Central de Downloads aplique os filtros:

   a. Linha: RM

   b. Versão: RM 12.1.12

   c. Tipo: Patch

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.

**Importante**: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Utilização

       1. Acesse o menu **Atendimento /Internação/Registro de Internações**.

       2. Preencha as informações referentes ao registro de internação e clique na aba **Responsável**.

       3. Clique no ícone de **Incluir responsável**.

       4.Selecione um responsável e clique em **OK**, as informações do responsável serão inseridas no **Cadastro de Visitante**.

divs
