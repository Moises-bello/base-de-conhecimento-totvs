---
article_id: 360015857031
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 846b052436f64314a32f0c53518336f7eacf6689738a4d0e8b65c4c0f56bc3d1
fetched_at: '2026-06-28T22:37:21.691801+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Conceito do Parâmetro
  MV_CNPROCP - Títulos Provisórios
type: support-article
updated_at: '2025-11-04T18:11:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015857031-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Conceito-do-Par%C3%A2metro-MV-CNPROCP-T%C3%ADtulos-Provis%C3%B3rios
---

**Dúvida**

Conceito do Parâmetro **MV\_CNPROCP** - Títulos Provisórios  
  
**Ambiente**

Microsiga Protheus - à partir da release 12.1.17  
  
  
**Solução**

Apareceram algumas dúvidas sobre as condições de pagamento do GCT (**Contrato e Planilha**) e seu impacto nos títulos provisórios. Segue abaixo a diferenciação de cada uma, a título de conhecimento:

* A condição de pagamento informada no momento onde é incluído o cronograma financeiro serve apenas para quebrar as parcelas do cronograma, ou seja, caso seja informada uma condição de pagamento em 3x serão 3 parcelas no cronograma.
* Para ativar a geração de títulos provisórios ative o parâmetro **MV\_CNPROVI:**

Na rotina de manutenção de contrato ( CNTA300 ), ao incluir um contrato de compras, na aba planilha, ao selecionar **o campo Nota/Título = Nota Fiscal** e torná-lo vigente: Será gerado um título provisório, tipo PR, no caso em contas à pagar, o qual será excluído, quando for incluída e encerrada uma medição, pois neste momento será gerado um pedido de compras.

Ao selecionar o **campo Nota/Título =Título** e torná-lo vigente: Será gerado um título provisório, tipo PR, no caso em contas à pagar, o qual será **substítuído**  quando for incluída e encerrada uma medição, pois neste momento será gerado um título efetivo no contas à pagar.

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5100876837015)**

Dessa forma o parâmetro **MV\_CNPROCP** tem influência apenas nos títulos Provisórios (PR) referente às parcelas do Cronograma Financeiro, que são gerados ao tornar o contrato Vigente.

Caso o parâmetro **MV\_CNPROCP** esteja como “S” para cada parcela gerada pelo cronograma financeiro serão gerados N títulos provisórios de acordo com a condição de pagamento do contrato (CN9). Exemplo: temos um contrato com 10 parcelas, foi colocado uma condição de pagamento de 3x no cabeçalho do contrato, serão gerados 3 títulos provisórios para cada parcela do cronograma financeiro.

O parâmetro **MV\_CNPROCP** com valor "S", aplica a condição de pagamento no momento de gerar os títulos provisórios nas parcelas já divididas no cronograma pela condição de pagamento.  
Esta situação causa o parcelamento do parcelamento, e o parâmetro **MV\_CNPROCP** deve conter valor "N" ao se utilizar a criação de um cronograma pela condição de pagamento.

Veja exemplo no artigo: [Parâmetro MV\_CNPROCP (Titulo Provisórios)](http://tdn.totvs.com/pages/viewpage.action?pageId=283403804)

**Obs** : Para que os títulos provisórios tenham a mesma data de vencimento informada na aba Cronograma Financeiro quando na inclusão utilizar a Periocidade na opção de Condição de Pagamento, utilizar o parâmetro **MV\_CNPROCP = N**.

***Saiba Mais:***

[Parâmetro MV\_CNPROCP (Titulo Provisórios)](http://tdn.totvs.com/pages/viewpage.action?pageId=283403804)

[MP - SIGAGCT - Como desativar a geração de títulos provisórios na mudança de situação do contrato ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018381871-MP-GCT-Como-desativar-a-gera%C3%A7%C3%A3o-de-t%C3%ADtulos-provis%C3%B3rios-na-mudan%C3%A7a-de-situa%C3%A7%C3%A3o-do-contrato)

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Vencimento do Titulo gerado na Medição não respeira Condição de Pagamento do Contrato](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21620710853783-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Vencimento-do-Titulo-gerado-na-Medi%C3%A7%C3%A3o-n%C3%A3o-respeira-Condi%C3%A7%C3%A3o-de-Pagamento-do-Contrato)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)
