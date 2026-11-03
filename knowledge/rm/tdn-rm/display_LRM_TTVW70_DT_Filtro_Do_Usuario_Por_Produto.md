---
content_hash: 308c0abf9e300ea17b4bed58f11d0ca545fb7fabbefbbb2588861e8494def8fe
fetched_at: '2026-06-29T00:06:20.742302+00:00'
page_id: '223154146'
product: rm
source: tdn-rm
title: TTVW70_DT_Filtro_Do_Usuario_Por_Produto
type: documentation
url: https://tdn.totvs.com/display/LRM/TTVW70_DT_Filtro_Do_Usuario_Por_Produto
version: 1
---

# FILTRO DO USUÁRIO POR PRODUTO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Filtro do usuário por produto* |
| **Situação/Requisito:** | O filtro do perfil do RMLabore, está interferindo no produto RMChronus. Considere que o usuário do RMLabore, não tem um filtro por usuário, mas tem um filtro por perfil para acesso ao cadastro do funcionário.  O usuário ao acessar o RMChronus no cadastro do funcionário, o sistema retorna todos os funcionários da coligada de todas as filiais. Porém só me permite editar o cadastro do funcionário que está parametrizado no filtro do perfil. |
| **Solução/Implementação:** | Realizado uma alteração para considerar o perfil do sistema chronus, da mesma forma que é realizado ao acessar a tela de funcionários. |
| **Chamados relacionados:** | TTVW70 |
| **Versões/Release:** | *12\_1\_9* |

divs
