---
article_id: 1500003113541
category: Financeiro - Liquidação a Receber
content_hash: 7948cc10e0e6654051d352004a2950f5c4b2b36396d044e76735fc82d1a3211c
fetched_at: '2026-06-28T22:37:42.330092+00:00'
product: protheus
section_id: 33830247616663
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FINA460 - Help FIN460AGRV
type: support-article
updated_at: '2026-05-20T17:18:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003113541-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FINA460-Help-FIN460AGRV
---

**Ocorrência**  
Ao efetuar uma Liquidação a Receber (FINA460) apresenta uma mensagem Help FIN460AGRV  
![teste_1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360104328613)  
  
**Ambiente**  
Microsiga Protheus – Financeiro – A partir da versão 12.1.17  
  
**Causa**  
Ocorre quando já possui um título em sua base com as mesmas informações que está para gerar.   
  
  
**Solução**  
A mensagem apresentada não caracteriza um erro do sistema, mas sim uma validação da rotina ao identificar que já existe um título na base com a mesma combinação de informações do registro que está sendo gerado.

Nas versões mais recentes, a rotina também passou a validar corretamente os campos configurados como obrigatórios, comportamento que anteriormente não ocorria em determinadas operações.

Os campos Prefixo, Número, Parcela e Tipo de Título compõem a chave primária da tabela SE1, portanto não é permitido existir mais de um título com a mesma combinação dessas informações.

Dessa forma, orientamos:

* Validar as informações apresentadas no help da mensagem;
* Conferir se já existe registro na tabela SE1 com os mesmos dados;
* Caso necessário, realizar o preenchimento correto da pergunta disponível no parâmetro F12 antes da execução da rotina.  
  ![teste_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102164234)

Em alguns casos, após a apresentação da mensagem inicial, pode ocorrer a exibição do seguinte help:

“AJUDA:OBRIGAT - Um ou mais campos obrigatórios não foram preenchidos. xxxxxxxxxxxxxx -> xxxxxxxxxxxxx Histórico”

O exemplo apresentado na ocorrência indica que o **campo Histórico** está configurado como obrigatório na tabela SE1. Com isso, ao realizar a liquidação pela rotina FINA460, o sistema exige o preenchimento desse campo para permitir a geração do novo registro.

Para que o processo seja concluído corretamente, será necessário:

* Ajustar a configuração do campo para que ele deixe de ser obrigatório; ou

Implementar tratamento/customização ou até mesmo gatilho que realize o preenchimento do campo obrigatório durante a execução da rotina FINA460.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40616022866583)  
  
Importante

O campo Histórico foi utilizado apenas como exemplo. O sistema poderá apresentar a mesma ocorrência para quaisquer outros campos configurados como obrigatórios.
