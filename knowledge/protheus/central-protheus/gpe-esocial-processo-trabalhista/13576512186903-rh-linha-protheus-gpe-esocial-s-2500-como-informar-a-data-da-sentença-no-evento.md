---
article_id: 13576512186903
category: GPE - eSocial - Processo Trabalhista
content_hash: 81c512bb34ab614fa7fbd082624cfec0f0848357d920cea8e3ac1aaa32a27567
fetched_at: '2026-06-28T22:45:00.631503+00:00'
product: protheus
section_id: 10604669539479
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2500 - Como informar a data da sentença
  no evento S-2500
type: support-article
updated_at: '2024-06-19T18:16:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13576512186903-RH-Linha-Protheus-GPE-eSocial-S-2500-Como-informar-a-data-da-senten%C3%A7a-no-evento-S-2500
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24294591499799) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como informar a data da sentença no evento S-2500?  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**O campo data da sentença {**dtSent**} deve ser preenchido com a data:   
a) do trânsito em julgado da decisão líquida proferida no processo trabalhista;   
b) da homologação de acordo judicial; ou   
c) do trânsito em julgado da decisão homologatória dos cálculos de liquidação da sentença.  
  
E somente devem ser enviados processos trabalhistas cujas decisões transitaram em julgado do dia 1º de abril de 2023 em diante.  
  
Na rotina **Cadastro de Processo** (ATPA100), deve ser informada a data no campo **Data Decisão**  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/13576027950743)**Essa data será levada para a rotina **Dados eSocial** (TAFA552D) no campo **Data da Sentença**.  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/13576184540055)**  
  
A data será demonstrada no xml do **evento S-2500**:  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/13576389017495)  
  
**Saiba Mais****Para saber mais consulte os *links* abaixo:   
[RH - Linha Protheus - GPE - Processos Trabalhistas - Premissas para geração dos eventos de processos trabalhistas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13317899021847)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-1-consolidada-ate-a-no-s-1-1-01-2023-retificada-em-20230124.pdf)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
