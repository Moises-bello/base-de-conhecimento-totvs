---
article_id: 26787860358039
category: Financeiro
content_hash: ee28268161782cae7c24d7076ce3e99f3a0b72709fae43ff36496254c03a3ac0
fetched_at: '2026-06-28T22:38:01.212663+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice linha Protheus - SIGAFIN - APP Minha Prestação
  de Contas envia e-mail de aprovação para o e-mail cadastrado na APDA020
type: support-article
updated_at: '2025-01-24T13:38:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26787860358039-Cross-Segmentos-Backoffice-linha-Protheus-SIGAFIN-APP-Minha-Presta%C3%A7%C3%A3o-de-Contas-envia-e-mail-de-aprova%C3%A7%C3%A3o-para-o-e-mail-cadastrado-na-APDA020
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26787860311959) Tempo aproximado para leitura: **02:00 min** **Dúvida**Qual é o e-mail cadastrado que receberá a notificação para aprovação das Viagens?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Financeiro - Todas as versões  
  
**Solução**O e-mail será enviado para o cadastro de e-mail que está preenchido na rotina **APDA020.**

Na rotina de Viagens (**FINA665**)

- Ao conferir a solicitação, transitando o status da mesma p/ "Aguardando Aprovação" - Notifica o aprovador.

Na rotina de Adiantamentos (**FINA667**)

- Ao gerar o adiantamento em status "Solicitado" - Notifica o aprovador;

- Ao reprovar um adiantamento na etapa de aprovação do gestor (incluindo a aprovação por lote) - Notifica o viajante;

- Ao liberar o pagamento do adiantamento gerando o título financeiro através da ação "Liberar Pagto" - Notifica o viajante.

Na rotina de Prestação de Contas (**FINA677**)

- Ao conferir uma prestação de contas pelo departamento de viagens através da ação "Conferir" - Notifica o aprovador;

- Ao reprovar uma prestação de contas na etapa de aprovação do gestor - Notifica o viajante;

- Ao liberar o reembolso para o viajante ou a devolução p/ a empresa, gerando o título financeiro através da ação "Liberar Financ." - Notifica o viajante.

Para que todo esse fluxo tenha a dinâmica do envio de e-mails, é necessário alguns pré-requisitos, tais como:

Configurar servidor de e-mail do Protheus;

**Ter o campo "E-mail" preenchido no cadastro do Participante com um endereço válido;**

Ter o parâmetro MV\_RESAVIS (presente no Assistente de Configuração, seção "Gerais") configurado como "1";

Permitir que o serviço de e-mail (Google, Office365, etc) seja acessado pelo Protheus. Essa ação só se faz necessária caso você receba um alerta Google/Microsoft sobre o bloqueio à tentativa de conexão de um dispositivo desconhecido.

Exemplo de um e-mail disparado para o gestor aprovador no momento em que o departamento de viagens conferiu a prestação de contas (ação "Conferir->Aprovar"):

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26787860326167)

**Saiba Mais**

[Viagens](https://tdn.totvs.com/display/public/PROT/Viagens+-+Financeiro+-+P12)
