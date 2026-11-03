---
article_id: 360056304554
category: RH - Folha de Pagamento
content_hash: 18419460d8f8cd1f0ac7fc1bf485ade298f126dee9a968452c8c2dedde3d666f
fetched_at: '2026-06-28T22:44:16.031944+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - O que fazer no sistema quando há desligamento e
  admissão do mesmo funcionário no período
type: support-article
updated_at: '2025-08-06T17:29:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056304554-RH-Linha-Protheus-GPE-O-que-fazer-no-sistema-quando-h%C3%A1-desligamento-e-admiss%C3%A3o-do-mesmo-funcion%C3%A1rio-no-per%C3%ADodo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26273702440087) Tempo aproximado para leitura: 00:02:00 min**

**Ocorrência**O que fazer no sistema quando há desligamento e admissão do mesmo funcionário no período?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoas**- Todas as versões****Solução**Para essa situação o ambiente deverá estar com o ultimo Acumulado RH e possuir no Menu a nova rotina dos múltiplos vínculos **(****GPEM930),** rotina essa que trata múltiplos vínculos.  
  
Por mais que não se trate da situação de múltiplos vínculos foi necessário efetuar a configuração, pois no mesmo período o sistema encontrou duas matriculas com o mesmo Número de CPF.  
  
Neste cenário daremos o exemplo de jovem aprendiz que foi efetivado no mesmo período, mas a configuração é a mesma para outras categorias.   
  
- Para isso deverá validar se já possui a nova rotina de Múltiplos Vínculos. Caso não tenha em seu Menu a rotina GPEM930, inclua.  
[https://tdn.totvs.com/pages/viewphttps://tdn.totvs.com/pages/viewpage.action?pageId=552575179age.action?pageId=552575179](https://meet.google.com/linkredirect?authuser=0&dest=https%3A%2F%2Ftdn.totvs.com%2Fpages%2Fviewpage.action%3FpageId%3D552575179)  
- Cerifique-se que os roteiros de cálculos a fórmula **S\_MULTV** esteja desabilitada.   
- Habilite o mnemônico P\_MULTV  
- Ao entrar na rotina GPEM930 - Múltiplos Vínculos, as matriculas desse funcionário, não constarão.   
- Na SRA (cadastro de funcionário),  deve estar com o campo Ocorrência = 05 nas duas matriculas  
- Se atentar a data base que o sistema está logado, pois ao alterar os dados na SRA (cadastro do funcionário) é populado a tabela SR9, e a data da alteração deve estar dentro do período, senão o sistema não entende o campo preenchido. Neste caso, se o teste será feito no período 09/2020 (exemplo), deve estar logado dentro do período, ou se estiver em outro período no ambiente de teste, deve estar logado no período que estiver aberto.

Cenário:  
- Cadastro do funcionário com o mesmo CPF e o campo RA\_OCORREM preenchido com 05

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360095562434)  
  
- Desabilite a fórmula S\_MULTV dos roteiros de cálculo.  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360095562514)  
  
- Habilite o mnemônico P\_MULTV

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097866333)  
  
- Gpem930 – não caracterizou as matriculas como Múltiplos vínculos  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097866413)  
  
- Cálculo das folhas:  
Após calculada a rescisão do Jovem aprendiz, integrado o roteiro RES   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26410049909399)  
  
- Folha do Jovem aprendiz já como celetista  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26410094621719)

Serão apresentados no calculo os Identificadores 0288 / 0289 / 0290 e 0291

**Saiba Mais**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)

[RH - Linha Protheus - GPE - INSS Múltiplos Vínculos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023123011-RH-Linha-Protheus-GPE-INSS-M%C3%BAltiplos-V%C3%ADnculos)
