---
article_id: 13767733350295
category: Férias
content_hash: 10065abc62b01f8307f7c0656b1f79d5e6c568dd0ffd2e41d47ab5abb5128d04
fetched_at: '2026-06-28T22:46:56.203153+00:00'
product: rm
section_id: 1500000861102
source: central-rm
title: 'RH - RM - FOP - Férias: Cálculo para comissionista'
type: support-article
updated_at: '2024-09-16T18:36:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13767733350295-RH-RM-FOP-F%C3%A9rias-C%C3%A1lculo-para-comissionista
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:03:48 min  
  
Dúvida**  
Como realizar calculo de férias para comissionista?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução  
  
1.** Acesse **Administração de pessoal | Sindicatos  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13765388684823)**  
**2.** Verificar se o Mínimo Garantido está preenchido:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13765394155159)  
  
Valor mínimo garantido  
O valor do mínimo garantido para os funcionários comissionados.  
Este valor é utilizado para o cálculo do salário base dos comissionados, com a seguinte consideração:  
  
Se a soma dos eventos que compõem o salário dos comissionados, dividido pelo número de meses para o cálculo da média, é menor que o valor do mínimo garantido, o cálculo das férias, 13º salário, aviso prévio e salário-maternidade serão sobre o valor do mínimo garantido.  
Se a média é maior, os cálculos serão sobre o valor da média.  
  
Este campo é utilizando também no cálculo dos eventos do tipo hora e dia, caso o funcionário não possua eventos que compõem o salário-comissão lançados na movimentação do mês de processamento.  
  
O valor da média é substituído pelo valor do mínimo garantido a partir do segundo mês, somente se o valor da média for de valor inferior ao mínimo garantido.  
  
**3.** No cadastro do evento é preciso estar marcado a seguinte flag:  
  
[RH - RM - FOP - Cadastro de Eventos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412771329815-RH-RM-FOP-Cadastro-de-Eventos)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13765579703959)  
  
**4.** Ao realizar o cadastro das férias veja como é feito o calculo.  
  
[RH - RM - FOP - Férias: cadastro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4915856599191-RH-RM-FOP-F%C3%A9rias-cadastro-)  
  
Evento 0084 - COMISSÃO lançado nos meses Janeiro, Fevereiro e Março com férias em Abril.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13765964636439)  
  
Ao realizar o calculo temos que validar o Log de Média:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13766017319063)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13766059072919)  
  
Valor considerado a média do evento de comissão para compor o salario de R$733,33.  
  
Após validar o calculo do Log de Calculo, veja que o valor encontrado da média será considerado como salario do comissionista:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13766102146327)  
  
Print Recibo:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13766080722199)
