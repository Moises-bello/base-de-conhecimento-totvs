---
article_id: 8580384175383
category: Integrações - Conceito e WebService
content_hash: b867a40b268d555adcaae45b687254f509b547c6bf59555ef16b07319b1640ae
fetched_at: '2026-06-28T22:46:44.732508+00:00'
product: rm
section_id: 1500000834721
source: central-rm
title: RH - RM - FOP - LGPD - Serviços Via WebService
type: support-article
updated_at: '2025-02-03T19:11:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8580384175383-RH-RM-FOP-LGPD-Servi%C3%A7os-Via-WebService
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:09:37 min****Dúvida**Quais regras de restrição a dados consumidos através de dataservers por meio dos serviços SOAP ?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**

Com base na [Lei Nº 13.709/18](http://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/L13709.htm) , implementamos algumas regras de restrição a dados consumidos através de dataservers por meio dos serviços SOAP e Rest. 

Estas restrições se aplicam aos registros retornados **restrição de linha** ao consultar dados através destes serviços e implicam que um usuário só poderá ter acesso as informações de cadastro que possua permissão e/ou que lhe pertencem, ou seja, informações que fazem referência a sua pessoa, ou caso o usuário seja chefe ou supervisor o mesmo terá acesso aos dados de seus subordinados, [clique](https://tdn.totvs.com/display/LRM/Chefes+e+Supervisores) para mais detalhes sobre o cadastro de chefes e supervisores.  
Para os serviços via SOAP as restrições de aplicam aos métodos **ReadView** , **ReadRecord** , **SaveRecord** e **Delete**.

**Exemplo de utilização**Foi criada a nova permissão de acesso **Desconsiderar Filtro de Produto em WebService***,* com objetivo de que o sistema passe a fazer filtro de segurança nos DataSevers ao realizar acesso via WebService. O novo parâmetro esta localizado em **Serviços Globais | Segurança | Perfis.**No caso de o usuário estar vinculado a um perfil que não contenha permissão, os DataSevers retornarão os registros filtrados conforme regra de negócio do produto, caso contrário o sistema continua com o comportamento padrão retornando todos os registros conforme filtro informado pelo usuário.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8580111698071/mceclip0.png)  
 **Filtro por chapa**Caso o usuário não tenha permissão no parâmetro **Desconsiderar Filtro de Produto em WebService**, os DataSevers retornarão apenas os dados do funcionário que o usuário esteja associado. Em caso de ser chefe ou supervisor, retornará também os dados de seus subordinados.

**A LISTA DE DATASERVERS COM RESTRIÇÕES:**

| FUNCIONALIDADE | DATASERVER | STATUS |
| --- | --- | --- |
| CADASTRO DE FUNCIONÁRIO | FopFuncData | ATIVO |
| FICHA FINANCEIRA | FopFichaFinancData | ATIVO |
| HISTÓRICO SALARIAL | FopHstSalData | INATIVO |
| SALÁRIO COMPOSTO | FopSalCompostoData | ATIVO |
| ENVELOPE DE PAGAMENTO | FopEnvelopeData | INATIVO |
| ENVELOPE DE PAGAMENTO | FopEnvelopeFeriasData | INATIVO |
| RECIBO DE FÉRIAS | FopFuFeriasReciboData | ATIVO |
| ENCARGO | FopEncargoData | ATIVO |
| GOZO DE FÉRIAS | FopFuFeriasPerData | ATIVO |
| GOZO DE FÉRIAS | FopFuFeriasPerDataBR | ATIVO |
| DEPENDENTES DO FUNCIONÁRIO | FopDependData | ATIVO |
| AFASTAMENTO DO FUNCIONÁRIO | FopHstAftData | ATIVO |
| VÍNCULOS EMPREGATÍCIOS COM OUTRAS EMPRESAS (TERCEIROS) | FopMultVinculosExternoData | ATIVO |
| DADOS DO RESIDENTE OU DOMICILIADO NO EXTERIOR | FopDadosResidExteriorData | ATIVO |
| OBSERVAÇÕES CONTRATUAIS | FopObservacoesData | ATIVO |
| CÓDIGOS FIXOS | FopCodFixData | ATIVO |
| EVENTOS PROGRAMADOS | FopEventoProgramadoData | ATIVO |
| RATEIO FIXO | FopRateioFixoData | ATIVO |
| CONVOCAÇÃO PARA TRABALHO INTERMITENTE | FopConvocacaoData | ATIVO |
| HISTÓRICO DE VALE TRANSPORTE | FopHstValeTrData | ATIVO |
| DADOS PERÍODO AQUISITIVO (FÉRIAS FUTURAS) | FopFuFeriasData | ATIVO |
| DADOS DA RESCISÃO | FopRescisaoData | ATIVO |
| DADOS DO AVISO PREVIO | FopAvisoPrevioData | ATIVO |

OBS: Para que o usuário tenha acesso aos demais DataServers que não receberam a implementação do filtro de segurança do produto, mantendo o comportamento que o sistema já possuía, deverá dar permissão a esse novo parâmetro.

**Filtro por Coligada**Caso o usuário não tenha permissão no parâmetro **Desconsiderar Filtro de Produto em WebService**, os DataSevers retornarão apenas os dados das coligadas que o usuário tenha permissão de acesso ao cadastro correspondente no produto.

**A LISTA DE DATASERVERS COM RESTRIÇÕES:**

| FUNCIONALIDADE | DATASERVER | STATUS |
| --- | --- | --- |
| CADASTRO DE CHEFE E SUPERVISOR | FopChefeSupervisorData | ATIVO |
| CADASTRO DE SEÇÃO | FopSecaoDataBR | ATIVO |
| CADASTRO DE EVENTO | FopEventoData | ATIVO |
| CADASTRO DE CENTRO DE CUSTO | FopCCustoData | ATIVO |
| CADASTRO DE FUNÇÃO | FopFuncaoData | ATIVO |
| CADASTRO DE SINDICATO | FopSindicData | ATIVO |

  
**Importante**  
Para que o usuário tenha acesso aos demais DataServers que não receberam a implementação do filtro de segurança do produto, mantendo o comportamento que o sistema já possuía, deverá dar permissão a esse novo parâmetro.

**Saiba mais**

[LGPD - Serviços Via WebService](https://tdn.totvs.com/pages/releaseview.action?pageId=545647849#1-2)
