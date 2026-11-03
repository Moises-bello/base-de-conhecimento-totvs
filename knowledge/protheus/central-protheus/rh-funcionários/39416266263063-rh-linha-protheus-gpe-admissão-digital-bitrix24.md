---
article_id: 39416266263063
category: RH - Funcionários
content_hash: a9d19c5b17faa25189981d4e9be6395b414c877274e2aac5891d2a6772ddd683
fetched_at: '2026-06-28T22:43:27.316253+00:00'
product: protheus
section_id: 360011909593
source: central-protheus
title: RH - Linha Protheus - GPE - Admissão Digital BITRIX24
type: support-article
updated_at: '2026-03-31T17:43:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39416266263063-RH-Linha-Protheus-GPE-Admiss%C3%A3o-Digital-BITRIX24
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39416262434071) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como realizar a Admissão Digital com integração BITRIX24?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Criar uma função que deverá buscar as informações da tabela de funcionários, preparar os dados e através do JOB, enviar dados para a API employee da NG, conforme a operação encontrada na tabela de Transações. Quando o JOB identificar registros do tipo RJP\_TAB - "SRA" e este registro não tiver data de integração, será chamada esta função, passando como parâmetro a chave de leitura RJP\_KEY e a operação RJP\_OPER.

A função deve ainda buscar dentro da tabela SRA os dados do registro que foi incluído, alterado ou excluído e chamar a integração;  
Durante a chamada da integração, se a operação for de exclusão, não é necessário incluir is dados, somente a chave única;  
No caso de algum erro na integração, será gravado o retorno da NG no campo RJP\_RTN.

Obs: O campo da API ID Único (Chave Única) é o campo RJP\_KEY.

Campos e suas correspondências:

|  | CAMPOS | PROPRIEDADE API |
| --- | --- | --- |
| 1 | RJP\_KEY | id |
| 2 | substr(RJP\_KEY, Tamanho da empresa) | erpCompany |
| 3 | RA\_FILIAL | erpBranch |
| 4 | RB\_MAT | registration |
| 5 | RA\_NOMECMP | name |
| 6 | RA\_NASC | birth |
| 7 | RA\_CIC | cpf |
| 8 | RA\_SEXO | gender |
| 9 | RA\_RG | rg |
| 10 | RA\_EMAIL | email |
| 11 | RA\_TNOTRAB | erpWorkShift |
| 12 | Empresa + | + Filial da tabela CTT + | + RA\_CC | CostCenter |
| 13 | Empresa + | + Filial da tabela SRJ + | + RA\_CODFUNC | Occupation |
| 14 | Empresa + | + Filial da tabela SQB + | + RA\_DEPTO | department |
| 15 | RA\_ENDEREC | street |
| 16 | RA\_NUMENDE | number |
| 17 | RA\_BAIRRO | district |
| 18 | RA\_MUNICIP | city |
| 19 | RA\_CEP | zipCode |
| 20 | RA\_TELEFON | phone |
| 21 | RA\_SITFOLH | situation |
| 22 | RA\_CATEFD | eSocialRoleId |
| 23 | RA\_ADMISSA | admissionDate |
| 24 | RA\_DEMISSA | dismissalDate |
| 25 | RA\_PIS | pisCode |
| 26 | RA\_CODUNIC | eSocialId |
| 27 | RA\_CATEG | sefipCategory |
| 28 | R6\_DESC | workshiftDescription |
| 29 | CTT\_DESC01 | costCenterDescription |
| 30 | RJ\_DESC | occupationDescription |
| 31 | QB\_DESCRIC | departmentDescription |
| 32 | Empresa + | + Filial da tabela SQ3 + | + RA\_CARGO | position |

O JOB (Schedule) que dispara a Transação de dados para a Integração com a NG, foi ajustado para que possa buscar informações de origem da Tabela de Funcionários (SRA). Depois que os dados foram pré-selecionados, eles são formatados na estrutura de recebimento da API e enviados à integração. Se os dados forem integrados corretamente, a data de integração (RJP\_DTIN), da tabela de Integrações (RJP), será preenchida. Porém, caso ocorra alguma inconsistência durante a integração, este campo de data permanecerá vazio e o campo de retorno (RJP\_RTN), será preenchido com o erro retornado pela integração.

**Saiba mais:**

[API - Cadastro de Funcionário](https://tdn.totvs.com/pages/releaseview.action?pageId=546694744)

[RH - Funcionários](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011909593-RH-Funcion%C3%A1rios)
