---
content_hash: cdef296148d5c84e29bbca8fb224ad1cf6c298ccf78d1aa843059b909b6bf502
fetched_at: '2026-06-29T00:08:31.991742+00:00'
page_id: '273979784'
product: rm
source: tdn-rm
title: DT Melhorias no Kit Pré-Montado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=273979784
version: 117
---

# Melhorias no Kit Pré-Montado

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Monta / Desfaz Kits de MAT/MED | | Kit Pré-Montado de MAT/MED | |
| **Cadastros Iniciais:** | Produtos / Produtos Compostos |
| **Parâmetro(s):** | Código de barras - Habilitar a utilização na estação de trabalho |
| **Requisito/S****tory/Issue :** | SAUHRM02-1026 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER® |
| **Tabelas Utilizadas:** | SZKITSMONTADO |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Implementada janela de pesquisa de itens na tela **Monta/Desfaz Kit de MAT/MED**, que possibilita a inserção de itens sem código de barras no kit pré-montado.

Também foi desenvolvida a tela **Kit Pré-montado de MATMED** para visualização de todos os kits pré-montados que foram cadastrados no sistema, e uma tela anexa listando todos os itens que fazem parte do kit.

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

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. Acesse **Opções/Parâmetros/Parâmetros por Estação de Trabalho**.
2. Marque o parâmetro **Código de barras - Habilitar a utilização na estação de trabalho**.

## Procedimento para Utilização

**Exemplo:**

  1.  Após habilitar o parâmetro **Código de barras - Habilitar a utilização na estação de trabalho**, acesse o menu **Estoques / Monta/Desfaz Kit de Mat/Med.**

  2. Clique no botão **Incluir**, é apresentada a tela para utilização do código de barras. Caso seja pressione a tecla **Enter**, com o campo do código de barras vazio, abre-se a tela de pesquisa de itens do estoque, para inclusão manual do item.

**Nova tela de Kit Pré-montado de MATMED**

1. Acesse o menu **Estoques / Kit Pré-montado de MATMED**.
2. Verifique que nesta tela, também foi criada uma tela anexa, com os itens que compõem o kit.

divs
