---
article_id: 7834417230999
category: Férias
content_hash: c841797e119bd62aeb28deca9e9fecbdc561133d16478f52a936247aaa9fe033
fetched_at: '2026-06-28T22:46:56.244171+00:00'
product: rm
section_id: 1500000861102
source: central-rm
title: 'RH - RM - FOP - Férias: Múltiplos Vínculos Outro emprego dentro do Mês'
type: support-article
updated_at: '2022-08-22T14:04:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7834417230999-RH-RM-FOP-F%C3%A9rias-M%C3%BAltiplos-V%C3%ADnculos-Outro-emprego-dentro-do-M%C3%AAs
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:04:07 min  
  
Dúvida**  
Como realizar calculo férias dentro do mês Múltiplos Vínculos Outro emprego?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**

Para solucionar esta dúvida, realize os seguintes passos:  
  
**1.**Parametrizar o sistema para o processo de múltiplos vínculos para atender o cálculo de INSS conforme o eSocial.

* Para calcular o INSS conforme o eSocial, será necessário marcar o parâmetro “Calcula INSS conforme eSocial” e informar a partir de quando o sistema iniciará a calcular desta forma, em Configurações | Parametrizador | Folha Normal | Geral;
* O sistema não irá trabalhar mais com chapa centralizadora, para atender o eSocial;
* Marcando esse parâmetro em uma coligada, todas deverão estar marcadas;
* O sistema irá validar a base de calculo através do CPF do funcionário.

Acessando o caminho: **Configurações | Parametrizador | Folha normal | Geral**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405510466455/mceclip0.png)

**2.**Cadastrar os códigos de cálculo abaixo para atenderem às situações de múltiplos vínculos:

[Código de Cálculo 186 - Base INSS Férias Mês Outro Emprego Desc. Complementar](https://tdn.totvs.com/pages/viewpage.action?pageId=452719931)

[Código de Cálculo 159 - INSS de Férias Outro Emprego](https://tdn.totvs.com/pages/viewpage.action?pageId=452718222)

**Para maiores informações quanto a parametrização e funcionalidades dos códigos de cálculos acima, [CLIQUE AQUI.](https://tdn.totvs.com/pages/releaseview.action?pageId=452719279)  
  
3.**Com a parametrização e o cadastro do evento acima, o sistema poderá processar o cálculo de múltiplos vínculos.   
  
Veja abaixo um exemplo do cálculo para esta situação:Cadastro férias dentro do mês:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7834254059415/mceclip0.png)  
  
Após **Salvar,**será necessário informar o evento com Código de calculo 156 em Eventos Adicionais.  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7970980036503/mceclip5.png)  
  
Deverá ser informada a base de cálculo de INSS férias no mês de outro emprego já acrescido 1/3 das mesmas evento com cc186.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7970879728535/mceclip0.png)  
  
Informar o evento com cc159 com o valor descontado no outro emprego  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7970927494295/mceclip1.png)  
  
Visualize o Recibo e o Log de calculo:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7970930120727/mceclip2.png)  
  
Print log de calculo:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7970983882391/mceclip3.png)  
O sistema realiza o calculo da Base Outro Emprego para abater o valor calculado da Base.  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7970977487255/mceclip4.png)
