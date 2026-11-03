---
content_hash: 3d7ea03d446c81674e8e23bb932d0e5cf49923ec64de39ce9cf09efc2258007d
fetched_at: '2026-06-29T00:10:53.903417+00:00'
page_id: '589523348'
product: rm
source: tdn-rm
title: Alterações S-2230
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=589523348
version: 5
---

false

**A partir das Versões:**

* 12.1.29.282
* 12.1.31.197
* 12.1.32.135
* e Superiores.

# Objetivo:

---

Apresentar as alterações realizadas no evento S-2230 para o leiaute do eSocial Versão S-1.0.

---

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Grupos {perAquis}:  alterada Ocorrência | Grupo novo | Período aquisitivo de férias Condição: O (se codMotAfast = [15] E  (o código de categoria no RET for igual a  [1XX, 301, 302, 303, 304, 306, 307, 309, 310,  312, 410] com {tpRegTrab} em S-2200/S-2300  = [1] OU o código de categoria no RET for  igual a [401] com tpRegTrab em S-2300 = [1] ou não informado) E dtIniAfast >= [2021-05-10]); N (nos demais casos) |
|  |  |  |
| Grupos {infoAtestado}: |  | Excluido |
| Grupos {emitente}: |  | Excluido |
| Grupos {ideVinculo}: Campo codcateg  Alteração da descrição | Preencher com o código da categoria do trabalhador,  conforme Tabela 01.  Validação: Só informar se o trabalhador tiver sido registrado como TSVE - Trabalhador Sem Vínculo de Emprego/Estatutário,  através do evento S-2300. Não informar nos demais casos. Se informado, deve existir na Tabela de Categorias de Trabalhadores (Tabela 01). | Preencher com o código da categoria do trabalhador. Informar somente no caso de TSVE sem informação  de matrícula no evento S-2300.  Validação: Informação obrigatória e exclusiva se não houver preenchimento de matricula. Se informado,  deve ser um código válido e existente na Tabela 01. |
| Grupos{iniAfastamento}:  Campo {dtIniAfast}   A | Data de início do afastamento.  Validação: Deve-se obedecer às seguintes regras: a) A data deve ser igual ou posterior a data de  admissão do vínculo ao qual se refere o evento  (no caso de sucessão ou mudança de CPF, igual  ou posterior à data da transferência ou à data de  alteração do CPF, respectivamente);  b) Não pode ser superior à data atual exceto se  {codMotAfast} = [15] (férias), situação em que pode  ser até 60 dias superior à data atual;  c) É necessário  que o trabalhador esteja, antes da data de início do  afastamento, em atividade, ou seja, não pode existir  evento de afastamento anterior a {dtIniAfast} sem que  este tenha sido encerrado | Data de início do afastamento.  Validação: Deve-se obedecer às seguintes regras: a) Não pode ser posterior à data atual, exceto se:  a1) codMotAfast = [15] (férias), situação em que pode  ser até 60 dias posterior à data atual;  a2) codMotAfast = [18], situação em que pode ser até  120 dias posterior à data atual;  b) É necessário que o trabalhador esteja, antes  da data de início do afastamento, em atividade,  ou seja, não pode existir evento de afastamento  anterior a dtIniAfast sem que este tenha sido  encerrado. |
