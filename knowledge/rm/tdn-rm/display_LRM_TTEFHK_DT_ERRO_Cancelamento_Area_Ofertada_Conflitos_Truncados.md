---
content_hash: 235355b6548c47e3a21e2c4d15c24bf5e2278d80678fb99a9d52015d4524b103
fetched_at: '2026-06-29T00:06:07.153756+00:00'
page_id: '201735547'
product: rm
source: tdn-rm
title: TTEFHK_DT_ERRO_Cancelamento_Area_Ofertada_Conflitos_Truncados
type: documentation
url: https://tdn.totvs.com/display/LRM/TTEFHK_DT_ERRO_Cancelamento_Area_Ofertada_Conflitos_Truncados
version: 2
---

# CANCELAMENTO DE ÁREA OFERTADA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Processo Seletivo* |
| **Função:** | *Cancelamento de Área Ofertada* |
| **Situação/Requisito:** | *No momento de cancelar uma área ofertada que tenha idioma ou documentos obrigatórios com nomes muito grandes e informar para que os candidatos sejam transferidos para uma área onde não tenha documento ou idioma, ao avançar o sistema exibe uma mensagem informando quais os idiomas ou documentos estão diferentes, porem quando o nome é muito grande a mensagem vem errada.* |
| **Solução/Implementação:** | *Trocado o componente TextBox por RichTextBox para exibir as informações de conflitos. O componente RichTextBox permite exibir uma barra de rolamento de acordo com seu conteúdo.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *12.1.8* |
