---
article_id: 1500007183482
category: Gestão de Frotas
content_hash: 331d8ce8503054f9f275094c20c7caceef763bfe83c13f4384ec7c418e5b1d49
fetched_at: '2026-06-28T22:42:39.364373+00:00'
product: protheus
section_id: 360012117873
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Definição da filial nas inconsistências
  de abastecimento
type: support-article
updated_at: '2021-10-29T11:28:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007183482-Manufatura-Linha-Protheus-MNT-Defini%C3%A7%C3%A3o-da-filial-nas-inconsist%C3%AAncias-de-abastecimento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023739612/time.png) Tempo aproximado para leitura:**00:00:30 min**  
**Dúvida**Como é definido a filial das inconsistências do abastecimento ?

**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Gestão de Frotas - Todas as versões  
  
**Solução**As inconsistências sempre serão gravadas na filial em que está sendo executada a rotina ou operação, independente se o veículo ou o posto pertencerem a mesma filial. A seguir são apresentados alguns exemplos de execução:

| Filial do veículo | Filial do abastecimento | Filial de Login | Gravação TQQ\_FILIAL / TQP\_FILIAL |
| --- | --- | --- | --- |
| M RJ 01 | M RJ 02 | M RJ 03 | M RJ 03 |
| M RJ 01 | M RJ 01 | M RJ 02 | M RJ 02 |
| M RJ | S SC | M RJ 01 | M RJ 01 |
| EM BRANCO | M RJ 01 | M RJ 02 | M RJ 02 |
