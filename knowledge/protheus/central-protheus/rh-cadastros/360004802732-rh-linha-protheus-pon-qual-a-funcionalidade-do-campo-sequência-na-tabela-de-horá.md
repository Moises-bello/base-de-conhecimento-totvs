---
article_id: 360004802732
category: RH - Cadastros
content_hash: c35a27f6b9f8c3c44f5ec49b0c70f1269be1baafe144fcd6ebe03f55cc027aba
fetched_at: '2026-06-28T22:44:53.102085+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Qual a funcionalidade do campo Sequência na Tabela
  de Horário Padrão
type: support-article
updated_at: '2026-02-04T16:51:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004802732-RH-Linha-Protheus-PON-Qual-a-funcionalidade-do-campo-Sequ%C3%AAncia-na-Tabela-de-Hor%C3%A1rio-Padr%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35189827673239) Tempo aproximado para leitura: 00:01:30 min**  
  
**Dúvida**  
PONA080 - Qual a funcionalidade do campo Sequência na Tabela de horário padrão?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Ao efetuar um cadastro de um turno de trabalho e, por consequência, acessar o cadastro **Tabela de Horário Padrão**, em **Atualizações > Cadastro do Ponto > Tabela de Horário Padrão**, ao clicar em **Incluir**, será inserida uma nova sequência para uma escala simples, que se repete a mesma toda semana. **Exemplo**: o funcionário sempre vai trabalhar de segunda a sexta e folgar no sábado e domingo. Neste caso, haverá apenas 1 sequência cadastrada:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32046433310359)

Para uma **escala de revezamento**, por exemplo, o funcionário trabalha 6 dias e folga 2. Neste caso, terá que informar várias sequências, onde **cada sequência corresponde a uma semana**, e cada semana terá dias diferentes para folgar. Deverá cadastrar as semanas **(sequências)** até que o dia da folga da primeira semana se repita e se tenha um ciclo de repetição completo.

Neste exemplo de revezamento, vamos supor que o funcionário folga no domingo a cada 6 semanas. Neste caso, o ciclo será de 6 sequências:![](https://centraldeatendimento.totvs.com/hc/article_attachments/32046403051159)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32046403053079)  
  
**Importante:** inicia-se a montagem do calendário com base na troca de turno e, para cada segunda-feira, será trocada a sequência na ordem da Tabela de Horário Padrão.

**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[RH - Linha Protheus - PON - Tabela de Horário Padrão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047920293-RH-Linha-Protheus-PON-Tabela-de-Hor%C3%A1rio-Padr%C3%A3o)
