---
content_hash: c43a15968f41ea494a862bff4f5c3bb6f2779a21db33a65866787858ee44fe31
fetched_at: '2026-06-29T00:05:53.976818+00:00'
page_id: '1072706900'
product: rm
source: tdn-rm
title: DT - Remoção de Menus e Realocação de Campos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1072706900
version: 38
---

## **01. DADOS GERAIS**

| Produto: | TOTVS RH |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Remoção de menus e realocação de campos. |
| País: | Brasil |
| Story: | [DRHROTRM-19151](https://jiraproducao.totvs.com.br/browse/DRHROTRM-19151) |

## **02. VERSÃO**

12.1.2606 e superiores.

## **03. S****ITUAÇÃO/REQUISITO**

Conforme informado nos próprios menus do produto e documentado no TDN [link](https://tdn.totvs.com/pages/viewpage.action?pageId=1040989302) , alguns menus precisão ser descontinuados a partir da release **12.1.2606.**

Essa descontinuação ocorre porque as funcionalidades correspondentes já foram substituídas pelos processos do eSocial no **TOTVS Folha de Pagamento**, não sendo mais necessárias as rotinas anteriormente disponibilizadas pelo sistema.

## **04. SOLUÇÃO**

Com o objetivo de tornar a navegação mais intuitiva e aderente aos processos atuais do produto, Simplificação da interface e a remoção de menus do **TOTVS Folha de Pagamento** que refletem a substituição dessas obrigações pelo eSocial, sendo:

Os menus abaixo foram removidos, pois suas funcionalidades foram substituídas pelos processos disponibilizados pelo eSocial e pela EFD-Reinf.

Recomendamos que os usuários passem a utilizar os processos equivalentes dessas obrigações, garantindo conformidade com a legislação vigente e aderência às evoluções do produto.

## 1. Menus removidos

Os menus abaixo foram removidos, pois suas funcionalidades foram substituídas pelos processos disponibilizados pelo eSocial e pela EFD-Reinf.

Recomendamos que os usuários passem a utilizar os processos equivalentes dessas obrigações, garantindo conformidade com a legislação vigente e aderência às evoluções do produto.

* Encargos | CAGED
* Anuais | RAIS
* Anuais | DIRF/Informe de Rendimentos | Atualizar Dados da DIRF -
* Anuais | DIRF/Informe de Rendimentos | Conversão de Operadora Perfil X Cadastro
* SEFIP
  + Encargos | Parâmetros SEFIP
  + Encargos | Liberação de Flags SEFIP
  + Encargos | FGTS | Comparativo SEFIP X Folha Analítica
  + Encargos | FGTS | Geração SEFIP
  + Encargos | FGTS | Relatório de Retificação de Dados do Trabalhador no SEFIP
* Integração Performance e Meta (P&M)
* Configurações | Conversão de perfis (Delphi X.Net)
* Configurações | Conversor da Contribuição Sindical
* Folha Mensal | Relatórios da Folha | Salário de Contribuição (AAS)
* Folha Mensal | Relatórios da Folha | Atualizar Base AAS

**Atenção:**

Caso seja necessário gerar informações retroativas relacionadas a essas rotinas descontinuadas, será necessário restaurar um backup de um período em que elas ainda estavam disponíveis e realizar o processamento em uma base de homologação.

Recomendamos que esse procedimento **não seja executado na base de produção**, preservando a integridade dos dados e do ambiente.

## 2. Menus alterados

Alguns grupos e campos do cadastro de funcionários foram renomeados e/ou reorganizados para refletir melhor os dados contratuais atualmente utilizados pelo produto.

**ANTES:** Funcionários | Grupo Rotinas Mensais / Anuais

**ATUAL:** Funcionários | Grupo Dados Contratuais

**ANTES:** Funcionários | Grupo Rotinas Mensais / Anuais | FGTS / SEFIP

**ATUAL:** Funcionários | Grupo Dados Contratuais I Dados I

**ANTES:** Funcionários | Grupo Rotinas Mensais / Anuais | RAIS

**ATUAL:** Funcionários | Grupo Dados Contratuais | Dados II

**ANTES:** Funcionários | Anexos | Históricos | Histórico de Ocorrência do SEFIP

**ATUAL:** Funcionários | Anexos | Históricos | Histórico de Ocorrência

## 3. Menus realocados

Algumas funcionalidades foram reorganizadas na estrutura de menus para facilitar a navegação e melhorar a experiência do usuário.

**ANTES:** Anuais | DIRF/Informe de Rendimentos | Atualizar dados da DIRF 

**ATUAL:** eSocial | Outros Processos

## 4. Lookups e validações removidos

**4.1 -** Foram removidos os lookups e validações que deixaram de ser utilizados pelo processo de integração.

**ANTES:** Configurações | Parametrizador | Integrações | TOTVS RH | Avaliação de Desempenho

**ATUAL:** Configurações | Parametrizador | Integrações | TOTVS RH | Avaliação de Desempenho

**4.2 -**Foi removida a obrigatoriedade de preenchimento do campo Grupo de AAS no cadastro de eventos.

Menu Cadastros | Eventos | Eventos

**ANTES:**  Validação que exigia o preenchimento do campo **Grupo de AAS**.

**ATUAL:** O preenchimento do campo **Grupo de AAS** deixou de ser obrigatório.

  

**4.3 -** Foram realizadas adequações no processo de Liberação de Competência para refletir as mudanças implementadas no produto.

Menu Folha Mensal | Liberação de competência

**ANTES**

**ATUAL**

## **05. DEMAIS INFORMAÇÕES**

* [SEFIP - Geração](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719275)
* [SEFIP - Comparativo SEFIP x Folha Analítica](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719469)
* [SEFIP - Histórico de Ocorrência do SEFIP](https://tdn.totvs.com/pages/viewpage.action?pageId=452719637)
* [SEFIP - Distribuir SEFIP](https://tdn.totvs.com.br/display/public/LRM/Distribuir+SEFIP)
* [CAGED - Geração de Arquivo de CAGED](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719356)






* [Atualizar Base AAS](https://tdn.totvs.com.br/display/public/LRM/Atualizar+Base+AAS)
* [Conversão de Perfis (Delphi x .NET)](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452718463)
* [Processo Conversor Contribuição Sindical](https://tdn.totvs.com.br/pages/releaseview.action?pageId=454843650)
* [Liberação de Competência Folha](https://tdn.totvs.com/pages/viewpage.action?pageId=452719172)
* [DIRF/Informe de Rendimentos](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719351)
* [Parametrização Reembolso Plano de Saúde](https://tdn.totvs.com.br/pages/viewpage.action?pageId=338367700)
