---
article_id: 36181199260183
category: Escrita Fiscal - Configurador de Tributos
content_hash: 62552cca0940a38941155da6f2a63a457189a3665d046712b5ba310946897c14
fetched_at: '2026-06-28T22:39:17.517491+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - FISA170 - Compartilhamento
  de Tabelas de Perfis, Regras de Cálculo e Regra de Escrituração
type: support-article
updated_at: '2025-11-12T14:32:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36181199260183-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Compartilhamento-de-Tabelas-de-Perfis-Regras-de-C%C3%A1lculo-e-Regra-de-Escritura%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36181199235095) Tempo aproximado para leitura: **00:10 min**  
  
**Dúvida**  
Como realizar o compartilhamento das tabelas de operações fiscais no Configurador de Tributos?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - A partir da versão 12.1.2210  
  
**Solução**  
Este documento tem como objetivo orientar a análise e configuração do **compartilhamento de tabelas relacionadas a Perfis, Regras de Cálculo e Regra de Escrituração** no Configurador de Tributos, garantindo a consistência das informações fiscais e contábeis entre filiais.

Antes de aplicar qualquer configuração de compartilhamento, é imprescindível compreender o **contexto operacional e fiscal da companhia**, considerando a estrutura de filiais, regimes tributários e particularidades regionais.

As tabelas listadas abaixo possuem **relação direta com regras tributárias** e demandam análise criteriosa antes de serem compartilhadas.

### **1. Tabelas Relacionadas**

#### **1.1 Perfis**

As seguintes tabelas contêm informações de perfis fiscais e de cálculo e **devem ser analisadas** antes do compartilhamento:

Perfis:

F20 - Perfis Tributários

F21 - Perfil Tributário Orig./Dest.

F22 - Perfil Trib. de Participante

F23 - Perfil Tributário de Operação

F24 - Perfil Tributário de Produto

F25 - Perfil Produto x Orige

F26 - Perfil Tipo de Operação

CIO - Código de Serviço Municipal do perfil de operações

#### **1.2 Regras de Cálculo**

Contêm parâmetros e expressões para o cálculo de tributos e retenções:

**Regras de Cálculo:**

F27 - Regra de Base de Calculo

F28 - Regra de Alíquota

F29 - Unidade de Referencia Fiscal

F2B - Regra Tributária

CIN - Cadastro de Fórmulas

#### **1.3 Regra de Escrituração**

Controla as regras aplicadas na escrituração contábil e fiscal:

CJ2 - Regra de Escrituração

#### **1.4 Tabela Genérica**

A tabela **SX5 (Tabela Genérica)** também deve ser analisada, pois pode conter códigos auxiliares utilizados nas regras mencionadas.

### **2. Restrições de Compartilhamento**

As seguintes tabelas **não podem ter o modo de compartilhamento alterado**, pois são estruturais e impactam diretamente as regras tributárias e escrituração fiscal:

**Tabelas estruturais de regras tributárias:**

F2D - Tributos Genéricos Calculados

F2F - Títulos de Tributos x NF

F2H - Apuração Tributo Genérico

F2I - Saldos Apuração Trib. Genérico

F2J - Resumo Apuração por Regra

F2K - Resumo Analítico Trib Gen

F2L - Títulos Apuração Trib. Gen.

F2M - Ajustes Apuração Trib Gen

CJ3 - Escrituração por item

### **3. Observações Importantes**

* O **modo de compartilhamento** poderá ser alterado conforme a necessidade de adequação às configurações fiscais e de tributação da companhia.
* Recomenda-se validar as alterações em **ambiente de homologação**, garantindo a integridade das regras antes da aplicação em **produção**.
* A alteração do compartilhamento das tabelas é de responsabilidade exclusiva do Cliente.

### **Referências**

* Documentação oficial TOTVS:

  + [CFGTRIB - Configurador de Tributos](https://tdn.totvs.com/display/public/PROT/CFGTRIB+-+Configurador+de+Tributos)

###
