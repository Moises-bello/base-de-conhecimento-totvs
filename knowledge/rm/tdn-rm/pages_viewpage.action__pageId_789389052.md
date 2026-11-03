---
content_hash: 3a2120c8dabb5da5987d416589480fb72d8302c9aee242039f470d3cc66c4857
fetched_at: '2026-06-29T00:11:39.250018+00:00'
page_id: '789389052'
product: rm
source: tdn-rm
title: Alterações - S-2299 - S-1.2
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=789389052
version: 12
---

false

**A partir das Versões:**

* 12.1.2302.235
* 12.1.2306.182
* 12.1.2310.116 e superiores

**CONTEÚDO**

IMPORTANTE!

---

## **01. VISÃO GERAL**

Este documento visa apresentar as mudanças no evento S-2299 para atender o Leiaute do eSocial versão S-1.2.

## **02. ALTERAÇÕES REALIZADAS**

### **02.01.** **TABELA 19 - MOTIVOS DE DESLIGAMENTO**

**Alteração:**Inclusão dos motivos de desligamento abaixo,  conformeTabela 19 - Motivos de Desligamento do leiaute eSocial:

* + 47 - Rescisão do contrato de trabalho por encerramento da empresa, de seus estabelecimentos ou supressão de parte de suas atividades;
  + 48 - Falecimento do empregador individual sem continuação da atividade

Acesse o menu Configurações | Parametrizador | eSocial | De/Para | De/Para de Desligamento para incluir o relacionamento dos novos motivos de desligamento, que serão apresentados na opção "Cod. Tipo eSocial".

Ao gerar o XML do funcionário com o "Tipo de Demissão" especificado no cadastro do "De/Para" (campo "Cod. Tipo Folha de Pagamento"), o sistema irá preencher a tag <mtvDeslig> com o motivo de desligamento eSocial, que também está relacionado no "De/Para" (campo "Cod. Tipo eSocial").

**Exemplo:**

No cadastro do "De/Para de Desligamento", selecionar o tipo de folha "9 - Outros casos" e associá-lo ao tipo eSocial "47 - Rescisão do contrato de trabalho por encerramento da empresa, de seus estabelecimentos ou supressão de parte de suas atividades":

Ao cadastrar a rescisão para o funcionário preencha o tipo de demissão "9 - Outros casos" ;

O XML será gerado preenchendo a tag <***mtvDeslig**>* com o código 47:

### **02.02.** **TAG <indPDV> - INDICATIVO DE DESLIGAMENTO COM ADESÃO A PROGRAMA DE DEMISSÃO VOLUNTÁRIA (PDV)**

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Grupo {infoDeslig} incluído campo (indPDV) | - | Indicativo se o desligamento ocorreu por meio de adesão a Programa de Demissão Voluntária (PDV). **Valores válidos:** S - Sim **Validação**: Não informar se mtvDeslig = [10, 11, 12, 13, 28, 29, 30, 34, 36, 37, 40, 43, 44]. |

**Alteração:** A inclusão da tag **<indPDV>** no evento S-2299 e a criação do parâmetro **"Adesão ao Programa de Demissão Voluntária"** no cadastro de rescisão do funcionário.

No cadastro de rescisão (normal, coletiva e global), foi criado o parâmetro "**Tem adesão ao Programa de Demissão Voluntária**" na aba "**Rescisão**". Esse parâmetro será **habilitado apenas** quando o **motivo de desligamento** do eSocial for **diferente de [10, 11, 12, 13, 28, 29, 30, 34, 36, 37, 40, 43, 44]**, conforme **Tabela 19 - Motivos de Desligamento**. O motivo de desligamento, por sua vez, está relacionado ao tipo de demissão informado (verificar [Mapeamento](https://tdn.totvs.com/display/LRM/Evento+S-2299) do evento) ou ao de/para cadastrado no parametrizador do eSocial.

Caso o parâmetro seja selecionado, será gerado no XML do eSocial a tag ***<indPDV>*** como "**S**", conforme exemplo abaixo:

Caso o parâmetro esteja **desmarcado** ou **desabilitado**, o XML **não irá gerar a *tag***em questão.

 **Como a *tag* só existe no Leiaute S-1.2, ela não será gerada em leiautes anteriores, ainda que esteja marcada no cadastro de rescisão do funcionário.**

## **03. MAPEAMENTO DO EVENTO**

Acesse o mapeamento do evento clicando no link abaixo:

* + [Evento S-2299](https://tdn.totvs.com/display/LRM/Evento+S-2299)
