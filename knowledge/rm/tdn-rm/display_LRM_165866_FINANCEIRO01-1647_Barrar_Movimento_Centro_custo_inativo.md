---
content_hash: 8a93f29b85e5d19c0b3c79e84ef6fd0b28ae45ab5d0911ee7caa6c652a666bd6
fetched_at: '2026-06-29T00:08:39.056051+00:00'
page_id: '286007415'
product: rm
source: tdn-rm
title: 165866_FINANCEIRO01-1647_Barrar_Movimento_Centro_custo_inativo
type: documentation
url: https://tdn.totvs.com/display/LRM/165866_FINANCEIRO01-1647_Barrar_Movimento_Centro_custo_inativo
version: 108
---

# BARRAR INCLUSÃO DE MOVIMENTO COM CENTRO DE CUSTO INATIVO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Totvs Gestão de Estoque, Compras e Faturamento. |
| **Função:** | Inclusão/Edição de movimentos. |
| **Situação/Requisito:** | Mesmo após desabilitar o parâmetro *Barrar Lançamento para Centro de Custo inativo* no Totvs Gestão Contábil o sistema ainda não permite a inclusão do movimento com centro de custo (do item, movimento ou rateio) inativo. |
| **Solução/Implementação:** | Quando o parâmetro *Barrar lançamento para centro de custo inativo* está desmarcado, na inclusão/edição de movimento/item de movimento, os lookups de centro de custo (Tabelas | Centro de Custo / Rateio Centro de Custo) devem exibir os centros de custos inativos, permitir selecioná-los e salvar o registro normalmente.  Quando o parâmetro do Totvs Gestão Contábil *Permitir Lançamento com Centro de Custo inativo por módulo* não estiver informado para o módulo corrente, na inclusão de movimento/item de movimento os lookups de centro de custo (Tabelas | Centro de Custo / Rateio Centro de Custo) não exibirão os centros de custos inativos. Além disso, para registros de movimento incluídos por outros meios que não a interface, não será permitida a inclusão.  OBS: no caso do serviço de inclusão/alteração a consistência sobre o parâmetro *Permitir Lançamento com Centro de Custo inativo por módulo* será pelo campo *Integra Aplicação* do movimento já que pode ser chamado por outras origem. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | 165866. |
| **Requisito:** | FINANCEIRO01-1647. |

divs
