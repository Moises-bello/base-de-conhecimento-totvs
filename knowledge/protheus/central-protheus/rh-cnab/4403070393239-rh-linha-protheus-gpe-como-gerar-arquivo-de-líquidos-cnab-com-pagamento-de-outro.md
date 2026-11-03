---
article_id: 4403070393239
category: RH - CNAB
content_hash: c0481e4c672b356909b67994d6367cc021a48f893e6d514f19d19619445e3d59
fetched_at: '2026-06-28T22:43:39.192432+00:00'
product: protheus
section_id: 360004833653
source: central-protheus
title: RH - Linha Protheus - GPE - Como gerar arquivo de líquidos (CNAB) com pagamento
  de outros bancos
type: support-article
updated_at: '2025-06-17T12:28:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403070393239-RH-Linha-Protheus-GPE-Como-gerar-arquivo-de-l%C3%ADquidos-CNAB-com-pagamento-de-outros-bancos
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32866946159767)**Tempo aproximado para leitura: **00:01:30 min**

**Dúvida**Como gerar arquivo de líquidos (CNAB) com pagamento de outros bancos?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as Versões.  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:  
  
Neste exemplo, usaremos 1 funcionário cadastrado com banco Itaú e outro funcionário cadastrado com banco Bradesco, sendo o banco pagador 237 - Bradesco. Com os funcionários já cadastrados com banco diferentes deve-se seguir o passo a passo abaixo:

1. Acesse Miscelânea / Líquidos /  Geração de Líquidos:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403165772951)

2. Selecione o roteiro que será gerado o arquivo líquido:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403158061463)

3. No campo banco, selecione o filtro e inclua todos os bancos de acordo com as duas opções apresentadas nos prints:   
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8340450702999)  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8340453938967)

4. No campo DOC outros bancos selecione a opção = "SIM":![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8441973557143)  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8441975384727)

**Obs:** importante validar com o banco, se o convênio permite o DOC para outros bancos.

5. Após o processamento, na geração do LOG de cálculo, os 2 bancos são apresentados, conforme será gerado no arquivo bancário (CNAB):  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8443586262551)

**Importante:**  
De acordo com o novo grupo de perguntas da rotina (GPEM080R2) é possível realizar o filtro de acordo com os bancos que deverão ser tratados no arquivo TXT.

Considerando o arquivo gerado com os dois bancos no passo a passo apresentado acima, realizamos um filtro para que o banco pagador não seja mais gerado no arquivo, no campo BANCO/AGÊNCIA:

Exemplo: '00100000-23699999;23800000-99999999'  
  
![GPEM080_Gif.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/8443948036887)

**Saiba Mais:**  
[Artigos - CNAB](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833653-RH-CNAB)
