---
content_hash: 71bd55a7e330decadcc02e7baa8dd96e46aed0414db940e6d065281ddae2d409
fetched_at: '2026-06-29T00:08:33.487519+00:00'
page_id: '274322826'
product: rm
source: tdn-rm
title: DT Regras de Lançamento em Conta
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274322826
version: 107
---

# Regras de Lançamento em Conta

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Substituição de Prestador na Conta | SauPrestadorContaAction |  |  | | --- | | **Rotina(s) envolvida(s)** | | Prontuário Eletrônico do Paciente | | Registro de Atendimentos Externos | | Elaboração de Contas | | Registro de Informações de Cirurgias | |
| **Cadastros Iniciais:** | Registro de Atendimentos Externos |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | SAUHRM02-985 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER® e ORACLE® |
| **Tabelas Utilizadas:** | SZPRESTADORCONTA  SZPRESTADORCONTACONVENIO |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Implementado o cadastro de regras para substituir **médico** **prestador** pela **unidade de faturamento** na conta, mediante configuração de Unidade de Atendimento, Especialidade, Tipo de Atendimento (Interno, Externo, Ambos), Procedimento (Exame, Honorário, Ambos), Relação com o Convênio (Credenciado, Não Credenciado, Ambos) e Convênio.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):

   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.17 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.17.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:

   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).

   2. Faça o login, com seu E-mail e Senha.

   3. Na barra de menu superior, clique em DOWNLOAD.

   4. No boxe Central de Downloads aplique os filtros:

   a. Linha: RM

   b. Versão: RM 12.1.17

   c. Tipo: Patch

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.

**Importante**: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Utilização

1. Acesse **Cadastros / Faturamento / Substituição de Prestador na Conta** (nova tela de cadastro de regra para Substituição de Prestador na Conta).

A tela possui os seguintes campos para a configuração da regra:

* Unidade de Atendimento.
* Especialidade.
* Tipo de Atendimento (Interno, Externo, Ambos).
* Procedimento (Exame, Honorário, Ambos).
* Relação com o Convênio (Credenciado, Não Credenciado, Ambos).
* Lista dos Convênios contemplados por esta regra.

**Aplicação da regra**

1. Acesse o menu ****Unidades Diagnóstico / Registro de Atendimentos Externos****.
2. Crie um registro de atendimento com Unidade de Atendimento, Convênio e Especialidade que atenda uma das regras configuradas na tela de Substituição de Prestador na Conta.
3. Ao inserir um registro na aba Guia/Autorização, caso o atendimento esteja de acordo com alguma das regras de substituição de prestador, ao clicar em lançamento em conta, é possível verificar que o médico prestador foi substituído pela unidade de faturamento.

**Prontuário Eletrônico do Paciente**

1. Acesse a aba Anamnese / Exame Físico, HPP, Procedimentos, ao clicar em **Consulta Paciente Internado**, será aberta a janela **Confirmação da Quantidade do Item.**
2. Clique em **OK**, se a consulta estiver de acordo com a regra de substituição de prestador, ele será substituído pela unidade de faturamento na prestação de contas.

**Registro de Informações de Cirurgias**

1. Ao selecionar um registro, e dentro dos processos a opção **Enviar dados para faturamento**, caso o atendimento esteja dentro de uma das regras configuradas para a substituição, o médico prestador será substituído pela unidade de faturamento.

divs
