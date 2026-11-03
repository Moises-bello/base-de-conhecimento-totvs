---
article_id: 10650723657239
category: Administração de Pessoal
content_hash: 2a5f5aa41223a9be6e16a44dfab4f030745b43ee2ed61354ff1533b640ab1e24
fetched_at: '2026-06-28T22:47:01.274957+00:00'
product: rm
section_id: 1500000861042
source: central-rm
title: RH - RM - FOP - Troca de CNPJ entre Matriz e Filial
type: support-article
updated_at: '2025-03-06T19:15:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10650723657239-RH-RM-FOP-Troca-de-CNPJ-entre-Matriz-e-Filial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:48min****Dúvida**No módulo da Folha de Pagamento, como realizar a troca de CNPJ entre Matriz e Filial, caso os funcionários continuem nas seções cadastradas?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Como os funcionários continuaram nas seções cadastradas, para que seja realizado a troca de CNPJ entre matriz e filial, será necessário realizar apenas a alteração dos campos **Descrição** e **Filial**, de modo que, onde for filial, deverá colocar matriz e vice-versa. Assim, deve inserir a filial nas seções corretas, pois o CNPJ irá ficar o mesmo.  
  
Para compreender melhor o processo, segue abaixo orientações:  
  
1. Acesse: **Administração de Pessoal | Seções** e edite o cadastro da Matriz que irá virar a Filial. Feito isso, edite o campo **Descrição** e campo **Filial** com os dados da Filial e salve.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10654094827031)  
  
2. Acesse o cadastro da Filial que irá virar Matriz. Feito isso, edite o campo **Descrição** e campo **Filial** com os dados da Matriz e salve.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10654183488151)  
  
O processo será dessa maneira pois caso seja realizado a troca de CNPJ no cadastro da seção irá apresentar uma mensagem de erro, já que o sistema compreende que existe um outro cadastro com o mesmo CNPJ. Diante disso, o sistema barra e não deixa realizar a troca de CNPJ. Veja a mensagem abaixo onde é realizada a tentativa de troca de CNPJ.  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10654232043415)
