---
content_hash: facdb5cef1bec425e0481fa7299dc95624b3eee79153bbe70bf4bda7c6fa38a8
fetched_at: '2026-06-29T00:08:21.454360+00:00'
page_id: '268825477'
product: rm
source: tdn-rm
title: MRH-215_DT_PAGINA_SUBORDINADOS_PORTAL
type: documentation
url: https://tdn.totvs.com/display/LRM/MRH-215_DT_PAGINA_SUBORDINADOS_PORTAL
version: 118
---

# Listagem de Subordinados - Portal

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Subordinados - Portal RM* |
| **Situação/Requisito:** | *Ao abrir a listagem de subordinados no portal, o carregamento da página era demorado quando havia muitos subordinados devido ao carregamento de muitas informações* |
| **Solução/Implementação:** | *Adicionado um parâmetro no parametrizador para optar por não carregar todos os detalhes já na listagem. Ao acessar o parametrizador do Labore, selecione o RM Portal e selecione um grupo de acesso. O novo parâmetro se encontra na aba de Supervisores. Existe também na página do portal um parâmetro temporário (que é gravado somente durante o acesso ao portal) que permite alterar a exibição ou não dos dados na página.* |
| **Chamados relacionados:** | MRH-215 |
| **Requisito (ISSUE):** | MRH-215 |

divs
