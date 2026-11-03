---
content_hash: d3fc204a47b4a47797db7acedcc1b17ae6f49b24ab3687f9e46b17ebb2f771e3
fetched_at: '2026-06-29T00:08:09.422184+00:00'
page_id: '239036785'
product: rm
source: tdn-rm
title: DT_Inativar_Cadastro_Procedimentos_Cirúrgicos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=239036785
version: 115
---

# Inativar Cadastro Procedimentos Cirúrgicos

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Procedimentos para Agenda de Cirurgia | | Agenda de Cirurgias | |
| **Requisito (ISSUE):** | RHRM01-49 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | Oracle®/ SQL Server® |
| **Tabelas Utilizadas:** | SZPROCCIRURGICO |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Implementada a inativação do Cadastro de Procedimentos para Agenda de Cirurgias.

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

       1.    Acesse o menu**Cadastros / Cuidado com o Paciente / Cirurgias / Procedimentos para Agenda de Cirurgia** e ative o procedimento.

             2. Acesse**Atendimento / Agendamento / Agenda de Cirurgias**. O sistema verificará se o procedimento esta ativo para novos agendamentos.

divs
