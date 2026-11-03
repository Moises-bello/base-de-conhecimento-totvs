---
article_id: 4427879770391
category: SIGAEST - CUSTOS
content_hash: 57312cbb1971a34391e06b7a96691628a97a8245c6e4c35d976645da5ce2ba25
fetched_at: '2026-06-28T22:39:02.227581+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - type mismatch
  on compare on MA330FOK(MATA330.PRX)
type: support-article
updated_at: '2026-04-16T11:37:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4427879770391-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-type-mismatch-on-compare-on-MA330FOK-MATA330-PRX
---

**Ocorrência**  
Ao executar o recálculo do custo médio - MATA330, o sistema retorna com o error.log type mismatch on compare on MA330FOK(MATA330.PRX)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Causa**  
A Função MA330FOK ->Checa marcação das filiais para calculo por empresa e a integridade dos parâmetros entre as filiais.  
  
Analisando o fonte podemos verificar que a função MA330FOK, tem como funcionalidade comparar os parâmetros descritos abaixo, e caso tenha alguma divergência, ira apontar na forma de um help.  
  
**Solução**  
1.  Realizar um teste configurando a pergunta "Cálculo de Custos por?" para "Selec. Filiais" e **selecionar apenas uma filial por vez** e verificar se o erro é reproduzido.   
  
2. Notando que ao selecionar **uma filial por vez, o erro não ocorre,** verifique se todos as filiais possuem o parâmetro MV\_ULMES corretamente preenchido, e avalie o tipo (X6\_TIPO) e o conteúdo (X6\_CONTEUD) dos parâmetros abaixo:

```
Exemplo de Query para SQL para filtro dos parametros:

SELECT X6_CONTEUD, X6_TIPO, X6_VAR, * FROM SX6010 WHERE X6_VAR IN ('MV_CQ', 'MV_CUSTEXC', 'MV_CUSFIFO', 'MV_CUSFIL', 'MV_CUSMED', 'MV_CUSZERO', 'MV_FIFOENT', 'MV_GERIMPV', 'MV_LOCPROC', 'MV_NGMNTPC', 'MV_NGMNTCM', 'MV_NGMNTES', 'MV_PRODPR0', 'MV_M330THR')
```

Conteudo padrão:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21465014994967)

3.  Neste exemplo, foi deixado o parâmetro MV\_ULMES com datas diferentes entre duas filiais, o sistema retornou a mensagem, "Atenção: Diferença no parâmetro MV\_ULMES''.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/12973433966999)   
4 . Outro cenário mapeado e que pode causar este erro é quando há a criação no Sistema de uma nova filial, onde o parâmetro MV\_ULMES ainda inexista para esta filial nova, fazendo assim com que o Sistema não identifique a data da última régua de Virada de Saldos (mesmo que seja nova, é necessário existir o parâmetro, que nasce com data 19970101). Ao incluir o parâmetro informando o código da filial (X6\_FILIAL), o erro deixará de ocorrer.

**Saiba mais:**  
[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)
