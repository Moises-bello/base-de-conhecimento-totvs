---
article_id: 4414663139863
category: Faturamento - Cadastros
content_hash: 8f06dde225f8bd0bb2ba4e306e6edfc76de3006a3452595c64a9c095246c1dee
fetched_at: '2026-06-28T22:38:36.847773+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT (Faturamento)
  - Configurar campos que não aparecem no facilitador de cadastro de clientes
type: support-article
updated_at: '2024-03-15T20:45:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414663139863-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Faturamento-Configurar-campos-que-n%C3%A3o-aparecem-no-facilitador-de-cadastro-de-clientes
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida** Como configurar campos que não aparecem no facilitador de cadastro de clientes?  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT (Faturamento) - Todas as versões.  
  
**Solução**

Para que apareça campos na funcionalidade facilitadora (**MATA984**) do cadastro de clientes (**MATA030/ ou CRMA980**) (principalmente a etapa 1/5 da funcionalidade) é necessário colocar os campos informados no parâmetro **MV\_A030FAC.**

Deve-se preencher o parâmetro com: **A1 + Nome do campo + a barra "/"**; exemplo: **A1\_CAMPOS/**

Após o nome do campo deve-se sempre incluir a barra "/", mesmo que seja o último campo informado no parâmetro.

**Exemplo 1 (Campo padrão que não aparece [A1\_NOME]):**

Padrão: Não há como selecionar o campo A1\_NOME (não vem pré-configurado)

Antes (MV\_A030FAC == vazio):

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11151126941591)

Depois (MV\_A030FAC == A1\_NOME/):

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11151223307671)

**Exemplo 2 (Campo criado customizado que não aparece [A1\_TESTE]):**

Padrão: Não há como selecionar o campo A1\_TESTE (não é dicionário padrão)

Antes (MV\_A030FAC == vazio):

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11151739608599)

Depois (MV\_A030FAC == A1\_TESTE/):

![facilitador_x_campo_de_usu_rio.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4414674729495/facilitador_x_campo_de_usu_rio.gif)

**Exemplo 3 (Mais de um campo para aparecer no facilitador);**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11151456693143)

Saiba mais:  
[Facilitador no Cadastro e Clientes (MATA030)](https://tdn.totvs.com/x/gjlPJQ)
