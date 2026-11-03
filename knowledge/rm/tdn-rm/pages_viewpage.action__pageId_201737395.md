---
content_hash: 0aed6c0b75c2714181a11f9a7271997a57d8508688eb9a095c6a5ae5f5d96044
fetched_at: '2026-06-29T00:06:07.742413+00:00'
page_id: '201737395'
product: rm
source: tdn-rm
title: ER_PCREQ-6540_SAÚDE_CIH_FLUIG_12.1.9_RELATÓRIOS_ ANVISA
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=201737395
version: 2
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### (Obrigatório)

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS CIH | **Módulo** | RELATÓRIOS |
| **Segmento Executor** | SAÚDE | | |
| **Projeto1** |  | **IRM1** | PCREQ -6530 |
| **Requisito1** | PCREQ -6540 | **Subtarefa1** |  |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** |  | **Réplica** |  |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### Objetivo

 Gerar relatórios estatísticos para notificação a ANVISA

### Definição da Regra de Negócio

 Os Dados Importados são compilados em relatórios numéricos, agrupados por interesse conforme a legislação vigente da ANVISA e são eles:

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

### Opcional

## Protótipo de Tela

*<Caso necessário inclua protótipos de telas com o objetivo de facilitar o entendimento do requisito, apresentar conceitos e funcionalidades do software>.*

**Protótipo 01**

### Fluxo do Processo

 

1. Clicar em Relatórios ANVISA
2. Seleciona o período desejado
3. Publica
4. Salva em pasta configurada

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
