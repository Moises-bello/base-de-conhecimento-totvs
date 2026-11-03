---
content_hash: 02224d82bd58b8001c8ab6b14669ae3492ec3b2787b24f2905682fcbc1910474
fetched_at: '2026-06-29T00:08:05.422476+00:00'
page_id: '235595202'
product: rm
source: tdn-rm
title: TUMRAT_DT_Portal_Requisicao_de_Treinamento
type: documentation
url: https://tdn.totvs.com/display/LRM/TUMRAT_DT_Portal_Requisicao_de_Treinamento
version: 117
---

# RM PORTAL - REQUISIÇÃO DE TREINAMENTO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão de Pessoas |
| **Função:** | Requisição de Treinamento |
| **Situação/Requisito:** | Ao realizar o cadastro de uma requisição de treinamento através do RM Portal, o sistema está apresentando mensagem de referência de objeto. O cadastro é realizado, mesmo apresentado a mensagem. |
| **Solução/Implementação:** | Verificado que o sistema tenta manipular objetos da tela que ainda não estão completamente carregados, o que faz gerar a mensagem. Adicionada validação, onde os objetos só serão manipulados caso já estejam carregados no contexto da tela. |
| **Chamados relacionados:** | TUMRAT |

divs
