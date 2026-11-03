---
content_hash: 94d0a7da294efa59b5db3edca604ab00f5d617ef644c2363896996adfde0f40d
fetched_at: '2026-06-29T00:10:53.789809+00:00'
page_id: '585318935'
product: rm
source: tdn-rm
title: Alterações S-1000
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=585318935
version: 7
---

false

**A partir das Versões:**

* 12.1.29.282
* 12.1.31.197
* 12.1.32.135
* e Superiores.

# Objetivo:

---

Apresentar as alterações realizadas no evento S-1000 para o leiaute do eSocial Versão S-1.0.

---

|  |  |  |
| --- | --- | --- |
| **GRUPO/CAMPO/ITEM** | **DE** | **PARA** |
| Grupo {contato} e respectivos campos | Excluido o grupo {contato} e respectivos campos: Nome, CPF, fone fixo, fone celular e email |  |
| Grupo {softwareHouse} e respectivos campos | Excluído o grupo {softwareHouse} e respectivos campos: cnpj, razão social, nome contato, telefone e email |  |
| Grupo {infoComplementares} | Excluído o grupo {infoComplementares} |  |
| Grupo {situacaoPJ} | Excluído o grupo {situacaoPJ} e respectivos campos: indicativo da situação PJ |  |
| Grupo {situacaoPF} | Excluído o grupo {situacaoPF} e respectivos campos: indicativo da situação PF |  |
| Grupo {infoOrgInternacional} – alterada condição | O (se {natJurid} tem o algarismo '5' na primeira posição) | O (se a natureza jurídica pertencer ao grupo [5]); |
| Grupo {ideEmpregador} Campo nrInsc | Alterado tamanho: 15 | Tamanho: 14 |
| Grupo {ideEmpregador} Campo nrInsc | Informar o número de inscrição do contribuinte de acordo com o tipo de inscrição indicado no campo {tpInsc}. Se for um CNPJ deve ser informada apenas a Raiz/Base de oito posições, exceto se natureza jurídica de administração pública direta federal ([101-5], [104-0], [107-4], [116-3], situação em que o campo deve ser preenchido com o CNPJ completo (14 posições). Validação: Se {tpInsc} for igual a [1], deve ser um número de CNPJ válido. Se {tpInsc} for igual a [2], deve ser um CPF válido. | Informar o número de inscrição do contribuinte de acordo com o tipo de inscrição indicado no campo {tpInsc}. Validação: Se {tpInsc} for igual a [1], deve ser um número de CNPJ válido. Neste caso, deve ser informada apenas a raiz/base (8 posições), exceto se natureza jurídica do declarante for igual a ([1015, 1040, 1074, 1104, 1139, 1163, 1198, 1252, 1287, 1317, 1341]), situação em que o campo deve ser preenchido com o CNPJ completo (14 posições). Se {tpInsc} for igual a [2], deve ser um CPF válido. |
| Grupo {infoCadastro}  Campo nmRazao | Excluído |  |
| Grupo {infoCadastro}  Campo natJurid | Excluído |  |
| Grupo {infoCadastro}  Campo indCoop | Somente pode ser diferente de ZERO se {natJurid} for igual a [2143]. | Somente pode ser diferente de ZERO se a natureza jurídica do declarante for igual a [2143]. |
| Grupo {infoCadastro}  Campo indEntEd | Excluído |  |
| Grupo {infoCadastro}  Campo indEtt | Excluído |  |
| Grupo {infoCadastro}  Campo nrRegEtt | Excluído |  |

Os campos relacionados acima como excluídos somente não serão informados no XML. Esses campos continuarão presentes no cadastro sem obrigatoriedade, exceto para o campo Natureza Jurídica porque há necessidade da informação desse campo para outras validações. E também não há mais necessidade de cadastrar a Software House.
