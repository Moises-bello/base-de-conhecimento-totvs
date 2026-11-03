---
content_hash: f028a6b4af96d2a5c748087d6667a336b6a6f6a0b20a87d95d55a9e209c6b6be
fetched_at: '2026-06-29T00:09:13.508865+00:00'
page_id: '421366349'
product: rm
source: tdn-rm
title: 3732562 FISCAL01-6640 DT Valor do ICMS-ST desonerado não está sendo calculado
  utilizando o CST 30
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421366349
version: 2
---

# Cadastro de Lançamento Fiscal

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Cadastro de Lançamento Fiscal - Serviço de Tributação |
| **Situação/Requisito:** | Valor do \***ICMSST**\* Desonerado não é carregado para a linha do Tributo \***ICMSST**\* quando utilizado o CST 30 /Tipo ISENTO |
| **Solução/Implementação:** | Em análise feita na situação foi constatado que a desoneração estava sendo calculada indevidamente para o ICMSST e por este motivo o processo sofreu os seguintes ajustes:   * O ICMS desonerado passou a ser calculado somente para o ICMS Normal e não considera mais o CST da natureza. * Se o usuário marcar o parâmetro ICMS DESONERADO que fica na aba DADOS ICMS da regra associada ao CFOP a desoneração será calculada sobre o total do ICMS Isento ou sobre a parte Isenta no caso de redução de base de cálculo. * Ajustado o processo de envio da NF-e que carregava o valor da desoneração do ICMSST. A partir de agora o valor é carregado do tributo ICMS normal mesmo que este seja do tipo Isento. |
| **Requisito:** | FIS000062 |
