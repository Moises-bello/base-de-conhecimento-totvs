---
article_id: 32376031535511
category: Financeiro - Viagens
content_hash: 5f62824aed25afcac7d9fd5eaf50351402b404779ff26af9858bf86876452c79
fetched_at: '2026-06-28T22:38:21.392549+00:00'
product: protheus
section_id: 1500001539201
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA665 - Como enviar
  e-mail no processo de viagens
type: support-article
updated_at: '2025-05-26T18:58:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32376031535511-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA665-Como-enviar-e-mail-no-processo-de-viagens
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32376051711127) Tempo aproximado para leitura: **00****:05:00 min** **Dúvida**Como enviar e-mail no processo de viagens?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
  
**Solução**Hoje a funcionalidade está preparada para o disparo de e-mails a partir da rotina Viagens ( **FINA665** ), no momento da geração da solicitação de viagens ( **FINA666** ), somente após a conferencia de Viagem.  
  
Alguns eventos do processo de Viagens realizam o envio de e-mail padrão para notificar o participante envolvido na ação que acabou de ser executada.

Veja quais são esses eventos:  
Na rotina de Viagens (**FINA665**)  
  
Ao conferir a solicitação, transitando o status da mesma p/ "**Aguardando Aprovação**" - Notifica o aprovador.  
  
Na rotina de Adiantamentos (**FINA667**)  
  
1. Ao gerar o adiantamento em status "**Solicitado**" - Notifica o aprovador;  
2. Ao reprovar um adiantamento na etapa de aprovação do gestor **(incluindo a aprovação por lote) -** Notifica o viajante;  
3. Ao liberar o pagamento do adiantamento gerando o título financeiro através da ação "**Liberar Pagto**" - Notifica o viajante.  
  
Na rotina de Prestação de Contas **(FINA677)**  
  
1. Ao conferir uma prestação de contas pelo departamento de viagens através da ação **"Conferir"** - Notifica o aprovador;  
2. Ao reprovar uma prestação de contas na etapa de aprovação do gestor - Notifica o viajante;  
3. Ao liberar o reembolso para o viajante ou a devolução p/ a empresa, gerando o título financeiro através da ação **"Liberar Financ."** - Notifica o viajante.  
  
Para que todo esse fluxo tenha a dinâmica do envio de e-mails, é necessário alguns pré-requisitos, tais como:  
  
• **[Configurar servidor de e-mail do Protheus](https://tdn.totvs.com/pages/releaseview.action?pageId=271166884)**  
• Ter o campo "**E-mail**" preenchido no **cadastro do Participante** com um endereço válido;  
• Ter o parâmetro **MV\_RESAVIS** **(presente no Assistente de Configuração, seção "Gerais" rotina FINA691)** configurado como "**1**";  
• Permitir que o serviço de e-mail (**Google, Office365, etc**) seja acessado pelo **Protheus**. Essa ação só se faz necessária caso você receba um alerta **Google/Microsoft** sobre o bloqueio à tentativa de conexão de um dispositivo desconhecido.

Saiba mais:

[Viagens - Financeiro - P12](https://tdn.totvs.com/display/public/PROT/Viagens+-+Financeiro+-+P12)

[FINA677 - Pontos de entrada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005083321-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA677-Pontos-de-entrada)
