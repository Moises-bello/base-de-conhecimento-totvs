---
article_id: 39663564104727
category: Folha Mensal
content_hash: 631b1917242e0ac34f650485acfea4c8fd9fb55b8c34ce2dd4111422b51bc45b
fetched_at: '2026-06-28T22:46:57.936918+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RH - RM - FOP – Crédito do Trabalhador: Como reutilizar evento de empréstimo
  finalizado ou renegociado'
type: support-article
updated_at: '2026-04-23T12:12:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39663564104727-RH-RM-FOP-Cr%C3%A9dito-do-Trabalhador-Como-reutilizar-evento-de-empr%C3%A9stimo-finalizado-ou-renegociado
---

⏱️ Tempo aproximado para leitura: 00:01:24 min

**Dúvida**  
Como reutilizar o evento de um empréstimo que foi finalizado ou renegociado?

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir dos patches:

12.1.2406.277  
12.1.2410.229  
12.1.2502.145  
12.1.2506 e superiores

**Solução**  
Para que o evento de um empréstimo finalizado ou renegociado possa ser reutilizado, é necessário que, no cadastro do empréstimo, o campo **“Comp. final Desc.”** esteja preenchido com uma data anterior à competência atual:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39939078926999)

Nos casos em que o empréstimo foi finalizado antecipadamente ou renegociado antes do término da data de competência final do seu cadastro, essa data permanece com o valor original informado no momento da importação. Como o governo ainda não disponibilizou um campo específico que informe a finalização ou renegociação do empréstimo, o RM não consegue identificar automaticamente essa situação nem atualizar esse campo.

Dessa forma, caso deseje reutilizar o mesmo evento de um empréstimo já finalizado por antecipação ou renegociado, será preciso alterar manualmente o campo **“Comp. final Desc.”**, informando uma data de encerramento anterior à competência atual. Após esse ajuste, o evento ficará disponível para utilização. Ao realizar a importação, esse evento será atribuído automaticamente aos novos contratos.

**Caso contrário, será necessário criar um novo evento para vinculá-lo ao novo contrato de empréstimo.**  
  
Realize o seguinte processo:

1. Acesse o cadastro do empréstimo localizado em **Administração de Pessoal | Funcionários | Selecione o funcionário desejado | Aba Empréstimos**;
2. Verifique o campo **“Comp. final Desc.”** se está preenchido com uma data anterior à competência atual;
3. Caso o empréstimo tenha sido finalizado antecipadamente ou renegociado, altere manualmente o campo **“Comp. final Desc.”**, informando uma **data anterior** à competência atual;
4. Após a alteração, o evento ficará disponível para reutilização;
5. Ao realizar a importação, o evento será atribuído automaticamente aos novos contratos;
6. Se não for possível alterar a data, crie um novo evento para vinculá-lo ao contrato de empréstimo.

**Saiba Mais**  
  
[RH - RM - FOP - Crédito do Trabalhador - Funcionário já possui empréstimo e não há mais eventos disponíveis no Cadastro de Eventos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33451795834519-RH-RM-FOP-Cr%C3%A9dito-do-Trabalhador-Funcion%C3%A1rio-j%C3%A1-possui-empr%C3%A9stimo-e-n%C3%A3o-h%C3%A1-mais-eventos-dispon%C3%ADveis-no-Cadastro-de-Eventos)

[RH - RM - FOP - Crédito do Trabalhador - Importação de Múltiplos Empréstimos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33401965386135-RH-RM-FOP-Cr%C3%A9dito-do-Trabalhador-Importa%C3%A7%C3%A3o-de-M%C3%BAltiplos-Empr%C3%A9stimos)
