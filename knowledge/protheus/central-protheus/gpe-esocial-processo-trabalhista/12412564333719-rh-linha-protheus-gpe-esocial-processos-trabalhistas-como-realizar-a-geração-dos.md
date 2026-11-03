---
article_id: 12412564333719
category: GPE - eSocial - Processo Trabalhista
content_hash: 908efce56c820cc16687723b85ae1d444e6cc0ad540200466f502485e95a06bc
fetched_at: '2026-06-28T22:45:00.649283+00:00'
product: protheus
section_id: 10604669539479
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - Processos Trabalhistas - Como realizar
  a geração dos eventos de processo trabalhista na rotina GPEM038
type: support-article
updated_at: '2024-02-01T18:24:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12412564333719-RH-Linha-Protheus-GPE-eSocial-Processos-Trabalhistas-Como-realizar-a-gera%C3%A7%C3%A3o-dos-eventos-de-processo-trabalhista-na-rotina-GPEM038
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18696053594647) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como realizar a geração dos eventos S-2500, S-2501 e S-3500 para o TAF?  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**É necessário realizar a inclusão do processo trabalhista nas rotinas de Processo (APTA100) e Dados eSocial (TAFA552D).

Após inclusão do processo, acesse a rotina GPEM038 - Geração Processos Trabalhistas:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12410210948503)

* A **Data Inicial e Data Final** obrigatoriamente deve ser no mesmo mês e ano, sendo a **data da decisão** localizada nas rotinas Processo (APTA100)
* **Marcar os eventos** conforme necessidade S-2500/S-2501/S-3500
* **Selecionar a empresa** que será gerada, conforme **[MOS](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-2-consolidada-ate-a-no-s-1-2-03-2023.pdf)** os eventos devem ser cadastrados no CNPJ raiz do declarante (matriz)
* Caso seja uma retificação, marcar a opção: Gera Retificador

No **Filtro** devemos **informar CPF do Reclamante e Numero do Processo** ( RE0\_PROJUD), os campos não podem ficar em branco, se necessário gerar para mais de um CPF ou processo preencha os campos conforme *print*:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18696638008599)

Selecionar o botão **Processar** para geração do evento selecionado. O sistema apresentará o *log* informando se o evento foi gerado ou se houve alguma inconsistência.  
  
**Saiba Mais**  
Para saber mais consulte os *links*abaixo:   
[RH - Linha Protheus - GPE - eSocial - Processos Trabalhistas - Premissas para geração dos eventos do eSocial para Processos Trabalhistas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13317899021847)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-1-consolidada-ate-a-no-s-1-1-01-2023-retificada-em-20230124.pdf)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
