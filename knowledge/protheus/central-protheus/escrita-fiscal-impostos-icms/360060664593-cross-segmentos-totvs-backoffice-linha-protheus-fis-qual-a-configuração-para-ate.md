---
article_id: 360060664593
category: Escrita Fiscal - Impostos - ICMS
content_hash: 1ce9b9dcc33fd21f5bb1b38c3a4b0d846ff9f36551edfe36ba849bfc862016ae
fetched_at: '2026-06-28T22:39:25.995070+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Qual a configuração
  para atender o Decreto 65.254 - Estado de SP?
type: support-article
updated_at: '2021-07-20T13:20:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060664593-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Qual-a-configura%C3%A7%C3%A3o-para-atender-o-Decreto-65-254-Estado-de-SP
---

**Dúvida**

Qual a configuração para atender o Decreto 65.254 - Estado de SP?

**Ambiente**

Protheus - Todas as versões

**Solução**

Para atender o Decreto 65.254/, será necessário configurar Redução da Base de Cálculo do ICMS, TES ou exceção fiscal:  
  
TES:  
Calcula ICMS = Sim  
L. Fiscal ICMS = Outros  
% Red ICM = ( 100- 77% ) = 23,00  
  
Exceção Fiscal:  
Estado = SP  
Tipo = Todos  
Grp Cli/ For = Criar código e amarrar no cadastro do cliente  
Alíquota interna = 18%, 25%, 4% ou 7%  
% RED ICM = 23,00  
UF Busca = Branco ou Destino

TES:   
Calcula ICMS = Sim  
L. Fiscal ICMS = Outros  
% Red ICM = 0,00 ( Já configurado na exceção fiscal)

Vincular o Grupo de tributação ao cadastro de produtos - Grupo Trib e Vincular GRP Cli/ For ao cadastro de Clientes - Grp Clientes.  
  
Segue exemplo configurando exceção, conforme exemplo de cálculo do Parecer acima, exemplo  77% do valor da operação ou prestação, quando sujeitas à alíquota de 18%;  
  
  
![](https://totvssuporte.zendesk.com/attachments/token/PknyJl8QaVY4nBdSQ1ceBi045/?name=inline-743889721.png)​

Parecer Consultoria Tributária:

<https://tdn.totvs.com/pages/releaseview.action?pageId=577001431>
