---
article_id: 360060586773
category: Férias
content_hash: c0f26a40eba7aab4fd50772754ff80ddf998bded658b130ea4d1a8372a83d72b
fetched_at: '2026-06-28T22:46:56.424312+00:00'
product: rm
section_id: 1500000861102
source: central-rm
title: 'RH - RM - FOP - Férias: Pagamento de 1/3 de férias MP927 - Incidências exclusivas
  de férias'
type: support-article
updated_at: '2024-10-18T15:37:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060586773-RH-RM-FOP-F%C3%A9rias-Pagamento-de-1-3-de-f%C3%A9rias-MP927-Incid%C3%AAncias-exclusivas-de-f%C3%A9rias
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:05:00 min  
  
Dúvida**Existem vários processos para se calcular o 1/3 de férias. Caso o usuário queira que seja calculado o IRRF e Pensão Alimentícia nos eventos específicos de férias, deverá ser feito pela rotina de Diferença. Sendo assim, como realizar o pagamento de 1/3 de férias pelo processo de diferença?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Criamos uma fórmula para pagamento de 1/3 de férias:  
  
**Fórmula - Pagamento de 1/3 de Férias**SE PROCESSO = 'DIFERENCA\_FERIAS'  
ENTAO  
VALORCODCALCULO(40)  
SENAO  
0  
FIMSE  
  
1. Associar a fórmula no evento de diferença. O evento deve ser do tipo provento e ter prioridade maior que o evento de [Código de Cálculo 38 - Férias](https://tdn.totvs.com/pages/releaseview.action?pageId=452718560)  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10534518541335)  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101397173/mceclip0.png)  
  
2. Inseri-lo em Eventos Adicionais Globais de férias em **Configurações | Parametrizador | Férias | Eventos Adicionais Globais.**  
  
![](https://tdn.totvs.com/download/attachments/544711845/image2020-12-9_18-24-59.png?version=1&modificationDate=1607549099171&api=v2)  
  
3. Executar o processo de diferença de Férias, marcando a opção dissídio **não**:

![](https://tdn.totvs.com/download/attachments/544711845/image2020-12-9_18-27-28.png?version=1&modificationDate=1607549249017&api=v2)  
  
Após executar a diferença, foi calculado o evento adicional global com o valor do 1/3 devido:  
  
![](https://tdn.totvs.com/download/attachments/544711845/image2020-12-9_18-34-57.png?version=1&modificationDate=1607549697143&api=v2)  
  
**Observação:**

1. No cadastro do Evento Adicional Global é possível inserir uma fórmula de seleção para que o processo considere somente os funcionários elegíveis ao recebimento da verba adicionada. Orientamos a usar este recurso;
2. Para que seja calculada a tributação exclusiva de IR para férias é necessário marcar a incidência 'IRRF de Férias' no evento acima. O sistema irá lançar o evento de CC 61;
3. Para que seja calculada a Pensão de Férias, é necessário marcar a incidência de pensão Férias. O sistema irá lançar o evento de CC 197 e inserir na movimentação de pensão do dependente o valor correspondente a cada dependente com o tipo de movimentação 5 - Dif. Férias;
4. O valor de diferença (1/3 de férias) é lançado no envelope com o evento de CC 88. Caso queira discriminar o valor do 1/3 de férias em um evento diferente, poderá informar no evento de código 'B100' um evento de diferença de Salário.
5. Como INSS é competência e o valor não está sendo calculado por dissídio, o INSS será o da folha normal, ou seja, a diferença de 1/3 de férias será somado com o valor de base de INSS da folha.
6. O INSS da diferença de férias não abaterá no imposto de renda de férias, e sim ao calcular o IRRF de Folha.

**Saiba mais em nosso TDN:**

[MP927 - Adicional de Férias](https://tdn.totvs.com/pages/releaseview.action?pageId=544711845)
