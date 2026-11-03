---
article_id: 360052257014
category: RH - Ponto Eletrônico
content_hash: b404f4e8ce8d71f18b0b0c335fa4c12d1013842ee4edb049d4473a41cc00188b
fetched_at: '2026-06-28T22:44:58.299811+00:00'
product: protheus
section_id: 206956208
source: central-protheus
title: RH - Linha Protheus - PON - Como gerar os Apontamentos a partir das marcações
  lidas no Ponto Eletrônico?
type: support-article
updated_at: '2022-07-19T17:53:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052257014-RH-Linha-Protheus-PON-Como-gerar-os-Apontamentos-a-partir-das-marca%C3%A7%C3%B5es-lidas-no-Ponto-Eletr%C3%B4nico
---

**Dúvida**Como gerar os Apontamentos a partir das marcações lidas no Ponto Eletrônico?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**Para **gerar apontamentos** no Ponto Eletrônico, primeiramente, são necessários alguns cadastros:

1- Ter um Período de Apontamento informado nos parâmetros MV\_PAPONTA e MV\_PONMES  
2- Turno de Trabalho cadastrado  
3- Tabela de Horário Padrão cadastrada  
4- Regra de Apontamento cadastrada  
5- Funcionário com Troca de Turno com o primeiro dia do Período de Apontamento que está trabalhando, exemplo: se o período for de 01 à 31.07.2020, deve existir registro de Troca de Turno com data de 01.07.2020  
  
Para apontar as hora de forma individual, acesse Atualizações -> Lançamentos -> Integrados (alterar ou incluir caso não tenha marcações no Período), clique no ícone conforme abaixo ou F12:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360085523813/mceclip1.png)  
  
O processo de Apontamento individual também pode ser feito através de Atualizações -> Lançamentos -> Marcações -> Atualizar, depois clique em Outras Ações -> Reaponta, conforme abaixo ou F9:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084410834/mceclip0.png)  
  
Para processar um Apontamento coletivo, acesse Miscelânea > Cálculos > Leitura/Apontamento, deixe a pergunta "Processamento?" como Apontamento conforme exemplo abaixo:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360085531273/mceclip3.png)

A pergunta Ler a partir do, quando é um processamento apenas de Apontamento, pode ser utilizada como Cadastro Funcionário ou por Relógio, porém quando temos um processamento em Ambos, o recomendado é utilizar a Leitura a partir do Cadastro do Relógio.  
Lembrando que, este processo é feito somente após as marcações já serem lidas pelo Sistema.  
  
**Informações complementares**[MP - PON - Período de apontamento desconfigurado. Como configurar: MV\_PAPONTA e MV\_PONMES](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115015809548-MP-PON-Per%C3%ADodo-de-apontamento-desconfigurado-Como-configurar-MV-PAPONTA-e-MV-PONMES?source=search)  
[MP - PON - Tabela de Horário Padrão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047920293-MP-PON-Tabela-de-Hor%C3%A1rio-Padr%C3%A3o-?source=search)  
[MP - PON - Como funciona a troca de turno dos funcionários?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015528671-MP-PON-Como-funciona-a-troca-de-turno-dos-funcion%C3%A1rios-?source=search)  
Pacote de Expedição Contínua do RH: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854>  
  
[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
