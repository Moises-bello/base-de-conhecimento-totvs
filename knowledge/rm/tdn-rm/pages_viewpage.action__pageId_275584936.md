---
content_hash: a5ff6fabe182432c49b19d6fd9b41f0b82629333f4062b08d7dcbda8c8704dd4
fetched_at: '2026-06-29T00:08:35.325256+00:00'
page_id: '275584936'
product: rm
source: tdn-rm
title: DT Cópia de Valores de Porte CBHPM
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=275584936
version: 109
---

# Cópia de Valores de Porte CBHPM

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Condição Financeira com Convênio |  |  | | --- | | **Rotina(s) envolvida(s)** | | Valores de Porte CBHPM | |
| **Cadastros Iniciais:** | Condição Financeira com Convênio |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | SAUHRM02-964 Cópia de valores de porte CBHPM |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER® e Oracle® |
| **Tabelas Utilizadas:** | SZCONDFINPORTECBHPM |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Implementada rotina que efetua cópia de uma tabela de portes CBHPM, com origem na tabela padrão de portes CBHPM ou de outra condição contratual com Convênio.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):

   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.17 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.17.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:

   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).

   2. Faça o login, com seu E-mail e Senha.

   3. Na barra de menu superior, clique em DOWNLOAD.

   4. No boxe Central de Downloads aplique os filtros:

   a. Linha: RM

   b. Versão: RM 12.1.17

   c. Tipo: Patch

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.

**Importante**: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Utilização

1. No menu **Cadastros/Faturamento/Condição Financeira com Convênio,** acesse **Processos/Copia Valores de Porte CBHPM**.
2. A tela do processo contém a opção de cópia de valores de porte CBHPM existentes, da tabela geral de portes ou de outra condição contratual com convênio.
3. Para qualquer opção de origem de dado, o campo **% Acréscimo** altera o valor de todos os registros copiados, sendo o cálculo efetuado: valor final = valor de origem + (valor de origem \* acréscimo/100).
4. A opção **Manter valores de porte existentes**, ao ser marcada, caso no momento da cópia já exista um valor de porte salvo na tabela de destino, esse mesmo valor será mantido, ignorando o valor novo.
5. Ao selecionar o tipo de origem **Condição Financeira**, os campos da parte inferior da tela são liberados, habilitando a seleção de um convênio e unidade de faturamento para cópia de uma tabela de portes de outra condição contratual.
6. O campo **Data Vigência** é habilitado somente quando os campos **Convênio** e **Unidade de Faturamento** estiverem preenchidos.
7. Clique no botão **Executar** para efetuar a cópia da tabela com base nas informações escolhidas.

divs
