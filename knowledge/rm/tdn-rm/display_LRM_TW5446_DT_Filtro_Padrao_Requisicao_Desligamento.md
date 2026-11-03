---
content_hash: 7784b5c0db556f593f8021ded21fa10bc41db1bb67db9ea6d7def5d84dfdf320
fetched_at: '2026-06-29T00:08:20.564249+00:00'
page_id: '268577372'
product: rm
source: tdn-rm
title: TW5446_DT_Filtro_Padrao_Requisicao_Desligamento
type: documentation
url: https://tdn.totvs.com/display/LRM/TW5446_DT_Filtro_Padrao_Requisicao_Desligamento
version: 112
---

# FILTRO PADRÃO NA SELEÇÃO DE FUNCIONÁRIOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construções e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Seleção de Funcionários* |
| **Situação/Requisito:** | *Em todas a telas de seleção de funcionário, onde é possível selecionar qual filtro será utilizado para restringir os funcionários que serão executados nos processos, ou na própria visão de funcionários, existe um filtro padrão disponibilizado pelo sistema que é de Requisição de desligamento.*  O sistema não estava verificando se o usuário possuía permissão neste menu para poder listar os funcionários nesta situação, desta forma usuários que não possuíam permissão no menu de requisição de desligamento estavam visualizando os funcionários que possuíam esta requisição. |
| **Solução/Implementação:** | *Foi ajustado o sistema para que no momento em que for utilizado o filtro padrão de requisição de desligamento, o sistema verifique se o usuário possui permissão no menu: [05.01.01.03] Req. Desligamento do perfil do Vitae.*  *Caso o usuário não possua tal permissão, nenhum funcionário será listado.* |
| **Chamados relacionados:** | TW5446 |

divs
