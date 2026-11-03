---
article_id: 37397500444311
category: Financeiro - Configurador
content_hash: b7f8efe748c5ccba605f200ee8a92df53909b325a470608cf31ced34677e222b
fetched_at: '2026-06-28T22:37:57.646403+00:00'
product: protheus
section_id: 1500001539601
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFIN - Movimentações geram o erro
  Data width error
type: support-article
updated_at: '2026-01-05T10:37:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37397500444311-Cross-Segmentos-Backoffice-Protheus-SIGAFIN-Movimenta%C3%A7%C3%B5es-geram-o-erro-Data-width-error
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37397468871703) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida:**

Em rotinas de processamentos ou movimentações no módulo Financeiro, é apresentado o erro: **"Data Width error"**.

**Ambiente:**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.

**Solução:**

O erro **"Data Width error"** ocorre quando o sistema tenta gravar ou processar um valor numérico que excede a capacidade de largura (tamanho) definida para um campo ou variável de memória.

**Exemplo:** o campo suporta até 14 dígitos com 2 decimais, mas o cálculo gerou um valor que necessitaria de **15 dígitos ou mais),** excedendo a capacidade pré determinada para este campo.

Para correção deste incidente, realize os seguintes passos:

1. Identifique no **error.log** qual é o campo ou variável que está gerando o estouro de tamanho;  
   **Exemplo**: Data width error - Field: **E5\_VALOR**
2. Acesse o módulo **Configurador (SIGACFG)**;
3. Vá em **Dicionário de Dados** > **Base de Dados** > **Dicionário**
4. Pesquise pela tabela citada no erro e verifique o tamanho atual do campo;

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/37397500434839)
5. Avalie se há necessidade de aumentar o tamanho do campo no dicionário ou se existe algum dado inconsistente (valor exorbitante) sendo digitado ou calculado que esteja causando o erro;
6. Caso realize a alteração de tamanho, confirme as alterações para que o sistema atualize a estrutura da tabela no banco de dados.
