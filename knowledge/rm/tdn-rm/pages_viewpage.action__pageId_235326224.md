---
content_hash: 821eccc4e35d3dc6b70c682b9082d9a8c9d5a2e769881035b816b8074c4d8ab2
fetched_at: '2026-06-29T00:08:03.833590+00:00'
page_id: '235326224'
product: rm
source: tdn-rm
title: DT_Lançamento_em_Conta_da_Taxa_de_Sala
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=235326224
version: 115
---

# Lançamento de Taxa de Sala Cirúrgica em Conta

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Registro de Informações de Cirurgias. |  |  | | --- | | **Rotina(s) envolvida(s)** | | Condições Contratuais com Convênios. | |
| **Requisito (ISSUE):** | [PCREQ-10748](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-10748 "PCREQ-10748") |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | MSSQL, Oracle® |
| **Tabelas Utilizadas:** | SZCONDCONTRAT |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Esta implementação tem por objetivo disponibilizar a funcionalidade de Lançamento automático de Taxa de Sala Cirúrgica, na conta do paciente, através do Registro de informações de Cirurgias.

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

1. Acesse o menu **Cadastros / Faturamento / Condições Contratuais com Convênios** e acesse o registro correspondente à condição contratual desejada.
2. Acesse a aba **Parâmetros 3** e na parte inferior do formulário, marque o checkbox “**Utiliza Cobrança de Taxa Cirúrgica**” e preencha os lookups “**Taxa de 1ª hora**” e “**Taxa de ½ hora Subsequente**”. Caso deseje, informe também o tempo de tolerância:
3. Salve as informações.

## Procedimento para Utilização

1. Acesse a **Elaboração de Contas** (ctrl+r) e selecione a conta de algum paciente do mesmo convênio e que esteja internado no momento.
2. Verifique se existe algum lançamento na aba **Taxas e Serviços**.
3. Acesse o menu **Cuidados com o Paciente / Centro Cirúrgico / Registro de Informações Cirúrgicas**.
4. Inclua um novo registro para o mesmo paciente selecionado anteriormente (selecione o mesmo atendimento e mesma parcial).
5. Preencha as informações obrigatórias na aba “**Identificação**”, deixando um intervalo entre o tempo de Inicio e Fim, nas informações de Tempo de Sala:
6. Na aba **Procedimentos**, informe um procedimento e uma equipe com um médico cirurgião.
7. Acesse o menu **Processos / Enviar dados para faturamento** e clique em **Executar**.
8. No exemplo acima, o tempo total de sala foi 04:05, portanto, deverão ser lançados na conta do paciente a taxa da 1ª hora e a quantidade de taxas de ½ hora do tempo restante, sendo que o volume restante de horas poderá ser cobrado como mais uma taxa de meia hora, caso exceda o tempo de tolerância parametrizado
9. Acesse novamente a **Elaboração de Contas** e acesse a aba **Taxas e Serviços**. As taxas lançadas deverão estar nesta aba.

divs
