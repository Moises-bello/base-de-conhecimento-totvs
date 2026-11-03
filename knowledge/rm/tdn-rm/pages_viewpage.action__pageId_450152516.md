---
content_hash: 33331e4d2823ba3f5010af4ffc18610e43d61b643a3c134cabcd26f6de5c1c5d
fetched_at: '2026-06-29T00:09:55.799753+00:00'
page_id: '450152516'
product: rm
source: tdn-rm
title: 4413640 FISCAL01-7581 DT EFD ICMS\IPI Campo desconto condicional não está sendo
  carregado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=450152516
version: 1
---

# EFD ICMS\IPI

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Geração do Arquivo EFD ICMS\IPI |
| **Situação/Requisito:** | * O campo 15 do C100 não leva os valores da soma do Desconto Condicional + ICMS Desonerado de dois itens no lançamento,   ou seja, quando há dois itens, leva a soma do Desconto Condicional + ICMS Desonerado apenas de um item.   * Os campos 12 do C100 e 5 do C190 estão divergentes quando há operação com Desconto Condicional e   ICMS Desonerado (operação para a área Suframada). |
| **Solução/Implementação:** | Ajustes na EFD ICMS/IPI   * No registro C100 o campo (15)VL\_ABAT\_NT será totalizado com o somatório do Abatimento do ICMS e Valor do ICMS Desonerado de todas as parcelas do lançamento fiscal. * No registro C190 o campo (09)VL\_OPR será subtraído o Desconto Condicional e somado a Despesa Condicional. |
| **Requisito:** | FIS000251 |
