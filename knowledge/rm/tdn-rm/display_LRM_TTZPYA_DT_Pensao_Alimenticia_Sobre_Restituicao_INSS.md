---
content_hash: eb33a3acc391a9facf28210f511edb2e35e41d645a2bbbdb9cdf32e714f932dd
fetched_at: '2026-06-29T00:08:06.195645+00:00'
page_id: '236588572'
product: rm
source: tdn-rm
title: TTZPYA_DT_Pensao_Alimenticia_Sobre_Restituicao_INSS
type: documentation
url: https://tdn.totvs.com/display/LRM/TTZPYA_DT_Pensao_Alimenticia_Sobre_Restituicao_INSS
version: 2
---

# NÃO ESTÁ DESCONTANDO PENSÃO ALIMENTÍCIA SOBRE RESTITUICAO DE INSS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Pensão Alimentícia* |
| **Situação/Requisito:** | *Não está sendo descontada Pensão Alimentícia quando o funcionário possui apenas o evento de Restituição de INSS (CC 92) em seu envelope de pagamento.*  *Evento de CC 92 está com a incidência em Pensão marcada.* |
| **Solução/Implementação:** | *Ajuste no cálculo da Pensão Alimentícia para considerar o evento de CC 92 - "Restituição de INSS" nos rendimentos brutos, mesmo se este for o único provento do envelope a compor a Base de Pensão.* |
| **Chamados   relacionados:** | *TTZPYA, TUVD23* |
| **Versões/Release:** | *11.82.44, 12.1.12* |
