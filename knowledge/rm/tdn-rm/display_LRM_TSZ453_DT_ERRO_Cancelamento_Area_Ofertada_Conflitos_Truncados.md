---
content_hash: 9208feec71af4a5feaefdebc333074980787743e7f3cda2aae193dcf271f8a1e
fetched_at: '2026-06-29T00:06:07.138659+00:00'
page_id: '201735523'
product: rm
source: tdn-rm
title: TSZ453_DT_ERRO_Cancelamento_Area_Ofertada_Conflitos_Truncados
type: documentation
url: https://tdn.totvs.com/display/LRM/TSZ453_DT_ERRO_Cancelamento_Area_Ofertada_Conflitos_Truncados
version: 4
---

# CANCELAMENTO DE ÁREA OFERTADA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Processo Seletivo* |
| **Função:** | *Cancelamento de Área Ofertada* |
| **Situação/Requisito:** | *No momento de cancelar uma área ofertada que tenha idioma ou documentos obrigatórios com nomes muito grandes e informar para que os candidatos sejam transferidos para uma área onde não tenha documento ou idioma, ao avançar o sistema exibe uma mensagem informando quais os idiomas ou documentos estão diferentes, porem quando o nome é muito grande a mensagem vem errada.* |
| **Solução/Implementação:** | *Alterado o componente TextBox por RichTextBox para exibir as informações de conflitos. O componente RichTextBox permite exibir uma barra de rolagem de acordo com seu conteúdo.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *11.82.41* |
