---
content_hash: c6ce8d1b3684e5f1badcb7d3b3232a6e549d5aea9abcc77d28208a8e52c5ecea
fetched_at: '2026-06-29T00:08:53.323489+00:00'
page_id: '344468663'
product: rm
source: tdn-rm
title: 1955683 MATESTCNTFTOF01-1771 DT Reporta Insumo Mnt
type: documentation
url: https://tdn.totvs.com/display/LRM/1955683+MATESTCNTFTOF01-1771+DT+Reporta+Insumo+Mnt
version: 6
---

# ASSISTENTE DE CÓPIA POR REFERÊNCIA -REPORTA INSUMO MNT

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento. |
| **Função:** | Assistente de Cópia por Referência - Reporta Insumo MNT. |
| **Situação/Requisito:** | Ao executar o processo para Reportar Insumo MNT, foi apresentada consistência de obrigatoriedade de Cliente/Fornecedor no movimento destino, sem que o movimento destino esteja configurador para utilizar Cliente/Fornecedor.  Quando a NF possui itens repetidos com preços diferentes, foi aplicado o mesmo preço para os itens repetidos. |
| **Solução/Implementação:** | O **Motivo de Referência 32 - Reporta Insumo MNT** não irá consistir Cliente/Fornecedor.  **No** **Assistente de Cópia por Referência - Reporta Insumo MNT** passo **Seleção dos Itens de Movimento** será apresentado no campo **Preço Unitário** o valor informado na Nota Fiscal selecionada.  Na Grid de seleção dos produtos a serem reportados, os seguintes campos passa a ser exibidos:   * **Reportar** → Quantidade do insumo a ser reportada ao SigaMNT; * **NF Qtde Original** → Somatório da quantidade do insumo, presente em todas as Notas Fiscais referenciadas; * **NF Qtde Restante** → Quantidade presente na Nota Fiscal, após dedução ao informar a quantidade a "Reportar"; * **SA/SC Qtde Original** → Quantidade oriunda da criação da OS, com insumo previsto, no SigaMNT; * **Já Reportado** → Quantidade do insumo cuja "Baixa" já foi realizada; * **SA/SC Qtde Pendente**→ Quantidade que ainda falta para reportar da SA/SC.   Nos movimentos de cópia por referência do reporte de insumo, **não deverão** ser utilizados rateios por departamento ou por centro de custo, uma vez que estas informações não são enviadas ao protheus. |
| **Conversores e Parâmetros:** | Executar o script **RetiraConsistenciaCliForMR32.zip,** que está anexado ao ticket, em uma base de homologação e assim que validados os dados, replicar para produção.  Abaixo o guia para execução do script: <http://tdn.totvs.com/display/public/rm/Executor+de+Scripts+RM> |
| **Tickets relacionados:** | 1955683. |
| **Requisito:** | MovReportaInsumoOSMntAction. |
| **Documento de Referência:** | . |
