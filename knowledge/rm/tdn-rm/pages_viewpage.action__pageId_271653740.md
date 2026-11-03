---
content_hash: 1b7a6182aa681051ade81768cfccecba8b93f3023f794614e8c9059e9b93baf5
fetched_at: '2026-06-29T00:08:28.024539+00:00'
page_id: '271653740'
product: rm
source: tdn-rm
title: DT Agendar Exames com Melhor Distribuição entre as Agendas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271653740
version: 114
---

# Agendar Exames com melhor distribuição entre as agendas

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Parâmetros Gerais | | Agendamento de Exames | |
| **Parâmetro(s):** | Não agrupar por agendas no agendamento de Exames  Não identificar agenda no agendamento de Exames |
| **Tickets relacionados** | 198251 |
| **Requisito****:** | SAUHRM02-588 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER® e Oracle® |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

A partir dessa implementação, é possível configurar o agendamento de exames com melhor distribuição entre as agendas, e parametrizar o agrupamento por exame e data, e a exibição (ou não) do médico da agenda.

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

1. Acesse **Opções/Parâmetros/Parâmetros Gerais**aba **Registro e Controle III**.
2. Marque os parâmetros **Não agrupar por agendas no agendamento de Exames** e **Não identificar agenda no agendamento de Exames**.

## Procedimento para Utilização

1. Acesse **Atendimento / Agendamento / Agenda de atendimentos**.
2. Crie ou altere um agendamento de exames.
3. Ao carregar os horários disponíveis, será  agrupado pelos horários, não mais por agenda, quando parametrizado.

* Verifique na imagem exemplo de quando utilizado somente o parâmetro **Não agrupar por agendas no agendamento de Exames**.

* Verifique na imagem exemplo de quando utilizado somente o parâmetro **Não identificar agenda no agendamento de Exames**.
* Verifique na imagem exemplo de quando utilizado os dois novos parâmetros.

divs
