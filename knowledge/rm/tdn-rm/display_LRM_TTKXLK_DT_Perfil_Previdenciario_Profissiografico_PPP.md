---
content_hash: 744e46aee1eb35cce404503d1b5baa11914649ea879d56ecc45fae062c4d249e
fetched_at: '2026-06-29T00:06:18.472410+00:00'
page_id: '219119818'
product: rm
source: tdn-rm
title: TTKXLK_DT_Perfil_Previdenciario_Profissiografico_PPP
type: documentation
url: https://tdn.totvs.com/display/LRM/TTKXLK_DT_Perfil_Previdenciario_Profissiografico_PPP
version: 1
---

# PPP - PERFIL PROFISSIOGRÁFICO PREVIDENCIÁRIO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Segurança e Saúde Ocupacional |
| **Função:** | Relatório do Perfil Profissiográfico Previdenciário - PPP |
| **Situação/Requisito:** | Ao realizar a geração do relatório PPP foram observadas as seguintes inconsistências   * Cabeçalho:  + Instrução Normativa do título do relatório está obsoleta.  * Campo 13:  + Datas incorretas quando da utilização de Tomadores de Serviço.  * Campo 15:  + Quebra de datas incorretas quando o passivo é Local de Trabalho, em relação às datas dos empréstimos de EPC's. + Dados de CA e Eficácia para empréstimos de EPC's. |
| **Solução/Implementação:** | Ajustes nos dados extraídos pelo relatório do PPP. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TTKXLK, TTIDFM, TTROJE e TTJC29 |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.42* |
