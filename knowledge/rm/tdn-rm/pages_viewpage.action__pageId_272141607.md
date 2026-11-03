---
content_hash: 75399bfc06126a2f7adf08176a6978590f34678c95e82c629ae6444772e312ed
fetched_at: '2026-06-29T00:08:29.029708+00:00'
page_id: '272141607'
product: rm
source: tdn-rm
title: DT Automatização da Profilaxia TVP
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=272141607
version: 114
---

# Sistema de Pontuação para Fatores de Risco e Profilaxia Default

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Prontuário Eletrônico |  |  | | --- | | **Rotina(s) envolvida(s)** | | Parâmetros Gerais | |
| **Parâmetro(s):** | Utiliza Sistema de Pontuação Fatores de Risco  Profilaxia Default |
| **Tickets relacionados** | 318043 |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | SAUHRM02-748 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server® e Oracle® |
| **Tabelas Utilizadas:** | SZPARAM e SZPROFTVP |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Implementado sistema de pontuação, ativado via parâmetro, para fatores de risco no TVP junto com a possibilidade de selecionar, via parametrização também, uma Profilaxia default para ele.

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

1. Acesse **Opções / Parâmetros / Parâmetros Gerais,** aba **Prontuário Eletrônico**, sub aba **Geral II**.
2. Marque o parâmetro **Utiliza Sistema de Pontuação Fatores de Risco** e selecione uma **Profilaxia default**.

## Procedimento para Utilização

1. Acesse o **Prontuário Eletrônico**.
2. Selecione um paciente.  
   * Se o paciente tem mais de 40 anos o Fator de Risco **Idade > 40 anos** será selecionado automaticamente.
   * Se o paciente tem mais de 60 anos o Fator de Risco **Idade > 60 anos**será selecionado automaticamente.
3. O sistema de pontuação incrementará **1 ponto** para cada fator de risco **exceto Idade > 60 anos** e **Trauma Grave** que contabilizarão **2 pontos**.
4. A pontuação para a Classificação de Risco funcionará da seguinte forma:  

   **SE pontuação < 2       = BAIXO**

   **SE pontuação** **≥** **2 e < 5 = MÉDIO**

   **SE pontuação** **≥** **5       = ALTO**
5. O parâmetro **Profilaxia Default** fará com que a profilaxia a ser utilizada no TVP venha selecionada por padrão.

divs
