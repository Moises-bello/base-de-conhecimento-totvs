---
article_id: 15195709324055
category: Rescisão
content_hash: 9d4a0f98ef2df246e3355912e353ed9cb1874979f7adbcdba8fe90657c6b8f9d
fetched_at: '2026-06-28T22:46:54.220568+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: 'RH - RM - FOP - Rescisão: Há cadastro de férias na situação marcadas e data
  de pagamento anterior a data de demissão'
type: support-article
updated_at: '2024-06-17T14:14:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15195709324055-RH-RM-FOP-Rescis%C3%A3o-H%C3%A1-cadastro-de-f%C3%A9rias-na-situa%C3%A7%C3%A3o-marcadas-e-data-de-pagamento-anterior-a-data-de-demiss%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15195701535383) Tempo aproximado para leitura: **00:02min 47sec****Ocorrência**Ao tentar realizar a rescisão ou transferência de um funcionário é retornado o erro: **"Há cadastro de férias na situação 'Marcadas' e data de pagamento anterior a data de demissão. Verifique a necessidade do lançamento das férias antes de realizar a transferência do funcionário."**

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões

**Causa**Essa mensagem é gerada pois existem períodos aquisitivos antigos ainda não finalizados no momento da transferência ou rescisão.  
  
**Solução**  
Para solucionar essa ocorrência, ao tentar realizar a transferência ou rescisão, é necessário que acesse os períodos aquisitivos anteriores desse funcionário e verifique se tem períodos a serem finalizados. Ou férias com a situação marcada em períodos aquisitivos antigos. Veja o passo a passo abaixo: 

1. Acesse **Funcionários | Período aquisitivo**, selecione o funcionário em questão e abra o período aquisitivo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15195686150679)  
  
2.  Feito isso, abra o período em aberto e todos os outros que o funcionário tenha e verifique se em algum deles possui período de gozo com a situação marcada, conforme demonstrado na imagem a seguir:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15195729235991)

3. Caso seja verificado que existem férias com esse status, é necessário alterar manualmente para finalizadas ou realizar o processo de finelização de férias. 

**Saiba Mais**

[RH - RM - FOP - Férias: Finalizar](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012328752-RH-RM-FOP-F%C3%A9rias-Finalizar-)
