---
content_hash: 4111074b64267d6e915e306dba066073fc12045d5417827ffa3dba3947212173
fetched_at: '2026-06-29T00:08:15.602093+00:00'
page_id: '244913151'
product: rm
source: tdn-rm
title: DT_Registro_de_Atendimento_Externo_Campo_Responsável_pelo_Exame
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244913151
version: 111
---

# Registro de Atendimento Externo - Campo Responsável pelo Exame

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Registro de Atendimento Externo | |
| **Parâmetro(s):** | psaRespExameObrigatorio |
| **Chamados Relacionados** | TVFGNV |
| **Requisito (ISSUE):** | SAUHRM01-579 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER® e ORACLE® |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Implementado novo parâmetro que torna obrigatória a escolha de um médico responsável ao solicitar um exame na tela de Registro de Atendimentos Externos, e realiza o preenchimento automático deste campo com o médico responsável pelo atendimento, caso exista um.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):

   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.13 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.13.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

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

**Exemplo:**

1. Acesse o menu **Opções / Parâmetros / Parâmetros Gerais**, aba "**Registro e controle II"**, e marque a opção “**Obriga responsável pelo exame no atendimento externo**”.
2. Na tela de **Registro de Atendimentos Externos**, crie um novo atendimento selecionando a unidade de atendimento como **Laboratório**.
3. Inclua um novo registro na aba "**Pedido de Exames"**.
4. Na aba de "**Exames Solicitados**", ao tentar incluir um registro sem um responsável pelo exame e sem um médico responsável pelo atendimento, será exibida uma mensagem informando que esse campo deve ser preenchido.
5. Caso exista um médico selecionado no campo **Médico Responsável**, na aba **"Dados Atendimento"**, ao gravar uma solicitação de exame o mesmo médico será inserido no campo **Responsável pelo Exame**, da aba de **"Exames Solicitados".**

divs
