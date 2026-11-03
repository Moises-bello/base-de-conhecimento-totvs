---
content_hash: 1a0cea293de268c1fcfec34870b0e42730356d8c73dbd40decfc524f4c88d8fa
fetched_at: '2026-06-29T00:08:15.694833+00:00'
page_id: '244921104'
product: rm
source: tdn-rm
title: TUJRTI_Ajustar_Valores_Crédito_Adiantamento_Vínculo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244921104
version: 113
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Gestão Financeira* |
| **Função:** | *Ajustar Valores do Crédito de Adiantamento para Vínculo* |
| **Situação/Requisito:** | *Na revitalização do vínculo é necessário ajustar o valor original dos créditos de adiantamento presente na base de dados* |
| **Solução/Implementação:** | *Na baixa do lançamento de adiantamento com retenção, o sistema gera o lançamento de crédito de adiantamento com o valor original constituído pela soma do valor líquido mais o valor das retenções do lançamento de adiantamento.*  *A partir desta versão, o valor original do lançamento de crédito de adiantamento, gerado pela baixa do lançamento de adiantamento com retenção, será composto somente pelo valor líquido do lançamento de adiantamento.*  *Desta forma, este processo tem como objetivo, percorrer todos os lançamentos de crédito de adiantamento gerados pela baixa do lançamento de adiantamento com retenção, para ajustar o seu valor original e consequentemente o seu valor vinculado, caso o lançamento esteja vinculado.*  *Vale ressaltar a importância da execução do processo "Ajustar Valor Baixado em Lançamentos Vinculados" disponível no menu "Utilitários -> Ajustes de Base"*  *Sabia mais:* |
| **Conversores e Parâmetros:** | *12.1.13* |
| **Chamados relacionados:** | *TUJRTI* |
| **Requisito (ISSUE):** | *FINTRF000161* |

divs
