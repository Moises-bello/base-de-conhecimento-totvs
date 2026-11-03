---
article_id: 360025729312
category: Gestão de Transportes (TMS)
content_hash: fa280d54ac151eb13e7ccad01964ed150df784fab3812d27d7ee7aabe01ed7d9
fetched_at: '2026-06-28T22:45:29.371414+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Integração TMS x Pamcard
type: support-article
updated_at: '2026-05-21T13:31:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025729312-Log%C3%ADstica-Linha-Protheus-TMS-Integra%C3%A7%C3%A3o-TMS-x-Pamcard
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30627988951319)*** Tempo aproximado para leitura: **00:03:30 min**  
  
**Dúvida**  
Quais as principais informações para integração **Pamcard** com o **SIGATMS** **- Gestão de Transportes**?  
  
**Ambiente**

TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**  
Para efetivar a integração da **Pamcard** com o módulo de **Gestão de Transportes** **SIGATMS** é necessário possuir os seguintes pré-requisitos:

1. Entrar em contato com o seu **EAR - Executivo de Atendimento e Relacionamento** para verificar os custos com relação a licença de uso desta integração;
2. Entrar em contato com o fornecedor **PAMCARY** para verificar os custos de utilização e solicitar o **Certificado digital** que será utilizado na integração;
3. Possuir as parametrizações do **Contrato Carreteiro** já efetivadas no **TMS**.

Abaixo estão relacionados os fontes envolvidos no processo da integração:

* **TMSPAMCARD - Biblioteca de funções da integração;**
* **PAMCARDNEW - Leitura do arquivo de Certificado Digital;**
* **TMSA240 - Complemento de viagem;**
* **TMSA250 - Contrato carreteiro;**
* **TMSA251 - Liberação contrato carreteiro;**
* **TMSA310 - Fechamento de viagem;**
* **TMSAE60 - Cadastro de gerenciadores de frota - Operadoras;**
* **TMSXFUNA** **- Biblioteca de funções;**
* **OMSA040 - Cadastro de motorista;**
* **OMSA100 - Cadastro de rotas;**
* **FINA080 - Baixa de títulos a pagar.**

A seguir os principais parâmetros:

* **MV\_TMSPRPD** - Apresenta informações da praça de pedágio, no cálculo do pedágio;
* **MV\_TMSUTSL** - Utiliza saldo para pagamento do pedágio;
* **MV\_FIMCONT** - Indica quantos dias além da data atual finaliza o contrato no **Pamcard**;
* **MV\_PAMIRRF** - Código do débito para **IRRF - Imposto de Renda de Pessoa Física** no Sistema **Pamcard**;
* **MV\_PAMINSS** - Código do débito para **INSS - Instituto Nacional do Seguro Social** no Sistema **Pamcard**;
* **MV\_PAMSEST** - Código débito para **SEST - Serviço Social do Transporte/SENAT - Serviço Nacional de Aprendizagem do Transporte** no Sistema **Pamcard**;
* **MV\_PAMDEB** - Código para outros débitos no Sistema **Pamcard**;
* **MV\_PAMISS** - Código do débito para **ISS - Imposto sobre serviço** no Sistema **Pamcard**;
* **MV\_PAMPIS** - Código do débito para **PIS - Programa de Integração Social** no Sistema **Pamcard**;
* **MV\_PAMCOFI** - Código do débito para **COFINS - Contribuição para o Financiamento da Seguridade Social** no Sistema **Pamcard**;
* **MV\_TMSCFUS** - Empresa configurada para utilizar saldo do cartão;
* **MV\_PAMCSLL** - Código do débito para **CSLL - Contribuição Social sobre o Lucro Líquido** no Sistema **Pamcard**;
* **MV\_PAMNATC** - Código padrão informado para a natureza das cargas na integração **Pamcard**;
* **MV\_PAMROTA** - Define se utiliza as rotas cadastradas na **Pamcard** para cálculo do pedágio e inclusão de contrato;
* **MV\_TMSOPDG** - Utiliza operadora de frota e vale-pedágio;

Temos vídeos com orientações dos processos de integração:

* **Pamcard Certificado ICP Brasil - Instituto Nacional de Tecnologia da Informação**:

   
   
   
   
 

* Formas de pagamento para mais de um cartão:

* Troca cartão cancelado:

**Saiba mais**  
Segue abaixo *links* dos boletins técnicos referentes as liberações em questão:

* [Integração Pamcard (Integrações - SIGATMS)](https://tdn.totvs.com/pages/releaseview.action?pageId=447093065)
* [Processo Para Integração Pamcard (Integrações - SIGATMS)](https://tdn.totvs.com/pages/releaseview.action?pageId=447093945)
* [Integração TMS x Pamcard - Viagem Modelo 3 (TMSAF60 - SIGATMS)](https://tdn.totvs.com/pages/viewpage.action?pageId=572728228)
* [DT Pamcard - Alteração no Modelo de Comunicação - ICP Brasil](http://tdn.totvs.com/pages/viewpage.action?pageId=349187659)
* [DT Troca do Certificado na Integração Entre SIGATMS x Pamcard](https://tdn.totvs.com/pages/releaseview.action?pageId=385848487)
* [DT Pamcard - Mais de um Cartão na Viagem](http://tdn.totvs.com/pages/viewpage.action?pageId=359470260)
* [DT Pamcard - Cancelamento de Cartão](http://tdn.totvs.com/pages/viewpage.action?pageId=390407676)
* [DT Pamcard - CIOT Por Período](http://tdn.totvs.com/pages/viewpage.action?pageId=307835680)
* [DT Alterações Pamcard - Consulta frete mínimo](https://tdn.totvs.com/pages/releaseview.action?pageId=517135033)
* [Logística - Linha Protheus - TMS - Pamcard - Fim do pagamento de pedágio por cartão.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/27487894471575-Log%C3%ADstica-Linha-Protheus-TMS-Pamcard-Fim-do-pagamento-de-ped%C3%A1gio-por-cart%C3%A3o)
* [Pagamento de Pedágio via TAG - Exemplo de utilização](https://tdn.totvs.com.br/pages/releaseview.action?pageId=612018573)
