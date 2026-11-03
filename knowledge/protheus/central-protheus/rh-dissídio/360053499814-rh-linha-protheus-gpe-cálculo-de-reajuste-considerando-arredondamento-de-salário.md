---
article_id: 360053499814
category: RH - Dissídio
content_hash: 0a79fbdec95d07b3aa5fc9eefdc6b728a409f3e9e9b8c389e753996cd03961e3
fetched_at: '2026-06-28T22:43:43.226107+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo de reajuste considerando arredondamento
  de salário
type: support-article
updated_at: '2025-08-06T18:21:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053499814-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-reajuste-considerando-arredondamento-de-sal%C3%A1rio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33994250796567)** Tempo aproximado para leitura:**01:00:00 min**

**Dúvida**Como funciona o arredondamento de salário no cálculo do reajuste salarial?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de pessoal - A partir da versão 12.  
  
**Solução**Exemplo:  
Funcionário que recebe o salário de 2.176,38 + 2.5% de aumento = 2.230,7895.  
  
Caso não queira nenhum tipo de arredondamento o sistema irá retornar esse resultado:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089316034)  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089316114)  
  
Caso queira o arredondamento de acordo com a terceira casa decimal após a virgula:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091464613)  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089317154)  
  
Importante: Caso as opções da pergunta "critério de arredondamento" não te atenda, é possível informar os centavos de arredondamento na pergunta abaixo, conforme conceito da rotina:   
  
**Arredonda em R$ ?** : Informe um valor para aplicação da regra de arredondamento. O valor informado aqui não é explicitamente o que será aplicado. O valor aplicado será o resto da divisão do salário reajustado pelo valor informado neste campo.

**Exemplo 1:**  
Salário = 4316,00  
Reajuste de 2,5%  
Salário Reajustado = 4423,90  
Arredonda em R$0,10  
**Calculo efetuado:** Inteiro(4423,90 / 0,10) = 44.239 (Não tem resto, portanto o valor permanece 4423,90)  
Novo Salário = 4423,90

**Exemplo 2:**  
Salário = 4316,00  
Reajuste de 2,5%  
Salário Reajustado = 4423,90  
Arredonda em R$0,20  
**Cálculo efetuado:** Inteiro(4423,90 / 0,20) = 22.119 (Sobra R$0,10, porque 22.119 \* 0,20 = 4423,80)  
Novo Salário = 4424,00 (4423,90 + (0,20 - 0,10) valor incluído menos o resto)

**Saiba mais:**

[Página Centralizadora do Dissídio](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109132-RH-Diss%C3%ADdio)
