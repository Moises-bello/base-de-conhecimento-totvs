---
content_hash: 1c206e167091bb401327a014e5ec1fc67276b1fc82cc1c8585db34b1b7956eb5
fetched_at: '2026-06-29T00:10:47.667756+00:00'
page_id: '560653268'
product: rm
source: tdn-rm
title: Informações para cancelamento do RPS/DPS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=560653268
version: 15
---

### Voltar para [Layout único de integração da NFS-e com o TSS](https://tdn.totvs.com/pages/viewpage.action?pageId=560652116)

| Nome | Pai | Tipo Elemento | Ocorrência | Descrição | Campo no RM | Observações |
| --- | --- | --- | --- | --- | --- | --- |
| **cancelamento** | **[rps](https://tdn.totvs.com/pages/viewpage.action?pageId=1056143227)** | **G** | **0-1** | **--** | **Tag raiz para as informações sobre a substituição de um documento.** |  |
| codmotcanc | cancelamento | E | 0-1 | Código do motivo do cancelamento do documento. Os conteúdos possíveis são:  •  1 – Extravio; •  2 – Dados incorretos;  •  3 – Substituição. | TMOVCOMPL.CODMOTCANC | Deve ser criado campo complementar no Movimento. Ele deve ser do tipo Alfanumerico  subtipo Texto de tamanho 2.  Os valores válidos são:  **1**, **2** ou **3**.  Sendo  1. Extravio | 2. Dados incorretos | 3. Substituição  Regra válida para:   * Anápolis/GO | TOTVS Colaboração 2.0**Anápolis/GO |** **TOTVS Colaboração 2.0** TOTVS Colaboração 2.0: Quando a Filial estiver parametrizada para usar TOTVS Colaboração ao solicitar o cancelamento, será exibido um formulário com campo para preenchimento do código de cancelamento desejado. * Barueri **Barueri**  A Filial deve ter o campo TIPO FTP parametrizada como Web Service.  Em Ambiente > Parâmetros > Integração > Fiscal > Dados Fiscais parametrize o Tipo FTP como **Web** **Service**.  Para mais informações acesse a nossa [Base de Conhecimento.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/29362467685271-Cross-Segmentos-TOTVS-Backoffice-Linha-RM-Doc-Eletr%C3%B4nicos-Como-emitir-nota-fiscal-para-o-munic%C3%ADpio-de-Barueri-SP-via-WebService)  FTP |
| motcanc | cancelamento | E | 1-1 | Motivo do cancelamento do documento. | TMOVFISCAL.MOTIVOCANCELAMENTO |  |
