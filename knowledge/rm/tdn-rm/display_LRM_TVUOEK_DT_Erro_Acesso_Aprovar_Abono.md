---
content_hash: a0c9b5e7cab01e9284c0c0d98c2fe194941735c8b07d4d0936397579a5810353
fetched_at: '2026-06-29T00:08:18.759352+00:00'
page_id: '266968562'
product: rm
source: tdn-rm
title: TVUOEK_DT_Erro_Acesso_Aprovar_Abono
type: documentation
url: https://tdn.totvs.com/display/LRM/TVUOEK_DT_Erro_Acesso_Aprovar_Abono
version: 114
---

# APROVAR ABONO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Aprovar Abono* |
| **Situação/Requisito:** | Quando a pessoa possui duas chapas ativas e ao tentar executar um processo de aprovação de abono pelo portal, o sistema retorna a mensagem abaixo quando uma das chapas não possui grupo de acesso, mesmo alterando o contexto para a chapa que possui grupo de acesso:     Ocorreu um erro ao efetuar a leitura da visão:     Funcionário 00214 não tem grupo de acesso ao RM Portal associado. |
| **Solução/Implementação:** | *Ajustado para apenas exibir a mensagem de erro quando for a chapa do contexto no RM Portal.* |
| **Chamados relacionados:** | *TVUOEK* |

divs
