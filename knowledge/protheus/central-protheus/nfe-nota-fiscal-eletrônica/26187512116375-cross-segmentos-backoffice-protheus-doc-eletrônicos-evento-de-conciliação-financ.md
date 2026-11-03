---
article_id: 26187512116375
category: NFe - Nota Fiscal Eletrônica
content_hash: 594455fc09005774462a95abe95011e7596271e61d19d7f03478fc0340162173
fetched_at: '2026-06-28T22:40:00.109937+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Evento de Conciliação
  Financeira - ECONF
type: support-article
updated_at: '2024-10-08T18:17:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26187512116375-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Evento-de-Concilia%C3%A7%C3%A3o-Financeira-ECONF
---

**Dúvida**

Como enviar o evento de conciliação financeira - ECONF?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos

Cross Segmentos - TSS

**Solução**

É necessário que tenha sido aplicadas as atualizações da [Nota Técnica 2024.002](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23926593195287-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Nota-T%C3%A9cnica-2024-002).

A funcionalidade está disponivel no **Módulo 05 - Faturamento > NFE SEFAZ**.

1 - Acessar a rotina NFe-Sefaz

Selecionar a Opção 5-ECONF clicar em OK

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26200443645591)

2 - Informar os parâmetros para listagem dos documentos.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26187594139415)

3 - Selecionar no browser o documento, para o envio do evento.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26200443646487)

4- Ajuste os parametros em Outras ações > Parametros:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26200407025943)

Após informar os parâmetros confirme clicando em + Salvar como grupo administrador e confirma no botão "OK".

5 - Ao selecionar o documento e acionar a funcionalidade (Transmissão) será redirecionado a tela principal dos eventos do ECONF.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26200443648407)

Selecione no menu Transações o evento desejado

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26187512096279)

**110750 - Transmitir Evento**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26187512098199)

| Campo | Tag XML |
| --- | --- |
| Tipo de Pagamento | indPag |
| Meio de Pagamento | tPag, xPag |
| Data Pagamento | dPag |
| CNPJ. Pgto. Processado | CNPJPag |
| UF. Estab. Processado | UFPag |
| CNPJ Instituição Financeira | CNPJIF |
| Bandeira do Cartão de Debito/Crédito | tBand |
| CNPJ. Estab. Beneficiério | CNPJReceb |
| UF. Estab. Beneficiário | UFReceb |
| Nro.Autorização de Transação | cAut |
| Valor do Pagamento | cPag |

**110751 - Cancelar Evento**

Selecione no browser a Sequência do evento que se deseja cancelar, e clique em Transmitir

É possível selecionar um evento de cada vez ou clicando no cabeçalho do browser selecionar todos os eventos disponiveis uma unica vez.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26187495910551)

**110000 - Monitor de Eventos**

Nesta funcionalidade estão disponivel as opções de Refresh (atualiza o browser com o status de rotorno da Sefaz) e a opção Menssagem (visualiza os dados da transmissão do evendo selecionado).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26187495912599)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26187495913367)

Boletim técnico: <https://tdn.totvs.com/pages/releaseview.action?pageId=865409531>
