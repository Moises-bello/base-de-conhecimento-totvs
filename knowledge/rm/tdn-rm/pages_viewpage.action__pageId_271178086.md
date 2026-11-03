---
content_hash: 5b6b11c3c974d4d37d64aca3a3c9639552397955ebd363fe21a1897e127f571c
fetched_at: '2026-06-29T00:08:26.396193+00:00'
page_id: '271178086'
product: rm
source: tdn-rm
title: DT Bloqueio de Agenda por Tipo de Convênio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271178086
version: 114
---

# Bloqueio de Agenda por Convênio

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina(s) envolvida(s)** | | Agenda de Atendimentos | |
| **Requisito (informe o requisito relacionado):** | SAUHRM02-329 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER® e Oracle® |
| **Tabelas Utilizadas:** | SZAGENDACONV |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Criada rotina que determina um limite de atendimentos por convênio.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema (executáveis, dlls e arquivos de configuração):

   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.15 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.15.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:

   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).

   2. Faça o login, com seu E-mail e Senha.

   3. Na barra de menu superior, clique em "DOWNLOAD".

   4. No boxe Central de Downloads aplique os filtros:

   a. Linha: RM;

   b. Versão: RM 12.1.15;

   c. Tipo: Patch.

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.

**Importante**: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Utilização

  1. Acesse o menu "**Atendimento -> Agendamento -> Agenda de Atendimentos**".  
  2. Selecione a unidade de atendimento.  
  3. Selecione a agenda.  
  4. Clique no botão "Opções".  
  5. Acesse a última página “Agendamento por convênio”.  
  6. Clique no botão "Incluir".

  7. Selecione o convênio e informe o Percentual.  
  8. A soma dos percentuais em cada dia não pode ultrapassar os 100%

  9. O percentual não pode ser menor ou igual a zero.

  10. Pelo menos um dia da semana deve ser selecionado.

**Caminho:** "**Atendimento > Agendamento > Agenda de Atendimentos**".

Ao agendar um novo registro, é feita a validação do convênio.

Ao utilizar a funcionalidade de copiar um atendimento e colar diretamente na grid de listagem.

Na tela de agendamento de exames.

Na rotina de agendamento seriado.

divs
