---
content_hash: cf4daa5ad2d44ea37f10dc6c07cbb832f867d7ac0e6ccb0757d0ce86a54b8b54
fetched_at: '2026-06-29T00:08:42.470710+00:00'
page_id: '287073903'
product: rm
source: tdn-rm
title: RMFIS00006_Registro C113
type: documentation
url: https://tdn.totvs.com/display/LRM/RMFIS00006_Registro+C113
version: 3
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Fiscal |
| **Versões:** | 12.X |
| **Ocorrência:** | Geração do Registro C113 |
| **Ambiente:** |  |
| **Passo a passo:** | Para a geração do C113 é necessário parametrizar a natureza de operação conforme tela abaixo:        *Obs.: Com esta parametrização, ativará a aba Referências no lançamento fiscal conforme última tela deste documento.*  Caso o lançamento seja gerado diretamente no Liber, basta preencher os dados nesta aba, caso venha escriturado do RM Nucleus deverá parametrizar conforme dados abaixo.    **Parametrização RM Nucleus**  Acesse o tipo de movimento e vá na Etapa Mov - Outros Dados e marque a opção Usar cópia do movimento por referência e informe o Motivo.    **/**    Na Etapa Fis - Escrituração 1/2 informe o Codigo do Motivo da Referência (Campo utilizado para gerar a Rotina SISIF)        **Ao realizar a escrituração os dados serão carregrados para a aba Referência do lançamento fiscal do RM Liber.** |
| **Observações:** |  |
