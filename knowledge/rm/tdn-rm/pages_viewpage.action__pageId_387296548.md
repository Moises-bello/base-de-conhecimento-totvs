---
content_hash: 838b8e954d60ebe83dd8442b0b488245133b5e2ffd61ebb482d7221c898ab436
fetched_at: '2026-06-29T00:09:08.384153+00:00'
page_id: '387296548'
product: rm
source: tdn-rm
title: 3344977 EDUCACIONAL01-5972 DT Geração de lançamento no processo seletivo contendo
  conta caixa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=387296548
version: 86
---

# PROCESSO SELETIVO - GERAÇÃO DE LANÇAMENTO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Processo Seletivo* |
| **Função:** | *Gerar lançamento da inscrição do candidato* |
| **Situação/Requisito:** | Ao salvar a inscrição de um candidato, o sistema apresentava mensagem de “Chave duplicada”. Ocorria somente se preencher os dados da conta caixa na identificação do processo seletivo e existisse um valor incorreto na coligada da conta caixa da área de interesse. |
| **Solução/Implementação:** | Otimizações realizadas no processo seletivo: - Na visão do cadastro da Área de interesse ofertada do processo seletivo foram acrescentadas as colunas “Coligada da conta caixa” e “Conta/caixa”. Estas mesmas colunas serão listadas ao preencher o campo “Conta/Caixa” do processo seletivo. - Para melhor entendimento, foi otimizado a mensagem da geração de lançamento, nos casos em que ocorre erro, para identificar qual a causa. - Ao salvar o processo seletivo, caso seja gerado lançamento financeiro, a conta caixa e a coligada da conta caixa deverão ser pesquisadas ambas no mesmo local, ou seja, na área de interesse ofertada ou na identificação do processo seletivo, nesta ordem. |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
