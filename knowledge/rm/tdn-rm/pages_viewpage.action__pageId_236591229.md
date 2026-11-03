---
content_hash: 508833c06cc3e3f5154db7b3f648bce508e1c6207ded217b74f2bf1eacf14dc7
fetched_at: '2026-06-29T00:08:06.424920+00:00'
page_id: '236591229'
product: rm
source: tdn-rm
title: TUTIMS_DT_Migração_do_Reprocessamento_de_Remessa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=236591229
version: 3
---

# Migração da rotina de Reprocessamento

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Faturamento de Convênios | SauFaturaProcFatForm | |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server / Oracle |
| **Tabelas Utilizadas:** | SZLOGFATURAMENTO, SZFATURACONVENIO, SZPARCIALATEND, SZATENDIMENTO, SZLOGCONTAS |
| **Sistema(s) Operacional(is):** | Windows ® |

## Descrição

Foi efetuada a migração da rotina de Reprocessamento de Remessas de convênios para nova MDI.

## Procedimento para Utilização

1. Acesse **RM.exe** no módulo **TOTVS Gestão Hospitalar**.
2. Através do menu **Faturamento**, acesse a rotina **Faturamento** **para** **Convênios**.
3. Selecione uma Remessa que encontra-se com status "**Faturada**" e através do menu **Processos**, selecione **Faturamento** **de Convênios**.
4. Na tela de **Opções de Faturamento**, selecione a opção "**Reprocessamento**" em seguida clique em **Avançar**.
5. Na próxima tela serão apresentadas as Opções de Reprocessamento, são elas:  
   * **Excluir conta(s) da Remessa**: Retorna a(s) conta(s) selecionada(s) para o status "**Liberada**" e remove os vínculos com a remessa.
   * **Cancelar remessa**: Exclui todas contas da remessa, retornando-as para o status "**Liberada**", e altera o status da remessa para "**Cancelada**".
   * **Retornar conta(s) para Correção**: Retorna a(s) conta(s) selecionada para o status "**Em** **Elaboração**", mantendo o vínculo com a remessa. (Observação: Neste caso será necessário Encerrar através da **Elaboração de Contas**).
6. Avance novamente, é necessário preencher o **Motivo de Reprocessamento**.
7. Clique em **Executar** e aguarde o término do processo.
