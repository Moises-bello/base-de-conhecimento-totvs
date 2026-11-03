---
content_hash: 6efbb6001c0724bff1dd7121bcf3546cce744d97b53b18a4b47c711cd44c8e59
fetched_at: '2026-06-29T00:09:16.298415+00:00'
page_id: '421385508'
product: rm
source: tdn-rm
title: Sincronização de Motivos de Improdutividade
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385508
version: 2
---

---

Os motivos de produtividade e improdutividade são necessários para que o módulo Manutenção de Ativos do Protheus possa realizar posteriormente o tratamento de apontamentos de horas produtivas e improdutivas.

Esses motivos de produtividade/improdutividade estão cadastrados no Manutenção de Ativos dentro do cadastro de Atividades. Eles são necessários para a realização dos apontamentos dentro do coletor móvel, por isso deve existir um sincronismo entre o cadastro de Atividades (Motivos de Produtividade/Improdutividade) do Manutenção de Ativos e o cadastro de Motivos de Improdutividade do TOP, que é de onde o coletor móvel vai importar os motivos de improdutividade.

Rotinas executadas automaticamente no Manutenção de Ativos vão prover a sincronização dos registros entre Protheus e TOP, sendo que qualquer inclusão, alteração ou exclusão realizada no Protheus será refletida automaticamente no TOP.

**Importante:**

Somente serão sincronizados os motivos de produtividade/improdutividade do tipo "Equipamento", os motivos do tipo "Mão-de-obra" não são vinculados ao Protheus e são cadastrados diretamente no TOP.

**Passos para sincronizar os Motivos de Produtividade / Improdutividade:**

1. Acessar o módulo Manutenção de Ativos (Protheus);

2. Acessar o cadastro de Atividades (Motivos de Produtividade/Improdutividade);

3. Inserir, alterar ou excluir um registro;

4. O Manutenção de Ativos envia ao TOP as modificações realizadas;

5. O TOP replica as modificações em seus registros.

---
