---
content_hash: 62c6afff756072d86820933c57815ef2aae0d1744056b268a5c1465339b8cf97
fetched_at: '2026-06-29T00:08:23.300738+00:00'
page_id: '270075188'
product: rm
source: tdn-rm
title: MRH-3103_DT_Ocorrencias_De_Acidente_De_Trabalho
type: documentation
url: https://tdn.totvs.com/display/LRM/MRH-3103_DT_Ocorrencias_De_Acidente_De_Trabalho
version: 110
---

# OCORRÊNCIAS DE ACIDENTE DE TRABALHO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Segurança e Saúde Ocupacional |
| **Função:** | Ocorrências de Acidente de Trabalho |
| **Situação/Requisito:** | Ao incluir uma nova situação geradora, o sistema não apresenta a mesma para ser selecionado no cadastro de CAT (Código situação geradora) ao menos que seja preenchido o campo "Cód. ESocial" dentro do cadastro da fonte geradora. |
| **Solução/Implementação:** | Criado checkbox no cadastro da CAT para que se consiga associar uma fonte geradora sem o campo ESocial preenchido. Este campo é provisório e ficará na tela até que os novos scripts do ESocial sejam liberados.  Este campo terá a seguinte descrição: Considerar Fonte Geradora sem Cód ESocial.  \* Se o mesmo estiver marcado listará também as fontes geradoras que estão com o campo "Cód. ESocial" em branco.  \* Se estiver desmarcado (default) listará apenas os cadastros que estão com o campo "Cód. ESocial" preenchidos.  Importante salientar que este campo é apenas provisório e o seu valor não será gravado no banco de dados. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | MRH-3103 |
| **Requisito (ISSUE):** |  |

divs
