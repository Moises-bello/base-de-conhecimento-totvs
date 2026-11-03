---
content_hash: e5388fe35d7c829391e1dec47bce1381ae27147caa32cddd16f32398e4f4aee1
fetched_at: '2026-06-29T00:11:26.426981+00:00'
page_id: '716368471'
product: rm
source: tdn-rm
title: tipoCom
type: documentation
url: https://tdn.totvs.com/display/LRM/tipoCom
version: 2
---

## Registro que apresenta o valor total da Receita Bruta por "tipo" de comercialização.

| Registro/Campo | Registro Pai | Ocorr | Tam | Descrição | Origem RM |
| --- | --- | --- | --- | --- | --- |
| tipoCom | ideEstab | 1-3 |  | Registro que apresenta o valor total da Receita Bruta por "tipo" de comercialização. | Este registro detalha as operações registradas. |
| indCom | tipoCom | 1-1 | 1 | Indicativo de Comercialização  Valores Válidos: 1 - Comercialização da Produção por Prod. Rural PJ/Agroindústria, exceto para entidades executoras do PAA; 8 - Comercialização da Produção para Entidade do Programa de Aquisição de Alimentos - PAA; 9 - Comercialização da Produção no Mercado Externo | SE for uma operação para o exterior (CFOP 7xxx) OU as seguintes CFOPs: **5501, 5502, 6501 e 6502**. ENTÃO o indicador será "9"  SENÃO  SE o campo FCFO.ENTIDADEEXECUTORAPAA do Cliente/Fornecedor estiver marcado ENTÃO o indicador será "8"  SENÃO o indicador será "1". |
| vlrRecBruta | tipoCom | 1-1 | 14 | Preencher com o valor total da comercialização.  Validação: Deve ser maior que "0" e não pode ser maior que {vlrRecBrutaTotal}. | Valor Líquido dos itens dos lançamentos selecionados. |
