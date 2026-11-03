---
article_id: 360017962152
category: Financeiro - Comissão
content_hash: baf705806a7a18b609208ce30a9d4e9b30d76e48f23f61f48e0a39aedaad3f17
fetched_at: '2026-06-28T22:37:50.810416+00:00'
product: protheus
section_id: 26655771327895
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA440 - Pontos de
  Entrada Recálculos Comissões
type: support-article
updated_at: '2026-04-13T18:53:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017962152-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA440-Pontos-de-Entrada-Rec%C3%A1lculos-Comiss%C3%B5es
---

**Dúvida**  
Quais são os pontos de entrada disponíveis na rotina de recálculo de comissões?  
   
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**

* **FA440VLD** - Validações de usuário para cálculo de comissão  
  <https://tdn.totvs.com/pages/releaseview.action?pageId=641148189>
* **SF2460I** - Atualização das tabelas referentes à nota fiscal  
  <http://tdn.totvs.com/pages/releaseview.action?pageId=6784447>
* **F440ABAS** - Altera base de comissão  
  <https://tdn.totvs.com/pages/releaseview.action?pageId=639944160>
* **F440CBASE** - Altera bases de comissão  
  <http://tdn.totvs.com/pages/releaseview.action?pageId=6071547>
* **F440JurDes** - Juros e Desconto na comissão  
  <http://tdn.totvs.com/pages/releaseview.action?pageId=6071604>
* **F440FAL** - Manipular a base na fatura e/ou liquidação.  
  <https://tdn.totvs.com/pages/releaseview.action?pageId=639944877>
* **FIN440PE** - Verificação dos percentuais de comissão  
  <http://tdn.totvs.com/pages/releaseview.action?pageId=6071281>
* **F440BASE** - Modifica dados da Comissão (P.E. é chamado quando a comissão está parametrizada na emissão)  
  <http://tdn.totvs.com/pages/releaseview.action?pageId=6071058>
* **F440VEND** - Comissão de vendedor   
  <https://tdn.totvs.com/pages/releaseview.action?pageId=639945790>
* **F440COM** - Cálculo da comissão para títulos de adiantamento  
  <http://tdn.totvs.com/pages/viewpage.action?pageId=6071705>
* **FINA440 -** Comissão na liquidação   
  <http://tdn.totvs.com/pages/viewpage.action?pageId=6070671>
* **F440DEL** - Trata comissão de recálculo.  
  <http://tdn.totvs.com/pages/viewpage.action?pageId=6071059>
* **MSE3440 -** Utilizado no tratamento complementar para gravação da comissão (SE3)   
  <https://tdn.totvs.com/pages/releaseview.action?pageId=42795994>
* **F440CVB** - Calcular comissão para vendedores bloqueados;  
  <https://tdn.totvs.com/pages/releaseview.action?pageId=653140199>
* **F440LIQ** - bloqueio o cálculo da comissão.  
  <https://tdn.totvs.com/pages/releaseview.action?pageId=6070671>
* **F440ABA2** - Alterar base de comissão - Evento Baixa  
  <https://tdn.totvs.com/pages/releaseview.action?pageId=732671904>
* **F440CVB** - Calcular comissão para vendedores bloqueados;  
  <https://tdn.totvs.com/pages/releaseview.action?pageId=653140199>
* **F440FLAGE3** - Retorna nome de campo que conterá flag da tabela SE3 (Comissões)

<https://tdn.totvs.com/pages/releaseview.action?pageId=877162116>

* **F040COM** - Gravação dos dados do título

<https://tdn.totvs.com/pages/releaseview.action?pageId=6070864>

Importante  
Uma vez que sua configuração possui particularidades de acordo com seu Banco e Contrato.  
Este procedimento não faz parte do nosso escopo de atendimento Help Desk, é efetuado apenas por analista in loco de implantação. Para solicitação de analista in loco, entre em contato com seu ENS Totvs.
