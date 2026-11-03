---
article_id: 16690899085335
category: SIGAEST - PROCESSAMENTOS
content_hash: 83788f196cf45e388ed3d0c44c8ea406380f5ef446dc186057d2e4b89c63aa18
fetched_at: '2026-06-28T22:39:04.916136+00:00'
product: protheus
section_id: 1500001538861
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA215 - Erro invalid
  typecast on MA215CHECK
type: support-article
updated_at: '2025-03-12T12:17:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16690899085335-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA215-Erro-invalid-typecast-on-MA215CHECK
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16690856387479) Tempo aproximado para leitura: **00:01:30 min****Dúvida**Ao processar a rotina MATA215, ocorre o erro: invalid typecast on MA215CHECK

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**Esse erro ocorre devido a rotina MATA215 estar sendo processada e algum processo ou usuário estar acessando, a mesma só é executada em modo exclusivo.

Enquanto não finalizar o processamento não pode ser acessado nenhuma rotina.  
  
Para não apresentar o error.log, altere o parâmetro MV\_A215CHK para ".T." e execute novamente a rotina.

Valide também se o seu parametro esta cadastrado conforme imagem abaixo, ele deve ser com conteudo "Lógico".

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16690834005015)

Se for diferente disso, o parametro deve ser reconfigurado via banco, uma vez o tipo sendo restrito de alteração.

**Clique aqui:**

*[MP - SIGAEST - MATA215 - É possível executar a rotina Refaz Empenhos apenas para um armazém ou produto específico?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063059713-MP-SIGAEST-MATA215-%C3%89-poss%C3%ADvel-executar-a-rotina-Refaz-Empenhos-apenas-para-um-armaz%C3%A9m-ou-produto-espec%C3%ADfico-)*

[*Clique aqui e veja mais artigos sobre Processamentos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033442-SIGAEST-PROCESSAMENTOS)
