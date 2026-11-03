---
content_hash: 9dcab1c3d35a239181c3bc9d3d9e6d3068178ba63596e7e711ec1985e109a5e5
fetched_at: '2026-06-29T00:06:18.764491+00:00'
page_id: '219686573'
product: rm
source: tdn-rm
title: 'RMFIS00003_Origem dos dados: Retenção RM Fluxus'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=219686573
version: 131
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Fiscal |
| **Versões:** | 12.1.12.x, 12.1.13.x e 12.1.14.x |
| **Ocorrência:** | Dirf - Origem dos dados: Retenção RM Fluxus |
| **Ambiente:** |  |
| **Passo a passo:** | Para geração da DIRF selecionando como “Origem dos Dados: Retenção RM Fluxus” na tela de geração da rotina, o sistema irá verificar as seguintes informações:    1. Lançamentos e Rendimentos em que houve retenção do IRRF para Fornecedor Pessoa Física:  * Lançamentos cujo Cli/For seja pessoa física; * Lançamentos cujo Estado informado na aba Endereço do Cadastro do Cli\For seja nacional; (Para confirmar se o Estado é nacional acesse o cadastro do Estado vinculado ao Cli\For e verifique se o flag "Nacional" está marcado); * Baixas e\ou Lançamentos que não tenham\estejam sido Canceladas; * Lançamentos cujo Tipo de Documento seja “Gerador de IRRF” ou “Gerador de IRRF e INSS”; * Lançamentos em que tenha sido gerada a Guia de recolhimento do imposto, Faturados (**somente para Lançamentos).**         2.  Lançamentos em que houve retenção ou que possuam o IRRF para Fornecedor Pessoa Jurídica:   * Somente serão selecionados os Lançamentos cujo Tipo de Documento seja “Gerador de IRRF” ou “Gerador de IRRF e INSS”; * Lançamentos que tenham sido Baixados ou Baixados Parcialmente, no caso de lançamentos que tiveram retenção do imposto. No caso de lançamentos que possuam o Tributo e ainda não houve a retenção, os mesmos devem estar em aberto * Lançamentos que não estejam cancelados. * Lançamentos em que tenha sido gerada a Guia de recolhimento do imposto, Faturados.        3.  Lançamentos em que houve retenção das Contribuições, cumulatividade do Imposto ou imposto não foi retido.   * Somente serão selecionados os Lançamentos que tenham sido gerados com a Classificação do Lançamento igual a “Pis RF”, “Cofins RF”, “Csll RF” ou “CSRF” * Lançamentos Baixados; * Lançamentos que não estejam cancelados; * Lançamentos que tenham sido Baixados ou Baixados Parcialmente (**Somente para rendimentos em que houve a cumulatividade do imposto)** * Lançamentos que não foram Faturados **(Somente quando o imposto não for retido)**     4.  Lançamentos de Rendimentos pagos a residentes ou domiciliados no exterior  Os lançamentos de Rendimentos pagos a residentes ou domiciliados no exterior serão controlados exclusivamente pelo RM Liber.   * Somente serão selecionados os Lançamentos que no ato da Baixa acumularam valor para o Tributo “IRRF Importação” * Lançamentos que não estejam\sejam cancelados, extemporâneos, estornados; * Lançamentos em que o Fornecedor seja do tipo “Empresa” ou “Cliente” * Lançamentos que não tenham sejam Notas Fiscais que acobertam Cupom Fiscal * Lançamentos que possuam o Tributo IRRF Importação |
| **Observações:** |  |

divs
