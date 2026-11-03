---
content_hash: 89780af60a4e8a35f0c05567ab648a83f8f04f47c12de821952ceca6c8898807
fetched_at: '2026-06-29T00:06:20.738978+00:00'
page_id: '223154054'
product: rm
source: tdn-rm
title: TTOTMU_DT_Filtro_Do_Usuario_Por_Produto
type: documentation
url: https://tdn.totvs.com/display/LRM/TTOTMU_DT_Filtro_Do_Usuario_Por_Produto
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
| **Chamados relacionados:** | TTOTMU |
| **Versões/Release:** | *11.82.43* |

divs
