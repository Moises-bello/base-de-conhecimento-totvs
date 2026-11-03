---
article_id: 38102008324631
category: Financeiro - Smart View
content_hash: 0fdecebdcfabcd69c3e0801b9897c9a66307e5d4b2c68181783d2f632d2482c1
fetched_at: '2026-06-28T22:37:44.842659+00:00'
product: protheus
section_id: 32632656432151
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - Smartview -  erro: "The requires
  authentication. The server might return this response for a page behind a login."'
type: support-article
updated_at: '2026-02-02T16:47:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38102008324631-Cross-Segmentos-Backoffice-Linha-Protheus-Smartview-erro-The-requires-authentication-The-server-might-return-this-response-for-a-page-behind-a-login
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38102008303383) Tempo aproximado para leitura: **00:04 min**  
  
**Dúvida**  
Ao acessar relatórios através do Smart View, o sistema apresenta a mensagem de erro: BadRequest: "The requires authentication. The server might return this response for a page behind a login."  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/38102008304535)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da release 12.1.2210.  
  
**Solução:**

É comum que esse incidente ocorra quando o parâmetro **MV\_HVERAO** está ativado.

Quando o **MV\_HVERAO** está configurado como **.T.**, o Protheus realiza automaticamente o ajuste de fuso horário referente ao horário de verão. Com isso, o **Token de autenticação do usuário passa a ser gerado com uma hora a menos em relação ao horário do servidor**.

Esse comportamento faz com que o **Smart View interprete o Token como já expirado no momento da sua criação**, impedindo a autenticação do usuário e, consequentemente, o acesso aos relatórios.

Para correção do cenário, é necessário **desabilitar o ajuste automático de horário de verão no Protheus**, ajustando o parâmetro **MV\_HVERAO** para **.F.**.  
Após essa alteração, a geração do Token passa a respeitar o horário correto do servidor, normalizando o processo de autenticação no Smart View.

1. Acesse o módulo **Configurador (SIGACFG)**.
2. Navegue até **Ambiente > Cadastros > Parâmetros**.
3. Localize o parâmetro **MV\_HVERAO**.
4. Altere o conteúdo do parâmetro para **.F.** (Falso).  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/38101991440663)
5. Confirme a alteração, reinicie o sistema e realize um novo teste de acesso ao Smart View na filial onde o incidente ocorria.
