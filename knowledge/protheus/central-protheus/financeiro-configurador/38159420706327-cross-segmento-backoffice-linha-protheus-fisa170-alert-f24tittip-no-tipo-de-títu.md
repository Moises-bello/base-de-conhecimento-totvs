---
article_id: 38159420706327
category: Financeiro - Configurador
content_hash: a5f3553d3c56d749f60c4ca7505e76c59f6c4c2504b829fa0be753906edf1328
fetched_at: '2026-06-28T22:37:57.577471+00:00'
product: protheus
section_id: 1500001539601
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - FISA170 - Alert F24TITTIP no tipo
  de título da Regra Financeira
type: support-article
updated_at: '2026-02-04T18:47:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38159420706327-Cross-Segmento-Backoffice-Linha-Protheus-FISA170-Alert-F24TITTIP-no-tipo-de-t%C3%ADtulo-da-Regra-Financeira
---

##### time.png Tempo aproximado para leitura: **05:00 min** **Ocorrência** Ao criar uma regra no **Configurador** de Tributos - **FISA170** - **Regra financeira** - **Regra de título** e selecionar o tipo de imposto **CID - (CIDE)** no campo**FKL\_TIPO** é apresentado o **Alert F24TITTIP**. **Ambiente** Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da 12.1.2210. **Causa** Este alerta ocorre porque o tipo de título não existe no parâmetro **MV\_TIPIMP**.

##### **Solução** Acesse o módulo **Configurador** e realize o cadastro do conteúdo no parâmetro **MV\_TIPIMP**, a fim de que o sistema apresente o imposto **CID (CIDE)** no campo **FKL\_TIPO**.

**Importante**

Caso haja a necessidade de incluir um novo tipo de imposto que ainda não exista na **tabela 05 da SX5**, basta realizar o cadastro correspondente na tabela e, em seguida, atualizar o conteúdo do parâmetro **MV\_TIPIMP**.

**Saiba mais**

[Regra título -tipo de título - imposto não consta no cadastro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052613913-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FISA170-N%C3%A3o-possuem-os-tipos-de-impostos-ao-criar-uma-regra-de-t%C3%ADtulo-no-campo-FKL-TIPO)

[Configurador+de+Tributos - FISA170](https://tdn.totvs.com.br/display/public/PROT/Configurador+de+Tributos+-+Regras+Financeiras)
