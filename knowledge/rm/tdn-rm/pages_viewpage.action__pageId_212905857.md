---
content_hash: 70f0c412931c69db3ead7c0f6de912aa4cf4f8351ca0eb676b60cfb77a5db605
fetched_at: '2026-06-29T00:06:17.180383+00:00'
page_id: '212905857'
product: rm
source: tdn-rm
title: 'RMFIS00002_Origem dos dados: Retenção RM Liber'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=212905857
version: 131
---

# 

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Fiscal |
| **Versões:** | 12.1.12.x, 12.1.13.x e 12.1.14.x |
| **Ocorrência:** | Dirf - Origem dos dados: Retenção RM Liber |
| **Ambiente:** |  |
| **Passo a passo:** | Para geração da DIRF selecionando como “Origem dos Dados: Retenção RM Liber” na tela de geração da rotina, o sistema irá verificar as seguintes informações:  Serão selecionados:   * Lançamentos cuja Data de Apuração do Lançamento (Data da Baixa, Vencimento ou Emissão) esteja dentro do Ano de Retenção informado na tela de geração da Rotina. * Lançamentos referentes a notas Recebidas, ou seja Lançamentos de Entrada, cujo Fornecedor possua retenção do Tributo em pelo menos um dos meses do Ano de Retenção. Obrigações Principais | Entrada * Lançamentos cuja Natureza de Operação seja não fiscal, ou Natureza de Operação vinculada ao Lançamento deve começar com “1.933 - Aquisição de Serviço tributado pelo ISS dentro do Estado” ou “2.933 - Aquisição de Serviço tributado pelo ISS fora do Estado”        * Lançamentos que não estejam cancelados, extemporâneos ou estornados.  * Lançamentos em que o Fornecedor seja do tipo “Empresa” ou “Cliente”.  * Lançamentos que não sejam Notas Fiscais que acobertam Cupom Fiscal  * Lançamentos que não possuam o Tributo INSS (“TIPOTRIBFISC” diferente de “16”).     Caso, na tela de geração da rotina, o usuário marque a opção:   * “**IRRF”,** o sistema selecionará Lançamentos que possuam o tributo “IRRF” (“TIPOTRIBFISC” igual a “5”).  * **“IRRF PJ”,** o sistema selecionará Lançamentos que possuam o tributo “IRRFPJ” (“TIPOTRIBFISC” igual a “22”).  * “**COSIRF”,** o sistema selecionará Lançamentos que possuam o tributo “COSIRF” (“TIPOTRIBFISC” igual a “26”).  * **“Contribuições Sociais”,** o sistema selecionará Lançamentos que possuam o tributo “CSLL RF” ou “PIS RF” ou “COF RF” ou “CSRF” (“TIPOTRIBFISC” igual a “18” ou “19” ou “20” ou “21”).     \* O tributo destacado no lançamento fiscal deve conter: base, alíquota, valor e código de receita preenchidos.    **IMPORTANTE**: Os lançamentos a serem selecionados estarão agrupados por Mês, CPF/CNPJ do Beneficiário e Código de Retenção. |
| **Observações:** |  |

divs
