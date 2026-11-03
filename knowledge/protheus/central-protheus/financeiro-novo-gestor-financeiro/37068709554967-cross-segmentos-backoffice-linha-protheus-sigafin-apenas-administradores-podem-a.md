---
article_id: 37068709554967
category: Financeiro - Novo Gestor Financeiro
content_hash: 0526ddada783a0c296deef976c80abb2d39b8a8c0f051d30fa1920f01ca85256
fetched_at: '2026-06-28T22:37:41.554123+00:00'
product: protheus
section_id: 33830415324183
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Apenas administradores
  podem acessar a rotina
type: support-article
updated_at: '2026-01-15T20:36:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37068709554967-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Apenas-administradores-podem-acessar-a-rotina
---

**Dúvida**  
Ao acessar as rotinas, FINA710, FINA716, ou FINAPP001 esta apresentando a mensagem "Apenas administradores podem acessar a rotina"  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**

Ao acessar algumas rotinas do menu Financeiro, como **Gestor Financeiro (FINA710)**, **Aplicações e Empréstimos (FINA716)** ou **Análise de Crédito (FINAPP001)**, o sistema apresenta a seguinte mensagem:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37068685072535)

📢 **“A rotina não foi restrita a administradores!”**

Houve uma **manutenção na rotina** para **remoção dessa validação indevida**, permitindo que o acesso ocorra conforme o **padrão geral do sistema**, sem exigir privilégio de administrador para execução das rotinas mencionadas.

Para correção do comportamento e normalização do acesso, é necessário **aplicar o pacote de atualização indicado abaixo e validar se o sistema esta com binários atualizados:**

* 12.1.2310:<https://r.totvs.io/p/1225691> ;
* 12.1.2410:<https://r.totvs.io/p/1225688> ;
* 12.1.2510:<https://r.totvs.io/p/1225689> ;

Após a aplicação do pacote, recomendamos que sejam realizados novos testes para validação do acesso às rotinas.
