---
content_hash: 95875b366a1749ed8fb0c1931eb6e8a541ee561a3d8db33b8dab8b374ac1bf95
fetched_at: '2026-06-29T00:08:17.108053+00:00'
page_id: '253984990'
product: rm
source: tdn-rm
title: TVMRFO_DT_Frequencia_Diaria_WebService
type: documentation
url: https://tdn.totvs.com/display/LRM/TVMRFO_DT_Frequencia_Diaria_WebService
version: 111
---

# FREQUÊNCIA DIÁRIA - WEBSERVICE

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Frequência Diária - WebService* |
| **Situação/Requisito:** | *Ao tentarmos executar o método SaveRecord do DataServer "EduFrequenciaDiariaWSData" retorna "Você não está autorizado a inserir registros!", mesmo com o usuário podendo executar tal ação pelo sistema ou pelo portal.* |
| **Solução/Implementação:** | *Ajuste nas permissões do dataserver EduFrequenciaDiariaWSData para que seja obedecido a permissão no perfil "Educacional | Matrícula e Avaliação | Notas e Faltas | Frequência diária" e/ou "Educacional | Outras Permissões | RM Portal | Professor | Diário de Classe | Frequência Diária" quando se utilizada WebService.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
