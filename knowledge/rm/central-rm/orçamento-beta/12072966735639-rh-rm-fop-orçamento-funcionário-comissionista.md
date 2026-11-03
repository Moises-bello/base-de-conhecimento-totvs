---
article_id: 12072966735639
category: Orçamento (Beta)
content_hash: 183ddc1ad75176695aa20f67850148ac714e06c5c1ae70150a3ec5869d69ddff
fetched_at: '2026-06-28T22:46:50.259692+00:00'
product: rm
section_id: 1500000834601
source: central-rm
title: 'RH - RM - FOP - Orçamento: Funcionário comissionista '
type: support-article
updated_at: '2024-09-16T18:54:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12072966735639-RH-RM-FOP-Or%C3%A7amento-Funcion%C3%A1rio-comissionista
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:02:26 min  
  
Dúvida**  
Como realizar geração Orçamento para funcionários comissionistas que não possuem salario cadastrado?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**  
1. Crie o Perfil de Admissão e veja que aqui aceitou salvar o salário como zero.  
![](https://totvssuporte.zendesk.com/attachments/token/2ou2QMPSJ46yY0QWntJFTgGmF/?name=image.png)  
  
2. Na opção Dados do orçamento crie um orçamento conforme segue;  
  
Na Step Admissão utilizei a chapa 00002 que é uma chapa base de comissionista. Você poderá utilizar a chapa base ou o perfil criado no passo 1.  
  
Veja que tive que informar valor 1,00 como salário e cadastrei 2 admissões para comissionista.  
  
![](https://totvssuporte.zendesk.com/attachments/token/wpWgd8V8bPA0C0b5BUeCMD8J5/?name=image.png)  
  
3. Na Step de grupo de eventos crie um específico para comissionista com o evento 0084.  
  
![](https://totvssuporte.zendesk.com/attachments/token/63KbVUG1AkkUqaEGWRbrMJ4s0/?name=image.png)  
  
No evento 0084 vincule uma formula para buscar o valor mínimo do sindicado.  
  
![](https://totvssuporte.zendesk.com/attachments/token/XmZvl4D59q33WgQwzIRlqpOOp/?name=image.png)  
  
4. Após o cálculo do orçamento veja que gerou movimentação para o funcionário e para as admissões considerando o salario mínimo do sindicato.  
  
Caso queira provisionar um valor maior de comissão basta otimizar a formula de cálculo buscando de uma tabela que tenha essa informação. Talvez da ficha financeira de outro comissionista.  
  
![](https://totvssuporte.zendesk.com/attachments/token/gYTBHPhjh6S4UuDSLB0qZQoEj/?name=image.png)  
  
**Saiba Mais**

[RH - RM - FOP - Orçamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4422739001623-RH-RM-FOP-Or%C3%A7amento)
