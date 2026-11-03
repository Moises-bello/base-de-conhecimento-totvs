---
article_id: 360015437631
category: Funcionários
content_hash: 863baa1051cbd37d7b23a1cb606fc606914967e1f009a11492817063afc2e80a
fetched_at: '2026-06-28T22:47:04.221251+00:00'
product: rm
section_id: 1500000861022
source: central-rm
title: RM - FOP - Lançamento de hora extra salário substituição
type: support-article
updated_at: '2025-03-14T13:08:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015437631-RM-FOP-Lan%C3%A7amento-de-hora-extra-sal%C3%A1rio-substitui%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30644182389911) Tempo aproximado para leitura: **00****:01:53 min**  
  
Dúvida**  
Como lançar horas extras para funcionário com salário substituição?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**

Para solucionar o problema siga as instruções abaixo:

**1.**Caso não tenha um salário substituição cadastrado, para realizar o cadastro você deve abrir a ficha financeira do funcionário, clicar na sub aba "Substituição", caso não tenha nenhum período criado, crie um período na primeira folhinha branca, depois de criar o período você adiciona um funcionário que será substituído:  
  
![](https://totvssuporte.zendesk.com/attachments/token/qB8z0O23aoj94NhXayKntPxeX/?name=inline1530511581.png)​

![](https://totvssuporte.zendesk.com/attachments/token/9Vz2rhD6tjVxqERoPreqFq11z/?name=inline1727869806.png)

​  
**2.**Verifique se o evento de hora extra tem a flag "incide substituição" marcada:

![](https://totvssuporte.zendesk.com/attachments/token/qhJ5WA2q3VHy5RVWj272G5VIa/?name=inline-1778703847.png)

**3.**Ao efetuar o cadastro do funcionário que será substituído, abra o envelope do funcionário que deseja cadastrar as horas extras e faça a inclusão do evento:

![](https://totvssuporte.zendesk.com/attachments/token/6dQosZ0cQ7ehqWTVdNblkfgHq/?name=inline-1186651863.png)​  
  
**4.**Depois de cadastrar o evento de horas extras, terá de fazer lançamento de outro evento para que seja realizado o cálculo do evento de substituição, esse evento tem código de calculo 123:

![](https://totvssuporte.zendesk.com/attachments/token/S4ybwf9nEFA3gIIPm1XzzXx1u/?name=inline-1610009425.png)​  
  
**5.**Feito a inclusão dos eventos, realize o recálculo da folha e o valor de substituição será cadastrado:

![](https://totvssuporte.zendesk.com/attachments/token/atN5zcx1nofLVUmG4hT6G9EJf/?name=inline434618538.png)​

**Saiba mais:**  
[Códigos de Cálculo - descrições](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412890806807-RH-RM-FOP-C%C3%B3digos-de-C%C3%A1lculo)
