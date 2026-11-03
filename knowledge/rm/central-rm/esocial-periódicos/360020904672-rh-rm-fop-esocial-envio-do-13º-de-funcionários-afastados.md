---
article_id: 360020904672
category: esocial - Periódicos
content_hash: b232ade5aebbdc00df1cb41dac59bd0544c5a399805da71be1afef942c54c4fd
fetched_at: '2026-06-28T22:47:09.253482+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: RH - RM - FOP - eSocial - Envio do 13º de funcionários afastados
type: support-article
updated_at: '2024-06-17T12:32:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020904672-RH-RM-FOP-eSocial-Envio-do-13%C2%BA-de-funcion%C3%A1rios-afastados
---

**Dúvida**Como realizar o envio do 13º para o eSocial no caso de funcionários afastados?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**O **Anexo II - Tabela de Regras** do Leiaute do eSocial informa que todos os trabalhadores admitidos em período igual ou anterior ao período de apuração que não estejam desligados ou cujo desligamento seja posterior ao período de apuração devem possuir o respectivo evento de remuneração já encaminhado para o mesmo período de apuração, exceto se o trabalhador estiver afastado durante todo o período de apuração em um dos seguintes códigos de afastamento [03,05,06,07,11,12,13,14,21,22,23,24,25,27,28,30,31].  
  
Para os funcionários cujo motivo do afastamento não se enquadra nos supracitados, deve-se enviar normalmente os eventos periódicos anuais relacionados ao 13º salário.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9913803643031)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9914123938711)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9914241358615)

**Importante**  
1. No caso de afastamento por acidente de trabalho (motivo **01 - Acidente/Doença do trabalho**), o eSocial está retornando a **mensagem de erro 162** informando que é necessário o envio da remuneração para o funcionário. Entretanto, este funcionário, quando afastado durante todo o ano, também não possui direito ao 13º. Entramos em contato com a Central de Atendimento do eSocial visto que a **regra de validação não condiz com a condição de pagamento**. Fomos orientados a, nestes casos, lançar uma verba de base de cálculo sem incidência, com rubrica informativa (9989) e um valor simbólico. Encaminhar um **S-1200 anual** para o funcionário com esta **verba informativa** e posteriormente encaminhar o S-1299 de fechamento anual.  
  
2. Foi criado o código de cálculo [CC 343 - Base de FGTS 13º Salário de Afastados](https://tdn.totvs.com/pages/releaseview.action?pageId=452719700) com o objetivo de facilitar a composição da Base de FGTS 13º do Funcionário afastado por Acidente de Trabalho(T), Serviço Militar(M) ou Doença Ocupacional(O). O código de cálculo 343 é semelhante ao código de cálculo 315, porém não faz nenhum cálculo interno no sistema, sendo necessário que o usuário insira uma fórmula para calcular o valor do evento e faça o lançamento do evento de forma manual para o envelope de pagamento do funcionário. Conforme informações da Central de Atendimento do eSocial, o S-1200 anual será utilizado apenas para a DCTFWeb, ou seja, serão apurados e retornados apenas os valores de INSS. Sendo assim, como o **CC 343 refere-se à FGTS**, deverá ser enviado **apenas no período de apuração mensal**.  
  
**Saiba mais**  
Para mais informações acesse:  
      • [Orientações para realizar o pagamento do 13º Salário - eSocial](http://tdn.totvs.com/pages/viewpage.action?pageId=439363960)   
      • [Relação do tipo de afastamento x motivo de afastamento eSocial](http://tdn.totvs.com/display/LRM/Evento+S-2230)
