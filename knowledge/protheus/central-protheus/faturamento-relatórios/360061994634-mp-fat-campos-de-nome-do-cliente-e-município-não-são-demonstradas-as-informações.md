---
article_id: 360061994634
category: FATURAMENTO - RELATÓRIOS
content_hash: f08babfefa621344f302e6abb5c5b75f2082c14f49c938f00fc110aeb989db8d
fetched_at: '2026-06-28T22:38:23.005854+00:00'
product: protheus
section_id: 1500001539381
source: central-protheus
title: MP - FAT - Campos de nome do cliente e Município não são demonstradas as informações  no
  relatório
type: support-article
updated_at: '2021-04-28T15:15:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061994634-MP-FAT-Campos-de-nome-do-cliente-e-Munic%C3%ADpio-n%C3%A3o-s%C3%A3o-demonstradas-as-informa%C3%A7%C3%B5es-no-relat%C3%B3rio
---

**Dúvida**

Ao gerar o relatório matr650 -Nota fiscal para transporte, o sistema não demonstra as informações dos campos nome do cliente e município  
  
**Ambiente**Microsiga Protheus - a partir da release 12.1.23.  
  
**Solução**

Verifique se o usuário que está gerando o relatório está com restrição para dados sensíveis da lei LGPD, por que se estiver, o relatório sairá com as informações do cliente e endereço com asterisco.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003602261/mceclip0.png)  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102436034/mceclip1.png)

Se eu marcar esses campos de restrição de acesso, o relatório sai corretamente.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360104613833/mceclip2.png)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102436174/mceclip3.png)

Saiba Mais sobre LGPD:  **[LGPD - Lei Geral de Proteção aos Dados Pessoais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025475192-LGPD-Lei-Geral-de-Prote%C3%A7%C3%A3o-aos-Dados-Pessoais?source=search)**
