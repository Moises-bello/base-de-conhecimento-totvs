---
content_hash: f76db3edbc52828a63f617cc555546e4f7e20f71013794a0d592eac9b82efe34
fetched_at: '2026-06-29T00:11:45.788968+00:00'
page_id: '821579406'
product: rm
source: tdn-rm
title: DT - S-1210 - Dependentes do TOTVS Gestão Financeira - Alterações relacionadas
  ao Leiaute S-1.2
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=821579406
version: 8
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | eSocial - S-1210 - Dependentes do TOTVS Gestão Financeira |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | DRHROTRM-7175 |

## **02.** **VERSÕES**

Lembrando que, será a partir dos patches:

* 12.1.2302.258
* 12.1.2306.218
* 12.1.2310.150  ou superiores

## **03.****SITUAÇÃO/REQUISITO**

Adequar o produto TOTVS Folha de Pagamento para a geração do evento S-1210 de acordo com o leiaute S-1.2, incorporando o grupo {infoDep} e os respectivos campos (cpfDep, dtNascto, nome, depIRRF, tpDep, descrDep) para os autônomos cadastrados no TOTVS Gestão Financeira. Essa adaptação permitirá que as informações dos dependentes sejam devidamente registradas e transmitidas conforme as novas exigências do leiaute.

## **04.****SOLUÇÃO**

O sistema agora considera os dependentes cadastrados no TOTVS Gestão Financeira. Para isso, é necessário cadastrar os dependentes no anexo "Dependentes" do cadastro do Cliente/Fornecedor no TOTVS Gestão Financeira, conforme demonstrado abaixo:

 

**,**

**ATENÇÃO:**

* + Para obter detalhes sobre o cadastro do dependente, acesse [Dependentes do Cliente/Fornecedor](https://tdn.totvs.com/pages/releaseview.action?pageId=787858319)
  + O sistema gerará automaticamente os dependentes que estiverem dentro do período de início e fim do período de apuração gerado para o S-1210.
  + Sempre que o sistema encontrar um dependente para o período de apuração, lançará automaticamente o grupo <dedDepen>, utilizando o valor cadastrado na tabela de valores fixos.

Geração do XML do evento S-1210**:**

## **05. DEMAIS INFORMAÇÕES**
