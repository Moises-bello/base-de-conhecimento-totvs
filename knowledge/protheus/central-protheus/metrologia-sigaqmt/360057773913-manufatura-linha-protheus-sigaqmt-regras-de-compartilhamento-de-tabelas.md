---
article_id: 360057773913
category: Metrologia (SIGAQMT)
content_hash: 50b814c7417dc7f5b1545398d3c8c22db45216730272fbb9bd333a7c65ce2279
fetched_at: '2026-06-28T22:42:24.896320+00:00'
product: protheus
section_id: 360005876694
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQMT - Regras de compartilhamento de tabelas
type: support-article
updated_at: '2021-08-10T18:51:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057773913-Manufatura-Linha-Protheus-SIGAQMT-Regras-de-compartilhamento-de-tabelas
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:30 min**  
**Dúvida**Quais são as regras de compartilhamento de tabelas no módulo **SIGAQMT - Metrologia**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Metrologia (SIGAQMT) - Todas as versões  
  
**Solução**As regras de compartilhamento das tabelas do **SIGAQMT** são:

1. As tabelas a seguir relacionadas, devem sempre obedecer a mesma situação da tabela **QM6 - Cabeçalho da Calibração**. Por exemplo, quando a tabela **QM6** estiver em modo **exclusivo**, todas as tabelas abaixo deverão também estar em modo **exclusivo**.
2. O uso **compartilhado** não é recomendado.  
     

   |  |  |
   | --- | --- |
   | **Tabela** | **Descrição** |
   | **QMR** | **Tolerância e Redutor de Faixas** |
   | **QMK** | **Amarração Escala por Família** |
   | **QMI** | **Instrumentos Utilizados na Medição** |
   | **QMC** | **Amarração Padrões por Escala** |
   | **QMA** | **Amarração Padrões P/ tipo Soma** |
   | **QM9** | **Escalas** |
   | **QM6** | **Cabeçalho da Calibração** |
   | **QM2** | **Instrumentos** |
   | **QM1** | **Famílias de Instrumento** |
   | **QM3** | **Padrões para Calibrações** |
   | **QMT** | **Padrões Usados na Medição Soma** |
   | **QM7** | **Resultado Medições por Escala** |
   | **QM8** | **Medições Efetuadas** |
   | **QMX** | **Incertezas tipo B na Medição** |
   | **QMJ** | **Não Conformidade por Instrumento** |
   | **QMS** | **Padrões Secundários por Ponto** |

**Importante**  
A não observância destas regras, pode implicar em problemas de funcionamento e apresentação dos dados em todo o ambiente de um modo geral.
