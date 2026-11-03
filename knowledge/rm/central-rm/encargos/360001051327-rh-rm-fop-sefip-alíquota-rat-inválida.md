---
article_id: 360001051327
category: Encargos
content_hash: 0eb9e4d51c7fd35183abb6535dce11ff1964ce884a30c69b193c8af27e4d4488
fetched_at: '2026-06-28T22:46:53.439191+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: 'RH - RM - FOP - SEFIP: Alíquota RAT inválida'
type: support-article
updated_at: '2025-03-13T11:25:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360001051327-RH-RM-FOP-SEFIP-Al%C3%ADquota-RAT-inv%C3%A1lida
---

**Ocorrência**  
Ao importar o arquivo da Sefip no validador, é apresentada a seguinte mensagem de erro: 100074 Alíquota RAT Inválida.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360001704887/mceclip0.png)  
  
**Ambiente**  
RM - Totvs Folha de Pagamento - Todas as versões  
  
**Causa**  
Quando no cadastro de Seção for informada uma alíquota diferente de 1, 2 ou 3, o erro será apresentado na importar da Sefip. Veja o exemplo abaixo:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360001790988/mceclip0.png)  
  
**Solução**Para correção do erro, veja os comentários abaixo:  
  
Acesse o cadastro de seções em **"Administração de Pessoal | Seções"** e ajuste o campo **"Percentual Acidente Trabalho"**, conforme o enquadramento da empresa. O ajuste deverá ser feito nas seções onde ocorre a quebra de CNPJ, que são utilizadas para geração da Sefip.  
  
Para facilitar a identificação das seções com código RAT incorreto é possível fazer uma validação diretamente via banco de dados. Caso queira fazer desta forma, veja a consulta abaixo e ajuste conforme sua necessidade:

|  |
| --- |
| select codigo, PERCENTACIDTRAB from psecao where CODCOLIGADA=1 --Informe aqui o numero da coligada |

**Saiba mais**  
Para maiores informações sobre RAT, SAT ou FAP, [CLIQUE AQUI](http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.GPSFAP.aspx).
