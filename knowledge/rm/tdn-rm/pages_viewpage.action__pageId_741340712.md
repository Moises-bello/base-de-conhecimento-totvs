---
content_hash: 6827141f0d78f01790154b2d9ca5608970d3a6369ef651d159b178fe9003c078
fetched_at: '2026-06-29T00:11:31.970185+00:00'
page_id: '741340712'
product: rm
source: tdn-rm
title: CERC - Cliente (Mutuário) - Dados de Contato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=741340712
version: 10
---

Para que o Processo [Integrar Registradora](https://tdn.totvs.com/display/LRM/Empreendimentos+-+Processos+-+Integrar+com+Registradora) seja executado com sucesso quando a Registradora de Recebíveis for a CERC, o TCGI deverá integrar também os **Dados de Contato do Cliente/Mutuário** do contrato de vendas.

|  |  |  |  |
| --- | --- | --- | --- |
| **CERC-IM004B - DADOS DE CONTATO** | **CAMPO API - MUTUARIO/DADOS CONTATO** | **CAMPO RM** | **DESCRIÇÃO** |
| Tipo de Operação | tipoOperacao | Ação | O Tipo de Operação a ser realizado na integração dos dados coma  CERC é definido pelo campo de **Ação** da tela do Processo [Integrar Registradora](https://tdn.totvs.com/display/LRM/Empreendimentos+-+Processos+-+Integrar+com+Registradora) |
| Identificador do  Contato | ``` idContato ``` | Cliente/Fornecedor | É o campo [**Cliente/Fornecedor**](https://tdn.totvs.com/pages/releaseview.action?pageId=421388786), da aba Identificação do cadastro de Cliente/Fornecedor. |
| CPF/CNPJ | cpfCnpj | CPF/CNPJ | É o campo [**CPF/CNPJ**](https://tdn.totvs.com/pages/releaseview.action?pageId=421388786), da aba Identificação do cadastro de Cliente/Fornecedor. |

Importante

Caso o Cliente queira informar a tag *Tipo de Contato,* por telefone, para a CERC, o TCGI sempre irá reportar o número cadastrado no campo [**Celular**](https://tdn.totvs.com/pages/releaseview.action?pageId=421388786), da aba Identificação do cadastro de Cliente/Fornecedor.

Após a execução com sucesso do Processo [Integrar Registradora](https://tdn.totvs.com/display/LRM/Empreendimentos+-+Processos+-+Integrar+com+Registradora) o sistema vai abastecer a aba [Visão das Registradoras dos Contratos do Mutuário](https://tdn.totvs.com/pages/viewpage.action?pageId=741835263), do cadastro de Clientes, quando aberto a partir do contexto do TCGI, com as informações relativas à esta integração.
