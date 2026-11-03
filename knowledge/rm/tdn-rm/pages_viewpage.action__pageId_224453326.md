---
content_hash: ed5c3af2ae59a8ca052987b14c37c3bdcedc409b3e416845d37d19153aa21f1a
fetched_at: '2026-06-29T00:06:25.938563+00:00'
page_id: '224453326'
product: rm
source: tdn-rm
title: DT_Divisão_de_Honorários_na_Solicitação_de_Exames
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=224453326
version: 118
---

# Divisão de Honorários na Solicitação de Exames

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Solicitação de Exames. | |
| **Requisito (ISSUE):** | [PCREQ-9955](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-9955) |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | MSSQL, Oracle |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Esta implementação possibilita que a funcionalidade de Divisão de Cobranças, antes disponível apenas na Elaboração de Contas, seja também utilizada na tela de Solicitação de Exames.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):  
   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.10 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.10.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:

   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).

   2. Faça o login, com seu E-mail e Senha.

   3. Na barra de menu superior, clique em DOWNLOAD.

   4. No boxe Central de Downloads aplique os filtros:

   a. Linha: RM

   b. Versão: RM 12.1.10

   c. Tipo: Patch

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.

**Importante**: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. Acesse o menu **Opções / Parâmetros / Parâmetros Gerais**, aba **Registro e Controle II**.
2. No agrupador **Registro de Atendimento** marque a opção **Torna a Divisão de Cobrança Default**.
3. Acesse o menu **Cadastro / Faturamento / Condições Contratuais com Convênios** e verifique qual tabela está em vigência para o convênio desejado.
4. Acesse o menu **Cadastros / Unidade de Diagnóstico / Exames e Serviços** e selecione o exame desejado.
5. Acesse o menu **Anexos / Item de Débito** e cadastre ao menos um item de débito para o exame selecionado.
6. Acesse o menu **Cadastros / Faturamento / Tabelas de Procedimentos e Serviços**.
7. Busque pelo exame que foi selecionado para item de débito anteriormente e informe os valores para “**Custo Operacional**” e “**Honorário**”.

## Procedimento para Utilização

1. Acesse o menu **Atendimento / Pronto Atendimento/Ambulatório / Registro de Atendimentos Externos**.
2. Crie um novo atendimento com o mesmo Convênio configurado.
3. Acesse a aba **Pedido de Exames** e inclua um novo pedido.
4. Acesse a aba **Exames Solicitados** e inclua uma nova solicitação do Exame que foi configurado.
5. Clique em **Lançamento em Conta** e verifique, na aba “**Diagnose e Terapia**”, se o valor total do Exame foi corretamente dividido, conforme as seguintes regras:

* Valor de Honorário vai para o Profissional Responsável pelo exame.
* Valor de Custo Operacional vai para o Prestador Principal, que está cadastrado na Unidade de Faturamento à qual a unidade de atendimento está vinculada.

divs
