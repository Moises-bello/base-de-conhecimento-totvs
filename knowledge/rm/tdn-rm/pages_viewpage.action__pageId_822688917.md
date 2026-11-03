---
content_hash: ce82023c5e090f66b33049b3437b7a6289bc6dd580ed64bce1dbe4f04f8238d7
fetched_at: '2026-06-29T00:11:46.545055+00:00'
page_id: '822688917'
product: rm
source: tdn-rm
title: tribMun/exigSusp
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=822688917
version: 5
---

O Grupo será gerado quando existir algum Processo associado ao Movimento:

Cadastro de Processo

Movimento:

**Regras para geração do Grupo:**

**Existir algum Processo vinculado ao Movimento e pelo menos um item com Tributo ISS com Base de Cálculo maior que Zero e Tipo de Recolhimento "Nenhum".**

| Nome | Pai | Obrigatório | Campo no RM | Descrição |
| --- | --- | --- | --- | --- |
| **exigSusp** |  | **Não** | DPROCESSOJUDICIAL | **Informações para a suspensão da Exigibilidade do ISSQN** |
| tpSusp | exigSusp | Sim | DPROCESSOJUDICIAL.TIPOPROCESSO | Opção para Exigibilidade Suspensa:  1 - Exigibilidade do ISSQN Suspensa por Decisão Judicial; 2 - Exigibilidade do ISSQN Suspensa por Processo Administrativo; |
| nProcesso | exigSusp | Sim | DPROCESSOJUDICIAL.NUMERO | Número do processo judicial ou administrativo de suspensão da exigibilidade. |
