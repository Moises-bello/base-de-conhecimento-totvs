---
content_hash: 7e69983656a3498dbb7fc0f973218f123c1b6845e2796d8ae93f884de777f0a0
fetched_at: '2026-06-29T00:10:58.775561+00:00'
page_id: '606831359'
product: rm
source: tdn-rm
title: Nota Técnica nº 01/2021
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=606831359
version: 10
---

false

**A partir das Versões:**

* 12.1.28.281
* 12.1.29.239
* 12.1.31.142
* e Superiores.

# Objetivo:

---

Em 01/03/2021 foi disponibilizado pelo eSocial a Nota Técnica 01/2021, apontando ajustes no Layout S-1.0.

---

Seguem orientações referente ao produto TOTVS Folha de Pagamento, para atender essa alteração:

1) Ao gerar o evento S-3000 para o evento S-1300 será gerado as tag's <ideFolhaPagto> e <indApuracao>.

 

2) Ao gerar os eventos S-2200 e S-2206 para funcionários com a categoria 111 a tag <horNotuno> não será impressa.

3) Geração do evento S-1299-Fechamento dos Eventos Periódicos

Menu RH | Folha de Pagamento | eSocial | Período de Apuração

Foi criado o campo "**Exclui informação sobre aquisições de produção Rural"**, ao selecionar esse campo o sistema irá gerar a nova tag <indExcApur1250> no evento S-1299.

**Importante:**Essa tag deverá ser enviada somente em caso de necessidade de exclusão ou retificação das informações enviadas de aquisição rural através do eSocial, ou seja, anterior a 21/05/2021.

As retificações  a partir de 21/05/2021 deverão ocorrer pelo evento **R-2055** no REINF.

**Exemplo:** Caso haja necessidade de uma exclusão/retificação das informações enviadas de aquisição rural no evento S-1250 dos períodos anteriores a competência 05/2021, deverá reabrir o período de apuração desejado (envio do evento S-1298) e após reenviar o evento S1299 com a tag <indExcApur1250>.

Mais informações sobre a alteração do S-1250 para o R-2055 acesse: [Gerar Eventos Periódicos](https://tdn.totvs.com/pages/viewpage.action?pageId=506387467).

4)  Atualizada a tabela  27 - Procedimentos Diagnósticos.

5) Ajuste no relatório de conferência de FGTS para verificar os valores retornados no S-5003.
