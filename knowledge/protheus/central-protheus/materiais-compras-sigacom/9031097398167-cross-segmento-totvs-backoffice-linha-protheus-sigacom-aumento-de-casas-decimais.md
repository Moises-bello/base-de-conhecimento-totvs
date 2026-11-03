---
article_id: 9031097398167
category: Materiais - Compras (SIGACOM)
content_hash: af270623cf08d950d23fee98dcf388725a1414fa3297cb49088cad44ad12ac2d
fetched_at: '2026-06-28T22:41:11.579087+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Aumento de Casas
  Decimais
type: support-article
updated_at: '2024-12-16T12:38:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9031097398167-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGACOM-Aumento-de-Casas-Decimais
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18051664944663) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como efetuar o aumento de casas decimais e quais as inconsistências podem ser geradas?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Versão 12  
  
**Solução**O aumento de casas decimais no Protheus é uma questão delicada. Quando realizado sem os devidos critérios, ou não recebe a devida manutenção, pode causar diversas inconsistências, portanto orientamos que a referida alteração seja efetuado por um especialista em base de dados.

As possíveis inconsistências ao alterar apenas alguns campos e outros não, podem ser desde Helps apresentados pelo Sistema até mesmo divergência de valores no Compras e/ou com outros módulos integrados, como Faturamento e Estoque.

Para solucionar a inconsistência, é preciso identificar e ajustar todos os campos relacionados de modo que todos possuam configuração compatível para que os dados não se percam.

Ou seja, campos de quantidade devem todos possuir mesmo tamanho/ máscara. Campos de valor também devem possuir mesmo tamanho/ máscara.  
**Com exceção de campos de Valor Total. CAMPOS TOTAIS NÃO SE ALTERA CASAS DECIMAIS, estes devem permanecer com 2 casas decimais (evitando inclusive erros em arquivos fiscais).**

Recentemente foi criado o grupo de campos numérico que contempla todos os campos de valor unitário, corelacionados. Veja no documento abaixo procedimento a ser efetuado para habilitar o grupo de campos :

[**Grupo de campos numérico**](https://tdn.totvs.com/pages/releaseview.action?pageId=742218277)

**IMPORTANTE**: Qualquer tratamento relacionado a casas decimais é considerado um desvio do Nativo do Protheus (no qual é padrão o uso de dois dígitos).  
Portanto, é indicado que qualquer alteração neste sentido seja realizado e documentado por um analista in loco (Consultar diretamente seu ESN) para análise pontual de sua base/ seu cenário, inclusive para as manutenções dessas alterações nas Tabelas (já que com as atualizações podem ser criados novos campos e novas tabelas na base).

Para mais informações, verifique o documento : **[Aumento de Casas Decimais no ambiente Faturamento SIGAFAT](https://tdn.totvs.com/x/twEmDg)**, nesse documento você pode consultar os campos de outros módulos, que também devem ter seu tamanho ajustado.

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
