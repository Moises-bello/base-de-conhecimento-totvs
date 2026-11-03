---
article_id: 11313435166359
category: SIGAEST - RELATORIOS
content_hash: 71eaa80f8acd83f25db534a356d80ad4a226a1eb6f58eb735d66a6690ea19f6a
fetched_at: '2026-06-28T22:39:06.090508+00:00'
product: protheus
section_id: 1500001538841
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR260 imprime qual
  descrição de Armazém quando Aglutinado por Filial?
type: support-article
updated_at: '2026-02-25T20:15:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11313435166359-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR260-imprime-qual-descri%C3%A7%C3%A3o-de-Armaz%C3%A9m-quando-Aglutinado-por-Filial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38644018196631) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Qual descrição de Armazém é impresso quando emitido o relatório Aglutinado por Filial?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**  
Ao emitir o relatório Posição de Estoques Analítico (MATR260) ***aglutinado por Filial ou Empresa*** e com a pergunta "***Imprime Descrição do Armazém"*** igual a "***Sim",*** a descrição que será impressa é sempre do ***último Armazém no intervalo que o produto tenha saldo***.

Veja no exemplo simulado abaixo:

***- DESCRIÇÃO DOS ARMAZÉNS***

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11314374874391)

***- SALDO DO PRODUTO***

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11314074956311)

***- PARÂMETROS DO RELATÓRIO***

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11314184023191)

***- RESULTADO DA IMPRESSÃO***

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11314258632087)

***Dica:*** Nesse cenário, como está emitindo o relatório por Filial ou Empresa, utilizar essa pergunta igual a Não;

Outra alternativa, seria customizar o padrão do relatório, a TOTVS disponibiliza o fonte desse relatório, [clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058126794-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Fontes-de-relat%C3%B3rios-Estoque-para-altera%C3%A7%C3%A3o-ou-customiza%C3%A7%C3%A3o-fora-do-padr%C3%A3o) e veja como fazer o download no portal do Cliente.

***Saiba Mais:***  
[*Clique aqui e veja mais artigos sobre Relatórios no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538841-SIGAEST-RELATORIOS)
