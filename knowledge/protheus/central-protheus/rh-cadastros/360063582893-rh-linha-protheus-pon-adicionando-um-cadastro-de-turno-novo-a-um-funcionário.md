---
article_id: 360063582893
category: RH - Cadastros
content_hash: 2de927895100ba3e77e1f83952007b664e4e67abe9743cab507e896b312e1b89
fetched_at: '2026-06-28T22:44:52.727889+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Adicionando um cadastro de turno novo a um funcionário
type: support-article
updated_at: '2026-02-04T17:15:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063582893-RH-Linha-Protheus-PON-Adicionando-um-cadastro-de-turno-novo-a-um-funcion%C3%A1rio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34286920241943)Tempo aproximado para leitura:00:01:00 min**  
  
**Dúvida**  
Como alterar e incluir um novo turno e relacionar ao funcionário?   
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
É possível alocar para um funcionário ativo no cadastro de funcionários (SRA), um novo turno recentemente cadastrado. Para isso acessar na rotina de Cadastro de Turnos de Trabalho em **Atualizações > Cadastros Gerais > Turnos de Trabalho** e cadastrar o novo turno, parametrizando as abas conforme desejado.  
  
Após o cadastro de um novo Turno de Trabalho, acessar a rotina Tabela de Horário Padrão em **Atualizações > Cadastro do Ponto > Tabela de Horário Padrão.** Na tela inicial selecionar o turno que acabou de cadastrar e clicando em Incluir, inserir os horário de trabalho de segunda a domingo e, se houver mais de uma sequência para cadastro. Veja como cadastrar a tabela de horário padrão, clicando [aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047920293-RH-Linha-Protheus-PON-Tabela-de-Hor%C3%A1rio-Padr%C3%A3o).  
  
Com o cadastro do Turno de Trabalho e Tabela de Horário Padrão, acessar a rotina Troca de Turno em **Atualizações > Cadastro de Funcionários > Troca de Turno,** inserir uma linha para o funcionário com data início do turno novo, sequência da tabela de horário padrão e regra de apontamento, assim como exemplo abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34286920242967)

**Observação**: No exemplo acima, a partir de 01/08/2025 o funcionário de matrícula 000088 que estava no turno 01 passará para o turno 03.  
  
Lembrando que, a troca de turno será efetiva somente se o período de apontamento cadastrado nos parâmetros **MV\_PONMES** e **MV\_PAPONTA** estiver contemplando a data da troca. Para mais detalhes [clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029175091-RH-Linha-Protheus-PON-Ao-efetuar-a-troca-do-turno-o-cadastro-do-funcion%C3%A1rio-n%C3%A3o-%C3%A9-atualizado)  
  
**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
