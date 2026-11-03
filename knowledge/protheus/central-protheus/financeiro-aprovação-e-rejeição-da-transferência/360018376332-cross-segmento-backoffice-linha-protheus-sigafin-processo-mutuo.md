---
article_id: 360018376332
category: Financeiro - Aprovação e Rejeição da Transferência
content_hash: 137fbd0d6d4ad1a494c3a2482cd3c4ed7c626528b8c69e15f386cff022c979bf
fetched_at: '2026-06-28T22:37:36.930286+00:00'
product: protheus
section_id: 35057458871575
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN -  Processo Mutuo
type: support-article
updated_at: '2025-11-26T20:06:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018376332-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Processo-Mutuo
---

**Dúvida**  
Como utilizar o processo de Mutuo no ***Protheus** ?*  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da versão 12.1.17  
  
**Solução**  
Este processo pode ser efetuado pela solicitação de transferência entre filiais **FINA621**. Esta rotina permite que uma empresa corporativa possa transferir os débitos dos clientes (títulos a receber) entre as filiais da empresa e/ou entre outros clientes. Este recurso atende, principalmente, o ramo de transportes, permitindo que uma empresa (corporativa) possa cadastrar seus débitos entre as filiais que originaram os títulos do Contas a Receber. O sistema disponibiliza um questionário ***checklist***, configurado pela tabela **G2** - ***Checklist*** para **Transferência de Débito**, no ambiente **Configurador**, para que o usuário possa decidir pela transferência ou não da cobrança. No entanto, caso seja necessário implementar opções de verificação no ***checklist***, a Tabela **AA** pode ser alterada, através do ambiente **Configurador**. Desta forma, somente será permitida a inclusão da solicitação, se todas as questões do **checklist** forem respondidas com **Sim** marcadas com **X**.  
A Tabela **SE6** - Solicitações de Transferência, armazena todas as informações da transferência, onde cada solicitação é gravada com um número sequencial no campo **Nº. Solic.** (**E1\_NUMSOL**).  
O campo **E6\_PARCDES** armazena a parcela do título gerado na filial de destino débito originado pela rotina de Transferência de títulos a receber entre filiais gravando e validando este código.  
Para que seja efetivada a transferência, a filial de destino pode aceitar ou rejeitar esta solicitação, através da rotina **Aprovação/Rejeição solicitação.**   
  
**Importante:**

Consulte as rotinas **FINA621, FINA620 , FINA631 eFINA630**

**Saiba Mais:**

<https://tdn.totvs.com/pages/releaseview.action?pageId=540892367>
