---
content_hash: 6ba000f159a09d72a5f01edb01ab6801074125299fd8c45691be2677e5b7222a
fetched_at: '2026-06-29T00:06:04.713848+00:00'
page_id: '200910635'
product: rm
source: tdn-rm
title: TTBFTW_DT_Avisos_Automaticos
type: documentation
url: https://tdn.totvs.com/display/LRM/TTBFTW_DT_Avisos_Automaticos
version: 2
---

# AVISOS AUTOMÁTICOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Avisos Automáticos* |
| **Situação/Requisito:** | *Ao enviar avisos automáticos agrupados por chefes e selecionando Tipo de Montagem Fórmulas, ocorre erro.* |
| **Solução/Implementação:** | *Ajuste em rotina de avisos automáticos quando *agrupados por chefes e selecionando Tipo de Montagem Fórmulas. Foi adicionada validação de retorno da sentença sql para não acessar linhas inexistentes. Foi ajustado verificação de controle de agrupamento por chefes afim de recuperar os e-mails necessários.** |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTBFTW* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.41* |
