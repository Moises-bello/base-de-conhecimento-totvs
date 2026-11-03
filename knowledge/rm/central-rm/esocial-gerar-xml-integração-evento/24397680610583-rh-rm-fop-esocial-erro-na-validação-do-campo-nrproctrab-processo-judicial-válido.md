---
article_id: 24397680610583
category: eSocial - Gerar XML/ Integração Evento
content_hash: c037b82b5dad1bd7273543f0a2678c386ed271d82828a31851b36ef77e942048
fetched_at: '2026-06-28T22:47:12.984438+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro na validação do campo ''nrProcTrab'': Processo
  judicial válido com 20 (vinte) algarismos no evento S-2299'
type: support-article
updated_at: '2024-09-26T15:39:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24397680610583-RH-RM-FOP-eSocial-Erro-na-valida%C3%A7%C3%A3o-do-campo-nrProcTrab-Processo-judicial-v%C3%A1lido-com-20-vinte-algarismos-no-evento-S-2299
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24397663887895) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**O erro ocorre quando geramos o evento S-2299 de **desligamento do funcionário:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24402376598551)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial -  Todas as Versões.  
  
**Causa**  
Ao gerar o S-2299 ocorre o erro quando o campo **Número do Processo Trabalhista** está preenchido sem a existência de um processo ou contém informações divergentes. Caso haja um processo, o campo deve ser preenchido com exatamente 20 algarismos conforme regra do eSocial.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24397663890583)

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse **Administração de Pessoal | Funcionários | Selecione o Funcionário;**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24403721930007)

2. Acesse a **Rescisão do Funcionário aba Rescisão;**   
3. Verifique se o **campo** está preenchido de forma indevida ou se é realmente necessário preenchê-lo.  
4. Edite o **Campo Nro. Processo Trabalhista;**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24403721940375)

3. Após seguir as orientações acima, gere o XML e envie ao eSocial.   
  
  
**Saiba mais**  
Para maiores informações acesse:   
[Mapeamento dos eventos eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409020102679-RH-RM-FOP-eSocial-Mapeamento-dos-eventos-eSocial)  
[Cadastro do evento S-1070 Tabela de Processos Administrativos/Judiciais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360008847432-RH-RM-FOP-eSocial-Cadastro-do-evento-S-1070-Tabela-de-Processos-Administrativos-Judiciais)
