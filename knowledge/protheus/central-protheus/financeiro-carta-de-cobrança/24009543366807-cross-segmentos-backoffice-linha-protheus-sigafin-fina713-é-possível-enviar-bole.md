---
article_id: 24009543366807
category: Financeiro - Carta de Cobrança
content_hash: 60ca81e46efb61add8280f6099c37dbe83b34e38398a06951916675b2c14f629
fetched_at: '2026-06-28T22:37:28.971093+00:00'
product: protheus
section_id: 35058223754903
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA713 - É possível
  enviar Boleto ou Carta de Cobrança por filial tendo o e-mail do remetente diferente?
type: support-article
updated_at: '2026-03-02T19:39:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24009543366807-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA713-%C3%89-poss%C3%ADvel-enviar-Boleto-ou-Carta-de-Cobran%C3%A7a-por-filial-tendo-o-e-mail-do-remetente-diferente
---

**Dúvida**  
É possível enviar boleto ou carta de cobrança por filial tendo o e-mail do remetente diferente?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA713 - Todas as versões.  
  
**Solução**

##### Atualmente, tanto o envio dos boletos registrados via API, através do Gestor Financeiro, como também o envio das cartas de cobrança via rotina FINA811, não possuem o recurso de múltiplas conexões com o servidor SMTP. Ou seja, o sistema realiza uma conexão no servidor SMTP, com isso sempre será utilizada uma única conta de e-mail para todos os títulos que estão pendentes de envio.

##### Porém, foi identificada esta necessidade e será implementada esta melhoria, tanto na funcionalidade de registro de boletos por API como também na rotina de carta de cobrança (FINA811).

##### Pedimos que acompanhe nossas documentações, que são liberadas juntamente com os pacotes de expedição contínua, para obter informações sobre novos recursos que serão liberados.

##### Acompanhe também nossa página com informação sobre o que temos previsto para roadmaps futuros. <https://produtos.totvs.com/produto/totvs-backoffice/totvs-backoffice-linha-protheus/>**Importante**

##### No final da página é possível baixar o arquivo ROADMAP DO PRODUTO e obter acesso às futuras inovações.

##### 

**Saiba mais**

[Novos Recursos de Envio FINA713-FINA811](https://tdn.totvs.com/pages/releaseview.action?pageId=635763626)
