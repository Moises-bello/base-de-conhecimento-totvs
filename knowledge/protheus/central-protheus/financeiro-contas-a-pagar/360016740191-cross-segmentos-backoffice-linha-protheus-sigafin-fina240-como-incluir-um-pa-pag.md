---
article_id: 360016740191
category: Financeiro - Contas a Pagar
content_hash: c2256ce4e19d3892e4f311c3c42a98a80f22fb80d746ba2ee42af8bfc7f31025
fetched_at: '2026-06-28T22:38:08.459182+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN -  FINA240 - Como incluir
  um PA (Pagamento Antecipado) em um borderô
type: support-article
updated_at: '2024-06-03T20:11:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016740191-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA240-Como-incluir-um-PA-Pagamento-Antecipado-em-um-border%C3%B4
---

**Dúvida**Como incluir um PA (Pagamento Antecipado) em um borderô?  
  
**Ambiente**Cross Segmento - TOTVS BackOffice (Linha Protheus) - Financeiro - FINA473 - Todas as versões  
  
  
**Solução**Acesse o módulo **Financeiro, Atualizações, Contas a Pagar> Contas a Pagar**, pressione a tecla F12 **(parâmetros)**  e será apresentado a pergunta: **Gerar Chq.p/Adiant** e **Mov.Banc.sem Cheque**. Através destas perguntas é definido se o **PA** gera movimento bancário na sua **inclusão** ou **não**.

**Configuração dos Parâmetros F12 da rotina Conta a Pagar (FINA050)**

**Gerar Chq.p/Adiant****= Não**

**Mov.Banc.sem Cheque = Não**

Desta forma, será possível a inclusão do PA em Borderô de Pagamento.

Para adicionar o PA - Pagamento Antecipado ao Bordero, no F12 da rotina, deve conter para a pergunta "Considera Titulo ?" = "Ambos" ou "Adiantamentos"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18224897184151)  
**Observação**:  
Se o banco utilizado na inclusão do PA estiver informado nos parâmetro **MV\_CARTEIR** ou **MV\_CXFIN** irá ocorre o **Help**: Recno **Problema**: Não existem registro no arquivo em pauta. O motivo é que os bancos cadastrados nos parâmetros **MV\_CARTEIR** ou **MV\_CXFIN** ficará impossibilitado de gerar de cheques no **Contas a Pagar**, pois o sistema entenderá que o banco é interno (caixa).

Se o parâmetro **MV\_CTLIPAG estiver =T**, e não efetuou a **liberação de baixa** desse **PA** na rotina **FINA580** também será apresentando o help abaixo.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102288874)

**Saiba mais:**  
[Diferença e tratamento: MV\_CARTEIR e MV\_CXFIN](https://tdn.totvs.com/pages/viewpage.action?pageId=172300136) 

Caso,

A configuração dos parâmetros esteja conforme abaixo:

**Gerar Chq.p/Adiant****= Não**

**Mov.Banc.sem Cheque = Sim**

ou 

**Gerar Chq.p/Adiant****= Sim**

**Mov.Banc.sem Cheque = Não**

Ao incluir o **PA** com esta configuração,será gerado movimento bancário na inclusão e consequentemente este **PA** não será considerado na geração do **Borderô de Pagamentos (FINA240).** Pois no padrão, se o **PA** gerou movimento bancário na inclusão não é considerado no **borderô**.

É possível incluir um PA que gerou movimento bancário na sua inclusão em um borderô, através do ponto de entrada: **FA240PA**.

Segue o link, correspondente documentação do ponto de entrada: **FA240PA**:

[FA240PA - Seleciona PA com movimento bancário](http://tdn.totvs.com/pages/releaseview.action?pageId=150635423)
