---
article_id: 1500007398482
category: Meu RH - Ponto
content_hash: 538e11fed432b379dec604e9e06ad7fbdcfd9ce109c8e56c7d5df155b612f3a9
fetched_at: '2026-06-28T22:47:30.389660+00:00'
product: rm
section_id: 1500000861782
source: central-rm
title: RH - RM - Meu RH -  Liberar acesso ao Espelho de Ponto para Funcionários Afastados
  ou de Férias
type: support-article
updated_at: '2025-09-12T19:34:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007398482-RH-RM-Meu-RH-Liberar-acesso-ao-Espelho-de-Ponto-para-Funcion%C3%A1rios-Afastados-ou-de-F%C3%A9rias
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:01:58 min**

**Dúvida**Como acessar o espelho de ponto de funcionários que estão com afastamento ou férias?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Meu RH - A partir da versão 12.1.17

**Solução**Ao acessar o espelho de ponto é retornada a mensagem ***"Ocorreu um erro ao efetuar a leitura do registro: Usuários em período de Férias ou Afastados não tem acesso ao Espelho".***

*![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10891980008087)*

*E*ssa mensagem é exibida pois o sistema está parametrizado para que os funcionários com afastamento ou férias não tenham acesso ao espelho de ponto. Para conceder esta permissão, acesse o módulo **Automação de Ponto >** **Configurações** > **Parametrizador > RM Portal**

**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10892121074711)**

Selecione o **Grupo de Quiosque** do usuário, na opção **Permissões** marque a flag ***"Permite acesso ao RM Portal para funcionários de férias / em afastamento"**.*  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10892239673367)

**Saiba mais**  
[Consultar Espelho Ponto](https://tdn.totvs.com/display/NPR/8.0++Consultar+Espelho+Ponto)
