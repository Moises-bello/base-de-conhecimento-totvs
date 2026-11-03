---
content_hash: fd4d6bd6f853ff2521a81e9cd0cd2c20139c54f1b3cfc9d2c3c19d13211aff02
fetched_at: '2026-06-29T00:11:49.740346+00:00'
page_id: '837863074'
product: rm
source: tdn-rm
title: DT - S-2299 e S-2399 - Tratativa nos dados da Pensão Alimentícia
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=837863074
version: 4
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | S-2299 e S-2399 - Tratativa nos dados da Pensão Alimentícia |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-9725](https://jiraproducao.totvs.com.br/browse/DRHROTRM-9725) |

## **02.** **LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2306.249
* 12.1.2310.190
* 12.1.2402.127 e superiores.

## **03.****SITUAÇÃO/REQUISITO**

Na geração dos eventos S-2299 e S-2399, as tags abaixo estão sendo geradas com base nas informações do cadastro de dependentes dos dados da pensão. Entretanto, o correto é que sejam geradas somente quando houver decisão judicial para que determinado percentual do saque do FGTS seja revertido para o beneficiário da pensão alimentícia.

| Tag | Descrição |
| --- | --- |
| pensAlim | Indicativo de pensão alimentícia para fins de retenção de FGTS. Valores válidos: 0 - Não existe pensão alimentícia 1 - Percentual de pensão alimentícia 2 - Valor de pensão alimentícia 3 - Percentual e valor de pensão alimentícia **Validação:** Preenchimento obrigatório e exclusivo se o vínculo for celetista (tpRegTrab em S-2200 = [1]). |
| percAliment | Percentual a ser destinado a pensão alimentícia. **Validação:** Deve ser maior que 0 (zero) e menor ou igual a 100 (cem). Informação obrigatória e exclusiva se pensAlim = [1, 3]. |
| vrAlim | Valor da pensão alimentícia. **Validação:** Deve ser maior que 0 (zero). Informação obrigatória e exclusiva se pensAlim = [2, 3]. |

## **04.****SOLUÇÃO**

Inicialmente, efetuamos o ajuste na geração dos eventos S-2299 e S-2399 para indicar "0-Não existe pensão alimentícia". Isso garantirá que o FGTS do funcionário não seja retido, conforme descrito abaixo.

Em breve, estaremos disponibilizando um parâmetro no cadastro de dependentes nos dados da pensão, permitindo que o usuário determine se o FGTS será retido, conforme detalhado na issue  [DRHROTRM-9904](https://jiraproducao.totvs.com.br/browse/DRHROTRM-9904 "View this issue").

## **05. DEMAIS INFORMAÇÕES**

[Perguntas e Respostas eSocial](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/perguntas-frequentes#:~:text=Como%20se%20d%C3%A1%20essa%20intera%C3%A7%C3%A3o,informados%20no%20evento%20S%2D1210)

[S-2299 - Desligamento](https://tdn.totvs.com.br/display/public/LRM/S-2299+-+Desligamento)

[S-2399 - Trabalhador Sem Vínculo de Emprego/Estatutário](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719061)
