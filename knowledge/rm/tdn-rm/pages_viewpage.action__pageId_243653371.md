---
content_hash: 3caf1ae44fd6fe70aada577bcdfa3ebfa69bae6581e8dba93fa3c863d71ebf6d
fetched_at: '2026-06-29T00:08:12.886692+00:00'
page_id: '243653371'
product: rm
source: tdn-rm
title: TVEAPN_DT_Erro_Guia_INSS_Filtro_Específico_Coligada_Autonomos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243653371
version: 117
---

# GERAÇÃO DE GUIA DE INSS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construções e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Geração da Guia de INSS* |
| **Situação/Requisito:** | *O filtro dos parâmetros específicos da coligada na geração da Guia de INSS (GPS) não atende os lançamentos financeiros de autônomos, sendo assim se tiver um lançamento financeiro com INSS de autônomo para uma filial e na geração da GPS informar um filtro que não busque os valores desta filial, o sistema leva estes valores mesmo assim desobedecendo os filtros.* |
| **Solução/Implementação:** | *Adição do parâmetro  *<Inibir geração de guia somente de autônomos (sem funcionários)>* na guia de Integrações do Processo de geração de Guia do INSS.*  *Esta flag definirá se os **autônomos** deverão **ser exibidos** em caso de **não existência de funcionários** na busca do filtro específico aplicado na coligada.*  ***Flag marcada:** Filtro específico por coligada não retorna nenhum funcionário e há autônomos para a filial -> os autônomos não serão carregados.*  ****Flag desmarcada:** Filtro específico por coligada não retorna nenhum funcionário e há autônomos para a filial -> os autônomos serão carregados.** |
| **Chamados relacionados:** | *TVEAPN* |

divs
