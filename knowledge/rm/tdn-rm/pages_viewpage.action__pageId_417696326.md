---
content_hash: 6b206048419c400bc423916a6f9a8c055fb53de53cf8ea352d3f2a221c6fffaf
fetched_at: '2026-06-29T00:09:12.364942+00:00'
page_id: '417696326'
product: rm
source: tdn-rm
title: Nota Técnica nº 09/2018
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=417696326
version: 18
---

---

Considerando a necessidade de ajustes na versão 2.4.02 leiaute do eSocial, disponibilizamos abaixo a relação das adequações realizadas.

Data prevista para implantação no ambiente de Produção Restrita: 27/09/2018.  
Data prevista para implantação no ambiente de Produção: 27/09/2018.

| EVENTO | GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- | --- |
| AJUSTES JÁ IMPLEMENTADOS (DISPONÍVEIS NOS AMBIENTES DE PRODUÇÃO RESTRITA E PRODUÇÃO) | | | |
| Tabela 21 | Alterados códigos de natureza jurídica [330-6] e [412-4] | 330-6 (...) 412-4 | **330-1** (...) **412-0** |
| AJUSTES QUE FLEXIBILIZAM VALIDAÇÕES E CONDIÇÕES DE PREENCHIMENTO | | | |
| S-1000 | Grupos {dadosIsencao}: alterada condição. | O(se {classTrib} for igual a [80]) N(nos demais casos) | **OC** (se {classTrib} for igual a [80]); N (nos demais casos) |
| S-2299 | Campo {nrCertObito}: alterada validação. | Validação: Deve ser preenchido se {mtvDeslig} for igual a [09,10]. Deve ser uma certidão de óbito válida, de acordo com o padrão de certidões estabelecido para Registro Civil das Pessoas Naturais. O 15° dígito deve ser igual a [4, 7]. | Validação: ~~**Deve ser preenchido se {mtvDeslig} for igual a [09,10].**~~ Não preencher se {mtvDeslig} for diferente de [10]. **Se informado**, deve ser uma certidão de óbito válida, de acordo com o padrão de certidões estabelecido para Registro Civil das Pessoas Naturais. O 15° dígito deve ser igual a [4, 7]. |
| AJUSTES DESCRITIVOS | | | |
| S-1010 | Campos {ideProcessoFGTS/nrProc}: alterada descrição. | Informar um número de processo cadastrado através do evento S-1070, cujo {indMatProc} seja igual a [7]. | Informar um número de processo cadastrado através do evento S-1070, cujo {indMatProc} seja igual a **[1, 7]**. |
| S-1070 | Campos {indMatProc}: alterada descrição. | Indicativo da matéria do processo ou alvará judicial: 1 - Tributária; 2 - Autorização de trabalho de menor; 3 - Dispensa, ainda que parcial, de contratação de pessoa com deficiência (PCD); 4 - Dispensa, ainda que parcial, de contratação de aprendiz; 5 - Segurança e Saúde do Trabalho; 6 - Conversão de Licença Saúde em Acidente de Trabalho; 7 - FGTS ou Contribuição Social Rescisória (Lei Complementar 110/2001); 8 - Contribuição sindical; 99 - Outros assuntos. | Indicativo da matéria do processo ou alvará judicial: **1 - Exclusivamente tributária ou tributária e FGTS;** 2 - Autorização de trabalho de menor; 3 - Dispensa, ainda que parcial, de contratação de pessoa com deficiência (PCD); 4 - Dispensa, ainda que parcial, de contratação de aprendiz; 5 - Segurança e Saúde do Trabalho; 6 - Conversão de Licença Saúde em Acidente de Trabalho; 7 - **Exclusivamente** FGTS e/ou Contribuição Social Rescisória (Lei Complementar 110/2001); 8 - Contribuição sindical; 99 - Outros assuntos. |
| S-2299 | Campo {procCS/nrProcJud}: alterada descrição (inclusive validação). | Informar um número de processo judicial cadastrado através do evento S-1070, cujo {indMatProc} seja igual a [7]. Validação: Deve ser um número de processo judicial válido e existente na Tabela de Processos (S-1070), com {indMatProc} = [7]. | Informar um número de processo judicial cadastrado através do evento S-1070, cujo {indMatProc} seja igual a [1, 7]. Validação: Deve ser um número de processo judicial válido e existente na Tabela de Processos (S-1070), com {indMatProc} = [1, 7]. |
| S-2299 e S-2399 | Campo {verbasResc/nrProcJud}: alterada descrição. | Informar um número de processo judicial cadastrado através do evento S-1070, cujo {indMatProc} seja igual a: - [1] se {tpTrib} = [1, 2]; - [7] se {tpTrib} = [3]; - [8] se {tpTrib} = [4]. | Informar um número de processo judicial cadastrado através do evento S-1070, cujo {indMatProc} seja igual a: - [1] se {tpTrib} = [1, 2]; - [1, 7] se {tpTrib} = [3]; - [8] se {tpTrib} = [4]. |
| DEMAIS AJUSTES | | | |
| S-1000 | Campos {natJurid}: alterada validação. | Validação: O preenchimento do campo é obrigatório e exclusivo para empregador PJ e administração pública. Neste caso, deve ser um código existente na tabela 21 e compatível com a informação constante no CNPJ. Se {classtrib} = [85], o número da {natJurid} deve iniciar por 1 (exemplo: 101-5, 112-0, etc.). | Validação: O preenchimento do campo é obrigatório e exclusivo para empregador PJ e administração pública. Neste caso, deve ser um código existente na tabela 21 e compatível com a informação constante no CNPJ. Se {classtrib} = [85], o número da {natJurid} deve iniciar por 1 (exemplo: 101-5, 112-0, etc.). **Não é permitida a utilização dos códigos 402-2 e 412-0.** |
| S-2200 e S-2206 | Campo {tpRegPrev}: alterada validação. | Validação: Se {codCateg} = [104], deve ser preenchido com [1]. | Validação: Se {codCateg} = [104], deve ser preenchido com [1]. **Se {codCateg} = [101, 102, 103, 105, 106, 111], não pode ser preenchido com [2].** |
| S-2300 | Campo {tpRegPrev}: incluída validação. | - | Validação: Se {categOrig} for relativa a Empregado, não pode ser preenchido com [2]. |
| REGRA\_COMPATIB\_  REGIME\_PREV | Alterada descrição. | O evento S-1200 só é permitido para informação de remuneração relativa a trabalhador cujo contrato de trabalho esteja vinculado ao Regime Geral de Previdência Social - RGPS ou por Regime de Previdência Social no Exterior. O evento S-1202 só é permitido para informação de remuneração relativa a trabalhador amparado por Regime Próprio de Previdência Social ou por Regime de Previdência Social no Exterior.  Observar o que segue:  1 - O S-1200 é permitido para informação de remuneração de trabalhadores:  a) cujo {codCateg} for igual a [1XX], [2XX], [401], [7XX], [9XX];  b) cujo {codCateg} for igual a [3XX] e {tpRegPrev} = [1];  c) cujo {codCateg} for igual a [410] e {tpRegPrev} relativo ao contrato de trabalho firmado com a empresa cedente/de origem for igual a [1];  d) cujo {codCateg} for igual a [410], {tpRegPrev} = [3] e {categOrig} relativa ao contrato de trabalho firmado com a empresa cedente/de origem for diferente de [3XX].  2 - O S-1202 só permitido para informação de remuneração de trabalhadores:  a) cujo {codCateg} for igual a [3XX, 410] e {tpRegPrev} = [2,3];  b) cujo {codCateg} for igual a [410] e {tpRegPrev} relativo ao vínculo firmado com o órgão público cedente/de origem for igual a [2];  c) cujo {codCateg} for igual a [410], {tpRegPrev} = [3] e {categOrig} relativa ao vínculo firmado com o órgão público cedente/de origem for igual a [3XX]. | O evento S-1200 só é permitido para informação de remuneração relativa a trabalhador cujo contrato de trabalho esteja vinculado ao Regime Geral de Previdência Social - RGPS ou por Regime de Previdência Social no Exterior. O evento S-1202 só é permitido para informação de remuneração relativa a trabalhador amparado por Regime Próprio de Previdência Social ou por Regime de Previdência Social no Exterior.  Observar o que segue:  1 - O S-1200 é permitido para informação de remuneração de trabalhadores:  **a) desligados na empresa sucedida, mas com remuneração devida na sucessora ({remunSuc} = [S]), independentemente de código de categoria;**  **b) cujo {codCateg} for igual a [1XX] e {tpRegPrev} = [1,3];**  **c)** cujo {codCateg} for igual a ~~**[1XX],**~~ [2XX], [401], [7XX], [9XX];  **d)** cujo {codCateg} for igual a [3XX] e {tpRegPrev} = [1];  **e)** cujo {codCateg} for igual a [410] e {tpRegPrev} relativo ao contrato de trabalho firmado com a empresa cedente/de origem for igual a [1];  **f)** cujo {codCateg} for igual a [410], {tpRegPrev} = [3] e {categOrig} relativa ao contrato de trabalho firmado com a empresa cedente/de origem for diferente de [3XX].  2 - O S-1202 só é permitido para informação de remuneração de trabalhadores:  a) cujo {codCateg} for igual a [3XX, 410] e {tpRegPrev} = [2,3];  b) cujo {codCateg} for igual a [410] e {tpRegPrev} relativo ao vínculo firmado com o órgão público cedente/de origem for igual a [2];  c) cujo {codCateg} for igual a [410], {tpRegPrev} = [3] e {categOrig} relativa ao vínculo firmado com o órgão público cedente/de origem for igual a [3XX]. |

falsefalse

**Produto:** Folha de Pagamento

false

**Rotina:** eSocial

false

**Versões:**

|  |
| --- |
| 12.1.23 |
| 12.1.22 |
| 12.1.21.126 |
| 12.1.20.385 |
| 12.1.19.386 |

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autor:**
