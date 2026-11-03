---
content_hash: 4b81722af4896df0dc4f0839144057ed072c8e236ac3f232793974ca990df8f8
fetched_at: '2026-06-29T00:12:14.620233+00:00'
page_id: '968146200'
product: rm
source: tdn-rm
title: DT - Smart View - Lista de Dependentes do Funcionário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=968146200
version: 18
---

## **01. DADOS GERAIS**

| Produto: | TOTVS RH |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Smart View - Lista de Dependentes do Funcionário |
| País: | Brasil |
| Épico | [DRHROTRM-14209](https://jiraproducao.totvs.com.br/browse/DRHROTRM-14209) |

## **02. VERSÃO**

12.1.2510 e superiores.

## **03. S****ITUAÇÃO/REQUISITO**

Migrar os relatórios abaixo para o novo modelo de ferramenta utilizando o Smart View.

* **FOPREL00069 - Dependentes baixados no mês - mês anterior ao atual.TotvsReport**
* **FOP001004 - Relatório Lista de Dependentes do Funcionário.TotvsReport**
* **FOPREL001004 - Relatório Lista de Dependentes do Funcionário.TotvsReport**

* FOPREL001004 - Relatório Lista de Dependentes do Funcionário

* FOPREL00069 - Dependentes baixados no mês - mês anterior ao atual

## **04. SOLUÇÃO**

Visando melhorar a experiência do usuário e otimizar a análise de informações, implementamos dois relatórios em um único relatório consolidado, agora disponível na ferramenta Smart View, a nova solução de análise de dados da TOTVS.

Além da junção dos dados, foi disponibilizado o objeto de negócios e o respectivo relatório diretamente no Smart View, oferecendo uma interface mais moderna, interativa e amigável ao usuário.

| Campo relatório | Tabela e campo |
| --- | --- |
| Empresa | GCOLIGADA.NOMEFANTASIA |
| Endereço | GCOLIGADA.RUA |
| Cidade | GCOLIGADA.CIDADE |
| UF | GCOLIGADA.ESTADO |
| CNPJ | GCOLIGADA.CGC |
| Departamento | PSECAO.DESCRICAO |
| Matrícula | PFUNC.CHAPA |
| Titular | PFUNC.NOME |
| Situação Atual | PFUNC.CODSITUACAO |
| Nome Completo Dependente | PFDEPEND.NOME |
| Relação Dependente | PFDEPEND.GRAUPARENTESTO |
| Data de Nascimento | PFDEPEND.DTNASCIMENTO |
| Idade | O cálculo da idade considera o ano da data de geração.  Por exemplo, para uma data de geração em **22/08/2025** e uma data de nascimento em **15/12/1989**, a idade apresentada será **36 anos**. |
| Incidência Salário Família | PFDEPEND.INSSALFAM OU [REGRA DE CÁLCULO](https://tdn.totvs.com/display/public/LRM/Dependentes) |
| Incidência  de IRRF | PFDEPEND.INCIRRF |

Preparamos uma demonstração com diferentes combinações de parâmetros e exemplos de seus respectivos resultados, para facilitar o entendimento, conforme apresentado abaixo:

| Incidência Salário Família | Incidência IRRF | Imprime funcionários sem dependentes | Resultados |
| --- | --- | --- | --- |
| Mostrar todos | Mostrar todos | Sim | Lista **todos os funcionários.**  Lista **todos os dependentes**. |
| Mostrar todos | Mostrar todos | Não | Lista **funcionários** **com dependentes.**Lista **todos os dependentes.** |
| Mostrar todos | Sim | Sim | Lista **todos os funcionários**. **Os dependentes** listados serão **apenas** os **que possuem incidência de IRRF = Sim**. |
| Mostrar todos | Sim | Não | Lista **funcioná****rios com dependentes.** **Os dependentes** listados serão **apenas** os **que possuem incidência de IRRF****= Sim**. |
| Mostrar todos | Não | Sim | Lista **todos os funcionários. Os dependentes** listados serão **apenas** os **que possuem incidência de IRRF =** **Não**. |
| Mostrar todos | Não | Não | Lista **funcioná****rios com dependentes.** **Os dependentes** listados serão **apenas** os **que possuem incidência de IRRF =** **Não**. |
| Sim | Mostrar todos | Sim | Lista **todos os funcionários. Os dependentes** listados serão **apenas** os **que possuem incidência de** **Salário Família = Sim**. |
| Sim | Mostrar todos | Não | Lista **funcioná****rios com dependentes.** **Os dependentes** listados serão **apenas** os **que possuem incidência de** **Salário Família = Sim**. |
| Não | Mostrar todos | Sim | Lista **todos os funcionários.**  **Os dependentes** listados serão **apenas** os **que possuem incidência de** **Salário Família = N****ão**. |
| Não | Mostrar todos | Não | Lista **funcionários com dependentes.**  **Os dependentes** listados serão **apenas** os **que possuem incidência de** **Salário Família = N****ão**. |
| Sim | Sim | Sim | Lista **todos os funcionários. Os dependentes** listados serão **apenas** os **que possuem incidência de****Salário Família = Sim e IRRF = Sim**. |
| Sim | Sim | Não | Lista **funcionários com dependentes.  Os dependentes** listados serão **apenas** os **que possuem incidência de****Salário Família = Sim e IRRF = Sim**. |
| Sim | Não | Sim | Lista **todos os funcionários. Os dependentes** listados serão **apenas** os **que possuem incidência de** **Salário Família = Sim e IRRF = Não**. |
| Sim | Não | Não | Lista **funcionários com dependentes.  Os dependentes** listados serão **apenas** os **que possuem incidência de** **Salário Família = Sim e IRRF = Não**. |
| Não | Sim | Sim | Lista **todos os funcionários. Os dependentes** listados serão **apenas** os **que possuem incidência de** **Salário Família = Não e IRRF = Sim**. |
| Não | Sim | Não | Lista **funcionários com dependentes.  Os dependentes** listados serão **apenas** os **que possuem incidência de** **Salário Família = Não e IRRF = Sim**. |
| Não | Não | Sim | Lista **todos os funcionários. Os dependentes** listados serão **apenas** os **que possuem incidência de** **Salário Família = Não e IRRF = Não**. |
| Não | Não | Não | Lista **funcionários com dependentes.  Os dependentes** listados serão **apenas** os **que possuem incidência de** **Salário Família = Não e IRRF = Não**. |

## **05. DEMAIS INFORMAÇÕES**

[FOPTRP0020 - Lista de Dependentes do Funcionário](https://tdn.totvs.com/pages/viewpage.action?pageId=968144925)
