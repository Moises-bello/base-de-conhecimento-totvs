---
content_hash: ede04e805ca34960e72088c62ce2322d41e9be67bd11efe0f245b1f7a6fd1ff0
fetched_at: '2026-06-29T00:08:28.906648+00:00'
page_id: '271866691'
product: rm
source: tdn-rm
title: DT Exames Associados ao Cuidado de Enfermagem
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+Exames+Associados+ao+Cuidado+de+Enfermagem
version: 111
---

# Exames Associados ao Cuidado de Enfermagem

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Itens da Enfermagem  Cuidados e Procedimentos com o Paciente  Prontuário Eletrônico do Paciente | |
| **Requisito****:** | SAUHRM02-593 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER® e Oracle® |
| **Tabelas Utilizadas:** | SZPEPENFSADT   SZRELPRESCPEDIDO |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Implementada rotina que associa exames aos cuidados de enfermagem, para tratar os casos de teste de glicemia capilar, onde é necessário ter pedidos de exames a cada horário prescrito.

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

## Procedimento para Utilização

1. Acesse **Cadastros/Cuidados com o Paciente/Prescrição Médica/Itens da Enfermagem**.
2. Na visualização de detalhes, quando a opção **Prescrição de Enfermagem** estiver marcada, habilitará a aba **Exames Associados**.

   Importante

   Essa aba estará habilitada para todos os itens de tipo Prescrição de Enfermagem.
3. É possível associar exames ao item de enfermagem.
4. No menu **Cadastros/Cuidados com o Paciente/Prescrição Médica/Cuidados e Procedimentos com o Paciente/Dieta**, vincule o cuidado que é prescrito pelo médico ao item de enfermagem do tipo Prescrição de Enfermagem.
5. O Item de Enfermagem deve ser informado e o Cuidado deve estar ativo para que ocorra a solicitação dos exames vinculados.
6. No menu **Prontuário**, acesse a aba **Prescrição Médica**.
7. Ao incluir um cuidado, que possua um item de enfermagem associado do tipo **Prescrição de Enfermagem**, na conclusão da prescrição, será verificado se existem exames associados a ele, e será gerado um pedido de exame para cada horário de aprazamento.
8. Verifique na imagem abaixo exemplo de pedido de exames gerado.
9. No menu **Prontuário**, acesse a aba **Prescrição Médica**.
10. Ao suspender um cuidado, que possua um item de enfermagem associado do tipo **Prescrição de Enfermagem**, caso existam exames associados a ele, serão realizados os cancelamentos de todos os pedidos de exame com horário de aprazamento superior à data e hora da suspensão do item.
11. Na aba de **Avaliações Complementares**, os exames que foram cancelados são indicados com a cor vermelha.

divs
