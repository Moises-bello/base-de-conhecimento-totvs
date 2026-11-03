---
content_hash: 911fc3d3e0b7dd55015b8db56e078ad0ceac234506900ed2ea675756c30abf64
fetched_at: '2026-06-29T00:10:12.299890+00:00'
page_id: '454433220'
product: rm
source: tdn-rm
title: 4878683 FISCAL01-7760 Gerador de Saídas - RMD Geração Valor Contábil Incorreto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=454433220
version: 1
---

# RMD SP

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Gerador de Saídas |
| **Situação/Requisito:** | A geração do valor do Campo 08 –Dedução do Registro 07, não pode ser baseado nos Lançamentos Fiscais Referenciados- Tipo Dedução. Pois no lançamento de Entrada não temos Lançamento referenciado para Dedução. **Alteração:**   * No Registro 07- Campo 07 (Valor total dos produtos) = Será a soma do Valor Contábil de Todos as Situações Tributárias. Caso tenha alguma Situação Tributária compatível com seleção de dados daRotina. * No Registro 07- Campo 08 (Valor a ser alocado para deduções) = A soma do Valor Contábil da Situação Tributária, dos Lançamentos de Entrada cuja a Natureza (CFOP) associado, esteja com o Campo"Classificação Operações Construção Civil" - na Pasta "Dados C.Civil", parametrizado. * Seleção de Dados: Esta seleção não faz sentido. Sugestão retirar. - Selecionar somente Lançamentos Fiscais que tenho Projeto associado "Situação Tributária – Sub Pasta Prestação de Serviço" |
| **Solução/Implementação:** | Alteração da geração da RMD SP:  **Seleção de Dados:** Selecionar somente Lançamentos Fiscais Entrada que tenha Projeto associado  "Situação Tributária – Sub Pasta Prestação de Serviço".  Registro 7 **Campo 7:** soma o Valor Contábil de todos as Situações Tributárias, de acordo com a Seleção de Dados, agrupando pelo DocIni **Campo 8:** soma o Valor Contábil de todos as Situações Tributárias, para Lançamentos de Entrada cuja a Natureza (CFOP), esteja com o Campo "Classificação Operações Construção Civil" - na Pasta "Dados C.Civil", parametrizado e que tenha um Projeto associado.  Registro 9 **Campo 3:** soma de todos os *campos 7* do Registro 7. **Campo 4:** soma de todos os *campos 8* do Registro 7. |
