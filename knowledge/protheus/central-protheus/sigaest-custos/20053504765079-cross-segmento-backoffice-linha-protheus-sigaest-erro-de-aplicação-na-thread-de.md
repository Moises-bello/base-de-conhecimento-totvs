---
article_id: 20053504765079
category: SIGAEST - CUSTOS
content_hash: ff7e826b1b8ccee9dd06d278f5709862b0468fecd69415b72702d6572d245bea
fetched_at: '2026-06-28T22:39:00.336011+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Erro de aplicação
  na thread de Custo Médio
type: support-article
updated_at: '2026-01-19T17:05:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20053504765079-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Erro-de-aplica%C3%A7%C3%A3o-na-thread-de-Custo-M%C3%A9dio
---

O erro na thread de Custo Médio no TOTVS Protheus ocorre durante a contabilização por threads, usada para melhorar performance. Se o ambiente está com alta utilização de disco e processador (80-90%), não é recomendado usar multithreads. Para corrigir, desative as threads ajustando os parâmetros MV\_M330THR=1 e MV\_M330JCM em branco, reinstale as procedures 14 a 22 e processe o custo médio novamente, aumentando gradativamente as threads para identificar erros.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20053504758551) Tempo aproximado para leitura: **00:02:40 min**  
  
**Dúvida**

O que fazer quando apresentar o Erro de aplicação na thread de Custo Médio?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

**Contabilização por Thread:**

Para ganho de performance no processamento da contabilização de custos, nas rotinas Recálculo de Custo Médio (MATA330) e Contabilização do Custo Médio (MATA331) implementou-se o conceito de contabilização por Thread, que permite definir através do novo parâmetro **MV\_M330THR** o número de Threads que devem ser executadas ao mesmo tempo pelo Sistema. **Vale ressaltar que se o ambiente estiver utilizando entre 80% e 90% de sua capacidade de leitura/gravação de disco e processador,** **não é recomendado a utilização de Mult-threads.**  
  
  
**Dado isso segue abaixo alguns questionamentos a se pensar, antes de usar threads**

- Quantos "%" de sua capacidade de leitura/gravação de disco e processador esta sendo utilizado?   
- Qual o tempo médio de sua execução da rotina?   
- Houve algum aumento significativo no tempo médio? Se sim, houve alguma alteração que pudesse impactar?  
- Qual seria seria o motivo e necessidade da ativação de multi-threads em seu ambiente?

**E como corrigir o erro gerado nas threads durante a contabilização?**

O primeiro passo é desligar as threads e sua contabilização, para isso os parâmetros abaixo conforme orientação:

**- MV\_M330THR = 1**

**- MV\_M330JCM = Deixa em branco**

**- Configurar a chave TraceStack no Appserver.ini e fazer o backup do console.log**

[**TraceStack**](https://tdn.totvs.com/display/tec/TraceStack)

**- Após esses ajustes nos parâmetros, reinstale as procedures 14 até a 22,**

**- Processe novamente o Custo Médio, para avaliar se ocorre algum error log.**

Caso não ocorra nenhum erro, então aumente gradativamente as THREADS de 5 em 5, e avalie da necesside de possuir o parametro MV\_M330JCM configurado para contabilização dos movimentos 100/300/500 caso não exista necessidade, deixe esse parâmetro em branco.

Assim ficara possivel identificar em qual thread ocorre o erro, ou então se ocorrer o erro sem threads, anexar o arquivo console.log do appserver gerado com o erro do processamento e também o arquivo dbconsole.log do Dbaccess  + inspetor de objetos, para avaliação junto ao time de suporte tecnico.

**Saiba mais:**

[Clique aqui e veja mais artigos sobre Processamentos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000275147)
