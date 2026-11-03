---
content_hash: 01724340992a51e5f1f7c48cb6a956abacc022a28143a4f0f7dce6ed30ae1d85
fetched_at: '2026-06-29T00:08:34.682457+00:00'
page_id: '274832566'
product: rm
source: tdn-rm
title: RSP0003_Nenhum_Tipo_de_Movimento_Apresentado_na_Analise_de_Sugestao_do_Ressuprimento
type: documentation
url: https://tdn.totvs.com/display/LRM/RSP0003_Nenhum_Tipo_de_Movimento_Apresentado_na_Analise_de_Sugestao_do_Ressuprimento
version: 1
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão de Estoque, Compras e Faturamento |
| **Versões:** | 11.82 e superiores |
| **Ocorrência:** | Nenhum tipo de movimento é apresentado na análise de sugestão. |
| **Ambiente:** | Ressuprimento - Análise |
| **Passo a passo:** | Ao realizar a Análise de Sugestão do Ressuprimento, nenhum movimento é apresentado no assistente. CAUSA 1- O Tipo de movimento não é de solicitação de compras;  2- A numeração do tipo de movimento não está como mostra;  3- O tipo de movimento não está parametrizado para “Geração de Movimento” na etapa de Estoque - Ressuprimento. SOLUÇÃO 1- Parametrizar o tipo de movimento para ser de Solicitação de Compras. Etapa Compra/Venda - Outros Dados;  2- Definir nos parâmetros do tipo de movimento para ter a numeração como mostra. Etapa Mov - Identificação, campo Edita Numeração.  3- Parametrizar o tipo de movimento na etapa de etapa de Estoque - Ressuprimento para “Geração de Movimento”      **Observação:**  A consulta sql que o sistema utiliza para verificar os movimentos que atendem à parametrização é a seguinte: false SELECT TTMV.CODTMV, TTMV.NOME FROM TITMTMV INNER JOIN TTMV ON (TITMTMV.CODTMV = TTMV.CODTMV AND TITMTMV.CODCOLIGADA = TTMV.CODCOLIGADA) WHERE TITMTMV.CODCOLIGADA = 1 AND TITMTMV.TIPOMOVCOMPRAS = 1 AND TTMV.EDICAONUMEROMOV = 'M' AND TITMTMV.TIPOGESTAOMAT = 1  Desta forma, caso queira verificar de uma forma mais ágil, basta executar diretamente no banco de dados. |
| **Observações:** | Para mais informações:  [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
