---
article_id: 31715306160663
category: TAF - eSocial - Eventos Não Periódicos
content_hash: ff3b071567563199f5f2834afde0e700d53a0fe1a358329fc21426426f5cef97
fetched_at: '2026-06-28T22:45:17.940132+00:00'
product: protheus
section_id: 1500001548002
source: central-protheus
title: RH - Linha Protheus - eSocial - Erro 272 - A inscrição informada deve corresponder
  a um estabelecimento/CNO/CAEPF do empregador, devidamente cadastrado e com período
  de vigência válido por todo o contrato informado
type: support-article
updated_at: '2026-06-26T11:21:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31715306160663-RH-Linha-Protheus-eSocial-Erro-272-A-inscri%C3%A7%C3%A3o-informada-deve-corresponder-a-um-estabelecimento-CNO-CAEPF-do-empregador-devidamente-cadastrado-e-com-per%C3%ADodo-de-vig%C3%AAncia-v%C3%A1lido-por-todo-o-contrato-informado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31715301148439) Tempo aproximado para leitura: 00**:01:36 min****Ocorrência**No envio eventos cadastrais de funcionários, estagiários, sócios ou até autônomos **(S-2200, S-2300, S-2206, S-2306**, etc)  é apresentado o erro Erro **272**: **A inscrição informada deve corresponder a um estabelecimento/CNO/CAEPF do empregador, devidamente cadastrado e com período de vigência válido por todo o contrato informado**  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Não Periódicos - Todas as versões  
  
**Causa**

O erro geralmente é apresentado quando não é localizado no governo um S-1005 com número de inscrição vigente no período correspondente ao evento a ser enviado ou enviado com data posterior ao evento que esta tentando enviar.

**Solução**

Para solucionar o erro 272, primeiramente, deve-se avaliar o **nrInsc** do evento a ser transmitido conforme relacionamento deste evento com o S-1005;

* S-1005: Campo **nrInsc** do grupo **ideEstab**
* S-2200 e S-2205: Campo **nrInsc** do grupo **localTrabGeral**

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31715306144919)**

Verifique a data de admissão e compare com a data de início de validade do S-1005 enviado - [RH - Linha Protheus - TAF - eSocial - Eventos de Tabela - S-1005 - Como acessar a rotina de Estabelecimentos, Obras ou Unidades de Órgãos Públicos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037760133-RH-Linha-Protheus-TAF-eSocial-Eventos-de-Tabela-S-1005-Como-acessar-a-rotina-de-Estabelecimentos-Obras-ou-Unidades-de-%C3%93rg%C3%A3os-P%C3%BAblicos)

A data de admissão deve ser igual ou Posterior a data de inicio do S-1005. Caso não seja, envie o S-1005 na data de obrigatoriedade do eSocial.

Confira também a data de vigência e transmissão do S-1000 - [RH - Linha Protheus - TAF - eSocial - Configurações - Como acessar o complemento cadastral](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034688453-RH-Linha-Protheus-TAF-eSocial-Configura%C3%A7%C3%B5es-Como-acessar-o-complemento-cadastral)

**Saiba Mais**Para saber mais consulte os *links* abaixo:  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
