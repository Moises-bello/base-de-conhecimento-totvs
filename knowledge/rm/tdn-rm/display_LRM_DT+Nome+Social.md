---
content_hash: d577021e9b90188d3a653781ccf104ad3997b61168c0c0b454cb3aea3fa90eaa
fetched_at: '2026-06-29T00:08:24.042207+00:00'
page_id: '270102743'
product: rm
source: tdn-rm
title: DT Nome Social
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+Nome+Social
version: 115
---

# Atendimento - Recepção - Dados de um Paciente - NOME SOCIAL

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina(s) envolvida(s)** | | Prontuário | | Pesquisa de Pacientes | | Agenda de Atendimentos | | Agenda de Cirurgias | | Controle de Leitos | | Pedido de Exames | | Tesouraria | | Toten de Pronto Atendimento | | Painel de Chamadas | |
| **Requisito (informe o requisito relacionado):** | SAUHRM02-324 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER® e Oracle® |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Realizadas alterações nas telas do sistema em que existe interação direta com o cliente, para exibir seu nome social quando existir.

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

## Procedimento para Utilização

Locais com adição ou exibição do nome social:

**Prontuário Eletrônico do Paciente**

* No menu **Prontuário** foi inserido o Nome Social no cabeçalho, substituindo o nome do paciente.O sistema dará prioridade para o Nome Social (se existir).
* Na aba **Identificação** foi incluído o campo **Nome Social**.

* Na aba **Enfermagem/Check de Medicamentos**, foi inserido o campo exibindo o Nome Social nos dados do paciente, e no botão “**Paciente**” do campo “**5 Certos**”.

**Pesquisa Clientes e Atendimentos**

* No menu **Dados de um Paciente**, na tela de **Pesquisa de Clientes e Atendimentos** foi incluída a coluna de **Nome Social** no grid de resultados da pesquisa, e foi incluída também a opção de pesquisa pelo Nome Social através do campo **Nome**.

* Ao selecionar um dos atendimentos do paciente, o campo nome dará prioridade de apresentação ao Nome Social (quando existir).

* Ao selecionar os clientes internados nesta data, o resultado da consulta apresenta a coluna de Nome Social.

* Na tela de pesquisa de pacientes (na agenda de atendimentos, opção de pesquisa padrão), foi adicionada a coluna de Nome Social e a opção de pesquisa pelo Nome Social através do campo de **Nome**.

**Agenda de Atendimentos/Agenda de Cirurgias**

* No menu **Atendimento/Agendamentos/Agenda de Atendimentos,** foi adicionada coluna com o Nome Social.

* Na tela de detalhes da Agenda de Atendimentos foi adicionado um label com o Nome Social, visível quando a tela carrega um novo paciente.

* No menu **Atendimento/Agendamento/Agenda de Cirurgias**, foi adicionada coluna com o Nome Social.

* Na tela de detalhes da agenda de cirurgias, caso o paciente possua um Nome Social, ele será apresentado em um label, visível quando a tela carrega um novo paciente.

**Controle de Ocupação de Leitos/Controle de Visitantes/Passagem de Plantão da Enfermagem**

       11.  Menu Atendimento\Internação\Controle de Ocupação de Leitos, incluído campo Nome Social nas informações do paciente.

* Foi incluída opção para busca do paciente pelo Nome Social, utilizando a pesquisa rápida de paciente.

* No menu **Atendimento/ Controle de Visitantes**, foi incluído campo Nome Social nas informações do paciente.

* No menu **Cuidados com o Paciente/ Postos de Enfermagem/ Passagem de Plantão**, foi incluído campo Nome Social nas informações do paciente.

**Controle de Pedidos de Exames/Tesouraria/Toten de Pronto Atendimento**

* No menu **Unidades Diagnóstico/Controle de Pedidos de Exame**, foi adicionada coluna com o nome social, bem como a pesquisa pelo Nome Social.

* Na tela de detalhes de um Pedido de Exame foi adicionado o campo de Nome Social.

* Na tela de exames, quando o exame for por imagem será apresentado o Nome Social.

* No menu **Tesouraria/Controle de Solicitação p Emissão de Nota Fiscal / Recibos**, foi adicionada coluna com o Nome Social.

* No menu **Atendimento/Pronto Atendimento / Ambulatorio/Toten de Pronto Atendimento**, foi incluída a chamada através do nome social (quando existir).

**Painel de Chamadas**

* Na tela do **Painel de Chamadas**, foi inserida rotina para dar prioridade à exibição do Nome Social.

divs
