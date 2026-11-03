---
content_hash: 6acda3b2cd4221c222793c78944afef44832cb95fae7caa8fe33316aba49c06d
fetched_at: '2026-06-29T00:05:53.768946+00:00'
page_id: '1070828872'
product: rm
source: tdn-rm
title: Totem de Atendimento
type: documentation
url: https://tdn.totvs.com/display/LRM/Totem+de+Atendimento
version: 2
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Parâmetros/Configurações**
3. **Fluxos de Senhas**
   1. **Padrão**
   2. **Auto Atendimento Eletivo**
   3. **Auto Atendimento Pronto Atendimento**
   4. **Atendimento Simplificado**

conteudoVisão Geral

## **01. VISÃO GERAL**

O totem de atendimento funciona como um ponto de autoatendimento que permite ao paciente identificar-se, selecionar o serviço desejado e gerar sua senha de atendimento, organizando as filas e tornando o processo de recepção mais rápido e eficiente.

Parâmetros

## **02. PARÂMETROS/CONFIGURAÇÕES**

## **Parâmetros Gerais: (Ambiente > Parâmetros > Gestão Hospitalar > Portais > Totem de Senhas)**

**Relatórios**: Relatório de Senha/Pulseira a ser Impresso após a geração da senha.  
**Cor Totem**: Cor do tema que o novo Totem de Atendimento irá seguir.  
**Utiliza Totem de Senha com escolha de especialidade**: Habilita a seleção de especialidade no totem de atendimento.

## **Parâmetros da Unidade de Atendimento: (Cadastros > Uso Geral > Unidade de Atendimento > Painéis)**

**Utiliza Setor:** Habilita a seleção de setores no totem de atendimento.  
**Utiliza senha preferencial no Totem:**Habilita a seleção de senhas **prioritárias** no totem de atendimento.  
**Painel Registro de Atendimento Automático:**Habilita o Fluxo de Registro de Atendimento automático de Eletivos/Pronto Atendimento.

## **Cadastro Totem de Atendimento: (Cadastros > Registro e Controle > Outros Cadastros > Totem)**

**Id. Totem:** Sequencial de controle interno. **Descrição:**Nome descritivo para controle do cadastro.  
**Usa Registro Atendimento Simplificado:**Habilita o fluxo de geração de senha para o Registro de Atendimento Simplificado no Totem de Atendimento.  
**Unidades de Atendimento associadas ao Totem:**Vinculo de quais Unidades de Atendimento serão apresentadas no Totem para geração de senha.  
**Setores associados ao Totem:** Vinculo de quais Setores serão apresentadas no Totem para geração de senha. Serão listados para inserção apenas Setores vinculados as Unidades de Atendimento configuradas.

Para funcionamento do Totem de Atendimento é obrigatório a configuração de pelo menos uma Unidade de Atendimento.IMPORTANTE!¹  
Quando a opção "Utilizar Registro de Atendimento Simplificado" estiver habilitada, ela prevalecerá sobre as configurações de Autoatendimento da Unidade de Atendimento.IMPORTANTE!²

## **Especialidades: (Atendimento> Pronto Atendimento / Ambulatório > Pronto Atendimento > Painel de Classificação de Eletivos (ou Risco) > Plantão)**

**Unidade de Atendimento:**Vinculo de Unidade de Atendimento com Especialidade para controle de exibição da Especialidade no totem.  
**Setor:**Vinculo de Setor com Unidade de Atendimento e Especialidade para controle de exibição da Especialidade no totem. Caso Setor não preenchido, a Especialidade deverá aparecer para todos Setores da Unidade.

Fluxos de Senhas

## **03. FLUXOS DE SENHAS**

O Fluxo de Senhas serve como um direcionador de quais etapas o Totem de Atendimento irá apresentar em tela, baseado nas configurações dos cadastros e parâmetros.

As etapas de Unidade de Atendimento, Setor, Especialidade e Prioridade não serão exibidas quando houver apenas uma opção disponível. Nessa situação, o sistema selecionará automaticamente a opção configurada.IMPORTANTE!  
Caso todas as etapas anteriores à Prioridade possuam apenas uma opção disponível, a etapa Prioridade será exibida para garantir o controle do fluxo de atendimento no totem.IMPORTANTE!²

Os Fluxos a seguir serão representados de maneira completa para apresentação, independente de configuração. (Ex.: Setores e Especialidades opcionais) (Informações meramente ilustrativas)

A opção "Falar com a Recepção" nas etapas de CPF serviram para direcionar o paciente ao fluxo padrão de senhas caso haja alguma dificuldade.

fluxosPadrão

## **03.a. PADRÃO**

Auto Atendimento Eletivo

## **03.b. AUTO ATENDIMENTO ELETIVO**

Auto Atendimento PA

## **03.c. AUTO ATENDIMENTO PRONTO ATENDIMENTO**

**Caso não seja encontrado nenhum atendimento com o CPF do Paciente na base de dados, será solicitado ao Paciente se direcionar a Recepção.IMPORTANTE!**

Atendimento Simplificado

## **03.d. ATENDIMENTO SIMPLIFICADO**

**Caso o CPF do Paciente não seja encontrado na base de dados, será criado o Atendimento para um "Paciente Sem Check-in" conforme regra do Registro de Atendimento Simplificado.IMPORTANTE!**
