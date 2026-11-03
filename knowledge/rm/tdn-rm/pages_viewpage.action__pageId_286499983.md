---
content_hash: 4a55de30030847b509f71445fe5a8cc1c8625db9dc74727d23d5a35775e01595
fetched_at: '2026-06-29T00:08:40.746942+00:00'
page_id: '286499983'
product: rm
source: tdn-rm
title: DT Hora Fim para Elaboração de Contas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286499983
version: 106
---

# Hora Fim para Elaboração de Contas

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Faturamento/Particular e Convênios/Lançamentos na Conta do Paciente | |
| **Tickets relacionados** | [Ticket #982159](https://totvssuporte.zendesk.com/agent/tickets/982159 "Open ticket in Zendesk Support") |
| **Requisitos** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-1341 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server® e Oracle® |
| **Tabelas Utilizadas:** | SZATENDHONORARIO, SZATENDHONORARIOGLOSA, SZATENDSADT, SZATENDSADTGLOSA |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Implementado na tela de Elaboração de Contas, o campo**Hora Fim** nas abas Honorários, Diagnose Terapia e Especial. Esta melhoria tem por objetivo a indicação de faixa de horário correspondente à execução de um procedimento ou exame, hora inicial e hora final, visando o correto preenchimento dos campos correspondentes nas guias TISS.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):

   Realize a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.18 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.18.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:

   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).

   2. Faça o login, com seu E-mail e Senha.

   3. Na barra de menu superior, clique em DOWNLOAD.

   4. No boxe Central de Downloads aplique os filtros:

   a. Linha: RM

   b. Versão: RM 12.1.18

   c. Tipo: Patch

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.

**Importante**: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Utilização

1. Acesse **Faturamento/Particular e Convênios/Lançamentos na Conta do Paciente**.
2. Para incluir um honorário em uma Elaboração de Contas, clique em **Pesquisar Atend**.
3. Pesquise um cliente, selecione-o e clique em **OK**.
4. Para incluir um Honorário clique no botão **Inclui**.
5. Preencha os campos, incluindo o novo campo **Hora Fim**.
6. Clique no botão **Grava** para salvar o registro.
7. Para incluir uma Elaboração de Conta do tipo Diagnose e Terapia clique na aba de mesmo nome.
8. Para incluir Diagnose e Terapia clique no botão **Inclui.**
9. Preencha os campos, incluindo o novo campo **Hora Fim**.
10. Clique no botão **Grava** para salvar o registro.
11. Para gerar lançamentos especiais clique na aba **Especial**.
12. Selecione Honorários ou Diagnose e Terapia.
13. Preencha os campos, incluindo o novo campo **Hora Fim**.
14. Clique no botão **Grava** para salvar o registro.
15. O novo honorário gerado na aba **Especial** pode ser visualizado na aba Honorários, a mesma rotina pode ser utilizada para Diagnose e Terapia.

Para honorários e diagnose e terapia sem Hora Fim cadastrado, ao encerrar a hora fim de ambas são preenchidos automaticamente com a hora inicial.

Após encerrar:

divs
