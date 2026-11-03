---
content_hash: fb4c1d2622d659918bb704ed01b273bab77f34fba98e474d6f5e53f31d927abc
fetched_at: '2026-06-29T00:10:58.778987+00:00'
page_id: '606836691'
product: rm
source: tdn-rm
title: Nota Técnica nº 21/2021
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=606836691
version: 9
---

false

**A partir dos patches:**

* 12.1.28.281
* 12.1.29.239
* 12.1.31.142
* e Superiores.

# Objetivo:

---

Em 01/03/2021 foi disponibilizado pelo eSocial a [Nota Técnica 21/2021](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/nota-tecnica-21-2021.pdf), apontando ajustes no Layout 2.5.

---

Seguem orientações referente ao produto TOTVS Folha de Pagamento, para atender essa alteração:

1) Geração do evento S-1299-Fechamento dos Eventos Periódicos

Menu RH | Folha de Pagamento | eSocial | Período de Apuração

Foi criado o campo "**Exclui informação sobre aquisições de produção Rural"**, ao selecionar esse campo o sistema irá gerar a nova tag <indExcApur1250> no evento S-1299.

**Importante:**Essa tag deverá ser enviada somente em caso de necessidade de exclusão ou retificação das informações enviadas de aquisição rural através do eSocial, ou seja, anterior a 21/05/2021.

As retificações  a partir de 21/05/2021 deverão ocorrer pelo evento **R-2055** no REINF.

**Exemplo:** Caso haja necessidade de uma exclusão/retificação das informações enviadas de aquisição rural no evento S-1250 dos períodos anteriores a competência 05/2021, deverá reabrir o período de apuração desejado (envio do evento S-1298) e após reenviar o evento S1299 com a tag <indExcApur1250>.

Mais informações sobre a alteração do S-1250 para o R-2055 acesse: [Gerar Eventos Periódicos](https://tdn.totvs.com/pages/viewpage.action?pageId=506387467).

2) Ajuste no relatório de conferência de FGTS para verificar os valores retornados no S-5003.

3) Cadastro de Eventos

Incluído na tabela de natureza de rubrica o código 6108-Relativa ao tempo de espera do motorista profissional.
