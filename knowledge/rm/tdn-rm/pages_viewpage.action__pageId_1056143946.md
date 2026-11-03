---
content_hash: 5e8964ae86cc2c25ede6247b56421420ca789a9bfe86fec962133d7e7f601d18
fetched_at: '2026-06-29T00:05:51.960386+00:00'
page_id: '1056143946'
product: rm
source: tdn-rm
title: Informações para cancelamento do RPS/DPS (TPF)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1056143946
version: 1
---

### Voltar para [Layout único de integração da NFS-e com o TPF](https://tdn.totvs.com/pages/viewpage.action?pageId=1056143731)

| Nome | Pai | Tipo Elemento | Ocorrência | Descrição | Campo no RM | Observações |
| --- | --- | --- | --- | --- | --- | --- |
| **cancelamento** | **[rps](https://tdn.totvs.com/pages/viewpage.action?pageId=1056143860)** | **G** | **0-1** | **--** | **Tag raiz para as informações sobre a substituição de um documento.** |  |
| codmotcanc | cancelamento | E | 0-1 | Código do motivo do cancelamento do documento. Os conteúdos possíveis são:  •  1 – Extravio; •  2 – Dados incorretos;  •  3 – Substituição. | TMOVCOMPL.CODMOTCANC | Deve ser criado campo complementar no Movimento. Ele deve ser do tipo Alfanumerico  subtipo Texto de tamanho 2.  Os valores válidos são:  **1**, **2** ou **3**.  Sendo  1. Extravio | 2. Dados incorretos | 3. Substituição  Regra válida para:   * Anápolis/GO | TOTVS Colaboração 2.0**Anápolis/GO |** **TOTVS Colaboração 2.0** TOTVS Colaboração 2.0: Quando a Filial estiver parametrizada para usar TOTVS Colaboração ao solicitar o cancelamento, será exibido um formulário com campo para preenchimento do código de cancelamento desejado. * Barueri **Barueri**  A Filial deve ter o campo TIPO FTP parametrizada como Web Service.  Em Ambiente > Parâmetros > Integração > Fiscal > Dados Fiscais parametrize o Tipo FTP como **Web** **Service**.  Para mais informações acesse a nossa [Base de Conhecimento.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/29362467685271-Cross-Segmentos-TOTVS-Backoffice-Linha-RM-Doc-Eletr%C3%B4nicos-Como-emitir-nota-fiscal-para-o-munic%C3%ADpio-de-Barueri-SP-via-WebService)  FTP |
| motcanc | cancelamento | E | 1-1 | Motivo do cancelamento do documento. | TMOVFISCAL.MOTIVOCANCELAMENTO |  |
