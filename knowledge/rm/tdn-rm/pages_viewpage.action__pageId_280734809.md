---
content_hash: e8386e05ca1128a2d77a8789d7c383f049661388a6de49267cef8560d6692c36
fetched_at: '2026-06-29T00:08:35.442832+00:00'
page_id: '280734809'
product: rm
source: tdn-rm
title: DT Alteração de Natureza de Batidas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=280734809
version: 111
---

# ALTERAÇÃO DE NATUREZA DE BATIDAS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **RMSegmento:** | Construção e Projetos |
| **Módulo:** | Automação de Ponto |
| **Função:** | Alteração da natureza de batidas pelo aplicativo e também pelo portal |
| **Situação/Requisito:** | Em algumas situações é necessário informar que algumas batidas não tenham sua natureza alterada durante o processo de acerto de natureza. Esse processo já foi implementado, porém a natureza só permaneceria fixa caso a natureza dela fosse alterada através do espelho do funcionário. O novo requisito consiste em marcar a natureza da batida quando o gestor/supervisor incluir uma batida pelo Portal RH/ Aplicativo, não alterando assim a natureza da batida para futuros acertos de natureza (Importação de batidas, Edição de batidas, entre outros). |
| **Solução/Implementação:** | Parametrização **1)** Habilitar o parâmetro: Configurações >> Parametrizador >> Iniciais >> Importação >> "Considera a alteração de natureza da batida no processo de acerto de batidas"   Inserção de batidas pelo aplicativo **1)** Inserir uma batida através do aplicativo dentro do espelho do funcionário:        **2)** Consultando a tabela **ABATFUN**, o campo **NATUREZAALTERADA** também foi alterado ao inserir a batida:        **3)** Utilizando a opção "Editar Batidas", ao inserir uma batida, o campo NATUREZAALTERADA também é alterado:        **4)** Consultando a tabela **ABATFUN**, o campo **NATUREZAALTERADA** também foi alterado ao inserir a batida:   Inserção de batidas pelo portal **1)** Inserir uma batida através do aplicativo dentro do espelho do funcionário:        **2)** Consultando a tabela **ABATFUN**, o campo **NATUREZAALTERADA** também foi alterado ao inserir a batida: |
| **Conversores e Parâmetros:** | Conversores: N/A  Parâmetros: Configurações >> Parametrizador >> Iniciais >> Importação >> "Considera a alteração de natureza da batida no processo de acerto de batidas" |
| **Tickets relacionados:** | [PONTO01-614](http://jiraproducao.totvs.com.br/browse/PONTO01-614) |
| **Requisito:** | Versão 12.1.16 (Último patch) e 12.1.17 |

divs
