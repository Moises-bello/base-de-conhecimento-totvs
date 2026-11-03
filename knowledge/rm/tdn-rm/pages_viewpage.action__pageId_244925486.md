---
content_hash: 59f4107665328f317f58ce764bfd33bd0bd5e3af7ade38b1727cac6d50982663
fetched_at: '2026-06-29T00:08:15.836790+00:00'
page_id: '244925486'
product: rm
source: tdn-rm
title: DT_Ajustes_na_Divisão_de_Cobranças
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244925486
version: 113
---

# Ajustes na divisão de Cobranças

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Faturamento |  |  | | --- | | **Rotina(s) envolvida(s)** | | Faturamento para Convênios | |
| **Requisito (ISSUE):** | SAUHRM01-401 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | MSSQL®, Oracle® |
| **Tabelas Utilizadas:** | SZESTOQUEPACIENTE |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Esta implementação tem como objetivo disponibilizar a funcionalidade de geração de XML específico, com cobranças divididas, para o padrão Doctor Clin de faturamento.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):

   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.13 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.12.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:

   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).

   2. Faça o login, com seu E-mail e Senha.

   3. Na barra de menu superior, clique em DOWNLOAD.

   4. No boxe Central de Downloads aplique os filtros:

   a. Linha: RM

   b. Versão: RM 12.1.13

   c. Tipo: Patch

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.

**Importante**: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Utilização

1. Acesse o menu **Cadastros / Faturamento / Condições Contratuais com Convênios**.
2. Selecione a Condição Contratual desejada e abra para edição.
3. Acesse o menu **Anexos / Divisão de Cobranças**.
4. Inclua as regras de divisão desejadas para o profissional que será utilizado.
5. Na aba **Eletrônico - TISS III**, selecione o padrão específico “**Dr. Clin**”.
6. Acesse a **Elaboração de Contas** de algum paciente internado para o convênio e unidade de faturamento configuradas.
7. Inclua o Honorário (Ou SADT), que foi configurado, colocando como médico responsável o mesmo médico configurado.
8. O item lançado deverá ser incluído com o valor dividido, sendo que o percentual configurado ficará com o profissional executante e o restante do valor com o prestador principal da unidade de faturamento.
9. Encerre a conta.
10. Acesse a nova MDI, menu **Faturamento / Faturamento Para Convênios**.
11. Inclua uma nova remessa para o convênio e unidade de faturamento configurados e inclua a conta nesta remessa.
12. Execute o processo de faturamento da remessa.
13. Verifique o XML gerado. O XML deverá conter apenas a parte da divisão que é correspondente ao profissional principal da unidade de faturamento, porém o nome do profissional que deverá constar no XML será o do profissional responsável.

divs
