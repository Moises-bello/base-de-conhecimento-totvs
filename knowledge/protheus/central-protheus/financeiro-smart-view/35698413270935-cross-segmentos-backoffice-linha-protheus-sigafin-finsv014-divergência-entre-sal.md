---
article_id: 35698413270935
category: Financeiro - Smart View
content_hash: 9cd68b316cb3095254ab16fed8121dc61a596931f406bab3dbe9978602bfbb38
fetched_at: '2026-06-28T22:37:44.838459+00:00'
product: protheus
section_id: 32632656432151
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN – FINSV014 – Divergência
  entre saldos bancários iniciais e finais
type: support-article
updated_at: '2026-06-16T14:34:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35698413270935-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINSV014-Diverg%C3%AAncia-entre-saldos-banc%C3%A1rios-iniciais-e-finais
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35698413263255) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Como proceder em casos de inconsistência nos saldos bancários?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
Quando houver divergências entre os saldos iniciais e finais nas rotinas financeiras, é necessário realizar uma análise retrospectiva para identificar a data exata em que a inconsistência foi originada.

**Passos**

**Passo 1)**

Acesse o módulo Financeiro (SIGAFIN), clique em Atualizações > Movimento Bancário > Saldos Bancários (FINA030).

Avalie os saldos inserindo no intervalo abrangente de datas (por exemplo: 01/01/2025 até 01/01/2026) para identificar o dia exato em que o saldo começou a divergir do saldo aglutinado do dia.

Após encontrar a data exata na rotina Saldos Bancários (FINA030) que começou a fazer a divergência dos saldos aglutinados que por isso se refletiu para os próximos dias e meses posteriores.

**Exemplo:** Exatamente na data do dia 09/06/2026, o sistema apresentou um saldo total aglutinado de R$ 50,00, mas o saldo correto deveria ser de R$ 1.000,00 a receber.

**Passo 2)**

Acesse o relatório de Extrato Bancário (FINSV014) e faça a emissão filtrando especificamente a data da divergência encontrada (utilizando a mesma data para o início e fim do período, por exemplo: 09/06/2026 até 09/06/2026).

Compare os lançamentos de entradas (a receber) e saídas (a pagar) gerados no Protheus com o extrato físico fornecido pela instituição bancária (créditos e débitos daquela mesma data) para que possa encontrar qual o título que está no extrato físico do banco, e não está sendo apresentando no extrato do protheus FINSV014 ou vise e versa.

**Passo 3)**

Após e encontrar um dos registros que está dando a divergência entre os extratos bancários.

Por meio dessa validação cruzada, verifique as seguintes hipóteses para o registro que gerou a diferença:

Se a baixa do título foi de fato gerada no sistema.

Se o título foi baixado com a data de movimentação incorreta.

Se a baixa do título não foi executada no sistema.

Se o motivo de baixa utilizado na operação estava devidamente configurado na rotina Cadastro Motivo de Baixa (FINA490) para permitir a movimentação bancária.

E entre mais detalhes..

Saiba mais:

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN  – FINA210 – Como executar corretamente a rotina de recálculo de saldos bancários quando possui SA6, SE8 compartilhadas e a SE5 exclusiva?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018852211-MP-SIGAFIN-FINA210-Como-executar-corretamente-a-rotina-de-recalculo-banc%C3%A1rio?source=search)
