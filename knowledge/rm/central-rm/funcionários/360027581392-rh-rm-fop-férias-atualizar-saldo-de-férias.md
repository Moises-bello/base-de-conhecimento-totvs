---
article_id: 360027581392
category: Funcionários
content_hash: e460398b736a8e9f8a6cfdd0f47c335c57dd544a24c33414a05d87d00c7bf31d
fetched_at: '2026-06-28T22:47:04.160780+00:00'
product: rm
section_id: 1500000861022
source: central-rm
title: 'RH - RM - FOP - Férias: Atualizar Saldo de Férias'
type: support-article
updated_at: '2025-03-06T18:20:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027581392-RH-RM-FOP-F%C3%A9rias-Atualizar-Saldo-de-F%C3%A9rias
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Caso o campo **Saldo período** no cadastro de férias do funcionário estiver em branco ou incorreto, como atualizo a informação?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para manutenção do campo **Saldo período** temos o processo **Atualizar saldo de férias**. Ele está localizado em **Administração de Pessoal | Funcionários | Processos | Atualizar Saldo de Férias**. Ao clicar, uma janela para inserir a quebra de seção e seleção de funcionários aparecerá. Basta selecionar e executar.  
  
**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10756698089751)**

Ações da rotina **Atualiza saldo de férias:**

1. Atualiza o saldo total de férias do funcionário de acordo com a competência atual.  
2. Atualiza o saldo (saldo do período vencido) de todos os períodos aquisitivos do funcionário.  
  
**Importante:**

**Sobre o sistema:** O sistema sempre atualizará automaticamente o Saldo conforme você o opere, ou seja, o campo sempre deverá refletir o que o funcionário tem de direito a depender dos períodos de gozo lançados. É possível, ao passar o mouse no saldo, verificar a informação **Campo calculado pelo sistema**. Para isso, clique com o botão direito em qualquer parte da janela que não tenha nenhuma informação e ative **Visualizar nome dos campos**. Neste tipo de campo, o sistema não consulta o banco para apresentar um dado, mas sim consulta outros campos e apresenta este dado apenas como um resultado. Em outras palavras, ele não está consultando o campo SALDO na tabela PFUFERIAS para exibir a informação.

![](https://totvssuporte.zendesk.com/attachments/token/DrtsTDV8s5nP9qfRuyCBOJwSa/?name=inline1343002309.png)

​  
Ao passar o mouse sobre o **Saldo período**, é retornada a informação **Campo calculado pelo sistema**.  
  
**Sobre o banco de dados**: O banco de dados apenas atualizará o campo SALDO da tabela PFUFERIAS em dois momentos: Ao finalizar as férias ou ao processar a rotina **Atualizar Saldo de Férias**. Quando o usuário consulta este dado no banco e ele é apresentado como NULL, é porque se trata de um período aquisitivo onde não foram lançadas férias ainda, portanto não houveram férias finalizadas, ou porque o processo **Atualizar Saldo de Férias** não foi executado.
