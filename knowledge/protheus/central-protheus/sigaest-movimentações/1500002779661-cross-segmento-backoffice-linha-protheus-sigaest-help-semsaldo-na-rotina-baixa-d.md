---
article_id: 1500002779661
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 524b35bb935e3cf2c64f41255f0b974b71efbca31ed668dfaea12605facf7ad5
fetched_at: '2026-06-28T22:38:55.608878+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - HELP SEMSALDO na rotina
  Baixa de CQ (MATA175)
type: support-article
updated_at: '2026-01-09T10:48:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002779661-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-HELP-SEMSALDO-na-rotina-Baixa-de-CQ-MATA175
---

O erro HELP: SEMSALDO ocorre na baixa ou rejeição de Controle de Qualidade (CQ) devido a inconsistências entre saldos registrados e físicos no armazém CQ. Causas comuns incluem divergências entre tabelas, devolução indevida, customizações inadequadas e desbalanceamento em itens com rastreabilidade. Recomenda-se usar relatórios MATR282 ou Smartview, consultar o Kardex e analisar a tabela SD7. Ajustes devem ser feitos por analista especialista para evitar impactos no banco de dados.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37544944123671) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**  
Ao tentar efetuar Baixa de C.Q é retornado o HELP SEMSALDO. O que fazer para resolver este problema?

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500002870601)  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**  
O erro **HELP: SEMSALDO** é gerado durante os processos de **Baixa ou Rejeição de CQ (Rotina MATA175)**. Ele indica uma inconsistência entre o saldo registrado no documento de entrada e o saldo físico/financeiro disponível no armazém destinado ao Controle de Qualidade (definido pelo parâmetro `MV_CQ`).

### **Abaixo estão detalhados os cenários mais comuns que resultam nesta inconsistência:**

* **Divergência entre Tabela de Movimentação e Saldo Atual:** O produto possui saldo registrado no campo **D7\_SALDO** (Documentos de Entrada no CQ), porém, o saldo real no armazém de CQ (Tabela **SB2**) é inferior à quantidade que se deseja baixar.
* **Devolução de Compra Indevida:** Realização de uma Devolução de Compra (Nota Fiscal de Saída) apontando diretamente para o armazém de CQ antes de efetivar a baixa oficial do documento pelo módulo de Inspeção/Estoque.
* **Customizações nos Tipos de Movimentação (TM):** Utilização de Tipos de Movimentação diferentes do padrão Protheus para baixas de CQ (Padrões: **RE4/DE4** para requisição/devolução ou **RE6/DE6**. Movimentações customizadas podem não atualizar corretamente as tabelas de controle do CQ.
* **Desbalanceamento em Itens com Controle de Rastreabilidade:** Para produtos que utilizam controle de **Lote** ou **Endereçamento**, pode haver uma divergência entre as tabelas **SB2** (Saldos), **SB8** (Lotes) ou **SBF** (Endereços).
* Saldo da SB8 menor que o saldo disponivel na SD7 no campo D7\_QTDE.
* Saldo da SB2 menor que o saldo disponivel na SD7 no campo D7\_QTDE.
* A quantidade que se pretende baixar (armazenada no objeto de estornos/colunas da tela) não pode ser maior que o saldo disponível no lote.

### **Situações de estorno**

* Se o sistema encontrar um movimento de estorno, a validação de saldo torna-se mais "permissiva", pois ele entende que a quantidade a ser baixada deve ser comparada com a soma do **Saldo Atual do Lote (**`B8_SALDO`**)** + a **Quantidade que está sendo estornada (**`D3_QUANT`**)**.
* O sistema compara a quantidade da baixa apenas com o **Saldo Atual do Lote (**`B8_SALDO`**)**.
* O sistema verifica se há movimentos de estorno (RE5) pendentes de processamento que possam "devolver" saldo ao lote durante a operação. Se houver, essa quantidade é somada ao saldo disponível para o cálculo de viabilidade.
* Se a `Quantidade Solicitada` > (`Saldo do Lote` + `Eventual Estorno`), a rotina interrompe o processo e retorna o Help **SEMSALDO**.
* O HELP pode variar para **A175MOVLOT** caso o parâmetro de estoque negativo esteja desabilitado no ambiente, indicando especificamente que a movimentação do lote deixaria o saldo negativo.

### **Procedimentos de Validação**

Caso o erro seja apresentado, recomenda-se realizar as seguintes conferências técnicas:

1. **Relatório de Conferência (**[**MATR282**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018463012-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR282-Parametriza%C3%A7%C3%A3o-CORRETA-para-identificar-diverg%C3%AAncia-de-saldos-entre-tabelas-SB2-x-SB8-x-SBF)**) ou** [**Smartview**](https://tdn.totvs.com/pages/viewpage.action?pageId=781210758) **do mesmo:** Extrair o relatório para verificar se há desbalanceamento entre os saldos de Lote/Endereço e o saldo do armazém.
2. **Consulta de Kardex:** Analisar a rastreabilidade do item para identificar se houve alguma requisição manual ou transferência que retirou o saldo do armazém de CQ indevidamente.
3. **Análise da Tabela SD7:** Verificar se o campo `D7_SALDO` condiz com o somatório dos itens ainda pendentes de inspeção.

Devido à complexidade das tabelas envolvidas e ao risco de gerar impactos em custos e na integridade do Banco de Dados, durante a analise do cliente, ser identificado um problema entre as tabelas mencionadas, **recomendamos**:

> **Atenção:** Em casos de divergência de saldo no CQ que impeçam a operação padrão, é aconselhável a atuação de um analista especialista *in loco*. A avaliação técnica visa identificar a causa raiz da quebra de integridade e aplicar o ajuste sem comprometer o histórico de movimentações do ambiente.

**Saiba mais:**

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA175 - HELP A175LIB Problema: Quantidade a ser liberada/rejeitada inválida*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022005311)

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
