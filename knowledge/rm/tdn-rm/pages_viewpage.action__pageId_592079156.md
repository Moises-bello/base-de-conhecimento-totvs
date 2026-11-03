---
content_hash: 51b27df6c5fe56f3bffd2ae03b98b8942874f24fdd8d42d02ec6386070fdf52e
fetched_at: '2026-06-29T00:10:56.150747+00:00'
page_id: '592079156'
product: rm
source: tdn-rm
title: Alterações S-1298
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=592079156
version: 6
---

false

**A partir das Versões:**

* 12.1.29.282
* 12.1.31.197
* 12.1.32.135
* e Superiores.

# Objetivo:

---

Apresentar as alterações realizadas no evento S-1298 para o leiaute do eSocial Versão S-1.0.

---

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Grupo {ideEvento} Campo procEmi  Alterado Tamanho | Tamanho:001 | Tamanho:1-2 |
| Grupo {ideEvento} Campo{indGuia}   Incluido tag |  | Tipo: N Ocorrência: 0-1  Tamanho: 1 Descrição: Indicativo do tipo de guia Valores válidos: 1 - Documento de Arrecadação do eSocial - DAE |
| Grupo {ideEmpregador} Campo{nrInsc}   Alterado Tamanho e Descrição | Tamanho:015  Informar o número de inscrição do contribuinte de acordo com o tipo de inscrição indicado no campo (tpInsc). Se for um CNPJ deve ser informado apenas RAIZ/BASE de oito posições,exceto se natureza jurídica de administração pública direta fedral ([101-5],[104-0],[107-4],[116-3], situação em que o campo deve ser preenchido com o CNPJ completo (14 posições)) Validação: Se (tpInsc) for igual a [1], deve ser um número de CNPJ válido. Se (tpInsc) for igual a [2], deve ser um CPF válido. | Tamanho:8,11ou 14  Informar o número de inscrição do contribuinte de acordo com o tipo de inscrição indicado no campo ideEmpregador/tpInsc e conforme informado em S-1000. |
