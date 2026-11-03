---
content_hash: 24ac78acf476199fe4528305d0668a86a9fd73c16228a20b0cdf6be8e6f8f52a
fetched_at: '2026-06-29T00:11:11.067461+00:00'
page_id: '645258288'
product: rm
source: tdn-rm
title: S-1000 - Informações do Empregador Órgão Público
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=645258288
version: 4
---

false

**A partir das Versões:**

* 12.1.29.282
* 12.1.31.197
* 12.1.32.135
* e Superiores.

# Objetivo:

---

Apresentar as alterações realizadas no evento S-1000 para atender ao leiaute do eSocial, versão S-1.0, para o grupo 4.

---

|  |  |
| --- | --- |
| **GRUPO/CAMPO/ITEM** | **Alterações** |
| Grupo {ideEmpregador} e campo nrInsc. | Se tpInsc for igual a [1], deve ser um número de CNPJ válido. Neste caso, deve ser informada apenas a raiz/base (8 posições), exceto se natureza jurídica do declarante for igual a 101-5, 104-0, 107-4, 110-4, 113-9, 116-3, 119-8, 125-2, 128-7, 131-7 ou 134-1, situação em que o campo deve ser preenchido com o CNPJ completo (14 posições).Se tpInsc for igual a [2], deve ser um CPF válido.Excluido o grupo {contato} e respectivos campos: Nome, CPF, fone fixo, fone celular e email |
| Grupo {ideEmpregador} e campo NatJur. | Foram inseridos novos códigos de natureza jurídica que são relativos aos órgãos públicos. 128-7: Fundo Público da Administração Indireta Federal 134-1: União |
| Grupo {ideEmpregador} e campo NatJur. | Criado o campo CNPJ do Ente Federativo Responsável - EFR.Preenchimento obrigatório e exclusivo se a natureza jurídica do declarante for Administração Pública (grupo [1]). Nesse caso, informar o campo com 14 (catorze) algarismos. |
