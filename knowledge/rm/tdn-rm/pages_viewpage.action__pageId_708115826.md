---
content_hash: 31054fac5ecd64b34e8d2b986250dcceb90effcf620fba8ae9d3060781a6001c
fetched_at: '2026-06-29T00:11:25.399322+00:00'
page_id: '708115826'
product: rm
source: tdn-rm
title: DT - Salário Família - Pagamento para dependente de guarda provisória
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=708115826
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS - Folha de Pagamento |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Cálculo Salário Família |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHCALCRM-975](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-975) |

## **02. SITUAÇÃO/REQUISITO**

Conforme Instrução Normativa 77/2015: Os trabalhadores que possuem guarda provisória para fins de adoção ou outra finalidade se equipara a pai/mãe para fins de recebimento de salário família. As cotas do salário família serão devidas desde que o trabalhador esteja dentro do teto/limite de remuneração devido.IN 77/2015, Art. 134. Equiparado a filho: certidão judicial de tutela e, em se tratando de enteado, certidão de casamento do segurado e de nascimento do dependente, observado o disposto no art.126; Art. 359. Salário-família é o benefício pago na proporção do respectivo número de filhos ou equiparados de qualquer condição até a idade de quatorze anos ou inválido de qualquer idade, independente de carência e desde que o salário de contribuição seja inferior ou igual ao limite máximo permitido nos termos do § 2º deste artigo, ao segurado empregado, exceto ao empregado doméstico, e ao trabalhador avulso. ([https://www.empresario.com.br/legislacao/edicoes/2018/0605\_guarda\_provisoria\_crianca.html](https://www.empresario.com.br/legislacao/edicoes/2018/0605_guarda_provisoria_crianca.html "Follow link"))

## **03. SOLUÇÃO**

Conforme mapeamento do eSocial, o tipo "6 - Irmão(ã), neto(a) ou bisneto(a) sem arrimo dos pais, do(a) qual detenha a guarda judicial." enviar conforme os tipos de dependentes cadastro no sistema abaixo:

Caso PFDEPEND.GRAUPARENTESCO seja "I - IrmaoValido" ou "N = IrmaoInvalido" ou "T - Neto" retorna "6 – Irmão (ã), neto(a) ou bisneto(a) sem arrimo dos pais, do(a) qual detenha a guarda judicial.

* Tratar no cálculo para quando for esses tipos ("I - IrmaoValido" ou "T - Neto") de dependentes e tenha as configurações iguais a tipo 1 - Filho Valido, lance o salário Família, sem necessidade de flag para forçar o valor
* Tratar no cálculo para quando o tipo "N = IrmaoInvalido" de dependente e tenha as configurações iguais a tipo 3 – Filho(a) Invalido, lance o salário família sem necessidade de marcar a flag para forçar o valor
* Tratar na liberação de competência para atualizar o histórico de dependentes de Salário Família

## **04.****ASSUNTOS RELACIONADOS**

* [Dependentes](https://tdn.totvs.com/display/LRM/Dependentes)
