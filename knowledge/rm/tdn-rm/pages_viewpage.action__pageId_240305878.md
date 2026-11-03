---
content_hash: 1355702c3588556db55787055313444cf2ff84567382d3423dd07aca0e1a6131
fetched_at: '2026-06-29T00:08:10.566348+00:00'
page_id: '240305878'
product: rm
source: tdn-rm
title: TVB827_DT_Migração_Padrão_de_Faturamento_IPERGS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=240305878
version: 3
---

# Migração do Padrão de Faturamento IPERGS

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Faturamento para Convênios | |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server® e Oracle® |
| **Tabelas Utilizadas:** | SZFATURACONVENIO, SZPARCIALATEND, SZATENDIMENTO |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Efetuada migração do faturamento de convênios que utilizam o Padrão de Informação IPERGS para nova MDI.

## Procedimento para Utilização

1. Acesse o menu **Cadastros / Uso Geral / Convênios**.
2. É necessário que o convênio esteja configurado para utilizar o Padrão de Informação **IPERGS**.
3. Acesse pela nova **MDI** o menu **Faturamento** do módulo **Gestão Hospitalar**.
4. Abra o menu **Faturamento para Convênios**.
5. Inclua uma nova **Remessa** para o convênio **IPERGS**.
6. Acesse o menu **Processos** e selecione **Faturamento de Convênios**.
7. Informe as opções de **Faturamento** e clique em **Avançar**.
8. Selecione as contas que serão incluídas na **Remessa** e clique em **Avançar**.
9. Informe a data de vencimento e clique em **Executar**.
10. Ao término do processo, o sistema apresentará a mensagem de conclusão.
11. Acessando os dados da remessa, pode-se verificar as informações atualizadas.
12. Também pode-se verificar os atendimentos vinculados à remessa

* **Nota importante:** Após a migração para nova **MDI**, a geração do arquivo passou a ser realizada na camada *Server*, desta forma é necessário se certificar que o **Servidor** tenha acesso de leitura/escrita no diretório configurado para **Mensagens Transmitidas**.

Com base no diretório configurado nos Parâmetros Gerais, será concatenado “Remessas/IPERGS/[data]” para salvar o(s) arquivo(s).
