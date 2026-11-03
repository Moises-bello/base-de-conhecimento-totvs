---
content_hash: 0d1cfbdc1476689a4fd60e182361fa2ee1b801ce2e90358c0e7785001673e907
fetched_at: '2026-06-29T00:08:07.855780+00:00'
page_id: '237393677'
product: rm
source: tdn-rm
title: TUWLNJ_DT_Visualizar_Todas_as_Evoluções
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=237393677
version: 119
---

# Visualizar Todas as Evoluções

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Prontuário Eletrônico | |
| **País(es):** | Brasil. |
| **Banco(s) de Dados:** | SQL Server®/Oracle® |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Implementada funcionalidade de impressão de todas as evoluções na aba Evolução, no Prontuário Eletrônico do TOTVS Gestão Hospitalar. Criado novo parâmetro, em Parâmetros Gerais (Aba Prontuário Eletrônico), que quando marcado altera o comportamento da visualização de todas as evoluções, fazendo com que, ao invés de perguntar ao paciente qual a data de início, o sistema imprima todas as evoluções que correspondam ao atendimento.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):

   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.11 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.11.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:

   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).

   2. Faça o login, com seu E-mail e Senha.

   3. Na barra de menu superior, clique em DOWNLOAD.

   4. No boxe Central de Downloads aplique os filtros:

   a. Linha: RM

   b. Versão: RM 12.1.11

   c. Tipo: Patch

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.

**Importante**: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. Acesse o menu **Opções/Parâmetros/Parâmetros Gerais**.
2. Marque o checkbox “**Ao clicar em "Visualiza Todas", na aba de Evolução, sistema imprime todas as evoluções, sem solicitar data de início**”, na aba **Prontuário Eletrônico**.

## Procedimento para Utilização

1. Acesse o **Prontuário Eletrônico** e selecione um paciente já internado e que possua algumas evoluções preenchidas no atendimento.
2. O sistema imprimirá todas as evoluções do atendimento, sem solicitar data ao usuário.
3. Acesse a aba **Evolução** e clique em **Visualizar** **Todas**.

divs
