---
content_hash: fab39699c5be0e4e221d5f0f912345e24df5467a7204b06b4b00b73c201e2013
fetched_at: '2026-06-29T00:08:14.832683+00:00'
page_id: '244718109'
product: rm
source: tdn-rm
title: EF_Aluguel_Contabilização
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244718109
version: 8
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Incorporação - Gestão de Locação |
| **Versões:** | 12.**1.13 e superiores** |
| **Ocorrência:** | PCREQ-9474 |
| **Ambiente:** | RM |
| **Requisito** | Contabilização de Aluguel |
| **Observações:** | Gerar contabilização a partir de processos do módulo de Gestão de Locação. |
|  |  |

|  |  |  |
| --- | --- | --- |
| **Rotinas Envolvidas** | | |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** |
| Contrato de Locação | Alteração | Aluguel -> Contrato de Locação |
| Modelo de Contrato | Alteração | Aluguel -> Cadastros/ Modelo de Contrato de Locação |
| Reajuste | Alteração | Aluguel -> Reajuste e Aluguel -> Contrato de Locação-> Aplicar Reajuste |
| Aditivos | Alteração | Aluguel-> Contrato de Locação -> Anexos-> Aditivos |
| Escalonamento | Alteração | Aluguel-> Contrato de Locação -> Anexos-> Escalonamento |
| Solicitação de Tarefas | Alteração | Contabilidade->Processos->Solicitação de Tarefas |
| Evento Financeiro | Alteração | Aluguel-> Evento Financeiro |
| Integração Contábil | Inclusão | Contabilidade |

|  |  |
| --- | --- |
| **SIGLA** | **DESCRIÇÃO** |
| CPC | Comitê de Pronunciamentos Contábeis |
| CFC | Conselho Federal de Contabilidade |
| ITs | Instruções Técnicas |
| CTs | Comunicados Técnicos |
| PMEs | Pequenas e Medias Empresas |
| NBC TG | NBC TG - são as Normas Brasileiras de Contabilidade convergentes com as normas internacionais emitidas pelo International Accounting Standards Board (Iasb); e as Normas Brasileiras de Contabilidade editadas por necessidades locais, sem equivalentes internacionais;   As NBC TG são segregadas em:   a) normas completas que compreendem as normas editadas pelo CFC a partir dos documentos emitidos pelo CPC que estão convergentes com as normas do Iasb, numeradas de 00 a 999;   b) normas simplificadas para PMEs que compreendem a norma de PME editada pelo CFC a partir do documento emitido pelo Iasb, bem como as ITs e os CTs editados pelo CFC sobre o assunto, numerados de 1000 a 1999;   c) normas específicas que compreendem as ITs e os CTs editados pelo CFC sobre entidades, atividades e assuntos específicos, numerados de 2000 a 2999. |
| ARRENDADOR | Que fornece imóvel; proprietário; locador; |
| ARRENDATÁRIO | Que toma o imóvel para locação; inquilino; locatário; |

# 1. Objetivo

Este documento deve definir o modelo de negócios para contabilização do Módulo de Aluguel do TOTVS Incorporação.

A contabilização descrita neste documento **não** atenderá o recurso TIN->Contratos-> Contratos de Venda e Alugueis onde o contrato de venda tem o “Tipo de Contrato” igual a “Aluguel” ou “Proposta de Aluguel”.

A integração contábil do módulo de Aluguel deve atender as linhas RM e Protheus.

Os métodos de contabilização são regulamentos pelo CPC e CFC, que estabelecem as regras gerais da contabilização de cada operação. O Comitê de Pronunciamentos Contábeis estabelece os CPCs que depois são regulamentados pelos NBC TGs entre outros.

No que permeia as relações de locação de imóveis devem ser atendidas as seguintes normas contábeis:

1. [NBC TG 01 (NBC T 19.10) - Redução ao Valor Recuperável de Ativos](http://www.cfc.org.br/sisweb/sre/detalhes_sre.aspx?Codigo=2010/001292).
2. [NBC TG 04 (NBC T 19.8) - Ativo Intangível](http://www.cfc.org.br/sisweb/sre/detalhes_sre.aspx?Codigo=2010/001303).
3. [NBC TG 06 (NBC T 10.2)– Operação de Arrendamento Mercantil](http://www.cfc.org.br/sisweb/sre/detalhes_sre.aspx?Codigo=2010/001304)
4. [NBC TG 16 (NBC T 19.20) - Estoques](http://www.cfc.org.br/sisweb/sre/detalhes_sre.aspx?Codigo=2009/001170)
5. [NBC TG 27 (R2) que dispõe sobre ativo imobilizado](http://www2.cfc.org.br/sisweb/sre/detalhes_sre.aspx?Codigo=2015/NBCTG27(R3))
6. [NBC TG 28 (NBC T 19.26) - Propriedade para Investimento](http://www.cfc.org.br/sisweb/sre/detalhes_sre.aspx?Codigo=2009/001178)
7. [NBC TG 31 (NBC T 19.28) - Ativo Não Circulante Mantido para Venda e Operação Descontinuada.](http://www.cfc.org.br/sisweb/sre/detalhes_sre.aspx?Codigo=2009/001188)
8. [NBC TG 32 (NBC T 19.2) - Tributos sobre o Lucro](http://www.cfc.org.br/sisweb/sre/detalhes_sre.aspx?Codigo=2009/001189).
9. [NBC TG 40 (NBC T 19.34) - Instrumentos Financeiros: Evidenciação.](http://www.cfc.org.br/sisweb/sre/detalhes_sre.aspx?Codigo=2009/001198)

Com destaque para a NBC TG 06, que regula o Arrendamento Mercantil Operacional, Financeiro e *Leaseback*, tratando principalmente as locações com possibilidade transferências do bem imóvel.

Não serão tratadas as contabilizações para demonstrações do **Arrendatário ou locatário**, pois para isso seria necessário o controle do Contrato de Locação a pagar, que não está previsto no módulo do TOTVS Incorporação/ Locação.

# Definição da Regra de Negócio

O contrato de locação TIN fornecerá recursos para integração contábil, independente do tipo de locação (locação imobiliária, arrendamento mercantil operacional ou financeiro, *leaseback, temporada*), que será identificado pelo usuário por meio do cadastro do Tipo de Contrato, não tendo o sistema meios para identificar se será feita ou não a transferência do ativo ao final do contrato. O usuário também identificará se todas as contabilizações de determinado contrato de locação **serão lineares ou não**, portanto este atributo será do modelo de contrato e do próprio contrato de locação. Não pode haver num mesmo contrato contabilizações lineares e não lineares.

Macro Fluxos de Processos
