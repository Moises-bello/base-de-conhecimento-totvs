---
article_id: 360050769153
category: RH - Benefícios
content_hash: 26701c211ee849bbd776f806ba6957f352844e047230628c08cf252ed941a1e4
fetched_at: '2026-06-28T22:44:03.844785+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Como parametrizar a coparticipação/reembolso
type: support-article
updated_at: '2025-09-05T17:27:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050769153-RH-Linha-Protheus-GPE-Como-parametrizar-a-coparticipa%C3%A7%C3%A3o-reembolso
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15238888030871) Tempo aproximado para leitura: **00:02:00 min**  
**Dúvida**Como parametrizar a coparticipação/reembolso?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**

**Coparticipação:**A coparticipação são valores adicionais pagos pelos beneficiários às empresas operadoras de assistência médica/ odontológica, quando participam do custeio de utilizações do plano de acordo com política da empresa e contrato vigente com operadora, cujos descontos ocorrem em folha de pagamento mensalmente e a empresa faz o repasse à operadora.  
Algumas operadoras fornecem o arquivo para importação no sistema dos lançamentos destes eventos de coparticipação, porém, não será contemplado no produto pelo fato de cada operadora utilizar um leiaute diferente de arquivo.

**Reembolso:**Os reembolsos são os valores pagos aos funcionários, quando qualquer um dos beneficiários utilizar prestador que não seja credenciado na operadora de planos vigente da empresa. Normalmente os beneficiários (titular/dependentes/agregados) ao utilizarem estes prestadores costumeiramente realizam o pagamento diretamente aos prestadores e posteriormente solicitam o reembolso à operadora através da empresa em que trabalham, no qual por vezes são reembolsados diretamente pela operadora. Porém, esta rotina possibilita que os pagamentos também sejam efetuados na folha de pagamento e o controle é efetuado de acordo com esse cadastro.

O lançamento deve ser feito para o usuário do plano de saúde que utilizou os serviços, ou seja, para o **Titular, Dependente ou Agregado.   
  
Para realizar o lançamento** acesse: **Atualizações > Benefícios > Plano de Saúde > Coparticipação/Reembolso**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15238839523095)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15238850527255)

Neste lançamento serão informados os seguintes campos:

**Data Ocorrenc:** Data do lançamento ou da consulta. Campo apenas informativo;

**Origem:** Informe se a coparticipação ou reembolso se refere a 1-Titular; 2-Dependente ou 3-Agregado;

**Tipo:** Informe se o lançamento se refere a 1-Assistência Médica ou 2-Assistência Odontológica;

**Cód. Fornec.:** Informe a operadora/Fornecedor do plano de saúde. Deve ser o mesmo informado no cadastro de planos ativos do titular, dependente ou agregado;

**Sequência:** Informe a sequência do dependente ou do agregado. Campo será ativado apenas quando a origem se referir a um dependente ou agregado;

**Nome:** Nome do Dependente ou Agregado. Este campo é preenchido automaticamente após informar a sequência. Campo apenas visual;

**Tipo do Lançam.:** Informe se o lançamento se refere a 1-Coparticipação ou 2-Reembolso;

**Verba Calcul.:** Informe a verba de desconto/provento que será enviada para folha de pagamento;

**Vlr Funcion.:** Valor que será descontando ou pago ao funcionário;

**Vlr Empresa:** Valor correspondente à empresa;

**Compet. Pagto:** Informe o ano e o mês de competência para desconto/pagamento em folha de pagamento.

Ao gravar o lançamento, o sistema verifica se o fornecedor lançado está de acordo com o informado no plano ativo, não permitindo gravar, caso este seja diferente.

Na integração com a folha de pagamento, o valor lançado no campo **Vlr Empresa**será somado à Verba vinculado aos Identificadores de **Cálculos Parte Empresa**. Caso a empresa não realize nenhum tipo de pagamento, seja de reembolso ou de coparticipação, este campo deve ser gravado sempre com o valor zero.

**Saiba Mais**[RH - Linha Protheus - GPE - Documentações relacionadas a rotina de coparticipação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11301756760855-RH-Linha-Protheus-GPE-Documenta%C3%A7%C3%B5es-relacionadas-a-rotina-de-coparticipa%C3%A7%C3%A3o)  
[RH - Linha Protheus - GPE - Sistema não está separando os valores de assistência médica e reembolso no quadro 07](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022352032-RH-Linha-Protheus-GPE-Sistema-n%C3%A3o-est%C3%A1-separando-os-valores-de-assist%C3%AAncia-m%C3%A9dica-e-reembolso-no-quadro-07?source=search)  
[RH - Linha Protheus - GPE - Como preencher os campos de informações complementares, para reembolso e coparticipação de assistência médica/odontológica para DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043029374-RH-Linha-Protheus-GPE-Como-preencher-os-campos-de-informa%C3%A7%C3%B5es-complementares-para-reembolso-e-coparticipa%C3%A7%C3%A3o-de-assist%C3%AAncia-m%C3%A9dica-odontol%C3%B3gica-para-DIRF?source=search)
