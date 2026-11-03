---
content_hash: 107b23b38e3b4a34634bee5279cfca7a7a4ef5f700a560122af7ead10cb4df2a
fetched_at: '2026-06-29T00:08:17.190020+00:00'
page_id: '253988733'
product: rm
source: tdn-rm
title: TURTCO_DT_Criacao_Usuario_Portal_Exibindo_Igual_Codigo_Usuario_Biblioteca
type: documentation
url: https://tdn.totvs.com/display/LRM/TURTCO_DT_Criacao_Usuario_Portal_Exibindo_Igual_Codigo_Usuario_Biblioteca
version: 112
---

# GERAR USUÁRIO DE ACESSO AO PORTAL

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Gestão Bibliotecária* |
| **Função:** | *Gerar usuário de acesso ao portal* |
| **Situação/Requisito:** | *Ao executar o processo de geração de usuários no portal para um usuário que já possui acesso porém com um usuário diferente, o sistema conclui o processo informando que o usuário já existe porém informando que o usuário do portal é o mesmo da biblioteca, sendo que no caso o usuário é diferente.* |
| **Solução/Implementação:** | *Foi feito uma alteração no log do processo para que se o usuário já tiver acesso ao portal da biblioteca o sistema irá informar que já possui acesso e as alterações devem ser feitas pelo cadastro de usuários em globais, caso o usuário  tenha acesso ao portal, porém sem perfil de acesso a biblioteca, o sistema irá alertar informando que o mesmo possui acesso ao portal porém sem acesso a biblioteca e que o perfil de acesso a biblioteca foi definido para o usuário e caso seja um novo usuário sem nenhum acesso, o mesmo irá confirmar a atribuição do acesso com sucesso, ressaltando que para todas as três situação o sistema sempre irá mostrar qual é o usuário de acesso ao portal, mesmo que seja diferente do usuário da biblioteca, assim facilitando o entendimento do processo e a identificação do acesso do código de acesso ao portal.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
