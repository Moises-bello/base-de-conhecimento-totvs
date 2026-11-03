---
content_hash: f5dbfcd86889d162449f73cb30e73354f72fab7c28f68bf8bb6b7f0338b68fa7
fetched_at: '2026-06-29T00:09:09.903850+00:00'
page_id: '394215175'
product: rm
source: tdn-rm
title: DEDUINTEGRACOES-3198 DT Falha ao carregar o evento customizado "SimularValoresParcelaEventHandle"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=394215175
version: 1
---

# FALHA AO CARREGAR O EVENTO CUSTOMIZADO "SIMULARVALORESPARCELAEVENTHANDLE"

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Simulação de valores de parcelas (customização)* |
| **Situação/Requisito:** | *Sistema não carrega o plugin de simulação de valores de parcelas acionado a partir da visão de parcelas de contratos.*  *Como a classe de cálculo de valores por crédito passou a não ser mais um RMSObject, a mesma passou a não carregar mais os plugins associados.* |
| **Solução/Implementação:** | *Ajuste no produto para que o evento customizado seja chamado pela classe de regra de negócio*EduLancamentoIntDataObj no cálculo de valores por crédito que é um RMSObject. Alteração da DLL de plugin bem como a geração de um script de alteração de base também tiveram que ser gerados pela equipe de customização. |
| **Conversores e Parâmetros:** | *N/A* |
| ****Tickets relacionados**:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Documento de Referência:** | N/A |
