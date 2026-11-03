---
article_id: 360016825391
category: RH - Reajuste Salarial
content_hash: 1dba58318c75abee66e269f205cfa99e61d3a97dcc890875bcdb6b058baf4280
fetched_at: '2026-06-28T22:43:15.883265+00:00'
product: protheus
section_id: 360010855214
source: central-protheus
title: RH - Linha Protheus - GPE - Como efetuar o Reajuste Salarial
type: support-article
updated_at: '2025-09-12T20:38:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016825391-RH-Linha-Protheus-GPE-Como-efetuar-o-Reajuste-Salarial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31714566375063) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Como efetuar o reajuste salarial no sistema?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**A rotina de reajuste **não calcula a diferença de meses anteriores**, apenas atualiza o salário do funcionário (Cadastro do funcionário, aba funcionais, campos **Salário** (RA\_SALARIO) e **Sal. Base Dis** (RA\_ANTEAUM)) .  
  
Acesse, Miscelânea > Reajuste > Salarial (GPER200)  
Preencher os parâmetros conforme necessário.  
  
Parâmetros importantes:  
**Aumento sobre?**:   
**Tipo de Aumento?**:   
**Atualiza Cadastro?**: **NÃO** (Utilize esta opção para que possa ser realizada a conferência das alterações que serão realizadas. Altere para **SIM** e execute a rotina novamente somente quando os valores de salário alterados estiverem conferidos, uma vez que não é possível desfazer o processo).  
**Atualiza Base Dissídio?**: **NÃO** (Utilize esta opção para que possa ser realizada a conferência das alterações que serão realizadas. Altere para **SIM** e execute a rotina novamente somente quando os valores de salário alterados estiverem conferidos, uma vez que não é possível desfazer o processo).

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101254913)  
  
**Após confirmar** os parâmetros, o sistema demonstrará a tela a seguir com **percentual, data de admissão, entre outras informações.**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412983761687)  
  
**Faixa mensal de:** Informar valor inicial (limite mínimo) da faixa salarial para aplicação do percentual e/ou valor adicional.  
**Faixa mensal até:** Informar valor final (limite máximo) da faixa salarial para aplicação do percentual e/ou valor adicional.  
**% aumento:** Informar o valor do percentual que será aplicado aos salários da faixa a que corresponde.  
**Valor do aumento:** O valor digitado neste campo será adicionado ao valor que resultar da aplicação do percentual informado no campo anterior sobre os salários contidos na faixa salarial definida.   
  
**Obs.:** Antes de realizar o processo, execute o *backup* das tabelas SRA, SR3 e SR7. Caso não seja realizado o *backup* destas tabelas previamente e houver algum erro no processo do reajuste, será necessário retornar os valores de salário manualmente.

Após efetuar o reajuste utilizando a opção **SIM** no parâmetro "Atualiza Cadastro" e "Atualiza Base Dissidio", verifique se a informação do campo **Sal. Base Dis** (RA\_ANTEAUM) no cadastro do funcionário (SRA) e o campo **Salário** (RA\_SALARIO) foram atualizados.  
  
**Saiba Mais**

[RH - Linha Protheus - GPE - Como conferir o reajuste salarial antes de efetivá-lo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028751191-RH-Linha-Protheus-GPE-Como-conferir-o-reajuste-salarial-antes-de-efetiv%C3%A1-lo)

[Pagina Centralizadora Reajuste Salarial](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010855214-RH-Reajuste-Salarial)
