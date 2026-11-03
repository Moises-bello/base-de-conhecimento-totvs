---
content_hash: b368b7e78c033826e1cfda7369b30aaab13df67ac395017cccb62604678b2609
fetched_at: '2026-06-29T00:06:06.526087+00:00'
page_id: '201731679'
product: rm
source: tdn-rm
title: TSYUSY_DT_Gerar_Contabilidade
type: documentation
url: https://tdn.totvs.com/display/LRM/TSYUSY_DT_Gerar_Contabilidade
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
| **Versões/Release:** | *11.82.41* |
