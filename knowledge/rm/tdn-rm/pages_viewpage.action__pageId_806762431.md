---
content_hash: 50503cb67bcc1c71da567104aafeb838cfe8feef9afef15e48e9cae88dc889e8
fetched_at: '2026-06-29T00:11:43.424956+00:00'
page_id: '806762431'
product: rm
source: tdn-rm
title: Relatórios Registro Atendimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=806762431
version: 11
---

1Visão Geral

## **01.** **VISÃO GERAL**

A funcionalidade inicia a partir de Atendimento > Registro de Atendimento

## **02. CONFIGURAÇÃO**

A configuração para utilização de relatórios do registro de atendimento deve ser realizada por unidade de atendimento.

Acesse: Cadastros > Unidade de Atendimento > Selecione a unidade > Relatórios

Para adicionar o relatório com algumas possíveis configurações.

****Relatório:****Selecione o relatório que deseja  
****Ordem:**** Ordem de impressão  
****Local de Impressão:**** Impressora responsável pela impressão do relatório  
****Tipo de assinatura eletrônica:**** Define se o relatório será assinado eletronicamente pelo paciente. (Essa opção inviabiliza o local de impressão, Tipo de Ação)  
****Tipo de ação:**** Define se o relatório será impresso ou se será somente exibido  
****Parâmetros P/ Digitação:**** Define se será necessário exibir a tela de parâmetros para impressão ou não

Assinatura Eletronica

## **01. VISÃO GERAL**

Caso o RM esteja devidamente configurado ao registrar o atendimento, os relatórios poderão ser assinados digitalmente. O processo é automático e o usuário deverá apenas estar autenticado no TAE. A assinatura está restrita apenas a assinatura digital da Totvs através do TAE ( Totvs Assinatura Digital ), para mais informações acessar o link [Integração com TOTVS Assinatura Eletrônica](https://tdn.totvs.com/pages/viewpage.action?pageId=562963400)  
Caso esteja parcialmente configurado ou o usuário não autentique o processo continuará sem bloqueio e o usuário deverá em outro momento solicitar a assinatura.

## **02. CONFIGURAÇÃO PARA ASSINATURA** **ELETRONICA**

Acesse: Cadastros > Unidade de Atendimento > Selecione a unidade > Relatórios  
Selecione o tipo de assinatura (TOTVS SIGN)

## **03. UTILIZAÇÃO**

Durante o registro do atendimento selecione a unidade cujo os relatórios foram configurado (para assinatura eletrônica) 

Após salvar o registro de atendimento será necessário informar o responsável pelo atendimento junto com o e-mail do responsável para que seja enviado os relatórios para assinatura.  
Logo após salvar o responsável pelo atendimento o envio será disparado novamente após salvar novamente o registro de atendimento ou fechar a tela do registro de atendimento.

Os relatórios enviados serão apresentados na aba de "Relatórios Enviados para TAE" com status "Enviado"

O paciente receberá e-mail conforme abaixo.

O paciente fará o acesso para assinatura com um token recebido no e-mail  - não será necessário criar um acesso ao portal TAE (Totvs Assinatura Eletrônica) para realizar assinatura.

Após o paciente assinar os relatórios recebidos via e-mail o status será atualizado automaticamente para "Assinado" com a data da assinatura

**Data validade****relatório**É possível definir data de validade para o relatório enviado, para que o paciente não realize assinatura após o vencimento.  
Configuração é realizada por convenio em:  
Cadastro > Faturamento > Condições contratuais  
  
Selecione o Convenio desejado e navegue até a aba "Eletrônico I"  
Preencha o parâmetro 'Dias validade para assinatura de relatório' (Informar a quantidade de dias que o relatório poderá ficar disponível para assinatura)  
  
Calculo de exemplo:  
**DIA ATUAL**:   
**Dias validade para assinatura de relatório:** 30  
**RESULTADO:** 29/11/2000 + 30(DIAS) = 29/12/2000

**Reenviar relatórios**Para reenviar relatórios para assinatura obrigatoriamente o status não pode ser "Assinado"  
Acesse: Registro Atendimento > Relatórios Enviados para TAE > Processo > Reenviar Relatórios para assinatura eletrônica.  
  
  
**Imprimir relatórios assinados**Acesse: Registro Atendimento > Relatórios Enviados para TAE > Processo > Imprimir relatórios assinados  
Os relatórios serão impressos no caminho de rede configurado em:  
Cadastro > Unidade de Atendimento > Integrações  
O caminho para salvar relatórios deve ser compartilhado na rede conforme o exemplo abaixo.

\\[SERVIDOR]\[PASTA-COMPARTILHADA]

**Cancelar atendimento**Ao cancelar o atendimento cujo a assinatura não foi realizada o status do relatório será atualizado para "Cancelado" o será excluído do portal TAE

**Modelo de relatório assinado**
