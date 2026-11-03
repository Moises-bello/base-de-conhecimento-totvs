---
content_hash: 9fe9c8e3d56e579406c7519a186beb0847fb164fea68e0e9905c5624727c9478
fetched_at: '2026-06-29T00:11:31.451244+00:00'
page_id: '737572135'
product: rm
source: tdn-rm
title: Medicamento (Prescrições avulsas)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=737572135
version: 5
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Funcionalidade**
3. **Exemplo de Utilização**

ItensVisão Geral

## **01.****VISÃO GERAL**

Insere medicamentos na prescrição avulsa selecionada.

Funcionalidade

## **02. FUNCIONALIDADE**

1. A prescrição de medicamentos possui algumas regras para poder ser utilizada:  
     
   * Os campos de **via**, **apresentação**, **quantidade**, **unidade** e **frequência** são de preenchimento obrigatório.
   * Caso seja selecionado um medicamento não cadastrado, será exibido um campo para informar um complemento, de preenchimento obrigatório.
   * Caso seja utilizado a opção de **se necessário**, o campo de **condição**será habilitado e deverá ser preenchido.
   * Caso seja utilizado um medicamento que solicite uma justificativa, dependendo de como o sistema estiver configurado, a justificativa será de preenchimento obrigatório.
   * Caso seja utilizado um medicamento que possua algum padrão de diluição e esse padrão de diluição seja selecionado, alguns campos adicionais serão apresentados, sendo de preenchimento obrigatório a seleção dos **diluentes** e sua **apresentação**, a **ação** que será realizada sobre esse diluente, a **quantidade** do diluente que será utilizado nessa ação, e a quantidade da solução a **administrar**.
2. Em alguns casos, poderão ser exibidos alertas para o medicamento selecionado:  
     
   * Alertas para alergia, caso o paciente possua alergia para qualquer um dos princípios ativos do medicamento.
   * Alertas para caso o medicamento compartilhe de um mesmo princípio ativo de outro medicamento prescrito anteriormente.
   * Alertas para interação medicamentosa, caso possua interação medicamentosa com qualquer medicamento prescrito anteriormente.
   * Alertas para duplicidade de prescrição, caso o medicamento já tenha sido prescrito anteriormente.
3. Não será possível inserir medicamentos na prescrição nos seguintes casos:  
     
   * A prescrição não for de responsabilidade do profissional inserindo os itens
   * A prescrição estiver vencida
   * O medicamento seja de uso proibido pelo convênio do atendimento do paciente.
Exemplo de Utilização

## **03. EXEMPLO DE UTILIZAÇÃO**

1. Prescrição de um medicamento:
2. Utilização de um padrão de diluição e solicitação da justificativa para item restrito:
3. Alertas para alergia do paciente:
