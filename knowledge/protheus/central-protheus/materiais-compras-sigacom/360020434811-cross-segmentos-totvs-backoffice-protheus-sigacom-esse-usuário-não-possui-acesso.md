---
article_id: 360020434811
category: Materiais - Compras (SIGACOM)
content_hash: fe0b1dee5b07adacd170d8dee0a59f2c3c01963ae093b20d1743cea4454b7793
fetched_at: '2026-06-28T22:41:07.396880+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - "Esse usuário não
  possui acesso para executar essa operação. Menu: MATA020 / Rotina:A020INCLUI" '
type: support-article
updated_at: '2023-09-01T16:42:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020434811-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Esse-usu%C3%A1rio-n%C3%A3o-possui-acesso-para-executar-essa-opera%C3%A7%C3%A3o-Menu-MATA020-Rotina-A020INCLUI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17208839823511) Tempo aproximado para leitura: **00:05:00 min**

**Ocorrência**No módulo **Configurador**, quando configurado o privilégio para o login do usuário na rotina MATA020/Cadastro de Fornecedor utilizando-se do grupo DEFAULT na aba Grupos. No momento em que o usuário tentar efetuar alguma operação no Cadastro de Fornecedor, é apresentada a mensagem "**Esse usuário não possui acesso para executar essa operação. Menu: MATA020 / Rotina:A020INCLUI**".  
  
**Ambiente**Protheus - Compras - Configurador - A partir da versão 12.1.017.  
  
**Causa**Problema com restrição de acesso do usuário na rotina MATA020.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1.Será necessário revisar o cadastro do privilégio de acesso à rotina MATA020, excluindo a linha referente à rotina e incluindo novamente, para que as opções de menu sejam atualizadas e o usuário tenha suas permissões respeitadas.  
Exemplo de opções de menu para inclusão: onde está "ViewDef.MATA020"deverá ficar "A020INCLUI".

Os campos abaixo devem estar como permitido.   
   
![](https://totvssuporte.zendesk.com/attachments/token/xtm2xRFcQMnKtYzeGTEdFDcDg/?name=image.png)  
 

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
