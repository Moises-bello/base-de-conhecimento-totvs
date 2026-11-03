---
article_id: 15648711756695
category: eSocial - Parametrizador
content_hash: db29c3b8e962a117894a9311836607aa278798098729a01b33561e73648296a0
fetched_at: '2026-06-28T22:47:06.280730+00:00'
product: rm
section_id: 1500000834501
source: central-rm
title: RH - RM - FOP - eSocial - Como alterar o período da folha de pagamento na geração
  do S-1210, para relacionar com o período que consta no governo
type: support-article
updated_at: '2024-10-30T13:28:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15648711756695-RH-RM-FOP-eSocial-Como-alterar-o-per%C3%ADodo-da-folha-de-pagamento-na-gera%C3%A7%C3%A3o-do-S-1210-para-relacionar-com-o-per%C3%ADodo-que-consta-no-governo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15648738571671) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como alterar o período da folha de pagamento na geração do S-1210, para relacionar com o período que consta no governo?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**Através deste processo o usuário poderá relacionar o código do período da folha de pagamento com o código de período que consta no eSocial, para realizar a alteração do campo <ideDmDev> na geração do evento S-1210 caso trabalhe com mês caixa.Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Acesse o módulo **Folha de Pagamento** e vá no menu **Configurações | Parametrizador | eSocial | De/Para | De/Para de Período**;  
  
2. Crie um novo período e informando mês e ano da competência, o período que consta na folha e o período que consta no eSocial (respectivamente);

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15648488530967)

3. Gere o XML e identifique se a *tag*ideDmDev foi alterada conforme solicitado.

**Importante**

* Caso seja necessário alterar o período do caixa no XML somente para um trabalhador, será necessário cadastrar o de/para e gerar o XML somente para o trabalhador desejado. Após isto, faz-se necessário a exclusão do de/para, pois a parametrização é realizada por mês e ano competência e não por trabalhador;
* É possível inserir também o de/para período através de fórmula.

**Saiba mais**  
Para maiores informações, acesse:

* [Como realizar a alteração do campo <ideDmDev> na entrada em produção caso trabalhe com mês caixa?](https://tdn.totvs.com/pages/releaseview.action?pageId=568942757)
* [De/Para de Período](https://tdn.totvs.com/pages/releaseview.action?pageId=568933013)
