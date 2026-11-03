---
content_hash: 4fe15b4867a03134032c11a01270c717f2ffe9c73a4a55fa154ac9d17bc9aed4
fetched_at: '2026-06-29T00:08:58.424139+00:00'
page_id: '359475330'
product: rm
source: tdn-rm
title: RMFIS00004_REINF R-2030 / R-2040 – Recursos Recebidos/Repassados por Associação
  Desportiva
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=359475330
version: 22
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Fiscal x TAF Totvs Automação Fiscal |
| **Versões:** | 12.1.18 |
| **Ocorrência:** | Eventos R-2030 / R-2040 – Recursos Recebidos/Repassados por Associação Desportiva. |
| **Ambiente:** |  |
| **Passo a passo:** | **R-2030 - Recursos Recebido por Associação Desportiva**  Fundamentado no [Art. 22, §§ 6º, 9º ao 11 da Lei nº 8.212/91](http://www.planalto.gov.br/ccivil_03/leis/l8212cons.htm), este evento deve ser enviado pelo tomador de serviços onde houve recursos recebidos por Associação Desportiva, que são os seguintes contribuintes:   * Informação prestada pela associação desportiva; * Totalizada por empresa que repassou o recurso; * Patrocínio; * Licenciamento de marcas e símbolos; * Publicidade; * Propaganda; * Transmissão de espetáculos; * Discriminando a base e a retenção sofrida.     **R-2040 -** **Recursos Repassados por Associação Desportiva**  Fundamentado no [Art. 22, §§ 6º, 9º ao 11 da Lei nº 8.212/91](http://www.planalto.gov.br/ccivil_03/leis/l8212cons.htm), este evento deve ser enviado pelo quando houver recursos repassados para Associação Desportiva de Informação prestada pelas seguintes empresas:   * Patrocínio; * Licenciamento de marcas e símbolos; * Publicidade; * Propaganda; * Transmissão de espetáculos; * Discriminando a base e a retenção sofrida.   Ambos os registros se tratam de eventos periódico. A origem dos dados para geração desses registro é do TOTVS Gestão de Estoque, Compra e Faturamento. Serão selecionados os movimentos cuja a parametrização "Movimentos de Repasse EFD Reinf" da Etapa 61 - Fiscal - Dados Fiscais, estiver marcada.    As informações, tanto do R-2030 como do R-2040, são enviadas para o TAF através do Registro T154 e "filhos" do Layout TAF.   121º Passo1º Passo Para habilitar o parâmetro basta acessar o TOTVS Gestão de Estoque, Compra e Faturamento. Acesse o menu Ambiente | Parâmetros | Gestão de Estoque, Compra e Faturamento | edite o tipo de movimento e acesse a etapa Etapa 61 - Fiscal - Dados Fiscais   22º Passo Também será consistido o campo IND\_ASSOC\_DESPORT (T001) selecionado na filial, que será gerado com valor "1 - Sim" se a filial estiver parametrizada como Associação desportiva.    **Observação**: O registro T003, será gerado com valor fixo "1 - Sim" para os participantes cuja origem for o T154. 33º Passo3º Passo Realizar a integração conforme documento:   * [Integração RM x TAF](http://tdn.totvs.com/pages/viewpage.action?pageId=336404337)   Após integração realizar a apuração e transmissão seguindo a partir do 6º Passo do documento abaixo:   * [RMFIS00002\_REINF R-1000 – Informações do Contribuinte](http://tdn.totvs.com/pages/viewpage.action?pageId=346500860) |
| **Observações:** |  |
