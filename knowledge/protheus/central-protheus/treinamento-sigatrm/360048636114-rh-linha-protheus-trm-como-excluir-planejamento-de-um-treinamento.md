---
article_id: 360048636114
category: Treinamento (SIGATRM)
content_hash: 6f30ec3c3608ce8eef982c474cc68f64b24257776349d44f6b7eb627a6d99e18
fetched_at: '2026-06-28T22:43:02.585695+00:00'
product: protheus
section_id: 206971527
source: central-protheus
title: RH - Linha Protheus - TRM - Como excluir  planejamento de um treinamento.
type: support-article
updated_at: '2021-04-06T17:05:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048636114-RH-Linha-Protheus-TRM-Como-excluir-planejamento-de-um-treinamento
---

**Dúvida**Quando um planejamento de treinamento não será mais realizado como podemos realizar sua exclusão?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Treinamento – Todas as Versões  
 **Solução**A rotina planejamento de treinamento tem como objetivo efetuar um planejamento para os cursos que serão ministrados na empresa em determinado período para um grupo de funcionários. O planejamento permite simular os custos e a quantidade de horas necessárias para o treinamento, possibilitando comparar o que foi planejado com o realizado através de relatórios.  
Sistema apenas permitirá sua exclusão quando não houver nenhuma tabela ou  rotina vinculada ao planejamento.  
Se existe algum relacionamento com este planejamento deverá avaliar e seguir o exemplo abaixo.  
  
**Exemplo de Caso:  
1.** Cadastro de treinamento com reservas:Caminho sigatrm: atualizações > calendários > treinamentos  
Observe que o calendário de treinamento esta vinculado com nosso planejamento  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072201454/mceclip0.png)  
  
**2.** Deve ser excluído a Geração das reservas:  
Caminho sigatrm: atualizações > calendários > reservas.  
Se observar a imagem em destaque existe uma reserva a este curso - calendário portanto devemos remover esta reserva para concluirmos o processo.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360073431113/mceclip1.png)  
  
Basta clicar sobre o funcionário reservado que será retirado sua reserva, salve o registro.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360073431393/mceclip2.png)  
  
**3.** Exclusão do Calendário treinamento, vinculado ao planejamento. Para isso acesse:Caminho sigatrm: atualizações > calendários > treinamentos > outras ações > excluir  
  
![Mo0B4MKnSduElXsZ9czpa5RwV (1365×468)](https://p23.zdusercontent.com/attachment/888110/Mo0B4MKnSduElXsZ9czpa5RwV?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..tBIV2Zf470dS-I-Y4BB2Ng.uRh-WY-O-e9xi11Uub5wzU2VDr5LMn6hI4e6lCwgYnVdZ1zsQZT23aDIl4IsP1AA-RRDkNuJXcEf4g3GyiaSgjRPsNQwXlCTrcLREKdYfwhg5miQK_leV20HSFtl1KD1shv_Cgi-DtCnKv5p8LfFeKONeeMd95cB5dPA1EkKXBkV523y9h2d_tUr8Vf9uVbt3lVjNSdN7_CDu_US4fJjEgrkocXwKtilC1jpfKrBv-HkCEsAu0I7ePbNj1vcNvkPzndcOMZ7kchGumsT6H9gPWGB9SHrBUBP9U3bNFqGsbE._wb8wnDmd_lUYOZb5vONCA)  
  
Necessário clicar em confirmar.  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360073431493/mceclip3.png)  
  
Será apresentado esta mensagem e o sistema apenas permitirá sua exclusão de não houver nenhum relacionamento com o registro em questão.  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360073431773/mceclip4.png)  
  
Após este verificação observe que o sistema realiza a exclusão do treinamento vinculado ao planejamento.  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360073431873/mceclip5.png)  
  
**3.** Somente quando chegar no cenário relatado acima poderá excluir o planejamento, para isso acesse:  
Caminho sigatrm: atualizações > calendários >planejamentos > planejamentos> outras ações > excluir.  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360073432033/mceclip6.png)  
  
Será apresentado a mensagem de verificação, basta clicar em confirmar.  
  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072202954/mceclip7.png)  
  
Deverá clicar em confirmar.  
  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360073432133/mceclip8.png)  
  
Observe que o planejamento foi excluído.  
  
![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072203034/mceclip9.png)
