---
article_id: 10592993360535
category: Rescisão
content_hash: c130e11fd68b9546a3a306ef40177855492db8bf6269e7fbb5481d2b30cc7e1c
fetched_at: '2026-06-28T22:46:54.289629+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: 'RH - RM - FOP - Rescisão: Cancelamento de Movimento demitido no mês'
type: support-article
updated_at: '2024-09-16T18:48:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10592993360535-RH-RM-FOP-Rescis%C3%A3o-Cancelamento-de-Movimento-demitido-no-m%C3%AAs
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:02:31 min****Ocorrência**  
Ao cancelar o movimento de demitido do mês o funcionário continua com a situação Demitido e com a informação de rescisão calculada igual a verdadeiro (PFUNC>RESCISAOCALCULADA=1). Para alterar essa informação de rescisão calculada via processo, é necessário fazer o cancelamento da rescisão. Porém todos os dados da rescisão são excluídos e retornado o mesmo para Ativo.   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - 12.1.2205.111 ou superior  
  
**Solução**Caso necessita que o mesmo permaneça como Demitido, porém com a informação de rescisão não calculada, para que o mesmo possa ser visualizado no portal para ajustes de informações no ponto antes do cálculo da rescisão.  
  
Foi criado o parâmetro 'Habilita controle de rescisão não calculada' no processo de cancelamento de movimento, que quando marcado, irá cancelar a movimentação do demitido no mês, sem alterar sua situação e retornando a informação de rescisão calculada para falso (PFUNC>RESCISAOCALCULADA=0).   
  
1. **Parâmetro Marcado**  
  
**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10592805964439)**Movimentação excluída:  
  
![](https://tdn.totvs.com/download/attachments/691461766/image2022-6-7_13-36-35.png?version=1&modificationDate=1654619796170&api=v2&effects=border-simple,blur-border)  
  
O campo RESCISAOCALCULADA = 0  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10592859633047)  
  
2. **Parâmetro Desmarcado:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10592864698519)**Movimentação excluída: **![](https://tdn.totvs.com/download/attachments/691461766/image2022-6-7_12-12-54.png?version=1&modificationDate=1654614774713&api=v2&effects=border-simple,blur-border)**O campo RESCISAOCALCULADA = 1 **![](https://tdn.totvs.com/download/attachments/691461766/image2022-6-7_13-33-39.png?version=1&modificationDate=1654619620160&api=v2&effects=border-simple,blur-border)  
  
Saiba Mais**  
[Cancelamento de Movimento - Demitido no mês](https://tdn.totvs.com/pages/viewpage.action?pageId=691461766)
