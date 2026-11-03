---
content_hash: cacae8ca045352690875ecdbb1e891161b0b6bb344fe6ee6d9e464ea62782885
fetched_at: '2026-06-29T00:06:07.149775+00:00'
page_id: '201735528'
product: rm
source: tdn-rm
title: ER_PCREQ-6559_SAÚDE_CIH_FLUIG_12.1.9_PRONTUÁRIO DO PACIENTE
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=201735528
version: 3
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### (Obrigatório)

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS CIH | **Módulo** | PACIENTE |
| **Segmento Executor** | SAÚDE | | |
| **Projeto1** | SAÚDE\_CIH\_FLUIG | **IRM1** | PCREQ-6527 |
| **Requisito1** | PCREQ-6559 | **Subtarefa1** |  |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.8 | **Réplica** |  |
| **País** | ( X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### Objetivo

 Tem como objetivo mostrar as informações do Paciente

### Definição da Regra de Negócio

Todas as Informações do paciente, compiladas em cada Internação são organizadas em abas definidas, que possibilitam a visualização, edição e inserção de Informações e serão elas:

 

 

Internação

 

Mostrará os dados das Internações e Alta realizadas pelos pacientes, são eles: Dados do Paciente -IH, Nome, Data da Internação, Observações, Especialidade, Unidade Clínica, Data da Alta, Tipo de Alta (Se for Alta do tipo Óbito, importa o Motivo do Óbito, Convênio, Método de Vigilância Pós Alta, Imunossuprido (Sim, Não), Momento CID (Internação. Alta), CID Primário e CID Secundário.

 

 

Movimentações

 

Mostrará os dados das movimentações internas realizados pelo pacientes, são eles: Unidade Clínica, Data de Entrada, Data de Saída e Leito.

 

 

Procedimentos Invasivos

 

Serão mostradas e com possibilidade de edição as Informações de nome dos procedimentos Invasivos, data de Início e fim destes, local de internação do paciente quando em uso de Cateteres vesonos.

 

 

Antibiótico

 

Os dados dos antibióticos administrados nos pacientes, sendo eles: Grupo, Princípio Ativo, DDD, data de Dispensação, dosagem, via de administração, data de iniico e fim da Prescrição, Médico prescritos e justificativa da prescrição, estas informações poderão ser associadas a Infecções ou Cultura. As informações devem ser validadas pelo SCIH e após esta checadas

 

 

Cultura

 

Os Dados das culturas finais ou Parcial do paciente, serão: Data da Cultura, Data do Resultado, Grupo de Materiais, Material, Unidade Clínica, Germe, Antibiograma, Número de Colonias, Gran e Observações. As informações poderão ser associadas a Antibióticos ou Infecções da mesma Internação ou até 365 dias após a ultima alta. As informações devem ser validadas pelo SCIH e checadas.

 

 

Cirurgia

 

Os dados das cirurgias dos pacientes, serão: Data da Cirurgia, Tipo da Cirurgia (Trauma, Urgência ou Eletiva), Risco Cirúrgico (ASA) – podendo ser de I a VI, Observações, Anestesta (CRM e Nome do médico anestesista), Tipo de Anestesia (Geral, Bloqueio e Local), Vias de Acesso (Especialidade, Tipo de Ferida, Tempo de Ferida Aberta, IRIC, Procedimentos, Cirurgiões e Infecções. As informações devem ser validadas pelo SCIH e checadas.

 

 

Infecção

 

As infecções deverão ser informadas manualmente pelo SCIH e contem os seguintes campos:Data: que pode ser até 365 dias após a alta, Método de Detecção (telefone, vigilância, email), Observações, Associação com Cultura ou Antibiótico, Sítio Secundário, associação comprocedimentos invasivos ou Cirurgia realizada durante a internação ou até 365 dias após a alta.

 

 

Eventos Adversos

 

Os dados dos Eventos Adversos sofridos pelo paciente possui as seguintes informações compiladas no prontuário: Data, Método de detecção, Observações, Tipo de Procedimento, Evento Adverso (Perda de PA, Lesões de Pele e/ou Partes Moles, Outras Lesões, Hemorragia Intra Ventricular, CPAP, Aspiração Pulmonar), Motivo e ou Consequência, Unidade Clínica, Especialidade e Observações. Os eventos Adversos podem ser associados a Procedimentos Invasivos ou não.

 

### Opcional

## Protótipo de Tela

*<Caso necessário inclua protótipos de telas com o objetivo de facilitar o entendimento do requisito, apresentar conceitos e funcionalidades do software>.*

**Protótipo 01**

### Fluxo do Processo

1. Acesso ao Menu Pacientes
2. Informar o nome do Paciente desejado ou clicar sobre ele na lista de Pacientes
3. Clicar na opção Desejada
4. Visualizar,editar ou Incluir as Informações.

 

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
