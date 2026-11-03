---
content_hash: e90c82379e9882dba1d1b6d76182f35209385ee0bb5e25db0acdcc203d7add38
fetched_at: '2026-06-29T00:08:11.268490+00:00'
page_id: '242388523'
product: rm
source: tdn-rm
title: DT_Incorporação_Custom_UBERABA
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=242388523
version: 107
---

# Incorporação Custom UBERABA

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Prontuário Eletrônico | | Assistência Domiciliar | | Score Nivelamento | | Planejamento de Visitas | | Agenda de Técnico de Enfermagem/Mapa de agendamento | |
| **Requisito (ISSUE):** | SAUHRM01-3 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server® e Oracle® |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Implementadas melhorias de Assistência Domiciliar, Planejamento de Visitas, Score Nivelamento e Mapa de agendamento de Técnico de Enfermagem.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):

   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.12 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.12.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:

   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).

   2. Faça o login, com seu E-mail e Senha.

   3. Na barra de menu superior, clique em DOWNLOAD.

   4. No boxe Central de Downloads aplique os filtros:

   a. Linha: RM

   b. Versão: RM 12.1.12

   c. Tipo: Patch

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.

**Importante**: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Utilização

* **Assistência Domiciliar**

1. Acesse o menu **Prontuário** na aba **Anamnese/Formulários Especiais**.
2. Clique em **Formulários de Assistência Domiciliar**.

* **Score Nivelamento (Nivelamento de risco)**

1. Acesse o menu **Prontuário** na aba **Anamnese/Exame Físico**.
2. Clique no botão **Score Nivelamento**. Será aberta a grid com os scores já cadastrador para o paciente e atendimento selecionado no Prontuário Eletrônico do Paciente.
3. Clicando no botão **Inserir**, é apresentada a tela de cadastro do nivelamento de risco.

* **Planejamento de visitas**

1. Acesse o menu **Prontuário** na aba **Anamnese/Exame** **Físico**.
2. Será aberto o grid filtrando pelo paciente e atendimento selecionados.
3. O clicar no botão **Inserir**, é exibida a tela para o cadastro do planejamento de visitas.

* **Mapa de técnico de enfermagem**

1. Acesse o menu **Atendimento/Agendamento/Mapa Téc. enfermagem**.
2. Será exibido o mapa apenas para visualização.
3. Os horários são preenchidos quando existem agendamentos para técnicos de enfermagem.
4. Para cadastrar, é necessário ter uma agenda do tipo Téc. Enfermagem. Acesse o menu **Cadastros/Uso Geral/Agendamento/Agendas**.
5. Cadastre uma agenda do tipo Téc. Enfermagem.
6. Ao realizar um agendamento para esta agenda, é necessário preencher os dados da aba **Assistência Domiciliar**.
7. Dessa forma, ao salvar o agendamento, o sistema calcula o tempo de deslocamento e o tempo de medicação e "bloqueia" os horários seguintes se baseando nos dois tempos informados.

divs
