---
article_id: 360059748093
category: MDT - PCMSO
content_hash: bae988eb21a0a7a5b79e297ed381ef0b0f2b9ca8a5d78c09037614e4ddcf723d
fetched_at: '2026-06-28T22:44:28.230612+00:00'
product: protheus
section_id: 360010945214
source: central-protheus
title: RH - Linha Protheus - MDT - Como emitir o Relatório de Encaminhamento (MDTR460)
type: support-article
updated_at: '2025-07-31T14:17:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059748093-RH-Linha-Protheus-MDT-Como-emitir-o-Relat%C3%B3rio-de-Encaminhamento-MDTR460
---

**Dúvida**Como emitir o Relatório de Encaminhamento (MDTR460)?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**O Encaminhamento emite relatório no formato de ficha individual para **encaminhamento do funcionário ao fornecedor de exames**. Com base nas informações da tabela de exames do funcionário (TM5) e na tabela de fornecedores de exames (TMD). O usuário seleciona o fornecedor desejado, poderá também selecionar um exame específico ou deixar que o programa lista todos os exames relacionados ao fornecedor previamente selecionado. Deve-se definir um **período de abrangência**.  
  
Na Ficha de Encaminhamento, encontram-se três agrupamentos de informação:

• Dados da empresa e do funcionário;  
• Dados do fornecedor;  
• Dados dos exames programados.

Por meio da pergunta “**Filtrar por Natureza?**” é possível realizar o filtro de dados pela Natureza do Exame **(Admissional, Demissional, Retorno ao trabalho, Mudança de Função e Periódico)**.  
  
![20201123_135617.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360100394233)  
  
**Obs.:** O relatório de encaminhamento (MDTR460) só será gerado na rotina, caso o exame cadastrado para o funcionário na rotina Exames do Func. (MDTA120) esteja com o campo **Data Result.** (TM5\_DTRESU) em **branco**.  
  
**Saiba Mais**  
[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-BR/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos PCMSO](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010945214-MDT-PCMSO)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-BR/sections/9198712823575-Assistente-Virtual-Carolina)
