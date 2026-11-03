---
article_id: 39994009551639
category: Rescisão
content_hash: 587541a51ad126136bade2947dad4aed7567d7d840240d8df4da5eb9dd0521c4
fetched_at: '2026-06-28T22:46:54.127344+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: 'RH - RM - FOP - Rescisão: Base de INSS negativa'
type: support-article
updated_at: '2026-04-27T17:00:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39994009551639-RH-RM-FOP-Rescis%C3%A3o-Base-de-INSS-negativa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39993998423319) Tempo aproximado para leitura: 00**:01:52 min**  
  
**Dúvida**  
Como proceder quando o valor de descontos (como atrasos ou banco de horas negativo) é superior aos proventos tributáveis, resultando em uma base de INSS negativa na rescisão?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**  
O valor negativo apresentado na base de INSS não gera impactos nos relatórios de Folha Analítica ou nas obrigações acessórias entregues ao Governo (como eSocial), uma vez que o sistema realiza o tratamento interno zerando essa base para fins de apuração. A exibição do valor negativo ocorre apenas na consulta de "Incidências" do envelope de pagamento para que o usuário tenha rastreabilidade dos valores calculados.

Caso seja uma particularidade da empresa que o valor da base apareça zerado também na visualização do envelope de pagamento, é necessário realizar o lançamento de um evento de base para equilibrar o saldo negativo.  
  
1. Acesse o menu: **Administração de Pessoal** e selecione **Eventos**;   
  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40046382845847)  
  
  
2. Identifique ou crie um evento com as seguintes características:

* **Tipo Evento:** Base de Cálculo (não interfere no líquido);
* **Incidência INSS:** Marcado;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39993998427159)

3. Acesse o movimento da rescisão do funcionário e lance este evento manualmente;

4. Informe no valor do evento a quantia exata necessária para zerar o saldo negativo da base de INSS;

5. Recalcule a rescisão e valide a informação na aba **Incidências** do envelope de pagamento.
