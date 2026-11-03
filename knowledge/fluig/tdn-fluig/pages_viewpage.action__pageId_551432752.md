---
content_hash: d0aac40b87dfa78de1327741f126186417cb644cf7181a7548ef79dedcbe183e
fetched_at: '2026-06-28T21:35:27.476388+00:00'
page_id: '551432752'
product: fluig
source: tdn-fluig
title: WCM - Por que meu formulário está sem espaçamento no componente Collapse?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=551432752
version: 5
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

**Versão:** 1.6.5-200226 ou superior

# Ocorrência

Por que meu formulário está sem espaçamento no componente Collapse?

sample1Formulário no TOTVS Fluig Plataforma 1.6.5-200218 ou inferior2Formulário no TOTVS Fluig Plataforma 1.6.5-200226 ou superior

# Causa

No Fluig Plataforma 1.6.5-200226, o Style Guide evoluiu a visualização de formulários no Mobile. Com isso, formulários criados com base no [exemplo disponível no projeto Samples](https://git.fluig.com/projects/SAMPLES/repos/style-guide/browse) precisam ser atualizados, pois uma classe ausente no exemplo deixou o formulário sem o espaçamento correto no componente Collapse.

# Solução

Adicionar a classe 'collapse-icon' no elemento <a>, localizado abaixo do componente com ID 'panel-title'. O projeto sample-component está corrigido. Compare o formulário de exemplo com o seu formulário e faça as alterações necessárias: <https://git.fluig.com/projects/SAMPLES/repos/style-guide/browse>

# Observações

Essa situação ocorre apenas em formulários que foram criados com base no formulário do projeto Samples e que utilizam o componente Collapse.
