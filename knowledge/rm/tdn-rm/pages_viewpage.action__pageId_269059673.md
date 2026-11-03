---
content_hash: ea5e29e2b88cfb5f5f4e2222de9a30187c006c2e2c5ac897060b2d4a852370cf
fetched_at: '2026-06-29T00:08:21.563323+00:00'
page_id: '269059673'
product: rm
source: tdn-rm
title: DT_Reclassificação_da_Senha_de_Atendimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269059673
version: 111
---

# Reclassificação da senha de atendimento

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Registros de Atendimento | | Registro de Triagem | | Painel de Classificação de Risco | |
| **Requisito (ISSUE):** | SAUHRM02-72 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER® e Oracle® |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Implementadas opções no menu suspenso da tela de listagens de Registros de Atendimentos e Registro de triagem no Painel de Classificação de Risco, que permitem marcar ou desmarcar a senha como prioritária.

## Procedimento para Implantação

1. Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):

      Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

      O Patch 12.1.14 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.14.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

      Para acesso siga as instruções abaixo:

      1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).

      2. Faça o login, com seu E-mail e Senha.

      3. Na barra de menu superior, clique em DOWNLOAD.

      4. No boxe Central de Downloads aplique os filtros:

      a. Linha: RM

      b. Versão: RM 12.1.14

      c. Tipo: Patch

      Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

      Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.

   **Importante**: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

      Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Utilização

1. No Painel de Classificação de Risco, clique com o botão direito do mouse sobre o registro que deseja alterar a prioridade.
2. Selecione a opção de adicionar ou remover o paciente na fila de prioritários, conforme imagens abaixo:

**Adicionar à fila de Prioritários**

* Verifique que o checkbox **Prioritário** foi marcado.

**Remover da fila de Prioritários**

* Verifique que o checkbox **Prioritário** foi desmarcado.

divs
