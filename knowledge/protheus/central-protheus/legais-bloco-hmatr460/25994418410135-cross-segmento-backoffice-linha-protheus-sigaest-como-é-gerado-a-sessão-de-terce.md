---
article_id: 25994418410135
category: LEGAIS - BLOCO H/MATR460
content_hash: 133b2694bb14866d917c9358088adcf67c1588dc009f4ead8bdf0e0596d9b756
fetched_at: '2026-06-28T22:42:15.056659+00:00'
product: protheus
section_id: 1500001538741
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como é gerado a sessão
  "DE TERCEIROS USADO EM OP" no relatório MATR460 ?
type: support-article
updated_at: '2026-06-19T21:50:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25994418410135-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-%C3%A9-gerado-a-sess%C3%A3o-DE-TERCEIROS-USADO-EM-OP-no-relat%C3%B3rio-MATR460
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25994397650327) Tempo aproximado para leitura: **00:01:15min** **Dúvida**Quais as validações no relatório MATR460 para montagem da sessão "De terceiros usado em OP" ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**O conceito da sessão do MATR460 "De terceiros usado em OP" é relacionado a requisições para OP que não agregam custo (RE9/DE9):  
   
![](https://totvssuporte.zendesk.com/attachments/token/pcmEELizgVsWDneMGiVE4ZQbp/?name=image.png)  
   
Para que isso ocorra, o produto deve estar com o campo B1\_AGREGCU = 1 e a TM (Tipo de Movimento) com o campo F5\_AGREGCU = 2, desta forma quando realiza uma requisição contra OP com essa TM e com este item, é gerado uma RE9 e essa quantidade utilizada é apresentada na sessão do MATR460 "De terceiros usado em OP", após apontamento da OP esse saldo persiste nessa sessão.  
   
Essa sessão é limpa do MATR460 quando se realiza o fechamento do estoque, sendo esse o comportamento padrão.  
   
Para que seja desconsiderados do calculo do saldo do material de terceiros movimentos RE9 e DE9 pode-se utilizar o Ponto de Entrada A460TUNI.  
   
[A460TUNI - Permite gravar o arquivo de trabalho na impressão do relatório.](https://tdn.totvs.com/pages/releaseview.action?pageId=651923107)

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Bloco H e MATR460 (P7) no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538741-LEGAIS-BLOCO-H-MATR460)*
