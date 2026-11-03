---
content_hash: d13e5c3fff5b172c69370e15cab497e2f291380edfc53804535086ee457e99ba
fetched_at: '2026-06-29T00:06:10.383262+00:00'
page_id: '203762522'
product: rm
source: tdn-rm
title: DT_Importação_Exportação_Pesquisa_Salarial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=203762522
version: 5
---

# IMPORTAÇÃO E EXPORTAÇÃO DE PESQUISA SALARIAL

## Características do Requisito

  

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **TOTVS Gestão de Pessoas** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Valorização* | *Importação e exportação de pesquisa salarial* | |
| **Versões/Release:** | *12.1.8* |

## Descrição

Importar ou Exportar pesquisas salarias e suas Respectivas Medidas Estatísticas.

## Procedimento para Utilização

Para importar pesquisas salarias vá em **Configurações / Importação** / **Pesquisas Salariais** no menu da MDI. Ao ser clicado, virá o processo de importação;

 Para e execução do processo, o usuário deve fornecer um arquivo *xml* de importação, este arquivo tem que estar formatado de acordo com o anexo *schema.xml*;  
       
    
    
  Após executar o processo, os registros importados deverão estar disponíveis nos cadastros de "Pesquisa Salarial" e no anexo "Medidas Estatísticas".

 Para exportar as pesquisas salariais vá em  "**Configurações / Exportação / Pesquisas Salariais**'' no menu da MDI, que ao ser clicado, aparecerá o processo de exportação;  
  
   
  
  Ao executar o processo, o usuário poderá informar um filtro de "Pesquisa Salarial" e obrigatoriamente deverá informar um diretório de destino;  
  
    
  
   
  Ao ser finalizado o processo, irá ser gerado um arquivo com o nome no formato de *VPESQUISASALARIALYYYYMMDDHHMMSS.xml* contendo os dados dos registros exportados no diretório informado pelo usuário;  
  O formato do arquivo será o mesmo utilizado no processo de importação.
