---
content_hash: ab807f1079bfa2e98b44d80dc4d9eb1ec08f1cea00cf7297e366c037994e7106
fetched_at: '2026-06-29T00:08:31.776218+00:00'
page_id: '273309891'
product: rm
source: tdn-rm
title: DT Melhorias no Painel de Eletivos
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+Melhorias+no+Painel+de+Eletivos
version: 115
---

# Painel de Eletivos

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Painel de Atendimentos Eletivos | |
| **Cadastros Iniciais:** | Agenda de Atendimentos |
| **Parâmetro(s):** | OMITECHAMADAPEPENFERMAGEM |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | SAUHRM02-845 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER® |
| **Tabelas Utilizadas:** | SZSENHACLASSIF, SZCLASSIFICACAORISCO |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Implementada melhoria que consiste em, um paciente com mais de um exame agendado mantém o mesmo número de senha para diferentes exames na mesma data e unidade de atendimento.

No painel de Enfermagem, foi realizada a substituição das colunas "Dt. Triagem" e "Espera" pelas colunas "Data do Agendamento" e "Hora do Agendamento".

Realizada a inclusão de campo com a descrição dos exames na aba de Posto de Enfermagem e na tela de Agendamentos do dia.

Implementado parâmetro para omitir a chamada do Prontuário Eletrônico ao chamar o paciente na aba de Posto de Enfermagem.

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

   b. Versão: RM 12.1.17

   c. Tipo: Patch

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.

**Importante**: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. Acesse **Opções/Parâmetros/Parâmetros Gerais,** aba **Classificação de Risco**.
2. Marque o parâmetro **No atendimento de enfermagem NÃO chama o prontuário do paciente**.

## Procedimento para Utilização

**Exemplo:**

1.  Acesse Menu **Atendimento / Pronto Atendimento/Ambulatório/ Painel de Atendimentos Eletivos**, aba **Registro de Atendimento**.

2. Selecione uma senha e inicie o atendimento. Caso o paciente escolhido possua mais de um agendamento nesta unidade de atendimento, o sistema perguntará se deseja registrar todos, responda Sim.

3. Na tela de **Agendamentos do Dia**, selecione um registro para dar início ao atendimento. Na imagem abaixo vemos a inclusão da coluna de **Procedimentos** nesta tela, com a descrição de todos os exames incluídos em cada agendamento.

4. Após registrar o primeiro atendimento, o sistema informa que já existe um atendimento em aberto para o paciente nesta data e pergunta se deseja criar um novo. Ao responder Sim, um novo atendimento será criado, porém mantendo o mesmo número de senha utilizado no primeiro atendimento.

5. Após passar pela **Classificação de Risco**, os exames aparecem individualmente na aba de **Posto de Enfermagem**, com a descrição dos procedimentos, e mesmo número de senha

6. No exemplo da imagem acima é possível observar também a substituição das colunas **Dt. Triagem** e **Espera** pelas colunas **Data do Agendamento** e **Hora de Início**, bem como a adição da coluna **Procedimentos**.

7. Quando o parâmetro **No atendimento de enfermagem NÃO chama o prontuário do paciente** estiver marcado, ao clicar duas vezes em um registro na aba de **Posto de Enfermagem**, a tela de **Prontuário Eletrônico** não será chamada, e será possível finalizar o atendimento apenas através do botão **Finalizar Atend**.

divs
