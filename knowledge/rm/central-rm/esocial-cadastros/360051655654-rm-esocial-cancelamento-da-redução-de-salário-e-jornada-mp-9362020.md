---
article_id: 360051655654
category: eSocial - Cadastros
content_hash: da5ff457d1debb99362825ae618f0c9387622484185b20576330d22682bf1483
fetched_at: '2026-06-28T22:47:14.577505+00:00'
product: rm
section_id: 1500000834341
source: central-rm
title: RM - eSocial - Cancelamento da redução de salário e jornada - MP 936/2020
type: support-article
updated_at: '2021-03-31T16:48:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051655654-RM-eSocial-Cancelamento-da-redu%C3%A7%C3%A3o-de-sal%C3%A1rio-e-jornada-MP-936-2020
---

**Dúvida**Como informar ao eSocial o cancelamento da redução de jornada e salário (MP 936)?  
  
**Ambiente**RM - eSocial - A partir dos *Patches* 12.1.26.258, 12.1.27.240 e 12.1.28.149  
  
**Solução**Com a liberação do novo layout 3.0 do arquivo B.E.M, foi disponibilizado um tipo especifico para o cancelamento da redução jornada e salário. Siga os passos abaixo, para o envio da informação ao eSocial:

1. No módulo **Folha de Pagamento**, acesse**Administração de Pessoal | Funcionários | Registro | B.E.M**e preencha o campo **Data do Cancelamento** com data exata de decisão do cancelamento;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083114433/mceclip1.png)

2. O sistema verifica se o evento S-2206 já foi enviado ao RET. Caso afirmativo, gera um gatilho S-3000 para exclusão deste evento com as informações do acordo B.E.M;

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083129233/mceclip2.png)

2.1. Caso ainda não tenha enviado ao RET o S-2206 com o cadastro inicial dos dados do B.E.M, estando o gatilho na fila de eventos com status **gerado**,  ao efetuar o **cadastro do cancelamento** o sistema irá apagar o gatilho da fila.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083132033/mceclip4.png)  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083134393/mceclip5.png)

**Importante**A data do cancelamento preenchida no cadastro deve representar o dia em que o acordo foi cancelado, podendo ser o mesmo dia da data do acordo.

Caso possua alguma outra alteração (exemplo, mudança de função) com a mesma data do acordo do B.E.M., será necessário a geração do gatilho manual para envio dessas informações.

Caso os campos do cadastro do **B.E.M.** já tenham sido preenchidos antes das versões que geram os gatilhos automaticamente dos novos campos (versões mencionadas no início desta documentação), será necessário a geração do gatilho manual do evento **S-3000 - Exclusão de Evento** ou **S-2206 - Alteração de Contrato de Trabalho** por funcionário.  
  
**Saiba Mais**  
Para maiores informações acesse:  
      • [Cancelamento B.E.M](https://tdn.totvs.com/pages/releaseview.action?pageId=556391463#)  
      • [MP 936 - Benefício Extraordinário Mensal](https://tdn.totvs.com/pages/releaseview.action?pageId=545641381)
