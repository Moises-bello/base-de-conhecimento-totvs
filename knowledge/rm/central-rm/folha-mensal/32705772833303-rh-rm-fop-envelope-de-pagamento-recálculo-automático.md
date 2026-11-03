---
article_id: 32705772833303
category: Folha Mensal
content_hash: 2478563b56e2ed2f324f484dae3f683ca58608d8ff5c436d7d73b5c12da96fa1
fetched_at: '2026-06-28T22:46:58.050361+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Envelope de Pagamento - Recálculo Automático
type: support-article
updated_at: '2026-02-23T12:41:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32705772833303-RH-RM-FOP-Envelope-de-Pagamento-Rec%C3%A1lculo-Autom%C3%A1tico
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32705786928279) Tempo aproximado para leitura: **00:02:38 min**  
  
**Dúvida**

Ao abrir o envelope de pagamento de um colaborador, o processo de recálculo está sendo executado automaticamente. Qual é o motivo desse comportamento?

**Ambiente**

TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir dos patches:

12.1.2406.278

12.1.2410.232

12.1.2502.146

12.1.2506 e superiores

**Solução**

O recálculo automático pode ocorrer por dois motivos.

1° - Quando o parâmetro "**Recalcular automaticamente o envelope** esta **marcado".** Este parâmetro esta localizado em **Configurações | Parametrizador | Folha normal | Ficha Financeira.**  
  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/38573495970839)**  
  
2° -  O recálculo automático ocorre porque o sistema identifica alterações que impactam diretamente o cálculo da folha de pagamento. Quando essas alterações são detectadas, os envelopes de pagamento já processados passam a ser considerados desatualizados, ficando pendentes de recálculo.

Esse comportamento é esperado e visa garantir que os valores apresentados estejam de acordo com os dados e regras mais recentes.

Os principais motivos que podem gerar o recálculo automático ao acessar o envelope de pagamento são:

* **Alterações nas tabelas de INSS e IRRF:**

  Quando as tabelas de cálculo das finalidades de INSS e IRRF são alteradas, e a competência atual da folha de pagamento está dentro do período de vigência dessas tabelas, os envelopes de pagamento calculados anteriormente passam a ficar pendentes de recálculo;
* **Alteração no Cadastro de Eventos:**   
  Ao realizar modificações no cadastro de eventos, como: Alterações de valores, fórmulas ou configurações, os envelopes de pagamento que foram anteriormente calculados passam a ficar pendentes de recálculo;
* **Configuração do Parametrizador:**

  Além disso, quando o parâmetro ***“*****Lança Grupo de Eventos sem recalcular envelope*****”***, localizado em **Configurações | Parametrizador | Folha Normal | Geral 1/2**, estiver marcado, os envelopes afetados pelo lançamento do grupo de eventos também ficam pendentes de recálculo.

Sendo assim, ao acessar um envelope de pagamento que se encontra nessa situação, o sistema identifica a pendência e executa automaticamente o recálculo do envelope.

Durante o processo, será exibido o progresso do recálculo e o log de depuração, permitindo ao usuário acompanhar a execução em tempo real, com a opção de cancelá-la, se necessário.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32705786928407)

**Saiba Mais:**

[Envelope de Pagamento - Dúvidas](https://tdn.totvs.com/display/public/LRM/Envelope+de+Pagamento)  
[Parametrizador - Ficha Financeira](https://tdn.totvs.com.br/display/public/LRM/Ficha+Financeira)
