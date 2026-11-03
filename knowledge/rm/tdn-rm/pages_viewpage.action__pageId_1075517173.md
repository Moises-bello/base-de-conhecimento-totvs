---
content_hash: f09a09e672b84f4bf65901f4cadb6b1ee018504c03748a996b6e8cf4f6dbe4b6
fetched_at: '2026-06-29T00:05:54.121209+00:00'
page_id: '1075517173'
product: rm
source: tdn-rm
title: DT - eSocial - Adequação para atender Rubricas de Férias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1075517173
version: 9
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento - eSocial |
| Função: | eSocial - Adequação para atender Rubricas de Férias |
| País: | Brasil |
| Issue: | [DRHROTRM-18304](https://jiraproducao.totvs.com.br/browse/DRHROTRM-18304) |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2506.330
* 12.1.2510.262
* 12.1.2602.176
* 12.1.2606 e superiores

## **03.****SITUAÇÃO/REQUISITO**

Adequação do produto TOTVS Folha de Pagamento para atendimento às alterações vigentes, contemplando a inclusão e atualização das rubricas relacionadas ao pagamento de férias.

Nesse contexto, foi instituída a nova rubrica 1015, destinada ao registro do adiantamento de férias, incluindo o terço constitucional.

Adicionalmente, foram atualizadas as descrições das rubricas 1016 e 1017.

* **Até 2025:** Utilizava-se a natureza 1016 tanto para o adiantamento quanto para o lançamento em folha, variando apenas as incidências de tributos.
* **A partir de 2026:** O adiantamento deve obrigatoriamente usar o código 1015 (com incidência de IR no pagamento), enquanto o gozo em folha permanece no 1016 (com incidência de INSS/FGTS).

| RUBRICA | DESCRIÇÃO DA NATUREZA DA RUBRICA ATÉ 31-12-2025 | DESCRIÇÃO DA NATUREZA DA RUBRICA A PARTIR 01-01-2026 |
| --- | --- | --- |
| 1015 - Adiantamento de férias | Não existia | Valor correspondente ao pagamento do adiantamento da remuneração de férias, inclusive do terço constitucional. |
| 1016 - Férias | Valor correspondente à remuneração devida na época da concessão das férias, inclusive o adiantamento de férias.  Nessa natureza deve ser classifica do também o valor pago mensalmente ao trabalhador avulso e ao empregado com contrato de trabalho intermitente, a título de férias | Valor correspondente à remuneração devida na época da concessão das férias.    Nessa natureza deve ser classifica do também o valor pago mensalmente ao trabalhador avulso e ao empregado com contrato de trabalho intermitente, a título de férias |
| 1017 - Terço constitucional de férias | Valor correspondente ao terço constitucional de férias relativo à remuneração devida na época da concessão das férias, inclusive o adiantamento de férias.  Nessa natureza deve ser classificado também o valor pago mensalmente ao trabalhador avulso e ao empregado com contrato de trabalho intermitente, a título de terço constitucional de férias | Valor correspondente ao terço constitucional de férias relativo à remuneração devida na época da concessão das férias.  Nessa natureza deve ser classificado também o valor pago mensalmente ao trabalhador avulso e ao empregado com contrato de trabalho intermitente, a título de terço constitucional de férias |

**Atenção:** As alterações estão destacadas em vermelho.

## **04. SOLUÇÃO**

Adequamos nosso produto TOTVS Folha de Pagamento para atender a [Nota Técnica 04/2025](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/nota-tecnica-s-1-3-04-2025-rev.pdf). Veja todos os detalhes no link disponibilizado no item "**Documentação**".

## **05. DOCUMENTAÇÃO**
