---
content_hash: 91d6bfe59c224d710a84246316e88606eca6d837a1f2d2667f2eb791ec5c08dc
fetched_at: '2026-06-29T00:11:31.984916+00:00'
page_id: '741847645'
product: rm
source: tdn-rm
title: CERC - Contrato X Cliente
type: documentation
url: https://tdn.totvs.com/display/LRM/CERC+-+Contrato+X+Cliente
version: 7
---

Para que o Processo [Integrar Registradora](https://tdn.totvs.com/display/LRM/Empreendimentos+-+Processos+-+Integrar+com+Registradora) seja executado com sucesso quando a Registradora de Recebíveis for a CERC, o TCGI deverá integrar também os dados de todos os **Clientes**/[Compradores](https://tdn.totvs.com/display/LRM/Contratos+de+Venda+-+Dados+Gerais+-+Compradores) que estão relacionados no  **Contratos**da Venda, que têm percentual de participação maior que zero.

|  |  |  |  |
| --- | --- | --- | --- |
| **CAMPO CERC-IM004C - CONTRATO X CLIENTE** | **CAMPO API - VINCULOMUTUARIOCONTRATO** | **CAMPO RM** | **DESCRIÇÃO** |
| Referência Externa - Projeto | referenciaExternaProjeto | Código da Coligada + Empreendimento | É formado com a junção dos campos **[Código da Coligada](https://tdn.totvs.com/display/LRM/Coligada)** (acrescido de zeros à esquerda, para ocupar 4 posições) + **[Empreendimento](https://tdn.totvs.com/pages/viewpage.action?pageId=435105154)** que é o identificador desta entidade (que é preenchido automaticamente pelo TCGI). |
| Referência Externa - Contrato | referenciaExternaContrato | Código da Coligada + Venda/Aluguel | É formado com a junção dos campos **[Código da Coligada](https://tdn.totvs.com/display/LRM/Coligada)**  + **Venda/Aluguel** da aba [Identificação](https://tdn.totvs.com/pages/viewpage.action?pageId=435105242) do Cadastro de Venda. |
| CPF/CNPJ | cpfCnpj | CPF/CNPJ | É o campo [**CPF/CNPJ**](https://tdn.totvs.com/pages/releaseview.action?pageId=421388786), da aba Identificação do cadastro de Cliente/Fornecedor, que é o [Comprador](https://tdn.totvs.com/display/LRM/Contratos+de+Venda+-+Dados+Gerais+-+Compradores) desta venda. |
| Responsável Financeiro | responsavelFinanceiro | Comprador Principal | É o campo **Comprador Principal**, da tela de cadastro de [Comprador](https://tdn.totvs.com/display/LRM/Contratos+de+Venda+-+Dados+Gerais+-+Compradores). |
| % Atribuído ao Cliente | percentualAtribuidoCliente | Participação | É o campo **Participação**, da tela de cadastro de [Comprador](https://tdn.totvs.com/display/LRM/Contratos+de+Venda+-+Dados+Gerais+-+Compradores).  O TCGI somente irá integrar os Compradores com percentual de Participação maior que zero. |

Após a execução com sucesso do Processo [Integrar Registradora](https://tdn.totvs.com/display/LRM/Empreendimentos+-+Processos+-+Integrar+com+Registradora) o sistema vai abastecer a aba Visão das Registradoras do Mutuário, do Cadastro de Venda, com as informações relativas à esta integração.
