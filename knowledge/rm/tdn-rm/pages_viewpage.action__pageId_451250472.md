---
content_hash: 608ba9bca30b8a87f1ec0997b7163af7fb01070e609bec5a1ca2d9d2bdc116c3
fetched_at: '2026-06-29T00:09:58.081610+00:00'
page_id: '451250472'
product: rm
source: tdn-rm
title: 4798354 FOPCALCULO01-5972 Base de INSS - Diferença de 13 salário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=451250472
version: 1
---

# Diferença de 13º Salário

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Plataforma RH |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Diferença de 13º Salário |
| **Situação/Requisito:** | No processo de diferença de 13º salário, devido ao governo não aceitar Sefip de 13º em janeiro o valor referente a diferença de INSS 13º é desconsiderada. Assim, em janeiro apenas é considerado o INSS de folha calculado através do código de cálculo 3 tendo como base o provento da diferença de 13º salário.  Porém, atualmente, para esse processo de diferença de 13º salário, o sistema ao recalcular o envelope de 13º referente a dezembro com base nos novos valores, ele recalcula o código de cálculo 49 utilizando o valor recalculado de INSS 13º para abater na base de IRRF 13º, sendo que deveria considerar o valor original de INSS 13º que foi calculado em dezembro. |
| **Solução/Implementação:** | Foi criado o parâmetro 'Diferença de IRRF 13º em janeiro não abate diferença de INSS 13º' em "Configurações | Parametrizador | 13º Salário | Cálculo" o qual deverá ser marcado para que mantenha o valor original do código de cálculo 103 quando lançada diferença de 13º salário em janeiro. |
| **Tickets relacionados:** | 4798354 |
