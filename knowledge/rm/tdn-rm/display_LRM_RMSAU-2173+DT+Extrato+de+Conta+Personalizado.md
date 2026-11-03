---
content_hash: 252d1ba7f1b75e9675993994b8143e1e714f8c908a3c21b266c25fa0a09de9d6
fetched_at: '2026-06-29T00:08:49.411370+00:00'
page_id: '330828681'
product: rm
source: tdn-rm
title: RMSAU-2173 DT Extrato de Conta Personalizado
type: documentation
url: https://tdn.totvs.com/display/LRM/RMSAU-2173+DT+Extrato+de+Conta+Personalizado
version: 5
---

# EXTRATO DE CONTA PERSONALIZADO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Elaboração de Contas | PSAFT001 | |
| **Cadastros Iniciais:** | Condições contratuais |
| **Tickets relacionados** | 1999224 |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | RMSAU-2173 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER® e ORACLE® |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Permitir criar relatórios no RM Reports para o Extrato da conta e Conta Médica para que seja customizada para cada convênio. O mesmo deve ser parametrizado nas Condições Contratuais.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):

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

1. Acesse o menu Cadastros / Faturamento / Condições Contratuais
2. Selecione a aba Parâmetros 2, grupo "Na Impressão da Conta". Marque que utiliza o tipo de relatório RM Reports. Uma vez selecionado, os dois relatórios Conta Médica e Extrato deverão estar no tipo escolhido
3. Pesquise o relatório desejado para cada opção
4. Acesse a Elaboração de Contas, selecione uma conta do convênio parametrizado e clique no botão Extrato de Débitos  
     
     
     
     
     
     
     
   **Observações:**  
   Para este chamado foi desenvolvido um relatório específico para o convênio SAMEDH, onde existem particularidades que devem ser verificadas para a utilizado do relatório "**ECH - Extrato de Conta\_SAMEDH.TotvsReport**"  
   No arquivo acima, existem dois relatórios que devem ser importados pela ferramenta do TOTVS Reports.   
   Após a importação, é necessário abrir o relatório "**ECH - Extrato Conta Hospitalar**", acessar a banda "**RodapédoDetalhe6**" e informar o relatório "**ECH.01 Consumo de materiais/medicamentos por paciente**". Salve as alterações do relatório .  
     
     
     
   Para utilizar o código de agrupamento de MATMED no relatório, informar o código nas Condições Contratuais, página "**Eletrônico III - TISS**"
