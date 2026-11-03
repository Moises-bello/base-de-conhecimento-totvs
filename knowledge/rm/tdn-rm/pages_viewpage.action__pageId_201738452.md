---
content_hash: df53e865df59650d9f6f1a1893a872f1e9012bb6915bde09d1f271a8da8e6c0e
fetched_at: '2026-06-29T00:06:07.825208+00:00'
page_id: '201738452'
product: rm
source: tdn-rm
title: ER_PCREQ-6542_SAÚDE_CIH_FLUIG_12.1.9_RELATÓRIOS ESTATÍSTICOS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=201738452
version: 2
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS CIH | **Módulo** | RELATÓRIOS |
| **Segmento Executor** | SAÚDE | | |
| **Projeto1** |  | **IRM1** | PCREQ-6530 |
| **Requisito1** | PCREQ-6542 | **Subtarefa1** |  |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** |  | **Réplica** |  |
| **País** | (X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### Objetivo

 Gerar Relatório estatístico

### Definição da Regra de Negócio

 Os relatórios são elaborados a partir dos dados Importados do ERP ou manualmente inseridos nos registros dos Pacientes.

É possível criar layouts de relatórios e salva-los.

Deve existir a opção de compilamento de dados de uma coligada em específico ou de todas as coligadas.

Todos os relatórios podem ser convertidos em gráficos estatísticos com possibilidade de escolha pelo cliente do formato do gráfico e gráfico epidemiológico com duas linhas de metas. 

Os relatórios podem ser  Salvos em arquivos externos e ou impressos.

Os Dados Importados são compilados em relatórios numéricos, agrupados por interesse conforme a legislação vigente da ANVISA e CDC e são eles:

**Infecção de Sítio Cirúrgico (ISC)****Numerador**: Número total de infecções relacionadas ao procedimento cirúrgico específico, ocorridas no serviço de saúde, no mês de vigilância.  
**Denominador**: Número total de procedimentos cirúrgicos específicos, realizados no serviço de saúde, no mês de vigilância.  
**Pneumonia Associada à Ventilação Mecânica (PAV)**  
**Numerador:** Número total de Pneumonias Associadas à Ventilação Mecânica (PAV) em pacientes internados, por Unidade de Terapia Intensiva, no mês de vigilância.  
**Denominador** (ventilação mecânica - dia): Soma do número total de pacientes que usaram ventilação mecânica, por Unidade de Terapia Intensiva, no mês de vigilância.  
**Infecção do Trato Urinário (ITU)  
Numerador:** Número total de Infecções do Trato Urinário (ITU) associadas ao uso de cateter vesical de demora, por Unidade de Terapia Intensiva, no mês de vigilância.  
**Denominador** (cateter vesical de demora – dia): Soma do número total de pacientes que usaram cateter vesical de demora, por Unidade de Terapia Intensiva, no mês de vigilância.  
**Infecção Primária de Corrente Sanguínea Clínica (IPCSC)**  
**Numerador:** Número total de Infecções Primárias de Corrente Sanguínea Clínica, por Unidade de Terapia Intensiva, no mês de vigilância.   
**Denominador** (cateter venoso central - dia): Soma do número total de pacientes que usaram cateter venoso central, por Unidade de Terapia Intensiva, no mês de vigilância.   
**Infecção Primária de Corrente Sanguínea confirmada laboratorialmente (IPCSL)**  
**Numerador:** Número total de Infecções Primárias de Corrente Sanguínea confirmadas laboratorialmente, por Unidade de Terapia Intensiva, no mês de vigilância.   
**Denominador** (cateter venoso central - dia): Soma do número total de pacientes que usaram cateter venoso central, por Unidade de Terapia Intensiva, no mês de vigilância.    
**Taxa de utilização de Cateter Venoso Central (CVC)  
Numerador** (cateter venoso central - dia): Soma do número total de pacientes que usaram cateter venoso central, por Unidade de Terapia Intensiva, no mês de vigilância.   
**Denominador** (paciente-dia): Soma do número total de pacientes internados, por Unidade de Terapia Intensiva, no mês de vigilância.   
**Taxa de Letalidade  
Numerador:** número de óbitos de pacientes por IPCS no mês de vigilância.  
**Denominador:** número de pacientes com IPCS no mês de vigilância.

 

**Microorganismos Isolados em Culturais:**

 

Após o compilamento das informações o sistema salva estes dados em local público.

Os filtros comuns a todas os relatórios são:

Leitos reais

Leitos virtuais

Todos os Leitos

Leitos Ativos

Leitos Inativos

Paciente

Peso

Unidade Clínica

Altas

Internações

Internados

TAXA GLOBAL

Sítios de Infecção

Infecções

Taxa de Infecção

Critérios Diagnósticos

 DISPOSITIVOS INVASIVOS

Tipo de cateter

Procedimentos

Infecções

Novos Procedimentos

Taxa de Infecção

Densidade de Utilização

PROCEDIMENTOS CIRÚRGICOS

especialidade

iric

cirurgião

procedimento

anestesia

anestesista

tipo de cirurgia

potencial de contaminação

função

data

validado

video

critério diagnóstico

via de acesso

infecções

cirurgias

taxa de infecção

próteses

ANTIBIÓTICO

indicação

Tipo de Infecção

Ferida

Grupo de ATB

Data

Médico

Especialidade

Unidade Clínica

Sítio Cirúrgico

Validado

Utilização

Antibiótico

Paciente

Prescrições

Via

Consumo Total - G-u

Consumo Médio

DDD

Tempo médio de consumo em dias

Tempo total de consumo em dias

Taxa = DDD/pac dia\*1000

Adequação

Momento da análise

Acerto Terapia

Empírico

CULTURA

Material

Grupo de Materiais

Especialidade

Grecimento Bacteriano

Relevânica Clínica

Tipo de Infecção

Número de Culturas

Germe

Multiresistência

ATB

Grupo de ATB

Testados

EVENTOS ADVERSOS

Evento adverso

Procedimento Invasivo

ANÁLISE DE ÓBITO

Procedimento Invasivo

Procedimento Cirúrgico

Convênio

Idade

Sexo

Infecção

Evento Adverso

Óbito

Taxa de Mortalidade

### Opcional

## Protótipo de Tela

*Caso necessário inclua protótipos de telas com o objetivo de facilitar o entendimento do requisito, apresentar conceitos e funcionalidades do software>.*

**Protótipo 01**

### Fluxo do Processo

Acesso aos relatórios

Seleção de período desejado

Seleção de Coligada

Seleção do relatório desejado

Seleção de gráfico desejado

Salvar arquivo

Imprimir arquivo

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
