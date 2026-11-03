---
article_id: 18251158351895
category: eSocial - Tabelas/Não Periódicos
content_hash: 94989b62e8f7df38edf2d7e24f21833211880b8dbfc6f1fb8a308e9cce9f38f6
fetched_at: '2026-06-28T22:47:10.362231+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro ao gerar S-2200/S-2206: campos ''tpInsc'' e
  ''nrInsc'' obrigatórios'
type: support-article
updated_at: '2026-01-09T11:58:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18251158351895-RH-RM-FOP-eSocial-Erro-ao-gerar-S-2200-S-2206-campos-tpInsc-e-nrInsc-obrigat%C3%B3rios
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18251150377751)  Tempo aproximado para leitura: **00:01:00 min**  
  
**Ocorrência**  
Ao gerar XML do evento S-2200 ou S-2206 são apresentadas as mensagens **O campo 'tpInsc' do registro 'aprend' é obrigatório e não está preenchido** e **O campo 'nrInsc' do registro 'aprend' é obrigatório e não está preenchido.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18250982440599)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - A partir dos Patches 12.1.2302.235, 12.1.2306.182 e 12.1.2310.116  
  
**Causa**  
Esse incidente ocorre quando no cadastro do funcionário **aprendiz** (categoria eSocial 103), menu **Registro**, aba **Dados do Aprendiz**, foi informada modalidade de contratação **Indireta**, mas não foi informado o **CNPJ/CPF do empregador cotista**.

                                                 

**Solução**  
Conforme leiaute do eSocial, as tags **tpInsc** e **nrInsc** são obrigatórias quando **indAprend** (modalidade de contratação) é igual a 2 (Indireta).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18251178323607)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18251039652119)

Sendo assim, para correção, ao informar a modalidade de contratação **Indireta**, é necessário preencher no campo **CNPJ Entidade Qualificadora/ Empregador Cotista** o CNPJ ou CPF da empresa cumpridora de cota de contratação de aprendiz.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18251142657559)

**Saiba mais**  
Para mais informações sobre a contratação de aprendiz, acesse:

* [Contratação de Aprendiz - Leiaute S-1.2](https://tdn.totvs.com/pages/viewpage.action?pageId=795092070)
