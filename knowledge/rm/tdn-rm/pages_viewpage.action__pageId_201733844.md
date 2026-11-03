---
content_hash: bc499ed62851a49c5c0e646faf42d0238a3a65b32d176add7489de3c9cbfe4d1
fetched_at: '2026-06-29T00:06:06.972952+00:00'
page_id: '201733844'
product: rm
source: tdn-rm
title: ER_PCREQ-6547_SAÚDE_CIH_FLUIG_12.1.9_IMPORTAÇÕES
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=201733844
version: 3
---

### (Obrigatório)

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | CIH | **Módulo** | Importações |
| **Segmento Executor** | Saúde | | |
| **Projeto1** | SAÚDE\_CIH\_FLUIG | **IRM1** | PCREQ-6530 |
| **Requisito1** | PCREQ-6547 | **Subtarefa1** |  |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.9 | **Réplica** |  |
| **País** | (X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### (Obrigatório)

## Objetivo

Permitir que o setor de Controle de Infecção Hospitalar (CIH) tenha informações atualizadas de toda a rotina do paciente dentro da unidade de internação. Desta maneira os responsáveis pelo CIH poderão implantar e desenvolver o sistema de vigilância epidemiológica das infecções hospitalates.

### (Obrigatório)

## Definição da Regra de Negócio

A importação deverá acontecer de forma automática, de acordo com o período de importação que for determinado pelo usuário da instituição nos parâmetros do sistema.

Serão importados os dados de todos os pacientes que estão internados na instituição, bem como os antibióticos que foram prescritos para estes pacientes, Cirurgias realizadas, resultados de Cultura Final, Eventos Adversos, Movimentações de Leito, dados das internações e alta do paciente, procedimento invasivo e também importará o CID.

Os dados importados serão:

* Internação e Alta: Dados do Paciente -IH, Nome, Data da Internação, Observações, Especialidade, Unidade Clínica, Data da Alta, Tipo de Alta (Se for Alta do tipo Óbito, importa o Motivo do Óbito, Convênio, Método de Vigilância Pós Alta, Imunossuprido (Sim, Não), Momento CID (Internação. Alta), CID Primário e CID Secundário.
* Antibiótico: Data de Início de Fim da Terapia , DDD (Dosagem Diária Definida), Dose do Medicamento, Via de Administração, Médico Prescitor e Justificativa da prescrição;
* CID: Código do CID de internação e Descrição do CID;
* Cirurgias: Data da Cirurgia, Tipo da Cirurgia (Trauma, Urgência ou Eletiva), Risco Cirúrgico (ASA) – podendo ser de I a VI, Observações, Anestesta (CRM e Nome do médico anestesista), Tipo de Anestesia (Geral, Bloqueio e Local), Vias de Acesso (Especialidade, Tipo de Ferida, Tempo de Ferida Aberta, IRIC, Procedimentos, Cirurgiões e Infecções.;
* Cultura Final: Data da Cultura, Data do Resultado, Grupo de Materiais, Material, Unidade Clínica, Germe, Antibiograma, Número de Colonias, Gran e Observações;
* Eventos Adversos: Data, Método de detecção, Observações, Tipo de Procedimento, Evento Adverso (Perda de PA, Lesões de Pele e/ou Partes Moles, Outras Lesões, Hemorragia Intra Ventricular, CPAP, Aspiração Pulmonar), Motivo e ou Consequência, Unidade Clínica e Especialidade;
* Movimentação de Leito: Unidade Clínica, Data de Entrada, Data de Saída e Leito;
* Procedimentos Invasivos: Tipo de Procedimento, Início e Data Fim.

### Opcional

## Protótipo de Tela

**Protótipo 01**

### Opcional

## Fluxo do Processo

1. O período de importação é parametrizado pelo usuário;
2. No período configurado o sistema inicia a importação de todos os dados do paciente;
3. Serão apresentados o total de importações realizadas com sucesso e um log, com as informações que possuíram erros;

### (Opcional)

## Grupo de Perguntas

 

*<Informações utilizadas na linha Protheus>.*

 

**Nome: FINSRF2**

|  |  |
| --- | --- |
| **X1\_ORDEM** | 01 |
| **X1\_PERGUNT** | Emissão De |
| **X1\_TIPO** | D |
| **X1\_TAMANHO** | 8 |
| **X1\_GSC** | G |
| **X1\_VAR01** | MV\_PAR01 |
| **X1\_DEF01** | Comum |
| **X1\_CNT01** | '01/01/08' |
| **X1\_HELP** | Data inicial do intervalo de emissões das guias de DARF a serem consideradas na seleção dos dados para o relatório |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
