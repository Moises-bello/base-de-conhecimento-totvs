---
content_hash: 4e9ce89e97ed14125570859b50bda209b7a0dea1d43307a34ae0f2fcab2dfde9
fetched_at: '2026-06-29T00:11:48.915520+00:00'
page_id: '829293510'
product: rm
source: tdn-rm
title: Parametrizador Gestão Hospitalar e Clinicas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=829293510
version: 22
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Estrutura do Processo**
3. **Tabelas utilizadas**
4. **Itens Alterados**

PainelVisão Geral

## **01. VISÃO GERAL**

Assistente de Implantação de Processos contendo os parâmetros do Gestão Hospitalar, disponível a partir do Release 12.1.2406

Menu Ambiente | Parâmetros | Gestão Hospitalar

A tela de Parâmetros na nova MDI (RM.exe) tem comportamento diferente da tela utilizada antes pelo RMSaude.exe (Delphi). Na nova MDI os parâmetros são salvos por assunto e um assunto de cada vez.

**Premissas:**

- É necessário liberar permissão de acesso ao menu Parâmetros | Gestão Hospitalar.

Em Serviços Globais, acesse o menu Segurança | Perfis. No Sistema: Hospitais e Clinica, marque permissão liberada para o item [15] Ambiente / [15.02] Configuração / [15.02.03] Parâmetros

- O arquivo RM.Lib.Params.Wizard.xml deverá estar na pasta Bin da instalação da Biblioteca (já acompanha o instalador).

Estrutura do Processo

## **02. Estrutura do processo**

Para melhorar a organização dos parâmetros, todas as telas de configuração foram consolidadas em uma única rotina de parametrização.

Além disso, reorganizamos alguns parâmetros, posicionando-os nos locais onde fazem mais sentido dentro do seu contexto.

Itens Alterados - Parâmetros Gerais

## **03. Itens Alterados - Parâmetros Gerais**

Essa etapa segue para informar quais itens presentes no novo processo de parametrização da nova MDI (RM.exe) tiveram alguma tipo de alteração (parâmetros movidos de contexto, e ou descontinuados) em relação ao Delphi.

InformaçõesA listagem dos itens abaixo será representada de vista ao Delphi:

| Aba | Alterações |
| --- | --- |
| Empresa | * Descontinuado * Os Parâmetros TISS (circulados) foram movidos para o item abaixo: |
| Prontuário Eletrônico | * Descontinuado |
| PEP RM | * Renomeado para "Prontuário Eletrônico" * Os Parâmetros de Integração Laudite foram movidos para dentro do Contexto de Unidade de Diagnóstico | Integrações. |
| Registro de Controle I, II, III e IV | * As abas foram agrupadas em um único menu de "Registro e Controle" * Os Parâmetros foram reorganizador para serem agrupados por contexto * Os Parâmetros de Cobrança Automática (previamente em Registro e Controle II) foram movidos para o menu de Faturamento no item com nome "Autorizações". * Os parâmetros a seguir foram descontinuados: |
| Integração | * Criado um submenu chamado Integrações BackOffice * Integração "RM Fluxus" renomeado para Gestão Financeira e movido para o submenu de "Integrações BackOffice" |
| Relatórios via Gerador | * Renomeado para "Relatórios" |
| Repasse | * Separado em 2 menus diferentes para facilitar acesso. |
| Estoques I e II | * As abas foram agrupadas em um único menu de "Estoque" * Os parâmetros a seguir foram descontinuados: |
| Tesouraria | * Movido para o menu de Faturamento dentro do contexto de Emissão de nota Fiscal. |
| Unidade de Diagnóstico I e II | * Os Parâmetros foram reorganizados para separar o contexto de Integrações dos parâmetros gerais da Unidade de Diagnóstico. * Os parâmetros a seguir foram descontinuados: |
| Faturamento I e II | * As abas foram agrupadas em único menu de Faturamento * Os Parâmetros foram reorganizados para serem agrupados por contexto * Os parâmetros a seguir foram descontinuados: |
| Impressão de Conta/Extrato | * Descontinuado, os relatórios são configurados dentro do contrato do convênio. |
| Med. Controlados | * O parâmetro a seguir foi descontinuado: |
| Controle e Recurso de Glosa | * O parâmetro a seguir foi descontinuado: |

Itens Alterados - Parâmetros de Estação

## **04. Itens Alterados -** **Parâmetros de Estação**

Os Parâmetros de Estação se encontram agora juntos dos parâmetros gerais dentro do assistente de parametrização do RM no caminho a seguir:

Hospitais e Clínicas > Ambiente > Configuração > Parâmetros > Gestão Hospitalar |Parâmetros de Estação de Trabalho

Itens Alterados - Parâmetros de Impressão

## **05. Itens Alterados -** **Parâmetros de Impressão**

Os Parâmetros de Impressão se encontram agora em conjunto dos Parâmetros de Estação de Trabalho dentro do assistente de parametrização do RM no caminho a seguir:   
Hospitais e Clínicas | Ambiente | Configuração | Parâmetros | Gestão Hospitalar | Parâmetros de Estação de Trabalho | Aba “Impressão” (ao editar cadastro)

Itens Alterados - Integração RM Nucleus

## **06. Itens Alterados -** **Integração RM Nucleus**

Os parâmetros da Integração RM Nucleus foram renomeados para “**Gestão de Estoque, Compra e Faturamento**”

O mesmo se encontra agora juntos dos parâmetros gerais dentro do assistente de parametrização do RM no caminho a seguir:   
Hospitais e Clínicas | Ambiente | Configuração | Parâmetros | Gestão Hospitalar | Integrações | Integrações BackOffice

Itens Alterados - Parâmetros SUS

## **07. Itens Alterados -** **Parâmetros SUS**

Previamente os "Parâmetros SUS" se encontravam em um menu separado, agora foram movidos para ficar agrupados com os parâmetros gerais dentro do assistente de parametrização do RM no caminho a seguir:   
Hospitais e Clínicas | Ambiente | Configuração | Parâmetros | Gestão Hospitalar | Parâmetros SUS.

## **08. TABELAS UTILIZADAS**

SZPARAM, SZPARAMGERAL, SZPARAMGERALC
