---
article_id: 18250478513175
category: eSocial - Tabelas/Não Periódicos
content_hash: db64e93d2df886aa531816724ddca8db3ff88341b6f9387171d11d834d8d81cb
fetched_at: '2026-06-28T22:47:10.353350+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro ao gerar S-2200/S-2206: campo ''cnpjEntQual''
  obrigatório'
type: support-article
updated_at: '2024-12-30T15:44:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18250478513175-RH-RM-FOP-eSocial-Erro-ao-gerar-S-2200-S-2206-campo-cnpjEntQual-obrigat%C3%B3rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18250511823255)  Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao gerar XML do evento S-2200 ou S-2206 é apresentada a mensagem **O campo 'cnpjEntQual' do registro 'aprend' é obrigatório e não está preenchido**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18250067103383)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - A partir dos Patches 12.1.2302.235, 12.1.2306.182, 12.1.2310.116   
  
**Causa**Esse incidente ocorre quando no cadastro do funcionário **aprendiz** (categoria eSocial 103), menu **Registro**, aba **Dados do Aprendiz**, foi informada modalidade de contratação **Direta**, mas não foi informado o **CNPJ da Entidade Qualificadora**.

                                                 

**Solução**Conforme leiaute do eSocial, a tag **cnpjEntQual** é obrigatória quando **indAprend** (modalidade de contratação) é igual a 1 (Direta). 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18250163529623)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18250155753751)

Sendo assim, para correção, ao informar a modalidade de contratação **Direta**, é necessário preencher no campo **CNPJ Entidade Qualificadora/ Empregador Cotista** o CNPJ da entidade qualificadora em questão.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18250194701463)

**Saiba mais**  
Para mais informações sobre a contratação de aprendiz, acesse:

* [Contratação de Aprendiz - Leiaute S-1.2](https://tdn.totvs.com/pages/viewpage.action?pageId=795092070)
