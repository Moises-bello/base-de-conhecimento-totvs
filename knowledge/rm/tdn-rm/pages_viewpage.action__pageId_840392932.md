---
content_hash: 0c238b93b5c46923148454b624e45e1831650864ffcc5a99a6af52d99a6a8db9
fetched_at: '2026-06-29T00:11:50.371757+00:00'
page_id: '840392932'
product: rm
source: tdn-rm
title: Previdências Estaduais - Informações para faturamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=840392932
version: 11
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Relatórios**
3. **Tabelas utilizadas**

itensVisão Geral

## **01. VISÃO GERAL**

O Gestão Hospitalar possui cálculos de faturamento específicos para as Previdências Estaduais de São Paulo e Minas Gerais, convênios:

#### **IAMSPE - Instituto de Assistência Médica ao Servidor Público Estadual de São Paulo :**

#### **IPSEMG - Instituto de Previdência dos Servidores do Estado de Minas Gerais :**

Relatórios

## **02. RELATÓRIOS**

Relatórios disponibilizados no Book de Relatórios do Gerador RM Reports (\*.TOTVSREPORT), comuns aos convênios IAMSPE e IPSEMG:

### **Relação de relatórios disponíveis na Elaboração da Conta do Paciente:**

|  |  |
| --- | --- |
| **CÓDIGO** | **RELATORIO RM REPORT** |
| SAUREL0131 | Conta Individual - Internação - Procedimento |
| SAUREL0132 | Conta Individual Consulta e/ou Procedimento |
| SAUREL0129 | Laudo Médico p/ Consulta e/ou procedimento em  PS |
| SAUREL0133 | Laudo Médico de Autorização para Internação |
| SAUREL0143 | Laudo p/ Emissão da Guia Suplementar de internação |

### **Relação de relatórios disponíveis no menu Fatura Convênio:**

|  |  |
| --- | --- |
| **CÓDIGO** | **RELATORIO RM REPORT** |
| SAUREL0139 | Fatura Pacotes - Externo e Interno |
| SAUREL0145 | Fatura de Clínicas de Exames Compl. de Diag. |
| SAUREL0141 | Fatura de Clínicas de Exames Compl. de Diag-UNICOR |
| SAUREL137 | Fatura Pacote Ambulatorial Procedimentos |
| SAUREL136 | Fatura Pacote Ambulatorial Profissionais |
| SAUREL0140 | Consultas Externas |
| SAUREL0142 | Capa de Fatura Profissionais - Consultas Externas |

### **Descrição dos campos comuns no layout dos relatórios :**

| CAMPO NO RELATÓRIO | DESCRIÇÃO |
| --- | --- |
| Matrícula SISSO | número que identifica a pessoa física ou jurídica cadastrada no IPSEMG. Pode se referir ao beneficiário ou ao prestador de serviços. Por exemplo: Matrícula SISSO Prestador, Matrícula SISSO Paciente, |
| Matrícula SISSO Paciente | no Gestão Hospitalar, esta informação corresponde ao campo "Cod. Usuário Convênio" no Registro de Atendimento do Paciente (tabela SZATENDIMENTO.CODUSUARIO). |
| Matrícula SISSO Prestador | no Gestão Hospitalar, esta informação corresponde ao campo "Credencial" que fica no menu Cadastro de Prestador | Anexos | Histórico de Credenciamento - do convênio IPSEMG (tabela SZCREDENCIAMENTODETALHE.CREDENCIALPRESTADOR) |
| Pacote Principal |  |
| Pacote Ambulatorial |  |
| Pacote Guias Suplementares |  |
| Serviços Profissionais |  |
| Consulta em Pronto Socorro |  |
| Recursos Complementares |  |

Tabelas Utilizadas

## **05. TABELAS UTILIZADAS**

SZATENDHONORARIO : campos específicos para este convênio SP, SH, SADT, SPPREST

SZTABPROCIPSEMG :  cadastro de valores do IAMSPE/IPSEMG no Anexo do Cadastro de Tabelas de Procedimentos e Serviços
