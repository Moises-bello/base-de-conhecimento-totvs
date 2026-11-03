---
content_hash: e8ded3f7163172569e560c92370bf2b943c2da7a04cdd67258003079cebe8209
fetched_at: '2026-06-29T00:05:48.691077+00:00'
page_id: '1027820652'
product: rm
source: tdn-rm
title: Valores relacionados a IBS e CBS no serviço (TPF)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1027820652
version: 12
---

### Voltar para [Layout único de integração da NFS-e com o TPF](https://tdn.totvs.com/pages/viewpage.action?pageId=1056143731)

| Nome | Pai | Tipo Elemento | Ocorrência | Tipo Dado | Descrição | Campo no RM | Observações |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ibscbs | [servico](https://tdn.totvs.com/pages/viewpage.action?pageId=1056144146) | G | 0-1 | -- | Tag raíz que conterá valores relacionados a IBS e CBS |  |  |
| codigoLocalIncidencia | ibscbs | E | 1-1 | Numérico | Código IBGE da localidade de incidência do IBS/CBS (local da operação) | TMOV.CODMUNOPER | Sistema relaciona o município encontrado no campo TMOV.CODMUNOPER com a View DVIEWMUNICIPIOS para encontrar a codificação do município  DVIEWMUNICIPIOS.CODIFICACAO  A relação considera a classificação de municípios informada nos parâmetros de NFS-e, caminho: Movimento | Integrações | Fiscal | Dados Fiscais | Classificação IBGE Município |
| nomeLocalIncidencia | ibscbs | E | 1-1 | Alfanumérico | Nome da localidade de incidência do IBS/CBS | TMOV.CODMUNOPER | Sistema relaciona o município encontrado no campo TMOV.CODMUNOPER com a View DVIEWMUNICIPIOS para encontrar o nome do município  DVIEWMUNICIPIOS.NOMEMUNICIPIO  A relação considera a classificação de municípios informada nos parâmetros de NFS-e, caminho: Movimento | Integrações | Fiscal | Dados Fiscais | Classificação IBGE Município |
| cTributacaoIbsCbs | ibscbs | E | 1-1 | Numérico | Código de Situação Tributária do IBS e da CBS | TTRBMOV.SITTRIBUTARIA |  |
| cClassTributaria | ibscbs | E | 1-1 | Numérico | Código de Classificação Tributária do  IBS e CBS | TTRBMOV.CLASSTRIB |  |
| cCredPresumido | ibscbs | E | 1-1 | Numérico | Código e classificação do crédito presumido: IBS e CBS | TTRBMOV.CODCREDPRESUMIDO |  |
| tpRetPisCofins | ibscbs | E | 0-1 | Numérico | Tipo de Retenção PIS/COFINS e CSLL | Será verificado o campo DTRIBUTO.TIPOTRIBFISC do cadastro do Tributo para identificar se o tributo informado no movimento é Retido ou Não Retido. | O valor da tag será gerado da seguinte forma:  Se não houver os tributos IBS/CBS   | **Código** | **PIS Retido?** | **COFINS Retido?** | | --- | --- | --- | | **1** | Sim | Sim | | **2** | Não | Não |     Se houver IBS/CBS   | **Código** | **PIS Retido?** | **COFINS Retido?** | **CSLL Retida?** | | --- | --- | --- | --- | | **0** | Não | Não | Não | | **3** | Sim | Sim | Sim | | **4** | Sim | Sim | Não | | **5** | Sim | Não | Não | | **6** | Não | Sim | Não | | **7** | Não | Sim | Sim | | **8** | Não | Não | Sim | | **9** | Sim | Não | Sim | |
| cSitTributariaRegular | tributacaoregular | E | 1-1 | Numérico | Código de Situação Tributária do IBS e da CBS de tributação regular | TTRBMOV.SITTRIBUTARIA | O sistema busca a situação tributária da regra tributária regular associada a regra tributária informada no movimento |
| cClassTributariaReg | tributacaoregular | E | 1-1 | Numérico | Código da Classificação Tributária do IBS e da CBS de tributação regular | TTRBMOV.CLASSTRIB | O sistema busca a classificação tributária da regra tributária regular associada a regra tributária informada no movimento |
|  | ibscbs | G | 0-1 |  | Grupo de informações relativas ao Imóvel | aba **“Integrações Fiscais” →****“Dest. Serviço”** |  |
| [imovel](https://tdn.totvs.com/pages/viewpage.action?pageId=1028924670) | ibscbs | G | 0-1 | -- | Grupo de informações relativas ao Imóvel | aba **“Integrações Fiscais” →****“Dest. Serviço”** |  |
