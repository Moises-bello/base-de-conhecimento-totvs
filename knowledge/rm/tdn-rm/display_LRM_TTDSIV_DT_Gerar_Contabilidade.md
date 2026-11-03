---
content_hash: 5dacf29fb29b54a6280b60e533fd343656749892403723eca8eea6ca80554d1f
fetched_at: '2026-06-29T00:06:06.766767+00:00'
page_id: '201731755'
product: rm
source: tdn-rm
title: TTDSIV_DT_Gerar_Contabilidade
type: documentation
url: https://tdn.totvs.com/display/LRM/TTDSIV_DT_Gerar_Contabilidade
version: 1
---

# Gerar Contabilidade

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Gestão de Estoque, Compras e Faturamento* |
| **Função:** | *Gerar Contabilidade* |
| **Situação/Requisito:** | O Sistema não está calculando corretamente o rateio gerencial quando o evento contábil está configurado para buscar as informações no rateio por centro de custo do item. |
| **Solução/Implementação:** | Foi ajustado o serviço responsável por calcular o rateio gerencial dos lançamentos contábeis, a rotina responsável por retornar o somatório dos rateios estava realizando o  cálculo incorretamente. |
| **Conversores e Parâmetros:** | *Não se Aplica* |
| **Chamados relacionados:** | *Não se Aplica* |
| **Requisito (ISSUE):** | *Não se Aplica* |
| **Versões/Release:** | *12.1.8* |
|  |  |
