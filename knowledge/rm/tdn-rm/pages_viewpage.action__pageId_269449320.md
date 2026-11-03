---
content_hash: dff0bcde49fbfbb6472ff4c005ec357ce026dc9cf69c9e8f1c3d4e70c4e4aa63
fetched_at: '2026-06-29T00:08:23.134505+00:00'
page_id: '269449320'
product: rm
source: tdn-rm
title: DT Avaliações Complementares Prontuário com Kit de Lançamentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269449320
version: 116
---

# Avaliações Complementares Prontuário com kit de lançamentos

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Classificação de Exames | | Avaliações Complementares - Solicitação de Exames | |
| **Parâmetro(s):** | Utiliza Classificação de Exames no PEP |
| **Requisito (ISSUE):** | SAUHRM02-331 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER® e Oracle® |
| **Tabelas Utilizadas:** | SZCLASSEEXAME - Classificação de Exames  SZGRUPOEXAMES – Exames pertencentes à Classificação de exames  SZKITLANC – Kit de lançamentos  SZKITLANCITEM – Itens do kit |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Implementada a rotina  de utilização de grupos de exames nas solicitações pelo Prontuário do Paciente. O sistema utilizava os itens de débito para cadastrar os exames que pertencem a um grupo (Kits de lançamento com o parâmetro Utilizado no PEP marcado). Como alguns itens de débito podem pertencer a mais de um exame, na rotina dentro do Prontuário Eletrônico do Paciente, são exibidos exames que não pertencem ao kit selecionado. O objetivo desta implementação é utilizar o cadastro de Classificação de exames para montar o kit de exames sem a repetição ou o surgimento de exames não desejados.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):

   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.15 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.15.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:

   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).

   2. Faça o login, com seu E-mail e Senha.

   3. Na barra de menu superior, clique em DOWNLOAD.

   4. No boxe Central de Downloads aplique os filtros:

   a. Linha: RM

   b. Versão: RM 12.1.15

   c. Tipo: Patch

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.

**Importante**: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. Acesse**Opções/Parâmetros/Parâmetros Gerais aba Unidade Diagnóstico**.
2. Marque o parâmetro **Utiliza Classificação de Exames no PEP**.

## Procedimento para Utilização

1. Acesse **Cadastros/ Unidade de Diagnóstico/ Classificação de Exames**.
2. Crie uma nova classificação de Exames.
3. Crie o grupo de exames.
4. Acesse o **Prontuário** aba **Avaliações Complementares / Solicitar Exame**.
5. A lista **Padrão Propedêutico** carregará os grupos criados na Classificação de Exames.
6. Selecione o ícone conforme imagem.
7. O sistema apresentará os exames do grupo selecionado.

divs
