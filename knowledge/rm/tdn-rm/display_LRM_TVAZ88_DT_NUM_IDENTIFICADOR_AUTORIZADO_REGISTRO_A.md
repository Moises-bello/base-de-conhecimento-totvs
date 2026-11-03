---
content_hash: 6109475040f721de21e72ab7cc7e141e4777b9f560040718ae817e2e14cb9810
fetched_at: '2026-06-29T00:08:11.539288+00:00'
page_id: '243011938'
product: rm
source: tdn-rm
title: TVAZ88_DT_NUM_IDENTIFICADOR_AUTORIZADO_REGISTRO_A
type: documentation
url: https://tdn.totvs.com/display/LRM/TVAZ88_DT_NUM_IDENTIFICADOR_AUTORIZADO_REGISTRO_A
version: 113
---

# CAGED

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Folha de Pagamento* |
| **Função:** | *Emissão do CAGED* |
| **Situação/Requisito:** | Para a emissão do campo "TIPO INDENTIFICADOR" o valor continua sendo obtido do parâmetro "Identificação" da Aba empresa tanto para os dados gerais como especifico para cada coligada.  Para o campo "NÚMERO IDENTIFICADOR" o sistema busca do parâmetro INSS ou CNPJ informado na aba Empresa, para o CNPJ casa não sendo informado busca da coligada. Já o parâmetro INSS é de preenchimento obrigatório e por isso ao selecionar a opção "CEI" no parâmetro "TIPO INDENTIFICADOR" o valor do parâmetro INSS é usado para preencher o campo "NÚMERO IDENTIFICADOR". |
| **Solução/Implementação:** | Disponibilizada a edição do Parâmetro CNPJ quando o parâmetro "identificador" tiver sido marcado a opção CNPJ o sistema passou a levar o valor do Parâmetro CNPJ para o campo "NÚMERO IDENTIFICADOR" do "REGISTRO A". |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TVAZ88* |
| **Requisito (ISSUE):** |  |

divs
