---
content_hash: 0dab819729b8ba943c36f138319c1676990bae828c2de910fe67971297bbcd92
fetched_at: '2026-06-29T00:11:31.443622+00:00'
page_id: '737570814'
product: rm
source: tdn-rm
title: CERC - Domicílio Bancário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=737570814
version: 8
---

Para que o Processo [Integrar Registradora](https://tdn.totvs.com/display/LRM/Empreendimentos+-+Processos+-+Integrar+com+Registradora) seja executado com sucesso quando a Registradora de Recebíveis for a CERC, o TCGI deverá integrar também o **Domicílio Bancário**, que está associado ao Empreendimento, através da aba [Dados Bancários](https://tdn.totvs.com/pages/viewpage.action?pageId=514742343).

|  |  |  |  |
| --- | --- | --- | --- |
| **CAMPO  CERC-IM011 – DOMICÍLIO BANCÁRIO** | **CAMPO API - DOMICILIOBANCARIO** | **CAMPO RM** | **DESCRIÇÃO** |
| Tipo de Operação | tipoOperacao | Ação | O Tipo de Operação a ser realizado na integração dos dados coma  CERC é definido pelo campo de **Ação** da tela do Processo [Integrar Registradora](https://tdn.totvs.com/display/LRM/Empreendimentos+-+Processos+-+Integrar+com+Registradora) |
| CNPJ | cnpj | CNPJ | É o campo **[CNPJ](https://tdn.totvs.com/pages/viewpage.action?pageId=435105154)** da aba Identificação do cadastro de Empreendimento |
| Razão Social | razaoSocial | Nome - Empreendimento | É o campo **Nome - Empreendimento** da aba [Identificação](https://tdn.totvs.com/pages/viewpage.action?pageId=435105154) do Empreendimento. |
| Referência Externa | referenciaExterna | Código Coligada + Identificador do Convênio | É formado com a junção dos campos **[Código da Coligada](https://tdn.totvs.com/display/LRM/Coligada)** + o Identificador do **[Convênio](https://tdn.totvs.com/pages/viewpage.action?pageId=421388845)**, que está cadastrado na aba [Dados Bancários](https://tdn.totvs.com/pages/viewpage.action?pageId=514742343) do Empreendimento. Sendo que um Empreendimento pode estar associado a um ou mais convênios e neste cenário, todos eles são integrados. |
| Banco | banco | Banco | É o campo **Banco**, da aba Identificação do [Convênio](https://tdn.totvs.com/pages/viewpage.action?pageId=421388845). |
| Agência | agencia | Agência | É o campo **Agência**, da aba Identificação do [Convênio](https://tdn.totvs.com/pages/viewpage.action?pageId=421388845). |
| Conta | conta | Conta | É o campo **Conta**, da aba Identificação do [Convênio](https://tdn.totvs.com/pages/viewpage.action?pageId=421388845). |
| Convênio de Cobrança | convenioCobranca | N/A | Valor fixo '000', Não identificado. Pois TCGI não possui este valor. |
| Cód Cedente | codigoCedente | Código Cedente | É o campo **Código Cedente**, da aba Dados Adicionais do [Convênio](https://tdn.totvs.com/pages/viewpage.action?pageId=421388845). |

Após a execução com sucesso do Processo [Integrar Registradora](https://tdn.totvs.com/display/LRM/Empreendimentos+-+Processos+-+Integrar+com+Registradora) o sistema vai abastecer a aba [Registradora Domicílio Bancário](https://tdn.totvs.com/pages/viewpage.action?pageId=737551676), do Empreendimento com as informações relativas à esta integração.
