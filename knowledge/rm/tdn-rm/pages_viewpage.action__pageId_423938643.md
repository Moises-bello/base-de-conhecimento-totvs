---
content_hash: 36f9be9340317202e50d7298865b29c40c53deaa01f4fe2cb9a5ea60ab5db6fd
fetched_at: '2026-06-29T00:09:28.064151+00:00'
page_id: '423938643'
product: rm
source: tdn-rm
title: Atualizar Participantes nos Lançamentos Contábeis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938643
version: 3
---

O processo "Atualizar Participante nos Lançamentos Contábeis" será responsável em rastrear a origem da contabilização (Gestão Patrimonial, Gestão Financeira, Gestão Tributária, Gestão de Estoque e Faturamento, Gestão Imobiliária) de um determinado lote e em um período específico e identificar a Filial ou Cliente/Fornecedor informado na origem, depois será verificado se eles estão cadastrados como participantes na Gestão Contábil e se um de seus relacionamentos compreende a data da contabilização identificada, caso as informações acima seja positiva o processo irá identificar o participante no lançamento contábil.  
Se um Participante for um Cliente/Fornecedor deverá ser observado se partidas de Cliente/Fornecedor diferentes foram agrupadas, pois dessa forma não será possível rastrear e identificar um único Cliente/Fornecedor.

Em um lançamento somente será definido um participante se a data do lançamento estiver entre o período do relacionamento do participante identificado.   
Ao efetuar o rastreamento da origem do lançamento deverá ser considerado o cliente/fornecedor definido na origem, caso ele não estiver preenchido, a filial será considerada, isto quando a origem for Gestão Financeira, Gestão de Estoque e Gestão Tributária.

Gestão de Estoque e Faturamento - Quando o cliente/fornecedor não estiver preenchido será verificada a filial de destino informada no movimento, caso ela também não esteja preenchida será verificado a filial do movimento.

Gestão Patrimonial - será considerada o Cliente/Fornecedor informado no bem (isto quando for gerada a contabilização na inclusão do bem).

No caso de transferência física da Gestão Patrimonial somente será verificado se é participante se for uma transferência entre filiais.
