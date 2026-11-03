---
content_hash: 3b9aced0a7d677d54ae95f846e07c628775080cab98c09ca46a717fd06877849
fetched_at: '2026-06-29T00:10:53.723550+00:00'
page_id: '579131357'
product: rm
source: tdn-rm
title: Alterações S-1070
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=579131357
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

Apresentar as alterações realizadas no evento S-1070 para o leiaute do eSocial Versão S-1.0.

---

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Grupo {ideEmpregador} Campo {nrInsc} | Alterado tamanho: 15  Informar o número de inscrição do contribuinte de acordo com o tipo de inscrição indicado no campo {tpInsc}. Se for um CNPJ deve ser informada apenas a Raiz/Base de oito posições, exceto se natureza jurídica de administração pública direta federal ([101-5], [104-0], [107-4], [116-3], situação em que o campo deve ser preenchido com o CNPJ completo (14 posições). Validação: Se {tpInsc} for igual a [1], deve ser um número de CNPJ válido. Se {tpInsc} for igual a [2], deve ser um CPF válido. | Tamanho: 14  Informar o número de inscrição do contribuinte de acordo com o tipo de inscrição indicado no campo {tpInsc}. Validação: Se {tpInsc} for igual a [1], deve ser um número de CNPJ válido. Neste caso, deve ser informada apenas a raiz/base (8 posições), exceto se natureza jurídica do declarante for igual a ([1015, 1040, 1074, 1104, 1139, 1163, 1198, 1252, 1287, 1317, 1341]), situação em que o campo deve ser preenchido com o CNPJ completo (14 posições). Se {tpInsc} for igual a [2], deve ser um CPF válido. |
| Grupos {dadosProcJud}: alterada condição. | O (se {tpProc} = [2]) N (nos demais casos) | O (se tpProc = [2] e indMatProc = [1]); N (nos demais casos) |
| Grupos {ideProcesso}: Campo {tpProc} excluído valor[3]. | Preencher com o código correspondente ao tipo de processo: 1 - Administrativo; 2 - Judicial; 3 - Número de Benefício (NB) do INSS; 4 - Processo FAP de exercício anterior a 2019. Valores Válidos: 1, 2, 3, 4. | Preencher com o código correspondente ao tipo de processo. Valores válidos: 1 - Administrativo 2 - Judicial 4 - Processo FAP de exercício anterior a 2019 |
| Grupos {ideProcesso}: Campo {nrProc} alterada validação. | Informar o número do processo administrativo/judicial ou do benefício de acordo com o tipo informado em {tpProc}. Validação: Deve ser um número de processo/benefício válido e: a) Se {tpProc} = [1], deve possuir 17 (dezessete) ou 21 (vinte e um) algarismos; b) Se {tpProc} = [2], deve possuir 20 (vinte) algarismos; c) Se {tpProc} = [3], deve possuir 10 (dez) algarismos; d) Se {tpProc} = [4], deve possuir 16 (dezesseis) algarismos. Regra de validação: REGRA\_CARACTER\_ESPECIAL | Informar o número do processo administrativo/judicial de acordo com o tipo informado em tpProc. Validação: Deve ser um número de processo válido e: a) Se tpProc = [1], deve possuir 17 (dezessete) ou 21 (vinte e um) algarismos; b) Se tpProc = [2], deve possuir 20 (vinte) algarismos; c) Se tpProc = [4], deve possuir 16 (dezesseis) algarimos. |
| Grupos {dadosProc}: Campo {indMatProc} excluída validação e excluídos valores [ 2, 3, 4, 5, 6, 8, 99]. | Tamanho  2.  Indicativo da matéria do processo ou alvará judicial: 1 - Exclusivamente tributária ou tributária e FGTS; 2 - Autorização de trabalho de menor; 3 - Dispensa, ainda que parcial, de contratação de pessoa com deficiência (PCD); 4 - Dispensa, ainda que parcial, de contratação de aprendiz; 5 - Segurança e Saúde no Trabalho; 6 - Conversão de Licença Saúde em Acidente de Trabalho; 7 - Exclusivamente FGTS e/ou Contribuição Social Rescisória (Lei Complementar 110/2001); 8 - Contribuição sindical; 99 - Outros assuntos. Validação: Se {tpProc} = [3], deve ser preenchido com [6]. Valores Válidos: 1, 2, 3, 4, 5, 6, 7, 8, 99. | Tamanho  1.  Indicativo da matéria do processo. Valores válidos: 1 - Exclusivamente tributária ou tributária e FGTS 7 - Exclusivamente FGTS e/ou Contribuição Social Rescisória (Lei Complementar 110/2001) |

Foram realizados ajustes em alguns campos no cadastro de processos judiciais e validações na geração do XML.

Acesse **RH | Gestão de Pessoas | Gestão Organizacional | Processos Jurídicos | Processos Jurídicos**

No campo **Tipo de Processo**o campo excluído no eSocial está com a descrição (INATIVO)

No campo **Indicativo da matéria do processo ou alvará judicial**os campos excluídos no eSocial estão com a descrição (INATIVO)

**Tratativa da geração do XML**

No campo **Tipo de Processo** ao  selecionar o campo excluído no eSocial com a descrição (INATIVO), apresentará erro na geração.

No campo **Indicativo da matéria do processo ou alvará judicial**os campos excluídos no eSocial com a descrição (INATIVO), apresentará erro na geração.

Sistema passa a imprimir grupo dadosProcJud somente se tpProc = [2] e indMatProc = [1]
