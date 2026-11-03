---
content_hash: 2bcdcfd6a6175e5c5dfca0293491adf27c187901e5f49f806bf217a69d1e748b
fetched_at: '2026-06-29T00:08:31.244599+00:00'
page_id: '273296701'
product: rm
source: tdn-rm
title: 429202 MRH-6039 SEFIP RetencaoLei9711_98PorCEI
type: documentation
url: https://tdn.totvs.com/display/LRM/429202+MRH-6039+SEFIP+RetencaoLei9711_98PorCEI
version: 111
---

# Parâmetros do SEFIP

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | TOTVS Folha de Pagamento. |
| **Função:** | Detalhamento por CEI no Parâmetros do Tomador de Serviço. |
| **Situação/Requisito:** | Para atender a lei 9711/98 a fim de detalhar os valores de retenção / Dedução e compensação do Tomador de serviço por CEI o sistema deve fornecer um cadastro que detalha os valores também por CEI e não só por tomador. |
| **Solução/Implementação:** | Para atender a lei 9711/98 foi criado o cadastro para e detalhar os valores de retenção / Dedução e compensação do Tomador de serviço por CEI.  Este cadastro é um anexo do cadastro "Parâmetros Tomadores de Serviço" dos parâmetros do SEFIP.  Ao Clicar no botão "Inicializar Todos os Tomadores no SEFIP" será preenchido também o detalhamento por CEI para os "Parâmetros Tomadores de Serviço".  No SEFIP o sistema passa a considerar primeiramente o Detalhamento por CEI para os Tomadores que tenha sido informado os valores para “Total de Salário Família”, “RetencaoLei9711\_98” e “Faturas do Tomador” nos respectivos campos 14 – “Salário Família”, 18 – “Valor de Retenção (Lei 9.711/98)” e 19 – “Valor das faturas emitidas para o tomador” para o Registro 20. Caso não tenha sido feito o detalhamento o sistema irá buscar os valores do cadastro "Parâmetros Tomadores de Serviço".  Na Guia de INSS o Tomador de serviço tendo CEI passa a ser verificado se possui detalhamento de CEI. Caso tenha será usado os campos “Valor de Retenção (Lei 9711/98)” e “Compensação do Mês” do detalhamento do CEI. Caso o tomador não tenha CEI ou não foi feito detalhamento por CEI nos parâmetros do SEFIP usará os respectivos campos do cadastro "Parâmetros Tomadores de Serviço". Os valores destes parâmetros serão usados nos campos "Retenção" e "Compensação/Reembolso" dos valores da seção referente aos parâmetros da GUIA de INSS.. |
| **Conversores e Parâmetros:** |  |
| **Tickets relacionados:** | 429202. |
| **Requisito:** |  |

divs
