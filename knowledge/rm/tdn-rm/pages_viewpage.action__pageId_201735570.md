---
content_hash: 2e8c52e4cec253970e3d30f17faaeb3b6fc103b46d07c961f4f8514f12222cbb
fetched_at: '2026-06-29T00:06:07.163886+00:00'
page_id: '201735570'
product: rm
source: tdn-rm
title: TSRIMI ER Libera Medição Acima 100% por Contrato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=201735570
version: 76
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## 

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | Totvs Obras e Projetos | **Módulo** | Contratos |
| **Segmento Executor** | Construção e Projetos | | |
| **Chamado** | TSRIMI | | |
| **Release de Entrega Planejada** | 12.1.8 | **Réplica** | Não |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

## 

## Objetivo

Possibilitar que para cada contrato das finalidades Contrato de Prestação de Serviços, Contrato de Parcelas Fixas, Contrato de Insumo e Contrato Extra-Histograma, seja parametrizada a permissão de medição/consumo superior a 100%. 

## 

## Definição da Regra de Negócio

O escopo dessa melhoria é permitir que seja definido individualmente para cada contrato das finalidades Contrato de Prestação de Serviços, Contrato de Parcelas Fixas, Contrato de Insumo e Contrato Extra-Histograma se o mesmo poderá ter medição/consumo superior a 100%.

Para isso foi criado o processo *"Alterar Parâmetro de Medição do Contrato"* através do qual poderá ser definido para os contratos selecionados se haverá ou não a 'Permissão para medição/consumo superior a 100%' podendo optar por: Sempre Permitir, Nunca Permitir, Solicitar Senha ou Obedecer ao Projeto. Este processo poderá ser executado ao mesmo tempo para vários contratos (*"Controle > Contrato > Contratos > Processos > Alterar Parâmetro de Medição do Contrato"*) ou individualmente pelo mesmo caminho ou estando na tela de edição do respectivo contrato.

Os dois parâmetros para liberação de medição/consumo superior a 100% (do contrato e dos parâmetros do Projeto) existirão simultaneamente, sendo que, sempre irá prevalecer o que estiver definido em cada contrato, ou seja, ao ser efetuada uma medição ou consumo que supere 100% do contratado,  o sistema deverá ou não permitir essa medição/consumo atendendo ao que está definido no próprio contrato, e somente irá checar o parâmetro do projeto caso o contrato esteja parametrizado como 'Obedecer ao Projeto'. 

Caso esteja utilizando o controle de Status de Contrato, este novo processo poderá ser executado apenas para os contratos no status “Em Negociação”.

Para manter a segurança no processo de cadastro e medição dos contratos, o acesso ao processo *"Alterar Parâmetro de Medição do Contrato"* será controlado através do perfil do usuário. Para isso será criado em "S*erviços Globais > Segurança > Perfis > Projetos > Construção e Projetos > Acesso a Menus"* , na opção [ 05 ] Controle - [ 05.01 ] Básico -  [ 05.01.02 ] Contrato - [ 05.01.02.01 ] Contratos, o novo  item  de  Perfil '[ 05.01.02.01.68 ] Parâmetro de Medir Contrato Acima de 100%'. Assim, somente terão acesso ao processo *"Alterar Parâmetro de Medição do Contrato"* , os usuários em cujo perfil esse novo item de permissão esteja liberado. 

Quando da criação de um novo contrato a pagar, o campo 'Parâmetro Medição' será automaticamente preenchido com a opção 'Obedecer ao Projeto', já na criação dos contratos a receber, o campo será automaticamente preenchido com 'Sempre Permitir'. Fica a cargo do usuário executar o processo para alterar o conteúdo do campo, caso vá optar por uma parametrização diferente da default. O mesmo procedimento se dará com todos os contratos já existentes atualmente na base de dados, ou seja, a partir da atualização da versão 12.1.8, para todos os contratos a pagar será automaticamente definido que obedecerão aos parâmetros do projeto e para todos os contratos a receber será automaticamente definido que sempre permitirão medição/consumo superior a 100%, bastando executar o processo caso deseje alterar essa parametrização.

Aconselhamos que a liberação e a utilização deste processo sejam efetuadas com critério visto que o mesmo possibilita medir/consumir além do que foi planejado na obra. 

Nos contratos das finalidades Marco Contratual e Fornecimento de Material o novo parâmetro não será apresentado e o processo não poderá ser executado.

## 

## Rotinas Envolvidas:

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Criação / Edição do Cadastro de Perfis | Alteração | Serviços Globais > Segurança > Perfis | Criado item de perfil |
| Criação / Edição de Contratos | Alteração | Controle > Contrato > Contratos | Criado o campo 'Parâmetro Medição' |
| Alterar Parâmetro de Medição dos Contratos | Criação | Controle > Contrato > Contratos > Processos > Alterar Parâmetro de Medição dos Contratos | Criado o processo |
| Medição de Contratos | Alteração | Controle > Contrato > Contratos > Processos > Medição de Item de Contrato | Incluída a consistência do campo 'Parâmetro Medição' |
| Consumo de Objetos de Contratos | Alteração | Controle > Contrato > Contratos > Processos >  Consumir Objetos de Contrato | Incluída a consistência do campo 'Parâmetro Medição' |

## Tabelas Utilizadas:

* MCNT - Contratos

## 

## Protótipos de Tela

**Protótipo 01 - Tela de Perfil**

**Protótipo 02 - Criação de Contrato a Receber**

********Protótipo 03 - Criação de Contrato a Pagar********

**Protótipo 04 - Contratos - Processos**

**Protótipo 05 - Alterar Parâmetro de Medição do Contrato**

**Protótipo 06 - Tela de Conclusão da Execução do Processo**

**Protótipo 07 - Contrato a Pagar com Parâmetro Alterado**

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
