---
content_hash: f115e5ec06298c677d85f7d15cd38c1a9c86160d61d25d189d784a8a9eb66bed
fetched_at: '2026-06-29T00:11:29.373309+00:00'
page_id: '736191246'
product: rm
source: tdn-rm
title: CERC - Unidade (Quadras/Torres).
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=736191246
version: 12
---

Para que o Processo [Integrar Registradora](https://tdn.totvs.com/display/LRM/Empreendimentos+-+Processos+-+Integrar+com+Registradora) seja executado com sucesso quando a Registradora de Recebíveis for a CERC, é obrigatório que no cadastro de **[Unidade](https://tdn.totvs.com/display/LRM/Empreendimento+-+Anexos+-+Unidade)**, informações estejam preenchidas, com base *CERC.*

|  |  |  |  |
| --- | --- | --- | --- |
| **CAMPOCERC-IM002A - QUADRAS/TORRES** | **CAMPO API - QUADRATORRE** | **CAMPO RM** | **DESCRIÇÃO** |
| Tipo de Operação | tipoOperacao | Ação | O Tipo de Operação a ser realizado na integração dos dados coma  CERC é definido pelo campo de **Ação** da tela do Processo [Integrar Registradora](https://tdn.totvs.com/display/LRM/Empreendimentos+-+Processos+-+Integrar+com+Registradora) |
| Referência  Externa - Projeto | referenciaExternaProjeto | Código da Coligada + Empreendimento | É formado com a junção dos campos **[Código da Coligada](https://tdn.totvs.com/display/LRM/Coligada)** (acrescido de zeros à esquerda, para ocupar 4 posições) + **[Empreendimento](https://tdn.totvs.com/pages/viewpage.action?pageId=435105154)** que é o identificador desta entidade (que é preenchido automaticamente pelo TCGI). |
| Identificador da Quadra/Torre | identificadorQuadraTorre | Identificador da Unidade | É o campo **Identificador da Unidade** cadastrado na aba [Integração Registradora Recebíveis](https://tdn.totvs.com/pages/viewpage.action?pageId=737563311) da Unidade. |
| Uso | uso | Tipo de Uso | É o campo **Tipo de Uso** da aba [Integração Registradora Recebíveis](https://tdn.totvs.com/pages/viewpage.action?pageId=737563311) do Empreendimento. |
| Unidades Total da Quadra/Torres | unidadesTotalQuadraTorre | Quantidade Subunidade | É o campo **Quantidade Subunidade/Lote/Apto**, que está informada na aba de [Identificação](https://tdn.totvs.com/display/LRM/Empreendimento+-+Anexos+-+Unidade) da Unidade. |
| Data do Habite-se (Prevista) | dataHabiteSePrevista | Data Habite-se | É o campo **Data Habite-se** da aba de [Identificação](https://tdn.totvs.com/pages/viewpage.action?pageId=435105154) do Empreendimento. |
| Data do Habite-se (Prevista + Prazo Legal) | dataHabiteSePrevistaPrazo | Data do Habite-se + 180 dias | É o campo **Data Habite-se** da aba de [Identificação](https://tdn.totvs.com/pages/viewpage.action?pageId=435105154) do Empreendimento.  Informativo: Considera limite legal do prazo + 180 dias. |
| Evolução da Obra - Total | evolucaoObraTotal | Percentual | É o campo que **Percentual**, informado no último [Avanço da Obra (POC)](https://tdn.totvs.com/pages/viewpage.action?pageId=435104746), inserido na aba de mesmo nome, do cadastro de Empreendimento.  Por último avanço cadastrado, entenda-se o que tem o Código de Andamento mais recente. |
| Data Base da  Evolução da Obra | dataBaseEvolucaoObra | Data Inicial | É o campo que **Data Inicial**, informado no último [Avanço da Obra (POC)](https://tdn.totvs.com/pages/viewpage.action?pageId=435104746), inserido na aba de mesmo nome, do cadastro de Empreendimento. |

Para as informações da Registradora de Recebíveis que forem comuns à várias Unidades, utilize o processo [Atualizar em Lote](https://tdn.totvs.com/display/LRM/Unidade+-+Processos+-+Atualizar+em+Lote)**.**

Após a execução com sucesso do Processo [Integrar Registradora](https://tdn.totvs.com/display/LRM/Empreendimentos+-+Processos+-+Integrar+com+Registradora) o sistema vai abastecer a [Visão das Registradoras](https://tdn.totvs.com/pages/viewpage.action?pageId=737563793) com as informações relativas à esta integração.
