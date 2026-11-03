---
article_id: 25937861021079
category: PCMSO / Exames
content_hash: eafc2bba7e6fd13977ed78984e36bf34aed4127e281a4b74a833ba496b743325
fetched_at: '2026-06-28T22:47:42.086638+00:00'
product: rm
section_id: 1500000861462
source: central-rm
title: 'RH - RM - SMT - Tipo de Atendimento: Cadastro não aparece a opção ''Consulta
  para Exame Toxicológico'''
type: support-article
updated_at: '2025-09-19T19:29:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25937861021079-RH-RM-SMT-Tipo-de-Atendimento-Cadastro-n%C3%A3o-aparece-a-op%C3%A7%C3%A3o-Consulta-para-Exame-Toxicol%C3%B3gico
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25937860995735) Tempo aproximado para leitura: **00:00:51 min****Dúvida**Ao realizar as configurações necessárias para geração dos Exames Toxicológicos, no cadastro do '**Tipo de Atendimento**' não consta a opção '**Consulta para Exame Toxicológico**' para marcar em '**Procedimento(s)**'.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25937852332439)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - **TOTVS Segurança e Saúde Ocupacional** - A partir das versões **12.1.2310.233, 12.1.2402.181, 12.1.2406.114** e superiores.  
  
**Solução**Neste caso, isso ocorre quando estão com o parâmetro para 'Controlar o registro de Exames Toxicológicos no TOTVS Folha de Pagamento' marcado em **Opções** | **Parametrizador** | **Exames** | **Exames Toxicológicos**.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25937861001495)  
  
Quando este parâmetro está marcado, o controle de registro do exame toxicológico será realizado através do TOTVS Folha de Pagamentos no cadastro de **Funcionários** | **Anexos** | **Folha de Pagamento** | **Exame Toxicológico**.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25937852336407)  
  
Com o parâmetro desmarcado, o controle de registro do exame toxicológico será realizado através do Prontuário Médico, podendo assim, cadastrar o '**Tipo de Atendimento**', informando o '**Procedimento**' como '**Consulta para exame toxicológico**'.   
  
**Saiba mais**  
Para maiores informações, acesse:  
- [RH - RM - SMT - Gerar o evento S-2221 - Exame Toxicológico do Motorista Profissional Empregado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/25679917455255)
