---
content_hash: 4afb28fb577dc1273c0ad0c7a94e253431c015a8306c29efd4c304d3f6dba171
fetched_at: '2026-06-29T00:11:31.964336+00:00'
page_id: '741337001'
product: rm
source: tdn-rm
title: CERC - Cliente (Mutuário) - Dados Pessoais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=741337001
version: 10
---

Para que o Processo [Integrar Registradora](https://tdn.totvs.com/display/LRM/Empreendimentos+-+Processos+-+Integrar+com+Registradora) seja executado com sucesso quando a Registradora de Recebíveis for a CERC, o TCGI deverá integrar também os **Dados Pessoais do Cliente/Mutuário** do contrato de vendas.

|  |  |  |  |
| --- | --- | --- | --- |
| **CERC-IM004A - DADOS PESSOAIS** | **CAMPO API - MUTUARIO/DADOSPESSOAIS** | **CAMPO RM** | **DESCRIÇÃO** |
| Tipo de Operação | tipoOperacao | Ação | O Tipo de Operação a ser realizado na integração dos dados coma  CERC é definido pelo campo de **Ação** da tela do Processo [Integrar Registradora](https://tdn.totvs.com/display/LRM/Empreendimentos+-+Processos+-+Integrar+com+Registradora) |
| Tipo de Pessoa | ``` tipoPessoa ``` | Categoria | É o campo [**Categoria**](https://tdn.totvs.com/pages/releaseview.action?pageId=421388786), da aba Identificação do cadastro de Cliente/Fornecedor. |
| Nome/Razão Social | nomeRazaoSocial | Nome Fantasia/Social | É o campo [**Nome Fantasia/Social**](https://tdn.totvs.com/pages/releaseview.action?pageId=421388786), da aba Identificação do cadastro de Cliente/Fornecedor. |
| CPF/CNPJ | cpfCnpj | CPF/CNPJ | É o campo [**CPF/CNPJ**](https://tdn.totvs.com/pages/releaseview.action?pageId=421388786), da aba Identificação do cadastro de Cliente/Fornecedor, que é o [Comprador](https://tdn.totvs.com/display/LRM/Contratos+de+Venda+-+Dados+Gerais+-+Compradores) desta venda. |
| CEP | cep | CEP | É o campo [**CEP**](https://tdn.totvs.com/pages/releaseview.action?pageId=421388786), do Endereço Principal, da aba Identificação do cadastro de Cliente/Fornecedor, |
| Logradouro | logradouro | Rua | É o campo [**Rua**](https://tdn.totvs.com/pages/releaseview.action?pageId=421388786), do Endereço Principal, da aba Identificação do cadastro de Cliente/Fornecedor. |
| Número | numero | Número | É o campo [**Número**](https://tdn.totvs.com/pages/releaseview.action?pageId=421388786), do Endereço Principal, da aba Identificação do cadastro de Cliente/Fornecedor. |
| Responsável Legal (Nome) | nomeResponsavelLegal | Nome | É o campo **[Nome](https://tdn.totvs.com/pages/viewpage.action?pageId=435105088)** do Cliente Pessoa Física que está informado no Código do Responsável, do agrupador Responsável Legal, na aba Comissão/Responsável, anexo de Dados Complementares (TOTVS Construção Gestão de Imóveis), do cadastro de Cliente/Fornecedor, quando este é aberto a partir do contexto do TCGI.    Esta informação é obrigatória, quando comprador for Pessoa Jurídica (CNPJ) e Opcional, quando comprador for Pessoa Física (CPF). |
| Responsável Legal (CPF) | cpfResponsavelLegal | CPF/CNPJ | É o campo **[CPF/CNPJ](https://tdn.totvs.com/pages/viewpage.action?pageId=435105088)** do Cliente Pessoa Física que está informado no Código do Responsável, do agrupador Responsável Legal, na aba Comissão/Responsável, anexo de Dados Complementares (TOTVS Construção Gestão de Imóveis), do cadastro de Cliente/Fornecedor, quando este é aberto a partir do contexto do TCGI.    Esta informação é obrigatória, quando comprador for Pessoa Jurídica (CNPJ) e Opcional, quando comprador for Pessoa Física (CPF). |
| Responsável Legal (Tipo) | tipoResponsavelLegal | Tipo Responsável | É o campo **[Tipo Responsável](https://tdn.totvs.com/pages/viewpage.action?pageId=435105088)** do Cliente Pessoa Física que está informado no Código do Responsável, do agrupador Responsável Legal, na aba Comissão/Responsável, anexo de Dados Complementares (TOTVS Construção Gestão de Imóveis), do cadastro de Cliente/Fornecedor, quando este é aberto a partir do contexto do TCGI.    Esta informação é obrigatória, quando comprador for Pessoa Jurídica (CNPJ) e Opcional, quando comprador for Pessoa Física (CPF). |
| Desenvolvedor Imobiliário | Campo não disponível na API [mutuario/dadospessoais](https://imobiliario-homolog.cerc.inf.br/q/swagger-ui/#/Mutuario%20Resource/post_mutuario_dadospessoais) da CERC | (não implementado) | (não implementado)    CNPJ do Desenvolvedor Imobiliário que está cadastrando o Mutuário |

Após a execução com sucesso do Processo [Integrar Registradora](https://tdn.totvs.com/display/LRM/Empreendimentos+-+Processos+-+Integrar+com+Registradora) o sistema vai abastecer a aba [Visão das Registradoras](https://tdn.totvs.com/pages/editpage.action?pageId=741835213), do cadastro de Clientes, quando aberto a partir do contexto do TCGI, com as informações relativas à esta integração.
