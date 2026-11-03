---
article_id: 14437141180695
category: Gestão de Distribuição (SIGAOMS)
content_hash: 38bd725478dd20f2514ac88d2c088f37aabe324799d04798d263babbfe322e7f
fetched_at: '2026-06-28T22:45:49.997696+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Pedido de Venda com Transportador de Redespacho,
  quais informações o OMS irá enviar na integração do TOL/TRE ao utilizar parametro
  MV_CPLRED
type: support-article
updated_at: '2025-05-22T19:38:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14437141180695-Log%C3%ADstica-Linha-Protheus-OMS-Pedido-de-Venda-com-Transportador-de-Redespacho-quais-informa%C3%A7%C3%B5es-o-OMS-ir%C3%A1-enviar-na-integra%C3%A7%C3%A3o-do-TOL-TRE-ao-utilizar-parametro-MV-CPLRED
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15613314172439) Tempo aproximado para leitura: **00:01:24 min** **Dúvida**Em um **Pedido de Venda** com **Transportador de Redespacho**, quais informações o **OMS** irá enviar na integração do **TOL/TRE** ao utilizar parâmetro **MV\_CPLRED?**  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões  
  
**Solução**Na integração do **Pedido de Venda do OMS com o TOL/TRE**, caso seja informado um **Transportador Redespacho**, temos o parâmetro **MV\_CPLRED**, permitindo enviar as seguintes informações:

1. **Conteúdo do parâmetro igual a Sim - preencher com .S.** :   
   Quando o campo **C5\_REDESP - Redespacho** esta preenchido, no arquivo **XML**, serão enviados os dados do **cliente/fornecedor** no **elemento destinationId**  e não serão enviadas as informações de endereço.
2. **Conteúdo do parametro igual a Não -  preencher com .N.** :  
   Quando o campo **C5\_REDESP - Redespacho** esta preenchido, no arquivo **XML**, serão enviados os dados da **Transportadora de Redespacho** e os **elementos de endereco**.

Os parâmetros da integração do **OMS** com o **TOL/TRE** estão localizados em **Atualizações/Cockpit Logistico/Parametros de Integração - OMSXCPL1**.

**Importante**O preenchimento **default** do parâmetro **MV\_CPLRED** é igual a **Não.  
  
Saiba mais**Mais informações poderão ser acessadas nos *link's*:  
[Logística - Linha Protheus - OMS - Envio de Pedidos do TOTVS OMS para TOL/TRE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011610682-Log%C3%ADstica-Linha-Protheus-OMS-Envio-de-Pedidos-do-TOTVS-OMS-para-TOL-TRE)  
[Logística - Linha Protheus - OMS - Integração Protheus TOTVS OMS x TOL/TRE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061123194-MP-OMS-Integra%C3%A7%C3%A3o-Protheus-TOTVS-OMS-x-TOTVS-Otimiza%C3%A7%C3%A3o-Log%C3%ADstica)  
[Comportamento da integração com o TOL/TRE em operações de redespacho - OMSXCPL6](https://tdn.totvs.com/pages/releaseview.action?pageId=729236321) **Glossário  
TOL** - TOTVS Otimização Logística **TRE**- TOTVS Roteirização e Entrega **TOTVS OMS**- Order Management System
