---
article_id: 360001066607
category: Férias
content_hash: 2ddaca060df8b1702fa21b4e7abeae76e843c25e7014d1d2fb2f1ef234b25bbf
fetched_at: '2026-06-28T22:46:56.512488+00:00'
product: rm
section_id: 1500000861102
source: central-rm
title: RH - RM - FOP - Licença Maternidade durante as Férias
type: support-article
updated_at: '2025-01-21T18:47:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360001066607-RH-RM-FOP-Licen%C3%A7a-Maternidade-durante-as-F%C3%A9rias
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:08:56 min  
  
Dúvida**  
Como devem ser tratadas, no TOTVS Folha de Pagamento, as situações em que uma colaboradora entra de licença maternidade no meio do período do gozo de férias?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**  
Ocorrendo o nascimento da criança durante o gozo de férias da empregada, o início do afastamento para recebimento do salário-maternidade ocorrerá no próprio dia do parto, suspendendo-se, consequentemente, o gozo das férias, o qual será retomado tão logo termine a licença-gestante (120 dias). Considerando que somente o efetivo gozo de férias é suspenso e posteriormente retomado, como o pagamento das férias já foi efetuado, só haverá complementação desse valor se houver reajuste salarial no decorrer do afastamento.  
  
De acordo com a Constituição Federal, Art. 7º, XVIII, Consolidação das Leis do Trabalho - CLT, Art. 392 e Instrução Normativa INSS nº 45/2010 art. 293.  
  
O tratamento no Folha de Pagamento, deverá ocorrer conforme abaixo:  
  
1. Finalize as férias da funcionária;  
  
2. Acesse o cadastro de período aquisitivo e edite o registro relacionado ao período da funcionária;  
    2.1. Na aba **Período de Gozo**, edite o período referente às férias gozadas;  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6148704967319/mceclip1.png)  
  
    2.2. Altere a situação das férias de **Finalizadas** para **Marcadas** e salve o cadastro;  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6148766786967/mceclip2.png)  
  
    2.3. Somente após salvar a alteração anterior, altere o período de gozo informando como término o dia imediatamente anterior ao início da licença maternidade e salve novamente o cadastro;  
  
    2.4. Volte a situação das férias para **Finalizadas** e salve o registro;  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6148785366295/mceclip3.png)  
      
2.5. Será apresentada mensagem de aviso relacionado à geração do gatilho do **S-2230**. Selecione a opção **Sim** para que o gatilho seja gerado automaticamente;  
  
3.  Transmita o evento de retificação do **S-2230** para o governo para ajustar o término do afastamento das férias;  
  
4. Ajuste o histórico de situação do funcionário, excluindo o registro de **Ativo** com data posterior à férias, mantendo como último registro no histórico a situação de **Férias**;  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6148850794519/mceclip4.png)  
  
5. Realize normalmente o cadastro da licença maternidade e transmita os eventos **S-2230** relacionado à licença para o governo;  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6149026904343/mceclip5.png)  
  
6. Após o término da licença, será necessário informar o restante do período de gozo. Para isso, acesse novamente o cadastro da funcionária;  
  
    6.1. Acesse o cadastro de período aquisitivo e edite o registro relacionado ao período da funcionária;  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6149032061847/mceclip6.png)  
  
    6.2. Na aba **Período de Gozo**, inclua um novo registro com data de início imediatamente após o retorno do afastamento da licença maternidade e status **Marcadas**;  
  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6149038425879/mceclip7.png)  
  
    6.3. Altere a situação das férias para **Finalizadas** e salve o registro;  
  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6149025134487/mceclip8.png)  
  
    6.4. Será apresentada mensagem de aviso relacionado à geração do gatilho do **S-2230**. Selecione a opção **Sim** para que o gatilho seja gerado automaticamente;  
  
7. Transmita o evento **S-2230** relacionado às férias para o governo.  
  
8. Incluir manualmente **Histórico de Situação.**  
  
![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6149331149207/mceclip9.png)

Observação:Por uma demanda interna do sistema, é necessário que o período de férias remanescente a ser cadastrado deve ser feito após a liberação de competência. Por exemplo: se a funcionária retornou da licença maternidade no dia 10/06 e precisa gozar mais 10 dias de férias, só se deve cadastrar estes 10 dias de férias após a liberação de competência para o mês 7. Isso se dá pois, ao cadastrar um período de gozo dentro da mesma competência nessa circunstância, o sistema buscará por um envelope com os eventos de férias, e como as férias já foram pagas, não haverá movimentação. Por isso, caso seja feito na mesma competência, o sistema não validará e retornará um erro na liberação de competência.  
  
Sobre o evento S-2230, como não é periódico, não há problema em gerar seu gatilho referente a uma situação alterada com data em competência anterior. Para além disso, as próximas liberações de competência não serão prejudicadas pois o sistema já não validará os dias de férias que foram marcados em competência anterior.  
  
**Importante**  
Qualquer rotina ou processo que demande a liberação de competência, sugere-se que o usuário faça os devidos testes primeiramente em uma base de homologação, a fim de conhecer o comportamento do sistema e reduzir alguma chance de falha no processo na base de produção.

**Saiba Mais**[Licença Maternidade interrompendo férias](http://tdn.totvs.com/pages/viewpage.action?pageId=507006948)  
[Férias: Lançamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007913092-RM-FOP-F%C3%A9rias-Lan%C3%A7amento)  
[Cadastro de Férias](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719354)
