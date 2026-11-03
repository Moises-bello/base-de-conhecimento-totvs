---
article_id: 1500003111442
category: Arquitetura Organizacional (SIGAORG)
content_hash: d0bbc972036ae57f3f95f60a31a6f6e738ffc9428ad6858a714cdeb84e76a374
fetched_at: '2026-06-28T22:42:52.962579+00:00'
product: protheus
section_id: 1500000904101
source: central-protheus
title: RH - Linha Protheus - ORG - Quais os principais parâmetros do Módulo Arquitetura
  Organizacional (SIGAORG)
type: support-article
updated_at: '2021-07-29T21:13:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003111442-RH-Linha-Protheus-ORG-Quais-os-principais-par%C3%A2metros-do-M%C3%B3dulo-Arquitetura-Organizacional-SIGAORG
---

**Dúvida**Quais os principais parâmetros do Módulo Arquitetura Organizacional **(SIGAORG)**?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Arquitetura Organizacional – Todas as versões  
  
**Solução**Os principais parâmetros do Módulo 70 Arquitetura Organizacional **(SIGAORG)** são:  
  
MV\_IORGRSP = Indica se a integração entre os módulos SIGAORG e SIGARSP está ou não ativada.   
0 - integração não ativada.   
1 - integração ativada.  
  
MV\_ORGCFG = Configura o modo de uso do módulo SIGAORG, se:

0 - Não utiliza (não há integração do SIGAORG com os demais módulos do sistema);  
1 - Utiliza com controle de Postos (habilita controle de "Postos" no Cadastro de Funcionários, na inclusão de funcionários);  
2 - Utiliza com controle de Departamentos (habilita controle de "Departamentos" no Cadastro de Funcionários, na inclusão de funcionários).  
  
MV\_ORGCEMP = Define se a carga de Departamentos considera todas as empresas, quando definido como "S" (Sim). "N" (Não), caso contrário.  
  
MV\_ORGSPFL =  Configura a integração das permissões de acesso ao recurso de Superfiltro, que valida o usuário no momento do login.  
  
**Saiba Mais**  
[Artigos sobre Arquitetura Organizacional](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206968028-RH-Arquitetura-Organizacional)
