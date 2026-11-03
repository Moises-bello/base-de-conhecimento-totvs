---
content_hash: 5748dddc810b5685e5f30f07793b1044578754b99a25b4eede4eb31a3800a37e
fetched_at: '2026-06-29T00:08:05.280444+00:00'
page_id: '235592546'
product: rm
source: tdn-rm
title: TUOXHW_DT_Publicacao_Link_Acesso_Vazio_Pesquisa_Web
type: documentation
url: https://tdn.totvs.com/display/LRM/TUOXHW_DT_Publicacao_Link_Acesso_Vazio_Pesquisa_Web
version: 117
---

# CONSULTA AO ACERVO - WEB

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Gestão Bibliotecária* |
| **Função:** | *Consulta ao acervo - Web* |
| **Situação/Requisito:** | *Foi identificado que quando uma publicação possui link de acesso, a referência quando a pesquisa é feita pelo portal seja a pública ou logado com um usuário, o sistema não mostra o link, o "Disponível em:" fica vazio no local do link.* |
| **Solução/Implementação:** | *Foi identificado que a falha era causa por uma interpretação do navegador (browser), o link fica entre "<>", estes caracteres são considerados tags html pelos navegadores, foi inserido tratamento na pesquisa web para que se o registro possuir link de acesso, este será tratado para que seja atribuído os códigos corretos dos caracteres , respectivamente "&lt;" e "&gt;".* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
