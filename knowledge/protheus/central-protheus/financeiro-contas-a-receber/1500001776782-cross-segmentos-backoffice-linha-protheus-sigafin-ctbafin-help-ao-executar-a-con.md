---
article_id: 1500001776782
category: Financeiro - Contas a Receber
content_hash: b6211c0e3283b74b987277f7ded4be14ffde7c2b4b1ef7f337c74a863ddf0000
fetched_at: '2026-06-28T22:38:13.904461+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN -  CTBAFIN - Help ao
  executar a Contabilização Offline - Não existe índice para esse alias no SINDEX
type: support-article
updated_at: '2022-09-12T17:18:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001776782-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBAFIN-Help-ao-executar-a-Contabiliza%C3%A7%C3%A3o-Offline-N%C3%A3o-existe-%C3%ADndice-para-esse-alias-no-SINDEX
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:04:00 min****Ocorrência**Ao contabilizar os movimentos no financeiro, é apresentada a mensagem **Não existe índice para esse alias no SINDEX.**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102688273/mceclip0.png)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeira - Todas as versões  
  
**Causa**Mensagem apresentada **Não existe índice para esse alias no SINDEX** quando há alguma configuração inadequada no **Lançamento Padrão.**  
  
**Solução**Localize o **Lançamento Padrão (LP)**, nos campos **CTK\_LP** e **CTK\_SEQ** na tabela **CTK,** **LP** e a sequência do último registro, cujo o conteúdo provavelmente é o **LP** com problemas,  faça a validação da configuração do seu **Lançamento Padrão**. Caso tenha dúvidas na sua configuração, desabilite todos os LP´s e realize um teste utilizando um campo fixo (exemplo: **SE5->E5\_VALOR)** no **LP**que apresenta a inconsistência, retirando as customizações ou sintaxes **ADVPL**.

**Importante**O Suporte Técnico não valida/configura **lançamentos padrões**, por envolver informações sobre o negócio/processos que deseja contabilizar. Informamos que as configurações de **LPs** são de responsabilidade do **cliente/analistas de implantação**, já que o mesmo é liberado para **configurações e customizações específicas**. Caso não tenha conhecimento na utilização do **cadastro de LP**, solicite ao seu executivo de soluções de negocio (ESN) a visita de um analista in loco para avaliar seu ambiente.

**Saiba Mais**<https://tdn.totvs.com/pages/viewpage.action?pageId=235585410>
