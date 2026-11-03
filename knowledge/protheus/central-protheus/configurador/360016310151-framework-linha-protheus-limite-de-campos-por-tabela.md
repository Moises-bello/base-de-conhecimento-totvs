---
article_id: 360016310151
category: Configurador
content_hash: becb5406e7b753abc32bd027e6b12a03599a3563b0443d40086221931c251799
fetched_at: '2026-06-28T22:42:19.065108+00:00'
product: protheus
section_id: 360000076767
source: central-protheus
title: Framework - Linha Protheus  - Limite de campos por tabela
type: support-article
updated_at: '2026-03-27T14:27:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016310151-Framework-Linha-Protheus-Limite-de-campos-por-tabela
---

**Dúvida**  
Qual o limite de campos suportado por tabela?  
  
**Ambiente**  
Protheus - Configurador - A partir da versão 11.80   
  
**Solução**

O número máximo de campos que podem ser criados em uma tabela é de 350. Essa é uma limitação estrutural do Protheus para garantia do funcionamento e compatibilidade com os bancos de dados homologados.

Caso haja necessidade de mais campos, existe a possibilidade de criar uma Tabela customizada de usuário, e tratá-la para ser consultada / alimentada via pontos de entrada contidos na rotina em questão, para desta forma, servir como auxiliar no tratamento da regra desejada.

Importante: Toda criação e manutenção de tabelas deve ser realizada exclusivamente pelas ferramentas disponibilizadas no módulo Configurador, bem como, toda manipulação de dados nas tabelas, exclusivamente via processamento. Não se recomenda quaisquer procedimentos diretamente no banco de dados.

*Obs: O Suporte Protheus não auxilia no desenvolvimento de customizações. É recomendado que realize junto a um desenvolvedor. Para obter informação de quais pontos de entrada há disponíveis na rotina desejada, acione nossos canais de autoatendimento e o canal de Suporte do módulo.*

A partir do Release 12.1.2510 (LIB 20251006) a validação de contagem de campos passa a considerar apenas os campos de contexto **Real** para o limite de 350 campos. Campos de contexto **Virtual** foram desconsiderados na contagem.

[Limite de campos por tabela](https://tdn.totvs.com/display/public/framework/Limite+de+campos+por+tabela)
