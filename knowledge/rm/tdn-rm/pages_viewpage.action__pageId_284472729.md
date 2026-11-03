---
content_hash: 43f6c45a9eebd9d465d119fd07774158f3d002763b9daa86e67658638e649675
fetched_at: '2026-06-29T00:08:36.280000+00:00'
page_id: '284472729'
product: rm
source: tdn-rm
title: DT Modificar Parâmetro Imprime Requisição Direto na Farmácia ao Concluir a
  Prescrição
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=284472729
version: 102
---

# Modificar o Parâmetro: Imprime requisição direto na farmácia ao concluir a prescrição, separadamente por unidade de atendimento

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Unidades de Atendimento  Parâmetros Gerais | |
| **Cadastros Iniciais:** | Unidade de Atendimento |
| **Parâmetro(s):** | Imprime requisição direto na farmácia ao concluir a prescrição |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | SAUHRM02-1098 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER®, ORACLE® |
| **Tabelas Utilizadas:** | SZPARAM, SZUNIDATEND |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Desabilitado o parâmetro geral "Imprime requisição direto na farmácia ao concluir a prescrição" e criado um novo parâmetro, com esta mesma descrição, vinculado a uma unidade de atendimento**.**

Na tela do Prontuário Eletrônico, quando o médico concluir uma prescrição, caso este parâmetro esteja marcado, a prescrição será impressa diretamente na farmácia.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema (executáveis, dlls e arquivos de configuração):

   Realize a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.18 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.18.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:

   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).

   2. Faça o login, com seu E-mail e Senha.

   3. Na barra de menu superior, clique em DOWNLOAD.

   4. No boxe Central de Downloads aplique os filtros:

   a. Linha: RM

   b. Versão: RM 12.1.18

   c. Tipo: Patch

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.

**Importante**: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Utilização

Menu Opções > Parâmetros > Parâmetros Gerais, aba Prontuário Eletrônico.

Excluído o parâmetro geral “Imprime requisição direto na farmácia ao concluir a prescrição”.

Menu Cadastros > Uso Geral > Unidades de Atendimento

Criado parâmetro "Imprime requisição Direto na Farmácia ao concluir a prescrição", para atender individualmente cada unidade.

Se o parâmetro estiver desmarcado o sistema não imprimirá a requisição direto na Farmácia para a Unidade em questão.

Na tela do Prontuário Eletrônico, aba Prescrição Médica, quando o médico concluir a prescrição, caso o parâmetro esteja marcado, a requisição será impressa na Farmácia.

A seguinte mensagem será apresentada

divs
