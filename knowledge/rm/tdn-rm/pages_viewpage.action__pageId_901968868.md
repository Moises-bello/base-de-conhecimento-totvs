---
content_hash: 7d943a01d60d7e6040d84be0f5664994a0c088ecc01965b12a3454abb54e4486
fetched_at: '2026-06-29T00:12:02.654903+00:00'
page_id: '901968868'
product: rm
source: tdn-rm
title: DT - RRA - Diferenças Salariais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=901968868
version: 10
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS RH |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Cálculo de RRA |
| País: | Brasil |
| Ticket: | 21908282; 22334590; 22356686; 22185394; 19168052; 19110638; 19358686 |
| Issue: | [DRHCALCRM-7528](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-7528); [DRHCALCRM-7760](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-7760); [DRHCALCRM-7761](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-7761); [DRHCALCRM-7677](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-7677);  [DRHCALCRM-6054](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-6054); [DRHCALCRM-6094](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-6094) |

## **02. SITUAÇÃO/REQUISITO**

Conforme o DECRETO Nº 9580, DE 22 DE NOVEMBRO DE 2018, (DOU DE 23.11.2018), SEÇÃO VI:  
DOS RENDIMENTOS RECEBIDOS ACUMULADAMENTE  
Art. 48 - Os rendimentos recebidos acumuladamente e submetidos à incidência do imposto sobre a renda com base na tabela progressiva, quando correspondentes a \*\* anos-calendário anteriores ao do recebimento \*, serão tributados exclusivamente na fonte, no mês do recebimento ou do crédito, separadamente dos demais rendimentos recebidos no mês, observado o disposto no art. 702 ao art. 706. (Lei nº 7713, de 1988, art. 12-A).

Porém existe situações que, apesar de envolverem pagamentos que se referem a períodos anteriores, **não são considerados como Rendimentos Recebidos Acumuladamente (RRA)**, pois não há um reajuste salarial retroativo:

**Pagamentos com Caixa Original em Anos Anteriores, mas Projeções no Ano Atual (Exemplo: Férias, Rescisão com Aviso):**

* **Exemplo:** O trabalhador tem direito a férias ou projeção de aviso prévio no ano atual, mas o pagamento (o caixa) ocorreu em um ano anterior e ele tem um reajuste salarial no ano atual.
* **Explicação:** Nesses casos, as projeções (ou o direito) se referem ao ano atual, ou seja, são valores devidos por um período que se estende para o ano atual.
* **Conclusão:** Embora o pagamento original tenha ocorrido em um ano anterior, para um cálculo de diferenças, ele **não é considerado como RRA**, pois não envolve o recebimento de rendimentos acumulados de anos anteriores (no sentido de um reajuste salarial retroativo a anos-calendários anteriores). Trata-se de valores devidos pelo período de competência, mesmo que o caixa tenha sido feito no passado. A projeção de valores para o ano atual mantém esse pagamento fora da classificação de RRA.

**Pagamentos de Diferenças Salariais com Competência no Ano Atual, mas o Caixa no Próximo Ano (Exemplo: Competência 12 e Caixa 01):**

* **Exemplo:** A competência é em dezembro (do ano atual), mas o pagamento efetivo do valor das diferenças salariais ocorre em janeiro (do ano seguinte).
* **Explicação:** Nesse cenário, a competência de pagamento das diferenças salariais refere-se ao ano atual, mas o pagamento é realizado no ano seguinte, o que pode gerar confusão. No entanto, como o pagamento é referente a um direito de competência do ano atual, e não a ajustes a anos-calendários retroativos, ele também não seria considerado RRA.
* **Conclusão:** A diferença salarial é devida em razão do trabalho realizado no ano de competência, mesmo que o pagamento (o caixa) ocorra no ano seguinte. Isso **não configura RRA**, pois não envolve um ajuste retroativo para períodos de anos anteriores.

**Resumo:**

* **RRA** é considerado apenas quando há um **ajuste salarial retroativo** que abrange rendimentos de anos-calendários anteriores (com efeitos retroativos para salários de anos passados).
* Nos casos acima, **não há retroatividade salarial** que modifique os rendimentos de anos anteriores, mas sim o pagamento de valores devidos por direito ao trabalhador no ano atual, o que os desclassifica como **RRA**.

## **03. SOLUÇÃO**

Foi adequado o cálculo do RRA para que tratasse os cenários onde as diferenças salariais que não contemplavam anos calendários anteriores, mesmo que a data de pagamento original fosse anos anteriores. Também foi ajustado para que cálculos de diferenças salariais realizado em competência de ano atual mas caixa de pagamento no próximo ano não fosse considerado como RRA e sim como um rendimento normal

## **04. DEMAIS INFORMAÇÕES**

## **05. ASSUNTOS RELACIONADOS**

* [Orientações Consultoria de Segmentos - Apuração e tributação de rendimento recebido acumuladamente (RRA)](https://tdn.totvs.com.br/pages/releaseview.action?pageId=152801855)
* [Aviso Prévio - Reajuste Salarial - Aviso Prévio 90 dias](https://tdn.totvs.com.br/pages/releaseview.action?pageId=898436786)
