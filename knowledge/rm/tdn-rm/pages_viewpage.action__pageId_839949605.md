---
content_hash: 8f434c7c473fdfba4f9781ab176253e69e0ba43c1ce0973f12adef388514b155
fetched_at: '2026-06-29T00:11:50.267336+00:00'
page_id: '839949605'
product: rm
source: tdn-rm
title: 8.1.1 Geração de Boleto com Nova Data de Vencimento pelo Portal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=839949605
version: 4
---

**Objetivo**

Alteração da data de vencimento do boleto no portal, inclusão de um novo boleto e aumento do limite para alteração.

**Importante**

* Alteração do parâmetro de “limite para alteração” para "Quantidade limite de dias após o vencimento do boleto para permitir a alteração". RM Portal | RM Portal Geral 8/15 no extrato antigo.
* Uma vez habilitado, será possível simular e alterar uma nova data de vencimento para o boleto através do Portal do Aluno, respeitando o limite de dias parametrizado. Por padrão, a data de vencimento considerada no limite de dias para alteração será a do lançamento.
* Uma vez executado, caso o boleto possua status de remessa igual a Registrado, Registrado Online ou Remetido a remessa será cancelada, o boleto será cancelado e será gerado um novo boleto com a nova data de vencimento associado ao lançamento.

Demais informações estão na documentação complementar: <https://tdn.totvs.com/display/public/LRM/Boletos+Portal>.
