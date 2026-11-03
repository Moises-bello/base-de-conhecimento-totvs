---
article_id: 360048643454
category: MDT - PCMSO
content_hash: d1504329781e9bb05bc065993bf1eb8842fc5f318cf4b9a9f866028e87d28c4b
fetched_at: '2026-06-28T22:44:28.318391+00:00'
product: protheus
section_id: 360010945214
source: central-protheus
title: RH - Linha Protheus - MDT - Ao tentar realizar uma movimentação na ficha médica,
  apresenta a mensagem REGBLOQ - Este registro está bloqueado para uso
type: support-article
updated_at: '2025-09-03T13:54:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048643454-RH-Linha-Protheus-MDT-Ao-tentar-realizar-uma-movimenta%C3%A7%C3%A3o-na-ficha-m%C3%A9dica-apresenta-a-mensagem-REGBLOQ-Este-registro-est%C3%A1-bloqueado-para-uso
---

**Ocorrência**Ao tentar realizar uma movimentação na ficha médica, é apresenta a mensagem REGBLOQ - Este registro está bloqueado para uso  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as Versões  
  
**Causa**Todos os funcionários cadastrados na tabela SRA (Cadastro de Funcionários), quando desligados da empresa, ficam, automaticamente, bloqueados para uso em processamentos nas demais rotinas.  
  
Este controle é realizado pelo campo RA\_MSBLQL.  
  
Apartir do momento que existe este bloqueio a empresa fica impossibilitada de realizar movimentações na ficha médica como inclusão de exames etc.  
  
**Solução**O ideal é instruir o seu departamento de RH e SESMT, a realizarem todos os lançamentos necessários a matricula/ Ficha Médica, enquanto a pessoa está ativa no sistema. Ou seja, incluir o exame mesmo que ainda não tenha o resultado, pois se já existe o lançamento do exame o sistema permite editar para informar o resultado. Somente após todos os lançamentos realizados poderá ser calculado a rescisão.  
  
Dependendo do porte da empresa esse processo de comunicação é tardio, portando existe a possibilidade de realizar o calculo da rescisão antes dos lançamentos necessários como exame toxicológico.  
  
Nestes casos a empresa pode configurar o parâmetro MV\_MSBLQL - .F. e desta maneira consegue das continuidade aos lançamentos.  
  
Para flexibilizar o bloqueio ou não bloqueio dos funcionários que foram desligados da empresa, existe no sistema o parâmetro MV\_MSBLQL, que pode ser configurado com as seguintes opções:  
  
T (true, verdadeiro) - determina o bloqueio de todos os funcionários da tabela SRA quando desligados pela rotina Rescisão Contratual (GPEM040);  
  
F (false, falso) - determina o não bloqueio dos funcionários da tabela SRA quando desligados pela rotina de Rescisão Contratual, mantendo-os disponíveis para uso em processamentos nas demais rotinas do Protheus.  
  
Importante reforçar que este erro é processual e não sistêmico e mesmo ativando o parâmetro não será todas as rotinas que acataram este comportamento.  
  
**Saiba Mais**[FAQS Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)[MV\_MSBLQL](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206971487-RH-Medicina-e-Seguran%C3%A7a-do-Trabalho)
