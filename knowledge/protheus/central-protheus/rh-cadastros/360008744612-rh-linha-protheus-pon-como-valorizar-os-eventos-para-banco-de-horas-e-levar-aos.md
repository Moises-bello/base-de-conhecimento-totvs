---
article_id: 360008744612
category: RH - Cadastros
content_hash: 10402d5b6c6b1e58a383b1ea4cd1d4b3e9ae1f5dc8fd35c9fc66b4819f764600
fetched_at: '2026-06-28T22:44:52.936841+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Como valorizar os eventos para Banco de Horas e
  levar aos Resultados com a porcentagem já apontada
type: support-article
updated_at: '2025-11-10T13:42:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360008744612-RH-Linha-Protheus-PON-Como-valorizar-os-eventos-para-Banco-de-Horas-e-levar-aos-Resultados-com-a-porcentagem-j%C3%A1-apontada
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34023508391575) Tempo aproximado para leitura: 01:30:00 min  
  
Dúvida:**Como valorizar os eventos para Banco de Horas e levar aos Resultados com a porcentagem já apontada?  
  
**Ambiente:**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução:**  
Para solucionar essa dúvida, realize os seguintes passos:  
  
**1 – Valorização do Banco de Horas**

A valorização das horas apontadas no **Banco de Horas** é realizada com base na configuração dos **eventos de ponto**.

Inicialmente, o percentual aplicado sobre as horas extras é definido diretamente no cadastro do evento correspondente. Para ajustar ou criar um evento com a valorização correta, siga os passos abaixo:

1. Acesse o menu: **Atualizações > Cadastro do Ponto > Eventos**
2. Para criar um novo evento, clique em **Incluir**
3. Para modificar um evento existente, selecione-o e clique em **Alterar**
4. Na aba Banco de horas, certifique-se de que o percentual de valorização está corretamente configurado conforme a política da empresa para o cálculo de horas extras no banco de horas.  
   ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099184753)

**2 – Percentual de Valorização**

Quando o campo **Percentual** está configurado com **150%**, significa que a hora extra será valorizada com base nesse índice. Ao efetuar o cálculo mensal, subirá na tela de manutenção de banco de horas, em **Atualizações> Lançamentos> Banco de horas**, filtre o funcionário e visualize as informações em tela.  
Na tela, Por exemplo, suponha que o colaborador realize **2h00** de horas extras. Será apresentado o seguinte:

* O **saldo normal** do Banco de Horas receberá **2h00**
* O **saldo valorizado** registrará **3h00**, considerando a aplicação do percentual de 150%

> 💡 **Importante:** Essa parametrização é essencial para que, no momento do **fechamento do Banco de Horas por horas valorizadas**, o sistema considere corretamente o total de **3h00** como saldo a ser compensado ou pago.  
> ![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096870334)

Com isso, ao registrar os apontamentos na **Manutenção do Banco de Horas**, o colaborador terá, no momento do fechamento, a possibilidade de optar por **fechar o saldo com base em horas normais ou valorizadas**, conforme a preferência do cliente.

Supondo que todos os apontamentos de horas extras já tenham sido registrados com os percentuais de valorização nos respectivos eventos, os **eventos de fechamento** terão apenas a função de **consolidar os valores já lançados**. Dessa forma, o sistema considerará essas informações no momento do fechamento do Banco de Horas, refletindo corretamente os resultados.  
  
**3. Cadastro da Verba:**Em **Atualizações> Cadastro do Ponto> Verbas,** garanta que as verbas não devem ser valorizadas, devido a valorização já terem sido aplicadas na movimentação do evento do BH no ponto. Veja como deve ficar o cadastro da verba na folha que foi vinculada ao evento de fechamento do BH:  
![8.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360008140452)

Assim, as horas serão levadas sem nenhuma valorização maior que a real da qual a Empresa pagará.  
  
  
**Saiba mais:**[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)[MP - PON - Como fechar o Banco de Horas por horas normais ou valorizadas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011971991-MP-PON-Como-fechar-o-Banco-de-Horas-por-horas-normais-ou-valorizadas?source=search)
