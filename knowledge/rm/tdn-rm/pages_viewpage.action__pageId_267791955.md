---
content_hash: 9e1914f18ff60f2ae7a3fd4f5d57c7da10af89c44270ad2152f55adedb8f3f0f
fetched_at: '2026-06-29T00:08:19.531033+00:00'
page_id: '267791955'
product: rm
source: tdn-rm
title: DT_Melhoria_Relatório_Pesquisa_Atendimentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=267791955
version: 117
---

# Melhoria no Relatório de Pesquisa de Atendimentos

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Pesquisa Clientes e Atendimentos | |
| **Requisito (ISSUE):** | SAUHRM02-70 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER® e Oracle® |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Melhoria no relatório de pesquisa de atendimentos (pacientes internados), na visualização da pesquisa dos pacientes. 

* Incluída uma listagem de campos para ordenação na tela de pesquisa dos dados do relatórios.
* Incluída informação de Leito no relatório.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):

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

1. Acesse  **Atendimento/ Internação/Registro de Internações**.
2. Pesquise os pacientes e configure o filtro para ordenação da visualização do relatório.

 

O relatório contém os dados:

* + Leito do paciente.
  + Nome do paciente.
  + Idade.
  + Código.
  + Data de Internação (Data Entrada).
  + Convênio.

divs
