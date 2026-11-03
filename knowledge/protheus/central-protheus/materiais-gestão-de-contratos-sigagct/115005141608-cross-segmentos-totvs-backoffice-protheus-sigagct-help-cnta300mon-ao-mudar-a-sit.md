---
article_id: 115005141608
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: a1a2950b470e111a04a6bbff785707c363031bd793da441c07600e642cd6dd44
fetched_at: '2026-06-28T22:37:20.066544+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Help CNTA300MON ao
  mudar a situação do contrato para Vigente ou confirmar uma Revisão de Contrato
type: support-article
updated_at: '2026-06-22T21:35:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115005141608-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Help-CNTA300MON-ao-mudar-a-situa%C3%A7%C3%A3o-do-contrato-para-Vigente-ou-confirmar-uma-Revis%C3%A3o-de-Contrato
---

**Dúvida**

Help CNTA100MON ao mudar a situação do contrato para Vigente

**Ambiente**  
Microsiga Protheus -  a partir da versão 12  
  
**Solução**

Esta ocorrência pode ser gerada por duas situações:

***Situação 1*** - Compartilhamento nas tabelas CNA x CNF.

O compartilhamento das tabelas CNA e CNF devem ser idênticos, caso estejam divergentes deve-se realizar o devido acerto.

***Situação 2*** - Valores diferentes entre a planilha e o cronograma:

No padrão do sistema, a mensagem está relacionada a quando ao mudar a situação para Vigente ou em uma revisão o montante de Valor Total do contrato e o montante de valor do Cronograma Financeiro (somatória das parcelas do cronograma) deste contrato não possuem o mesmo valor.

Em uma Revisão, ao alterar o valor total do contrato, o montante ou valor total do Cronograma também deve ser ajustado conforme o montante que ficou o contrato.

Na revisão, caso não seja feito o ajuste do cronograma ocorre a primeira mensagem em que se tem a possibilidade de ajustá-lo automaticamente levando o valor de diferença para a última parcela do cronograma, clicando em "Sim".

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405310800663)

Caso clique em "Não" na mensagem acima, se não for realizado o ajuste do cronograma, ocorre a segunda mensagem, ao tentar confirmar a Revisão:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405315127447)

Dessa forma, o ajuste do Cronograma na Revisão do Contrato pode ser realizado clicando na opção "Sim" da primeira mensagem conforme demonstrado ou também manualmente no cronograma financeiro deixando seu montante com o mesmo que Valor Total do Contrato.

Para atualizar o cronograma antes de confirmar a Revisão, pode-se também utilizar a opção em "Outras Ações -> Atualizar Cronograma Financeiro" realizando a devida parametrização na Aba "Parâmetros/Revisão" antes de usar esta opção:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405310923671)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405310963095)

**Importante**: Embora o Help menciona que sejam revisados os cronogramas **Financeiro e Físico**, caso exista o cronograma contábil, é imprescindível que o mesmo também seja **revisado e  atualizado**.

Veja também a FAQ do link abaixo:

[***GCT0068 - Como resolver o help CNTA100MON***](http://tdn.totvs.com/display/PROT/GCT0068+-+Como+resolver+o+help+CNTA100MON)

***Saiba Mais:***

[GCT0068 - Como resolver o help CNTA100MON](http://tdn.totvs.com/display/PROT/GCT0068+-+Como+resolver+o+help+CNTA100MON)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
