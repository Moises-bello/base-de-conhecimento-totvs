---
article_id: 1500001811521
category: SIGAEST - PODER DE TERCEIROS
content_hash: 34969b18987d0ffe67aa3d0e6928a658838ba4ea5ea26a4847c7a11f89bdbb6c
fetched_at: '2026-06-28T22:39:03.211452+00:00'
product: protheus
section_id: 1500001538881
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA103 Botão "Retorno
  Ben" gera mensagem de que "não foi identificada nenhuma remessa de beneficiamento
  para esta ordem de produção"
type: support-article
updated_at: '2026-02-04T17:47:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001811521-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA103-Bot%C3%A3o-Retorno-Ben-gera-mensagem-de-que-n%C3%A3o-foi-identificada-nenhuma-remessa-de-beneficiamento-para-esta-ordem-de-produ%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33308802068375) Tempo aproximado para leitura: **00:05:00min**  
  
**Ocorrência**

Ao tentar realizar o processo de retorno de beneficiamento com vínculo de OP apresenta uma mensagem "Não encontrou remessa de beneficiamento".

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Protheus Release 12.1.25 ou Superior.  
  
**Causa**

Quando o cliente realiza e configura o processo de retorno de beneficiamento com vinculo de OP, conforme a documentação [MP - SIGACOM - Retorno de beneficiamento com vínculo e baixa automática da OP no documento de entrada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050279993-MP-SIGACOM-Retorno-de-beneficiamento-com-v%C3%ADnculo-e-baixa-autom%C3%A1tica-da-OP-no-documento-de-ntrada)

No momento do retorno via MATA103 (Documento de entrada) ao clica em "outras ações" -> beneficiamento e informa a OP correspondente, ocorre a mensagem de erro:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102791473)

**Solução**  
Geralmente este tipo de HELP ocorre em alguns cenário possíveis, conforme descrito abaixo:   
  
**Desbalanceamento entre os campos D1\_OP e C2\_OP**

* Neste tipo de caso a solução é efetuar o ajuste dos campos com o mesmo tamanho   
  (atualmente o tamanho padrão do campo é de 14 caracteres)

**Não possuir nota de remessa para esta devolução:**

* Neste caso é necessário avaliar se realmente ocorreu a nota fiscal de remessa, para esta devolução, conforme demonstrado na documentação indicada no inicio deste artigo.

**Produtos de consumo sem empenho para esta Ordem de Produção**

* Este cenário geralmente ocorre quando por algum motivo não foi gerado o empenho dos itens que serão consumidos na OP. Para correção deste cenário é possível efetuar o empenho manualmente desta OP dentro das rotinas MATA380 ou MATA381.
* Caso deseje evitar possíveis recorrências deste cenário no futuro é possível configurar o parâmetro MV\_REQAUT igual "**A**" junto ao pergunta "Mostra tela Alt. de Empenhos" no F12 da rotina MATA650 igual a "SIM", conforme print abaixo:  
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/33308817555735)

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Poder de Terceiros no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360012199513-SIGAEST-PODER-DE-TERCEIROS)
