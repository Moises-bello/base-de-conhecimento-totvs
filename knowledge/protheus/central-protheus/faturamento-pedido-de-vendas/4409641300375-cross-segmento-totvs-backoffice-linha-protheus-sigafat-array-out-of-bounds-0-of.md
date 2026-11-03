---
article_id: 4409641300375
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: dd31d4b2cc50fe6f1129d9b37809fafc734e5f33997f2a370f487ba1da0a882e
fetched_at: '2026-06-28T22:38:38.443691+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - array out of
  bounds ( 0 of 71 ) on A410LINOK(MATV410A.PRW)
type: support-article
updated_at: '2021-09-29T11:45:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409641300375-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-array-out-of-bounds-0-of-71-on-A410LINOK-MATV410A-PRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao incluir ou alterar um pedido, ocorre o erro: array out of bounds ( 0 of 71 ) on A410LINOK(MATV410A.PRW)  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões  
  
**Causa**

O erro se refere que o array tentou ler um campo de sua composição e não foi encontrado, ou por que não existe no dicionário, ou não está marcado o uso ou por que mudou o nível dele , que no padrão é 1.  
  
Neste caso, o sistema está buscando pelo campo **C6\_RATEIO** , verificando se existe no dicionário via configurador, se está marcado como usado e se está com o nível 1, e como não encontra retorna o erro de array out of bounds.  
  
**Solução**

Para solucionar essa ocorrência, realize os seguintes passos:

1. Via configurador, acesse Dicionário, Base de Dados,Dicionário de Dados ;

2. Localize a tabela **SC6** e edite;

3. Dentro da tabela **SC6**, localize o campo em questão, deixe o nível de campo igual a 1, e marque a opção usado.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409627543319/mceclip0.png)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409627566743/mceclip1.png)

4.Salve as alterações e atualize o dicionário de dados.

5.Reinicie o Smartclient para que as configurações surtam efeito no sistema.

**Obs...a partir da release 12.1.25, por padrão de dicionário de dados,  as opções de nível de campo e usado, não podem ser alteradas no configurador, já vem configurados conforme as imagens acima.**
