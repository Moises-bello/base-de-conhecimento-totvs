---
article_id: 39963628597143
category: SIGAEST - MOVIMENTAÇÕES
content_hash: bffbd74659876b1eac1294164fb4f23ece095fc613f79fa78c6c7e145e7274b1
fetched_at: '2026-06-28T22:38:55.744732+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA106 - type mismatch
  on .AND.  on MATGERAAE(COMXFUN.PRX)
type: support-article
updated_at: '2026-04-24T10:58:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39963628597143-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA106-type-mismatch-on-AND-on-MATGERAAE-COMXFUN-PRX
---

O erro "*type mismatch on .AND. on MATGERAAE(COMXFUN.PRX)*" na Pré-Requisição (MATA106) ocorre quando o parâmetro MV\_SOLICSA está com tipo errado (Caracter em vez de Lógico). A correção é alterar o tipo para lógico (L) via Configurador, o que elimina o erro no error.log.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39963636740119) Tempo aproximado para leitura: **00:01:12 min**  
  
**Dúvida**  
Como corrigir o error.log "*type mismatch on .AND.  on MATGERAAE(COMXFUN.PRX)*" na Pré-Requisição (MATA106)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
Normalmente este erro é apresentado devido ao parâmetro **MV\_SOLICSA** estar com o tipo (X6\_TIPO) = C -> **Caracter** sendo que o correto é L -> **Lógico**. Dessa forma, será necessário alterá-lo para que o erro não seja reproduzido. Caso não consiga alterar via Configurador.

No padrão o parâmetro é do tipo lógico.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39964496739351)

Após o ajuste o error log deixará de ocorrer.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
