---
article_id: 22005700095767
category: RH - Reajuste Salarial
content_hash: cedd187944bc9098544c0ab0f99e2c717e37e3401f4705afc072e82b8078b1c7
fetched_at: '2026-06-28T22:43:15.907808+00:00'
product: protheus
section_id: 360010855214
source: central-protheus
title: RH - Linha Protheus - GPE - Verbas que incorporam salário no cálculo de Reajuste
  Salarial
type: support-article
updated_at: '2025-09-15T11:48:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22005700095767-RH-Linha-Protheus-GPE-Verbas-que-incorporam-sal%C3%A1rio-no-c%C3%A1lculo-de-Reajuste-Salarial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22005700054679) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Validação de verbas que incorporam salário no cálculo de Reajuste Salarial  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução:**No cálculo de Reajuste Salarial, quando uma verba está parametrizada para **incorporar ao salário** na aba **Incidências**, o sistema sempre irá considerar essa verba no **Histórico Salarial,** independentemente de haver ou não um ID de cálculo.  
Esse comportamento ocorre quando a verba é calculada na Folha de Pagamento da **mesma competência em que está sendo realizado o Reajuste Salarial,** portanto, ao **fechar o período** da Folha, o sistema automaticamente carrega essa verba para a rotina de **Histórico Salarial**, considerando o valor da verba incorporado ao salário do funcionário.  
  
Exemplo de como o sistema se comporta, levando em consideração um cenário de cálculo de Folha e Reajuste Salarial no período **10/2023:**  
**1** - Configuração da verba com **Incorpora Salário = SIM:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31291465839255)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31291459157527)  
  
  
  
**2 -** Aplicação de reajuste na competência **10/2023:**![](https://centraldeatendimento.totvs.com/hc/article_attachments/31291459158423)

**3 -** Histórico Salarial:   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22006295905943)

**4 -** Cálculo da Folha de Pagamento com a verba de Gratificação configurada com o campo **Incorpora Salário = SIM:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22006359370007)

**5 -** Após realizar o **Fechamento do Período**, ao acessar o **Histórico Salarial** do funcionário é possível verificar que as verbas que estão configuradas com **SIM** para **Incorpora Salário,** e que foram **calculadas na Folha de Pagamento daquela competência**, são automaticamente geradas e registradas no histórico salarial:**![](https://centraldeatendimento.totvs.com/hc/article_attachments/22006359409559)**

Cabe ressaltar que **não existe** nenhuma configuração no padrão do Produto, que **altere ou valide de forma diferente** a verba que possui o campo Incorpora Salário = SIM para fins de registro no Histórico Salarial.  
  
Em consultas de cálculos anteriores, caso a verba **não tenha sido registrada** no **Histórico Salarial**, é importante verificar:  
**>** Se o campo **Incorpora Salário** foi **alterado** para SIM **após o cálculo da Folha  
>** Se na **competência** em que ocorreu o **Reajuste Salarial**, a verba foi **calculada** na **Folha de Pagamento.**

**Saiba Mais:**

[Pagina Centralizadora Reajuste Salarial](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010855214-RH-Reajuste-Salarial)

[Página Centralizadora do Dissídio](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109132-RH-Diss%C3%ADdio)
