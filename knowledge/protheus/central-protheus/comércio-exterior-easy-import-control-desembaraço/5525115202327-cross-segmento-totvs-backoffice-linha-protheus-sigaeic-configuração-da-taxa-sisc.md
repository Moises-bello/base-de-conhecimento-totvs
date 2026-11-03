---
article_id: 5525115202327
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: a94dc995bce3c314fb10257d95d1749cd1f44bb7d19254e72ed9e695b4114078
fetched_at: '2026-06-28T22:39:51.404160+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus -SIGAEIC - Configuração da
  taxa siscomex
type: support-article
updated_at: '2022-04-18T18:37:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5525115202327-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Configura%C3%A7%C3%A3o-da-taxa-siscomex
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como configurar o cálculo da taxa siscomex?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - *Easy Import Control* - Todas as versões  
  
**Solução**A Taxa de Siscomex, quando “Não tem DI Eletrônica” , ou seja **MV\_TEM\_DI igual F** pode ser rateado por:

* **Valor;**
* **Quantidade de Adições;**

Configuração

1. O parâmetro **MV\_CODTXSI** , deve estar com o código da despesa Taxa Siscomex que está no cadastro de despesas. Exemplo: 415.
2. A Taxa Siscomex tem que ser Base de ICMS= 1- Sim e Rateia Peso= 2-Nao.  
   ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5523745820055/mceclip0.png)
3. A Taxa Siscomex aparece nas Notas: Primeira/ Única e Mãe.
4. Parâmetro **MV\_TXSIRAT**: Rateado por CIF despesa base de ICMS, caso o parâmetro esteja igual a **T (verdadeiro) rateia por Valor**, parâmetro igual a **F (falso) rateia por Quantidade;**
5. Parâmetro **MV\_EIC0005**: Define que a taxa Siscomex pode ser rateada por CIF quando despesas base de ICMS rateadas por FOB;
6. Parâmetro **MV\_RATCIF**: Configura rateio de despesas por valor na NF SIGAEIC, caso esteja igual a **S = Rateio por CIF, N = Rateio por Valor;**
7. Parâmetro **MV\_EIC0038:** Para a rotina de Receb. Importação (EICDI154) que permite ao usuário efetuar o rateio das **Despesas Base Imposto** **por CIF ou por FOB**, respeitando a configuração do parâmetro 'MV\_RATCIF'. O conteúdo deste parâmetro deve obedecer a seguinte regra, para ratear por CIF (.T.) e para ratear por FOB (.F.).    
   **Observação**: Vale lembrar que esta configuração apenas será considerada caso o parâmetro 'MV\_RATCIF' estiver habilitado."

A Taxa de Siscomex, quando “Tem DI Eletrônica” ou seja **MV\_TEM\_DI igual T**, pode ser calculado por "quantidade de adições".

Configuração:

1. O parâmetro **MV\_CODTXSI** , deve estar com o código da despesa Taxa Siscomex que está no cadastro de despesas. Exemplo: 415 (Tabela SWD);
2. Se o parâmetro **MV\_TXSIRAT** **(T) estiver ligado** o sistema rateia a taxa siscomex por CIF ou FOB, verificando o criterio definido no parâmetro **MV\_RATCIF**;
3. Se o parâmetro **MV\_TXSIRAT (F) estiver desligado** o sistema irá ratear por adição.   
   Caso o usuário informe um valor diferente do calculado pelo sistema o rateio será por FOB (Ex: Valor para uma adição R$ 374,00 e o usuário informa R$ 308,00, o sistema irá ratear R$ 308,00 por FOB).  
   ![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5524422146711/mceclip1.png)  
   Neste caso, é necessário verificar se a quantidade de adição do processo esta de acordo com a DI, e se os valores para a taxa siscomex estão informados corretamente.   
   Para conferencia dos valores acesse o SIGACFG em Atualizações \ Bases de Dados\Dicionário\Bases de dados selecione Tabelas Genéricas, busque pela tabela C5:  
   ![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5524556963991/mceclip2.png)
