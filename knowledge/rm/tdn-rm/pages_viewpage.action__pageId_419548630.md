---
content_hash: fb5c1ddb1576104ca464fa815b817bd3faca4e4f98d952a28a9b24a24f5933ba
fetched_at: '2026-06-29T00:09:13.369541+00:00'
page_id: '419548630'
product: rm
source: tdn-rm
title: 3921068 FISCAL01-6598 DT  Integração RMxTAF - Campo Ente Federativo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=419548630
version: 4
---

# Integração RMxTAF

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Geração de Registros RMxTAF |
| **Situação/Requisito:** | Na geração da REINF no registro T001 o campo 17 está sendo preenchido mesmo a filial não sendo órgão público. |
| **Solução/Implementação:** | A expressão, referente ao campo 17 (IDEEFR), foi alterada no layout do TAF, que agora verifica se foi parametrizado um valor no campo CPNJ do Ente Federativo Responsável  para que gere o valor correto no campo 17, do bloco T001. Sendo:   * 1 - CNPJ da ERFB válido. * 2 - CNPJ da ERFB inválido ou não informado.   Após essa alteração, ao realizar o processo de Geração de Registro - TAF Fiscal  foi selecionado o  layout TAF. A filial a ser realizado o processo foi  “TOTVS SA REINF teste”, e não foi parametrizado um valor para o campo CPNJ do Ente Federativo Responsável.  No bloco T001, campo 17, foi gravado o valor 2 (2 - CNPJ da ERFB inválido), valor correto.  No cadastro da filial “TOTVS SA REINF teste”,  foi parametrizado o valor “81399815000197” para o campo CPNJ do Ente Federativo Responsável. No bloco T001, campo 17, foi gravado o valor 1 (2 - CNPJ da ERFB válido), valor correto.  No cadastro da filial “TOTVS SA REINF teste”,  foi apagado o valor “81399815000197” do campo CPNJ do Ente Federativo Responsável. No bloco T001, campo 17, foi gravado o valor 2 (2 - CNPJ da ERFB inválido), valor correto.  Obs: Na geração do bloco T001, a flag “Filial é Órgão Público”, não é utilizada. |
| **Requisito:** | FIS000408 |
