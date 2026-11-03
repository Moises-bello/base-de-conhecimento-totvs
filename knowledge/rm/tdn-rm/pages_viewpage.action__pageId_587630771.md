---
content_hash: 354c10bec3045f1f66d7381860b32520dc55a5ac6928f5655156798bc3332881
fetched_at: '2026-06-29T00:10:53.828735+00:00'
page_id: '587630771'
product: rm
source: tdn-rm
title: Alterações S-1020
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=587630771
version: 14
---

false

**A partir das Versões:**

* 12.1.29.282
* 12.1.31.197
* 12.1.32.135
* e Superiores.

# Objetivo:

---

Apresentar as alterações realizadas no evento S-1020 para o leiaute do eSocial Versão S-1.0.

---

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Grupos {dados da lotação}: Campo {tpInsc}.  Alterada Validação  Tamanho | Preencher com o código correspondente ao tipo de inscrição, conforme tabela 5.  Validação: O campo não deve ser preenchido se {tpLotacao} for igual a [01, 10, 21, 24, 90, 91]. Nos demais casos, observar conteúdo exigido para o campo {nrInsc}, conforme Tabela 10 - Tipos de Lotação Tributária. Valores Válidos: 1, 2, 4. 20   Tamanho:15 | Tamanho:14 Validação: O campo não deve ser preenchido se tpLotacao for igual a [01, 10, 21, 24, 90, 91]. Nos demais  casos, observar conteúdo exigido para o campo dadosLotacao/nrInsc, conforme Tabela 10  Valores válidos:  1 - CNPJ  2 - CPF  4 - CNO |
| Grupos{infoEmprParcial}: Campo {tpInscProp}  Validação: Deixou de ser obrigatorio | Campo obrigatorio (1-1) | Não obrigatorio (0-1) |
| Grupos{infoEmprParcial}: Campo {nrInscProp} | Campo obrigatorio (1-1)  Preencher com o número de inscrição (CNPJ/CPF) do proprietário do CNO.  Validação: Deve ser um CNPJ ou CPF válido, conforme indicado em {tpInscProp}, e constar como responsável no cadastro do CNO. | Não obrigatorio (0-1)  Preencher com o número de inscrição (CNPJ/CPF) do proprietário do CNO.  Validação: Preenchimento obrigatório e exclusivo se tpInscProp for informado. Deve ser um número de CNPJ ou CPF válido, conforme indicado em tpInscProp, e constar como responsável no cadastro do CNO. |
