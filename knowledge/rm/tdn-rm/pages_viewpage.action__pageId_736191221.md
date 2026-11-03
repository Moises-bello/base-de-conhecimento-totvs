---
content_hash: 3f215c31717bf02510a28494e5db841e97f1f01cc5b7fa6da511ed7eb093d08f
fetched_at: '2026-06-29T00:11:29.366400+00:00'
page_id: '736191221'
product: rm
source: tdn-rm
title: CERC - Empreendimento.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=736191221
version: 15
---

Para que o Processo [Integrar Registradora](https://tdn.totvs.com/display/LRM/Empreendimentos+-+Processos+-+Integrar+com+Registradora) seja executado com sucesso quando a Registradora de Recebíveis for a CERC, é obrigatório que no cadastro de **[Empreendimento](https://tdn.totvs.com/display/LRM/Empreendimento)**, informações estejam preenchidas.

|  |  |  |  |
| --- | --- | --- | --- |
| **CAMPO CERC-IM001 - CADASTRO E ATUALIZAÇÃO DO EMPREENDIMENTO** | **CAMPO API - EMPREENDIMENTO** | **CAMPO RM** | **DESCRIÇÃO** |
| Tipo de Operação | tipoOperacao | Ação | O Tipo de Operação a ser realizado na integração dos dados coma  CERC é definido pelo campo de **Ação** da tela do Processo [Integrar Registradora](https://tdn.totvs.com/display/LRM/Empreendimentos+-+Processos+-+Integrar+com+Registradora) |
| Referência  Externa - Projeto | referenciaExternaProjeto | Código da Coligada + Empreendimento | É formado com a junção dos campos **[Código da Coligada](https://tdn.totvs.com/display/LRM/Coligada)** (acrescido de zeros à esquerda, para ocupar 4 posições) + **[Empreendimento](https://tdn.totvs.com/pages/viewpage.action?pageId=435105154)** que é o identificador desta entidade (que é preenchido automaticamente pelo TCGI). |
| Identificador da SPE/Desenvolvedor Imobiliário | idSpe | CNPJ | É o campo **[CNPJ](https://tdn.totvs.com/pages/viewpage.action?pageId=435105154)** da aba Identificação do cadastro de Empreendimento |
| CNS do Cartório | cns | Código do Cartório de Registro de Imóveis | É o campo ***Código do Cartório de Registro de Imóveis*** do cadastro de [Cartórios](https://tdn.totvs.com/pages/viewpage.action?pageId=435105389). |
| Número da Matrícula | numeroMatricula | Matrícula | É o campo **[Matrícula](https://tdn.totvs.com/pages/viewpage.action?pageId=435105074)** localizado na aba Informações do Empreendimento. Sendo composto pelos 7 primeiros dígitos da matrícula. |
| Razão Social | razaoSocial | Nome - Empreendimento | É o campo **Nome - Empreendimento** da aba [Identificação](https://tdn.totvs.com/pages/viewpage.action?pageId=435105154) do Empreendimento. |
| Nome Comercial | nomeComercial | Nome Fantasia | É o campo **Nome Fantasia** da aba [Identificação](https://tdn.totvs.com/pages/viewpage.action?pageId=435105154) do Empreendimento. |
| CPF Responsável | cpfResponsavel | CPF/CNPJ | É o campo **CPF/CNPJ** da Pessoa Física, do cadastro de [Cliente/Fornecedor](https://tdn.totvs.com/pages/viewpage.action?pageId=421388786), que é o responsável por gerir esta integração. |
| Nome Contato | nomeContato | Responsável | É o campo **Nome** da Pessoa Física, do cadastro de [Cliente/Fornecedor](https://tdn.totvs.com/pages/viewpage.action?pageId=421388786), que é o responsável por gerir esta integração. |
| Email | email | E-mail | É o campo **E-Mail** da Pessoa Física, do cadastro de [Cliente/Fornecedor](https://tdn.totvs.com/pages/viewpage.action?pageId=421388786), que é o responsável por gerir esta integração. |
| Celular | celular | Celular | È o campo **Celular** da Pessoa Física, do cadastro de [Cliente/Fornecedor](https://tdn.totvs.com/pages/viewpage.action?pageId=421388786), que é o responsável por gerir esta integração. |
| CEP | cep | CEP | É o campo **CEP** da aba [Identificação](https://tdn.totvs.com/pages/viewpage.action?pageId=435105154) do Empreendimento. |
| Logradouro | logradouro | Logradouro | É o campo **Logradouro** da aba [Identificação](https://tdn.totvs.com/pages/viewpage.action?pageId=435105154) do Empreendimento. |
| Número | numero | Nro. | É o campo **Nro.** da aba [Identificação](https://tdn.totvs.com/pages/viewpage.action?pageId=435105154) do Empreendimento. |
| Uso | uso | Tipo de Uso | É o campo **Tipo de Uso** da aba [Integração com Registradora de Recebíveis](https://tdn.totvs.com/pages/viewpage.action?pageId=737551378) do Empreendimento. |
| Tipo de Implantação | tipoImplantacao | Tipo de Implantação | É o campo **Tipo de Implantação** da aba [Integração com Registradora de Recebíveis](https://tdn.totvs.com/pages/viewpage.action?pageId=737551378) do Empreendimento. |
| Registro de Incorporação | registroIncorporacao | Tipo de Incorporação | É o campo **Tipo de Incorporação** da aba [Integração com Registradora de Recebíveis](https://tdn.totvs.com/pages/viewpage.action?pageId=737551378) do Empreendimento. |
| Averbação - RI | ri | Nro da Averbação/Ônus | Se o campo *Registro de Incorporação* for SIM, este campo é obrigatório, No TCGI, esta informação está no campo **Nro da Averbação/Ônus** da aba [Integração com Registradora de Recebíveis](https://tdn.totvs.com/pages/viewpage.action?pageId=737551378) do Empreendimento. |
| Data - Registro de Incorporação | dataIncorporacao | Data do Registro da Incorporação | Se o campo *Registro de Incorporação* for SIM, este campo é obrigatório, No TCGI, esta informação está no campo **Data do Registro da Incorporação** da aba [Integração com Registradora de Recebíveis](https://tdn.totvs.com/pages/viewpage.action?pageId=737551378) do Empreendimento. |
| Patrimônio de Afetação | patrimonio | Patrimônio de Afetação | É o campo **Patrimônio de Afetação** da aba [Integração com Registradora de Recebíveis](https://tdn.totvs.com/pages/viewpage.action?pageId=737551378) do Empreendimento. |
| Averbação | averbacao | Número da Averbação do Patrimônio de Afetação | Se o campo *Patrimônio de Afetação* for SIM, este campo é obrigatório, No TCGI, esta informação está no campo **Número da Averbação do Patrimônio de Afetação** da aba [Integração com Registradora de Recebíveis](https://tdn.totvs.com/pages/viewpage.action?pageId=737551378) do Empreendimento. |
| Data da Constituição do Patrimônio de Afetação | dataPatrimonio | Data da Constituição do Patrimônio de Afetação | Se o campo *Patrimônio de Afetação* for SIM, este campo é obrigatório, No TCGI, esta informação está no campo **Data da Constituição do Patrimônio de Afetação** da aba [Integração com Registradora de Recebíveis](https://tdn.totvs.com/pages/viewpage.action?pageId=737551378) do Empreendimento. |
| Domicílio Bancário | domicilioBancario | Código Coligada + Identificador do Convênio | É formado com a junção dos campos **[Código da Coligada](https://tdn.totvs.com/display/LRM/Coligada)** + o Identificador do **[Convênio](https://tdn.totvs.com/pages/viewpage.action?pageId=421388845)**, que estão cadastrados na aba [Dados Bancários](https://tdn.totvs.com/pages/viewpage.action?pageId=514742343) do Empreendimento. Sendo que um Empreendimento pode estar associado a um ou mais convênios e neste cenário, todos eles são integrados. |
| Identificação da Quantidade de Quadra Torres | quantidadeQuadrasTorres | Quantidade de Unidades | É o campo **Quantidade de Unidades/Quadras/Lotes/Torres** localizado na aba [Informações](https://tdn.totvs.com/pages/viewpage.action?pageId=435105074) do Empreendimento |

Para as informações da Registradora de Recebíveis que forem comuns à vários Empreendimentos, utilize o processo [Atualizar em Lote](https://tdn.totvs.com/display/LRM/Empreendimento+-+Processos+-+Atualizar+em+Lote)**.**

Após a execução com sucesso do Processo [Integrar Registradora](https://tdn.totvs.com/display/LRM/Empreendimentos+-+Processos+-+Integrar+com+Registradora) o sistema vai abastecer a [Visão das Registradoras](https://tdn.totvs.com/pages/viewpage.action?pageId=737551520) com as informações relativas à esta integração.
