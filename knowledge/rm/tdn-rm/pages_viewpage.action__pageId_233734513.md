---
content_hash: d13e3a96149d42dbccbe44184edba3b8acbe68616675effb3c4e9cf853e2c9c4
fetched_at: '2026-06-29T00:06:27.539006+00:00'
page_id: '233734513'
product: rm
source: tdn-rm
title: DT_Duplo_Click_Painel_Classificação_de_Risco
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=233734513
version: 124
---

# Duplo Click no Painel de Classificação de Risco (Painel de Atendimento Médico)

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Atendimento | Painel de Classificação de Risco | |
| **Requisito (ISSUE):** | PCREQ-9986 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server, Oracle |
| **Tabelas Utilizadas:** | SZCLASSIFICACAORISCO |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

O objetivo desta implementação é estabelecer as ações que o médico pode realizar ao dar um duplo clique sobre um determinado paciente no painel de classificação de risco.

Esta ação tem como finalidade evitar que um paciente seja chamado no painel, quando o médico não tiver esta intenção.

Quando o médico der um duplo clique num determinado paciente da fila de atendimento, o sistema deverá exibir uma tela com as seguinte opções:

* **Chamar**: fará a chamada do paciente no painel de chamados se ainda não estiver em atendimento.
* **Somente Abrir o Prontuário**: abrirá o prontuário do paciente para que o médico visualize algum dado anterior a este atendimento.
* **Cancelar**: fechará a tela com as opções.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):  
Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.10 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.10.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

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

## Procedimento para Utilização

1. Acesse o menu **Atendimento/Pronto Atendimento/Toten de Pronto atendimento**.
   1. Selecione a unidade de atendimento.
   2. Clique na especialidade desejada.
   3. Gere uma senha.
2. Acesse o menu **Atendimento/Pronto Atendimento/Painel de Classificação de Risco**.
   1. Selecione a unidade de atendimento.
   2. Selecione a aba **Registro de Triagem**.
   3. Clique no botão **Chamar** e faça a triagem.
   4. Selecione a aba **Registro de atendimento** e realize o atendimento do paciente.
3. Saia do sistema e realize o login com um usuário de perfil Médico.
4. Acesse o menu **Atendimento/Pronto Atendimento/Painel de Classificação de Risco**.
   1. Selecione a unidade de atendimento.
   2. Na aba **Atendimento Médico**, dê um duplo clique numa senha/paciente.
   3. A tela abaixo será exibida.
   4. Ao clicar no botão **Chamar**, a senha seja exibida no painel de chamada.
   5. Ao clicar no botão "**Somente abrir prontuário**", o prontuário será exibido.

divs
