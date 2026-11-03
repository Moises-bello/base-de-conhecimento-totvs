---
content_hash: 1c6945e72967e773be0b065250bfd3f60091b0d27ea2d88f7ec849f6ba937673
fetched_at: '2026-06-29T00:06:15.353257+00:00'
page_id: '210053074'
product: rm
source: tdn-rm
title: TTEBXK_DT_Geracao_De_Relatorios
type: documentation
url: https://tdn.totvs.com/display/LRM/TTEBXK_DT_Geracao_De_Relatorios
version: 1
---

# GERAÇÃO DE RELATÓRIOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Geração de Relatórios do tipo "Dados Minha Equipe" e "Meus Dados"* |
| **Situação/Requisito:** | No Gerador Reports, foram removidos tratamentos de produtos como os códigos do Labore para relatórios do tipo "Dados Minha Equipe" e "Meus Dados", fazendo com que os relatórios desses tipos passassem a trazer dados incorretos. |
| **Solução/Implementação:** | Foi criado um provider do Labore que é chamado pelo Reports, passando o filtro apropriado em casos de relatórios do tipo "Meus Dados" ou "Dados Minha Equipe" |
| **Chamados relacionados:** | TTEBXK |
| **Versões/Release:** | *12.1.8* |

divs
