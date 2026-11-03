---
article_id: 360044649014
category: RH - Rescisão
content_hash: 6353764f8a318d65d66128c8cb6970dc6c688948d51a94a9759bf6044e0e44fd
fetched_at: '2026-06-28T22:43:48.588829+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Como calcular multa por dispensa/pedido de demissão
  antes do término de contrato determinado na rescisão
type: support-article
updated_at: '2025-04-16T18:36:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044649014-RH-Linha-Protheus-GPE-Como-calcular-multa-por-dispensa-pedido-de-demiss%C3%A3o-antes-do-t%C3%A9rmino-de-contrato-determinado-na-rescis%C3%A3o
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26593891871767)***Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Como parametrizar o sistema para calcular multa por dispensa/pedido de demissão antes do término de contrato determinado na rescisão?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**1. Criar uma nova verba sem ID, seja de Provento ou Desconto (de acordo com o cálculo a ser realizado, pois se for pagamento da multa pela empresa, deverá ser provento, se for desconto da multa pelo fato do funcionário ter pedido demissão, deverá ser desconto) de acordo com as incidências que a empresa achar devidas:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360062024173)  
  
2. No cadastro do funcionário em questão, o campo selecionado abaixo **deverá estar preenchido obrigatoriamente**, pois caso contrário, o sistema não terá de onde buscar a informação:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360061132154)  
  
3. Na Tabela S043 na rotina Manutenção de Tabela cadastrar um novo tipo de rescisão, onde na coluna Pgt.Mul.Det deverá constar a verba criada para pagamento ou desconto da multa:  
**OBS.: Os demais campos abaixo não devem ser considerados, pois cada empresa irá parametrizar conforme verificado com o seu Jurídico).**  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360061127314)  
  
4. Ao calcular a rescisão, escolher o Tipo de Rescisão criado para pagamento ou desconto da multa por dispensa antes do término de contrato determinado:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360062024553)

**Saiba mais:**

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)
