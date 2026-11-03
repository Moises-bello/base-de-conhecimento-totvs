---
content_hash: 6972bb912b67128a69b1e4ea19aa2281eb646994fb7683f2783fd23799e60cf8
fetched_at: '2026-06-29T00:11:54.922020+00:00'
page_id: '859065989'
product: rm
source: tdn-rm
title: Central de Assinatura
type: documentation
url: https://tdn.totvs.com/display/LRM/Central+de+Assinatura
version: 10
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Ativação de recursos em tempo real**
   1. **Visão Geral**
   2. **Funcionalidade**

Central de assinatura1. Visão Geral

## **01. VISÃO GERAL**

A nova funcionalidade Central de assinaturas foi implementada com o objetivo de otimizar e facilitar o processo de assinatura de documentos pelos profissionais de saúde, possibilitando assinar um conjunto de documentos de diferentes pacientes de uma única vez. A Central de assinaturas poderá ser acessada através da área de  do usuário, clicando no ícone “visualizar” do tipo de documento exibido ao expandir a aba “Assinatura digital pendente”.

2. Exemplo de utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

Para acessar a central de assinaturas, o usuário deverá clicar no ícone de notificações, e se houver alguma documentação pendente de assinatura, ao expandir a aba “Assinatura digital pendente” e clicar no respectivo ícone de visualização, o usuário será redirecionado para a tela principal da central.

Na aba “Assinatura digital pendente” da , todos os documentos com assinatura pendentes serão listados por tipo e com a sinalização do número total de assinaturas pendentes.

Na tela principal da central de assinatura será exibido uma tabela de assinaturas pendentes, composta por:

* Data e hora da finalização do documento
* Tipo de documento
* Nome do paciente
* Situação:
  + Pendente (aguardando assinatura)
  + Processamento (documento enviado para assinatura)
  + Falha (falha na assinatura)
  + Finalizado (documento assinado com sucesso)
* Ações:
  + Acessar: abre o documento em PDF em uma nova guia
  + Gerar impresso: inicia download do documento em PDF

Para assinar um ou mais documentos, marque o checkbox dos respectivos itens e clique no botão "Assinar selecionados". Em seguida será exibido uma modal solicitando o PIN do certificado digital conforme parametrizado. Para finalizar, clique no botão "Assinar" para assinar os documentos.

Em caso de falha na assinatura de algum documento, o mesmo permanecerá listado na tabela com o status “Falha”, sinalizado na coluna “Situação” e a notificação continuará na aba “Assinatura digital pendente” da worklist do usuário.

Enquanto o documento estiver aguardando o processo de assinatura digital, o status será alterado para “Processamento” na coluna “Situação”.

Para documentos assinados com sucesso, as notificações correspondentes serão removidas da worklist e da tabela. Para visualizar o documento novamente na tabela, utilize o filtro “Finalizado”.

  

Para filtrar um período específico, assim como status da assinatura e tipo do documento, o usuário poderá clicar no botão “Filtrar”. Para realizar a busca, preencha os respectivos campos de data, tipo de documento e status e clique no botão “Filtrar”. Para limpar a seleção, clique no botão “Remover filtros” e para cancelar a busca clique no botão “Cancelar”.

3. Ativação de recursos em tempo real

## **03. ATIVAÇÃO DE RECURSOS EM TEMPO REAL**

## **a.****VISÃO GERAL**

A configuração para ativação de recursos em tempo real possibilita um nível maior de interação entre os usuários acessando a aplicação, habilitando o envio de informações do servidor de aplicação para os usuários.

## **b. FUNCIONALIDADE**

1. 1. Para habilitar esse recurso, é necessário adicionar uma chave no arquivo de configuração em que está instalado o servidor de aplicação (**RM.Host**ou **RM.Host.Service**).
   2. Localize o arquivo de configurações referente a instalação do **RM.Host**ou **RM.Host.Service**, e dentro da sessão **configuration /****appSettings**inclua a chave **EnableRealtime**com o valor **"true"**.
   3. Com a chave habilitada, o sistema permitirá o envio de informações no sentido servidor de aplicação -> usuários, possibilitando que uma rotina processada no servidor envie notificações para os usuários acessando o sistema.
