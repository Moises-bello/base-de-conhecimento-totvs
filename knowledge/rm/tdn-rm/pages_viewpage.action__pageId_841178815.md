---
content_hash: 6b250fe7c4619026262668d392a1983a012a46427364891227e77a24f36a8ab1
fetched_at: '2026-06-29T00:11:50.462995+00:00'
page_id: '841178815'
product: rm
source: tdn-rm
title: DT - S-2299 e S-2399 - Tratativa nos dados da Pensão Alimentícia quando possui
  retenção no FGTS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=841178815
version: 6
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | S-2299 e S-2399 - Tratativa nos dados da Pensão Alimentícia quando possui retenção no FGTS |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-9904](https://jiraproducao.totvs.com.br/browse/DRHROTRM-9904) |

## **02.** **LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2306.258 e superiores.
* 12.1.2310.203 e superiores.
* 12.1.2402.143 e superiores.

## **03.****SITUAÇÃO/REQUISITO**

Na geração dos eventos S-2299 e S-2399, as tags abaixo deverão ser geradas com base nas informações e parâmetro "Possui Retenção FGTS" do cadastro de dependentes dos dados da pensão. 

| Tag | Descrição |
| --- | --- |
| pensAlim | Indicativo de pensão alimentícia para fins de retenção de FGTS. Valores válidos: 0 - Não existe pensão alimentícia 1 - Percentual de pensão alimentícia 2 - Valor de pensão alimentícia 3 - Percentual e valor de pensão alimentícia **Validação:** Preenchimento obrigatório e exclusivo se o vínculo for celetista (tpRegTrab em S-2200 = [1]). |
| percAliment | Percentual a ser destinado a pensão alimentícia. **Validação:** Deve ser maior que 0 (zero) e menor ou igual a 100 (cem). Informação obrigatória e exclusiva se pensAlim = [1, 3]. |
| vrAlim | Valor da pensão alimentícia. **Validação:** Deve ser maior que 0 (zero). Informação obrigatória e exclusiva se pensAlim = [2, 3]. |

## **04.****SOLUÇÃO**

Implementado o parâmetro "**Possui Retenção FGTS**" no cadastro de dependentes. Ao ativá-lo, o sistema passará a gerar automaticamente as tags de informação sobre pensão alimentícia, de acordo com os dados cadastrados.

Esse parâmetro deve ser marcado apenas quando houver decisão judicial que estabeleça que um percentual do saque do FGTS seja destinado ao beneficiário da pensão alimentícia.

1) Acesse o menu Funcionários | Anexos Dependentes | Aba Dados da Pensão e marque o campo conforme demonstração abaixo:

2) Ao gerar o XML do evento S-2299 ou S-2399 a tag será preenchida conforme demonstrado abaixo:

## **05. DEMAIS INFORMAÇÕES**
