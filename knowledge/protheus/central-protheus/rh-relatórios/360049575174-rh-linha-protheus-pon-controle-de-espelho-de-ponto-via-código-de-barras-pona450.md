---
article_id: 360049575174
category: RH - Relatórios
content_hash: e617c17ce7ba8fc9df600d015e3433657786e2dbf19db66a042d8ec889f88cfc
fetched_at: '2026-06-28T22:44:43.515980+00:00'
product: protheus
section_id: 32419371267223
source: central-protheus
title: RH - Linha Protheus - PON - Controle de Espelho de ponto via código de barras
  - PONA450
type: support-article
updated_at: '2025-06-13T18:53:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049575174-RH-Linha-Protheus-PON-Controle-de-Espelho-de-ponto-via-c%C3%B3digo-de-barras-PONA450
---

**Dúvida**Controle de Espelho de ponto via código de barras - PONA450  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões **Solução**Esta rotina permite visualizar os funcionários que não devolveram o espelho de ponto assinado no período, além de informar os motivos para a não devolução. Também é possível dar baixa nos espelhos que foram entregues.  
Todo espelho de ponto impresso com código de barras gera um registro na tabela Controle de Espelhos de Ponto (SR4).  
  
O *browser* da rotina é baseado no Cadastro de Funcionários: em Outras Ações - Filtrar Espelhos de Ponto, existe a opção para definir as datas de inicio e fim para filtro dos espelhos de ponto, caso nada seja informado no filtro, em Manutenção/Visualização são exibidos todos os espelhos do ponto emitidos para o funcionário. Os registros com o status Devolvido aparecerão com a legenda verde, enquanto os registros com os status Pendente e Cancelado aparecerão com a legenda amarela e vermelha respectivamente. Nesta tela é possível informar um motivo pelo qual o espelho não foi devolvido.  
  
**Importante:**Apenas os espelhos impressos com código de barras serão exibidos. Caso seja impresso mais de um espelho para o mesmo período, todos aparecerão. Recomenda-se que apenas o espelho de ponto oficial seja impresso com código de barras, para que a tabela não seja poluída com informações duplicadas. Em todo caso será possível excluir eventuais registros duplicados através da opção de Manutenção.  
  
Ao gerar o espelho de ponto com a pergunta Código de Barras = SIM, a tabela RS4 será alimentada com os códigos de barras gerados em cada espelho de funcionário, como demonstrado abaixo:  
![RS4_gera__o.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074547054/RS4_gera__o.png)  
  
Após, acessamos a rotina PONA450 - Controle de Espelho de Ponto e, individualmente, podem dar a baixa no espelho que fora devolvido e assinado:  
![Baixa_espelho.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075754693/Baixa_espelho.png)  
  
Com isso, a tabela RS4 será modificada para status de Devolvido:  
![RS4_com_a_baixa.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074547134/RS4_com_a_baixa.png)  
  
É importante ressaltar que não temos suporte à baixa do Espelho de Ponto via Leitor de Código de Barras, somente a baixa individual do espelho de ponto.
