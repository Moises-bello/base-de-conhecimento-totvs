---
article_id: 41463411182487
category: Integrações - Ahgora
content_hash: 743f305a03d273e20e8a6d70bf3fa3a39a135160da7da9d3ac176ffbf477f8bb
fetched_at: '2026-06-28T22:46:39.887634+00:00'
product: rm
section_id: 36553540355351
source: central-rm
title: RH - RM - FOP - Integração RM Folha de Pagamento x Ahgora- Funcionários ou
  líderes não são integrados no agendamento automático
type: support-article
updated_at: '2026-06-26T11:56:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41463411182487-RH-RM-FOP-Integra%C3%A7%C3%A3o-RM-Folha-de-Pagamento-x-Ahgora-Funcion%C3%A1rios-ou-l%C3%ADderes-n%C3%A3o-s%C3%A3o-integrados-no-agendamento-autom%C3%A1tico
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41463411161751) Tempo aproximado para leitura: **00:03:00 min**  
  
**Ocorrência**  
Por que alguns funcionários ou líderes não estão sendo enviados para o Ahgora no agendamento automático do RM?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir da versão 12.1.2402  
  
**Causa**  
Esse comportamento ocorre quando o campo **DT.Movimento** está em branco na tela de integração com o Ahgora. O agendamento automático integra apenas os registros que possuem a **DT.Movimento** preenchida. Quando esse campo está vazio, o funcionário ou líder não é considerado para envio automático.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41463411162135)  
  
**Solução**  
Quando a integração com o Ahgora é ativada em uma base que já possui funcionários cadastrados, esses registros existentes não são enviados automaticamente pelo agendamento. Como se trata da **carga inicial**, é necessário realizar o primeiro envio manual desses colaboradores.

Após a ativação da integração, todas as novas admissões passam a ter a **DT.Movimento** preenchida automaticamente para fins de controle. Dessa forma, esses novos registros serão enviados normalmente pelos agendamentos automáticos.

**Observação**: Esta mesma regra é considerada para os **afastamentos**, somente os registros que possuírem a **DT.Movimento** preenchida serão enviados automaticamente no agendamento. Caso não tenha esta data preenchida, é necessário realizar a integração de forma manual.

**Por que alguns funcionários foram enviados automaticamente antes da carga inicial?**

Em alguns casos, funcionários admitidos antes da ativação da integração podem ser enviados pelo agendamento automático. Isso ocorre quando houve alguma alteração cadastral que gerou uma **DT.Movimento** para o registro.

Um exemplo comum é a habilitação da opção **"Utiliza ponto Ahgora"**. Essa alteração gera um movimento cadastral, preenchendo a **DT.Movimento** e tornando o funcionário apto para integração automática.

**Quando a DT.Movimento é gerada?**

A **DT.Movimento** é criada sempre que ocorre uma alteração em dados cadastrais que são enviados ao Ahgora, como por exemplo:

* Nome;
* Nome social;
* Cargo;
* Opção **"Utiliza ponto Ahgora"**;
* Outros campos integrados com o Ahgora.

Se não houver nenhuma alteração cadastral em campos integrados, a **DT.Movimento** permanecerá em branco.

**Considerações importantes**

* Apenas os funcionários e líderes admitidos antes da ativação da integração necessitam de uma primeira integração manual.
* Após essa carga inicial, qualquer alteração cadastral gerará uma **DT.Movimento**, permitindo que as próximas atualizações sejam enviadas automaticamente pelo agendamento.
* Funcionários admitidos após a ativação da integração já terão a **DT.Movimento** criada durante o processo de cadastro e, portanto, serão integrados automaticamente.
