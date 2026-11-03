---
content_hash: e2b33faaf3d17dd960af7d31258bcc59b80522d5a3308e4b8159945067a60624
fetched_at: '2026-06-29T00:11:39.783338+00:00'
page_id: '789973149'
product: rm
source: tdn-rm
title: Mudança de Leito
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=789973149
version: 9
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de Utilização**
3. **Permissões e Parâmetros**
   1. **Habilitar/Desabilitar Desocupa Leito Anterior**
   2. **Trazer Data/Hora Preenchido**

SumárioVisão Geral

## **01. VISÃO GERAL**

A funcionalidade de **Mudança de Leito** permite que você e sua equipe registrem a mudança de um paciente de um leito para outro de forma rápida e segura. Ao utilizar esta tela, você garante que a localização do paciente esteja sempre atualizada no sistema do hospital, facilitando a organização diária das equipes e garantindo a continuidade e a qualidade do cuidado ao paciente.

Acesse pelo caminho: menu **Atendimento> Outros > Mudança de Leito**.

Exemplo de Utilização.

## **02. EXEMPLO DE UTILIZAÇÃO**

Nesta tela selecione os três pontos para localizar o paciente internado.

Informe o nome do paciente e/ou clique em **Internados nesta data** apósclique em **OK**.

**Selecione** e **confirme** para qual leito o paciente será transferido.

Informe o **Responsável pela diferença de diária**, caso necessário e se o sistema deverá desbloquear ou não o leito anterior.

Atenção: O checkBox **Desocupa leito anterior**, quando não estiver marcado, a mudança de leito ocorre sem liberar o leito anterior, o mesmo permanece com status ocupado com as informações do paciente.

**Caso o hospital trabalhe com processo onde sempre libera o leito anterior, seria importante desabilitar esse recurso para evitar erros.**

A partir da versão 12.1.2606 foi incluído o parâmetro "**Executar o processo de Mudança de unidade de atendimento do paciente ao realizar a transferência de leito**" que se estiver ativo a unidade de atendimento do registro de atendimento será igual ao do Leito novo

Por fim clique em **Avançar** e o processo será realizado.

Configurações e Parametros

## **03.** **PERMISSÕES E PARAMETROS**

1. 1. **Habilitar/Desabilitar Desocupa Leito Anterior**
   2. **Trazer Data/Hora Preenchido**
   3. **Executar o processo de Mudança de unidade de atendimento do paciente**
   4. **Verificar pendências de processamento de Estoque**
   5. **Integração com o Prontuário Eletrônico**

Configurações e ParâmetrosHabilitar/Desabilitar Desocupa Leito Anterior

## A. **DESOCUPAR LEITO ANTERIOR**

**Para habilitar ou desabilitar**, acessar **Serviços Globais > Segurança > Perfis**, selecione o perfil e em seguida acesso o item conforme print abaixo e desabilite o mesmo.

**Caso o hospital trabalhe com processo onde sempre libera o leito anterior, seria importante desabilitar esse recurso para evitar erros.**

Trazer Data/Hora Preenchido

## B. **TRAZER DATA/HORA PREENCHIDO**

Um novo parâmetro foi adicionado ao sistema para agilizar as transferências. Acessando o menu ***Ambientes > Gestão Hospitalar > Registro e Controle > Registro e Controle 5***, você encontrará a opção **'Trazer data/hora preenchido'**. Quando ativada, o sistema preenche automaticamente a data e a hora atuais no momento da transferência, mantendo a flexibilidade para que o usuário altere essas informações manualmente, se necessário.

Executar o processo de Mudança de unidade de atendimento do paciente

## C. **MUDANÇA DE UNIDADE DE ATENDIMENTO DO PACIENTE AO REALIZAR A TRANSFERÊNCIA**

Parâmetro disponível a partir da versão : 12.1.2606

O parâmetro para mudar a unidade de atendimento do registro de atendimento em conjunto com a transferência de leito se encontra no caminho:

**Ambientes> Gestão Hospitalar> Registro e controle> Gestão de Leitos > Executar o processo de Mudança de unidade de atendimento do paciente ao realizar a transferência de leito**

Verificar Pendências de processamento de estoque

## D. **VERIFICAR PENDÊNCIAS DE PROCESSAMENTO DE ESTOQUE**

O parâmetro para Verificar pendências de processamento de Estoque em conjunto com a transferência de leito se encontra no caminho:

***Ambientes > Gestão Hospitalar > Registro e Controle > Registro e Controle 5* > Verificar pendências de processamento de Estoque na mudança de leito**

Integração com o Prontuário Eletrônico

## E. **INTEGRAÇÃO COM O PRONTUÁRIO ELETRÔNICO**

O parâmetro para realizar a definição da URL Do Prontuário eletrônico se encontra no caminho: 

***Ambientes > Gestão Hospitalar > Prontuário Eletrônico > URLs e Tokens***
