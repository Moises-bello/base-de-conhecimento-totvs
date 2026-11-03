---
content_hash: a374eb145fd467f4eadd19c435526f64be76104da65d155755a0ca5201e28648
fetched_at: '2026-06-29T00:11:29.381638+00:00'
page_id: '736191253'
product: rm
source: tdn-rm
title: CERC - Subunidade (Unidade).
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=736191253
version: 13
---

Para que o Processo [Integrar Registradora](https://tdn.totvs.com/display/LRM/Empreendimentos+-+Processos+-+Integrar+com+Registradora) seja executado com sucesso quando a Registradora de Recebíveis for a CERC, é obrigatório que no cadastro de **[Subunidade](https://tdn.totvs.com/display/LRM/Unidade+-+Anexos+-+Subunidade)**, informações estejam preenchidas, com base no *CERC.*

|  |  |  |  |
| --- | --- | --- | --- |
| **CAMPOCERC-IM002B - UNIDADE** | **CAMPO API - UNIDADE** | **CAMPO RM** | **DESCRIÇÃO** |
| Tipo de Operação | tipoOperacao | Ação | O Tipo de Operação a ser realizado na integração dos dados coma  CERC é definido pelo campo de **Ação** da tela do Processo [Integrar Registradora](https://tdn.totvs.com/display/LRM/Empreendimentos+-+Processos+-+Integrar+com+Registradora) |
| Referência  Externa - Projeto | referenciaExternaProjeto | Código da Coligada + Empreendimento | É formado com a junção dos campos **[Código da Coligada](https://tdn.totvs.com/display/LRM/Coligada)** (acrescido de zeros à esquerda, para ocupar 4 posições) + **[Empreendimento](https://tdn.totvs.com/pages/viewpage.action?pageId=435105154)** que é o identificador desta entidade (que é preenchido automaticamente pelo TCGI). |
| Identificador da Quadra/Torre | identificadorQuadraTorre | Identificador da Unidade | É o campo **Identificador da Unidade** cadastrado na aba [Integração Registradora Recebíveis](https://tdn.totvs.com/pages/viewpage.action?pageId=737563311) da Unidade. |
| Identificador da Unidade | identificadorUnidade | Subunidade | É o campo **Subunidade/Lote/Apto,** da aba de Identificação, do cadastro de [Subunidade](https://tdn.totvs.com/display/LRM/Unidade+-+Anexos+-+Subunidade). |
| Tipo Imóvel | tipoImovel | Tipo Imóvel | É o campo **Tipo Imóvel**, da aba [Integração Registradora Recebíveis](https://tdn.totvs.com/pages/viewpage.action?pageId=737567392), da Subunidade. |
| Fração Ideal - Tipo | fracaoIdealTipo | Tipo Fração Ideal | É o campo **Tipo Fração Ideal**, da aba [Integração Registradora Recebíveis](https://tdn.totvs.com/pages/viewpage.action?pageId=737567392), da Subunidade. |
| Fração Ideal | fracaoIdeal | Fração Ideal | É o campo **Fração Ideal,** da aba de Identificação, do cadastro de [Subunidade](https://tdn.totvs.com/display/LRM/Unidade+-+Anexos+-+Subunidade). |
| Metragem Total | metragemTotal | Área Total (m²) | É o campo **Área Total (m²)**, da aba Dimensões/Áreas, do cadastro de [Subunidade](https://tdn.totvs.com/display/LRM/Unidade+-+Anexos+-+Subunidade). |
| Metragem Útil | metragemUtil | Área (m²) | É o campo **Área (m²)**, da aba Dimensões/Áreas, do cadastro de [Subunidade](https://tdn.totvs.com/display/LRM/Unidade+-+Anexos+-+Subunidade). |
| Pavimento | pavimento | Nro do Pavimento | É o campo **Nro do Pavimento**, da aba [Integração Registradora Recebíveis](https://tdn.totvs.com/pages/viewpage.action?pageId=737567392), da Subunidade. |
| Quantidade de Garagens Privativas | quantidadeGaragensPrivativas | Vagas | É a **soma da quantidade de registros** cadastrados na aba [Vagas](https://tdn.totvs.com/display/LRM/Subunidade+-+Anexo+-+Vagas), da Subunidade |
| Preço M² | precoM2 | Preço por m² | É o campo **Preço por m²**, da aba de Identificação, do cadastro de [Subunidade](https://tdn.totvs.com/display/LRM/Unidade+-+Anexos+-+Subunidade), que herda essa informação da [Tabela de Preço](https://tdn.totvs.com/pages/releaseview.action?pageId=435105236). |
| Data da Tabela (ref M²) | dataTabela | Data Início Vigência | É o campo **Data Início Vigência**, da [Tabela de Preço](https://tdn.totvs.com/pages/releaseview.action?pageId=435105236) ao qual esta Subunidade está associada.  Depois de Vendido, assume a data do contrato ativo.  Portanto, é obrigatório que a Subunidade esteja associada a uma [Tabela de Preço](https://tdn.totvs.com/pages/releaseview.action?pageId=435105236). |
| Identificação Ônus | identificacaoOnus | Tipo Gravame/Ônus | É o campo **Tipo Gravame/Ônus**, da aba [Integração Registradora Recebíveis](https://tdn.totvs.com/pages/viewpage.action?pageId=737567392), da Subunidade. |
| Status da Unidade | statusUnidade | (controle interno) | Esta informação é controlada internamente pelo TGCI, sendo tratada com a seguinte lógica:  *001 = Disponível*, caso não haja nenhuma Número de Venda/Contrato ativo associado à Subunidade.  *003 = Indisponível*, caso haja algum Número de Venda/Contrato ativo associado à Subunidade. |
| Classificação de Direcionamento da Unidade | classificacaoDirecionamentoUnidade | Tipo de Classificação | É o campo **Tipo de Classificação**, da aba [Integração Registradora Recebíveis](https://tdn.totvs.com/pages/viewpage.action?pageId=737567392), da Subunidade. |

Para as informações da Registradora de Recebíveis que forem comuns à várias Unidades, utilize o processo [Atualizar em Lote](https://tdn.totvs.com/display/LRM/Subunidade+-+Processo+-+Atualizar+em+Lote)**.**

Após a execução com sucesso do Processo [Integrar Registradora](https://tdn.totvs.com/display/LRM/Empreendimentos+-+Processos+-+Integrar+com+Registradora) o sistema vai abastecer a [Visão das Registradoras](https://tdn.totvs.com/pages/viewpage.action?pageId=737567520), da Subunidade, com as informações relativas à esta integração.
