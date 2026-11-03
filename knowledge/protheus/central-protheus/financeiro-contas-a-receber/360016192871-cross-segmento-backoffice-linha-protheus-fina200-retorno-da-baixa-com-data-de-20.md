---
article_id: 360016192871
category: Financeiro - Contas a Receber
content_hash: 6d800c25aa127216588557071c33f0aadecc54997bcb736c31f7f4869acee1a7
fetched_at: '2026-06-28T22:38:12.700025+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - FINA200 - Retorno da baixa com
  data de 2020
type: support-article
updated_at: '2021-09-30T22:10:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016192871-Cross-Segmento-Backoffice-Linha-Protheus-FINA200-Retorno-da-baixa-com-data-de-2020
---

**Ocorrência**No módulo **FINANCEIRO** rotina **FINA200**, ao realizar o retorno das baixas via **CNAB**é apresentada a na baixa data de 2020.  
  
**Ambiente**  
Cross Segmento - Backoffice Linha Protheus – Financeiro – A partir da versão 11.80  
  
**Causa**   
Esse incidente ocorre, pois a parametrização do sistema está incorreta para o Formato da data que é usado pelo sistema no retorno.   
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse o modulo financeiro - 06;  
2. Entre na Rotina Parâmetros de Bancos - (**FINA130**) ;  
3. Na configuração do Banco , Aba cadastrais - Campo FORMATO DATA.  
4. Ajustar o campo para valor = 4 - formato - ddmmaaaa;

Imagem ilustrativa abaixo:

![FINA130.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360011834232/FINA130.png)
