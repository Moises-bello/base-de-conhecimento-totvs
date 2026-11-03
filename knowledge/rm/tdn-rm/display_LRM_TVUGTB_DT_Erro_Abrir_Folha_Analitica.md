---
content_hash: 4d900df14638c5e58739306130f8533b7fd002587121576211109ce959d4401c
fetched_at: '2026-06-29T00:08:19.957802+00:00'
page_id: '267801778'
product: rm
source: tdn-rm
title: TVUGTB_DT_Erro_Abrir_Folha_Analitica
type: documentation
url: https://tdn.totvs.com/display/LRM/TVUGTB_DT_Erro_Abrir_Folha_Analitica
version: 110
---

# FOLHA ANALÍTICA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Folha Analítica* |
| **Situação/Requisito:** | Ao acessar a rotina de folha analítica .Net apresenta a seguinte mensagem de erro:     InvalidArgument=Value'6' não é um valor valido para 'index'. Nome do parâmetro: Index     A folha analítica .Net é gerada normalmente, mesmo apresentando o erro. |
| **Solução/Implementação:** | *Foi feito um tratamento para que não processe Códigos Ativos com mais de 6 posições.*  Na base havia espaço em branco que gerava o erro informado.  Saída de contorno: Ir nos parâmetros da Folha de Pagamento mudar o valor de um código ativo, gravar e retornar o valor. Após esse processo o problema é solucionado na base. |
| **Chamados relacionados:** | *TVUGTB* |

divs
