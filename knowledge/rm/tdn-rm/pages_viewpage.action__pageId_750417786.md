---
content_hash: 32af8d77bd174ca4629de55b84622cbb08b06834add7d67442918bcb671d9951
fetched_at: '2026-06-29T00:11:32.923739+00:00'
page_id: '750417786'
product: rm
source: tdn-rm
title: Faturamento Convênios - Layout Próprio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=750417786
version: 4
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Pré-Requisitos**
3. **Cadastros / Parametrizações**
4. **Geração do Faturamento**

## **01. VISÃO GERAL**

Essa rotina tem como objetivo permitir o faturamento de convênios que não seguem um padrão estabelecido pelo mercado (TISS, SUS ou Instituto de Previdências) e possui um layout próprio (Relatório ou Arquivo Texto) para realizar o faturamento. Essa rotina realiza todo o processo interno referente às consistências da informação e fluxo de cobrança do convênio como os demais modelos de faturamento (Ex.: Criar uma fatura, número de remessa, atualização dos atendimentos/contas/parciais do convênio com a remessa gerada, enviar o prontuário para o controle de documentos, encerramento da remessa, espelho da fatura, repasse, geração de movimento de fatura, etc).

Por essa rotina ser mais flexível com o meio de envio de informações para a operadora, é permitido o uso de relatórios customizados (Menu de relatórios da visão de dados da tela de faturamento para convênios) e elaboração / configuração de um layout próprio de um arquivo TXT pela própria equipe de TI da instituição de saúde.

## **02. PRÉ-REQUISITOS**

Funcionalidade disponível a partir da release 12.1.2306 e somente na MDI .Net.

Arquivo eletrônico disponível apenas nos formatos suportados pela rotina de [Gerador de Saídas](https://tdn.totvs.com/pages/viewpage.action?pageId=161351633).

## **03.** **CADASTROS / PARAMETRIZAÇÕES**

Para utilizar esse modelo de faturamento siga os passos abaixo para parametrizar o convênio.

* TOTVS Saúde => Hospitais e Clínicas => Cadastros => Uso Geral => Convênio => No campo "Padrão de Informação" informe o valor "1 - FATMED.BR".

* TOTVS Saúde => Hospitais e Clínicas => Cadastros => Faturamento => Condições Contratuais => Aba Eletrônico I => No campo "Layout Faturamento Próprio (Fatmed.BR)" informe o layout disponível na ferramenta de gerador de saídas que atende melhor ao formato de exportação de arquivo TXT definido pelo convênio
  + Caso o convênio não utilize arquivo TXT para envio do faturamento esse campo deverá ficar em branco
  + O layout a ser configurado neste campo deverá ser desenvolvido pelo usuário da instituição de acordo com a documentação enviada pelo convênio

**04. GERAÇÃO DO FATURAMENTO**

Para realizar o faturamento utilizando esse padrão de informação basta executar os seguintes passos:

* Registrar os atendimentos para os pacientes que utilizam esse convênio
* Realizar o processo de encerramento das parciais a serem faturadas
* Criar uma nova remessa de faturamento (TOTVS Saúde => Hospitais e Clínicas => Faturamento => Particular e Convênios => Faturamento para Convênios)
* Executar o processo de Faturamento de Convênios e realizar todos os filtros necessários para que as contas desejadas sejam incluídas nessa remessa. Observe que o padrão Fatmed.Br será indicado no alto da tela à direita.
* Ao finalizar o processo, a remessa será faturada com todos os processos descritos na área de visão geral executados.
* Caso o convênio utilize um layout de geração de arquivo TXT o mesmo será gerado no diretório padrão informado no Layout selecionado em seu cadastro:
