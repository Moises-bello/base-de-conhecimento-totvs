---
article_id: 360044457834
category: MDT - PCMSO
content_hash: 045ceadb079adb0204b0c08a04519ee5e1f40fef8c764731eb2d0c4d7bab6215
fetched_at: '2026-06-28T22:44:28.423110+00:00'
product: protheus
section_id: 360010945214
source: central-protheus
title: RH - Linha Protheus - MDT - Como realizar o lançamento de exames  para fichas
  médicas demitidas.
type: support-article
updated_at: '2025-10-06T18:03:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044457834-RH-Linha-Protheus-MDT-Como-realizar-o-lan%C3%A7amento-de-exames-para-fichas-m%C3%A9dicas-demitidas
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30362757217175)**Tempo aproximado para leitura:**00:02:00 min  
  
Ocorrência**Como realizar o lançamento de exames  para fichas médicas demitidas?

**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho  – Todas as versões  
  
**Solução**Todos os funcionários cadastrados na tabela **SRA (Cadastro de Funcionários)**, quando desligados da empresa, ficam, automaticamente, bloqueados para uso em processamentos nas demais rotinas.

Este controle é realizado pelo campo **(RA\_MSBLQL)**.

A partir do momento que existe este bloqueio a empresa fica impossibilitada de realizar a inclusão do exame toxicológico.

O ideal é instruir o seu departamento de RH a realizar todos os lançamentos necessários a matricula, enquanto a pessoa está ativa no sistema. Ou seja, incluir o exame mesmo que ainda não tenha o resultado, pois se já existe o lançamento do exame  o sistema permite editar para informar o resultado.

Após isso pode ser realizado o calculo da rescisão.

Dependendo do porte da empresa esse processo de comunicação é tardio, portando existe a possibilidade de realizar o calculo da rescisão antes dos lançamentos necessários como exame toxicológico.

Nestes casos a empresa pode configurar  o parâmetro MV\_MSBLQL - .F. e desta maneira consegue das continuidade aos lançamentos.

Todos os funcionários cadastrados na tabela **SRA (Cadastro de Funcionários)**, quando desligados da empresa, ficam, automaticamente, bloqueados para uso em processamentos nas demais rotinas.

Este controle é realizado pelo campo **(RA\_MSBLQL)**.  
  
Para flexibilizar o bloqueio ou não bloqueio dos funcionários que foram desligados da empresa, existe no sistema o parâmetro **MV\_MSBLQL**, que pode ser configurado com as seguintes opções:

* T (true, verdadeiro) - determina o bloqueio de todos os funcionários da tabela SRA quando desligados pela rotina **Rescisão Contratual**;
* F (false, falso) - determina o não bloqueio dos funcionários da tabela SRA quando desligados pela rotina de **Rescisão Contratual**, mantendo-os disponíveis para uso em processamentos nas demais rotinas do Protheus.  
    
  Para localizar o parâmetro acesse o configurador no seguinte caminho: **Ambiente - Cadastro - Parâmetro** - pesquise por **MV\_MSBLQL** e edite conforme a necessidade da empresa  
    
  ![oSrpqts6Sk.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/19201520787607)

**Saiba Mais**[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-BR/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-BR/sections/9198712823575-Assistente-Virtual-Carolina)
