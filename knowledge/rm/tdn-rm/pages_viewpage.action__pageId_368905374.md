---
content_hash: 731eaccea8cb4fe4b441f9102bbd6a012c201dadb5934d260f919af0ac065d05
fetched_at: '2026-06-29T00:09:00.490549+00:00'
page_id: '368905374'
product: rm
source: tdn-rm
title: RMFIS00008_Melhoria integração RM x TAF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=368905374
version: 3
---

# Seleção de registros pertinentes a REINF.

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Fiscal |
| **Versões:** | 12.1.18 |
| **Ocorrência:** | Melhoria na seleção dos registros de Integração RM x TAF. |
| **Ambiente:** | CorporeRM |
| **Passo a passo:** | Este documento tem como objetivo demonstrar a melhoria realizada no processo de integração RM x TAF de forma que será possível selecionar apenas os registros de Integração pertinentes a REINF.    **Versões do sistema:**  Implementação disponível a partir dos Patches **12.1.18.225, 12.1.19.185 e 12.1.20.126** ou superior, disponível no [Portal do Cliente - área de download.](https://suporte.totvs.com/portal/p/10098/download#company/)  Atualizar o Layout da Rotina do TAF – Data do layout 05/06/2018 ou superior. Disponível na pasta objetos gerenciais da Biblioteca.    **Implementação:**  Inclusão do Parâmetro **"Gerar somente registros pertinentes a rotina REINF"**, este parâmetro será visível na pasta Demais Parâmetros 3.    Se o Parâmetro estiver habilitado serão gerados apenas os registros pertinentes a rotina federal REINF, que atendam as seguintes regras:   * Lançamentos Fiscais que possuam os tributos INSS, ou FUNRURAL ou CPRB informados; * Dados da apuração da CPRB (Bloco P da EFD Contribuições – Período de Apuração); * Movimentos do Nucleus referente associação desportiva.   Observação:  Os registros filhos do Lançamento Fiscal como, por exemplo, participante (T003), CFOP(T009) e Itens (T007) também serão gerados. |
| **Observações:** |  |
