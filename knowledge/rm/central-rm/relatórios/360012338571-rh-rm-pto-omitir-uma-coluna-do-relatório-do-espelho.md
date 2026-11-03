---
article_id: 360012338571
category: Relatórios
content_hash: 1bcaf69690534310c82073dd11de18128481aaa8204b685cb7296021f52cec05
fetched_at: '2026-06-28T22:46:39.320536+00:00'
product: rm
section_id: 1500000861642
source: central-rm
title: RH - RM - PTO - Omitir uma coluna do relatório do espelho
type: support-article
updated_at: '2025-02-19T00:47:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012338571-RH-RM-PTO-Omitir-uma-coluna-do-relat%C3%B3rio-do-espelho
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16979989859479)****Tempo aproximado para leitura:** **00:01:15 min****Dúvida**Como omitir dados de uma coluna do relatório do espelho de cartão de ponto ?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto - A partir da versão 11.82.  
  
**Solução**Para realizar a modificação de estrutura do relatório de espelho do cartão de pontoe assim omitir as informações de uma coluna, siga os passos abaixo:  
  
1. Acesse o módulo de Automação de Ponto e vá em Gestão| RM Reports | clique para expandir e listar os relatórios do produto;

![image.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360008643771)

2. Selecione o relatório e acesse a opção processos| Editar estrutura;

![image.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360008643251)

3. Quando a estrutura do relatório for aberta, expandir o item CabeçalhoNome, em grade de propriedade que será apresentada no canto direito, altere o campo Visível para **Falso.**

![image.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360008607872)

4. Este mesmo procedimento deverá ser efetuado para os demais cabeçalhos, e a opção Batidas,  na grade de propriedade que será apresentada no canto direito, altere o campo Visível para **Falso.**

**![image.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360008608192)**

5. Após esta modificação salve a alteração no relatório.

![image.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360008644451)

6. Após a modificação ao gerar o relatório as informações referente a falta não serão apresentadas.  
  
**![image.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360008608332)**

**Saiba mais**

Caso deseje formatar a estrutura do relatório acesse a documentação [Relatórios-RM Reports.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003780132-RM-BI-Formatar-campos-RMREPORTS)

Para mais informações sobre o **Relatório do Espelho do Cartão**acesse a documentação [Relatório do Espelho do Cartão de Ponto](https://tdn.totvs.com/pages/releaseview.action?pageId=452719152)
