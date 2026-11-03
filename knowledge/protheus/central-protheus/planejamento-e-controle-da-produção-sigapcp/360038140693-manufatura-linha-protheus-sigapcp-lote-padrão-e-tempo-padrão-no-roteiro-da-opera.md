---
article_id: 360038140693
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: be10ba5e51dcd0350c1e64e88be42feb65766ea10e7dfd13c528ef1b3950eb26
fetched_at: '2026-06-28T22:42:43.548130+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Lote padrão e tempo padrão no Roteiro
  da Operação
type: support-article
updated_at: '2021-07-09T16:33:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038140693-Manufatura-Linha-Protheus-SIGAPCP-Lote-padr%C3%A3o-e-tempo-padr%C3%A3o-no-Roteiro-da-Opera%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:20 min****Dúvida**Como funciona o **lote padrão** e **tempo padrão** cadastrados no **Roteiro de Operações - MATA632**?  
  
 **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**  
Nos campos **Lote Padrão** e **Tempo Padrão** do **MATA632** é registrada a quantidade produzida num determinado intervalo de tempo. Essa informação é utilizada para calcular o tempo que será necessário para a produção de uma **OP - Ordem de Produção**.  
  
Quando o **Tipo Operac** for **Normal**, o Sistema divide a quantidade da **OP** pela quantidade do **Lote Padrão** e multiplica pelo **Tempo Padrão** para saber qual o tempo necessário para a execução daquela operação.  
  
Já quando o campo **Tipo Operac** possuir o conteúdo **Tempo Fixo** ou **Ilimitado**, não são realizados cálculos, considerando o tempo definido no campo **Tempo Padrão**, independentemente da quantidade.   
Porém, se for definida que é uma operação por **Tempo Mínimo**, o Sistema sempre considera múltiplos do lote definido no cadastro até atender a necessidade do pedido.  
  
Esse cálculo acontece somente se o parâmetro **MV\_PEOPERA - O prazo de entrega dos produtos fabricados deve ser calculado pelo roteiro de operações?** estiver com o conteúdo igual a **T**. Se o conteúdo for **F** o cálculo será pelo tempo cadastrado na aba **MRP/Suprimentos** do produto no campo **Entrega - B1\_PE**.
