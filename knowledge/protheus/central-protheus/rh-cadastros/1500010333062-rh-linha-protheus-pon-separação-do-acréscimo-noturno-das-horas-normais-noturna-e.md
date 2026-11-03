---
article_id: 1500010333062
category: RH - Cadastros
content_hash: fbf1402f56c96af8594a3c5613b1551495b0c7e6e14f77128e5a178d566d1ac2
fetched_at: '2026-06-28T22:44:53.152519+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Separação do Acréscimo Noturno das Horas Normais
  Noturna e das Horas Extras Noturna
type: support-article
updated_at: '2026-02-03T16:57:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010333062-RH-Linha-Protheus-PON-Separa%C3%A7%C3%A3o-do-Acr%C3%A9scimo-Noturno-das-Horas-Normais-Noturna-e-das-Horas-Extras-Noturna
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38133336640663)****Tempo aproximado para leitura: 00:01:30 min**  
  
**Dúvida**  
Como configurar para efetuar a Separação dos eventos de Acréscimo Noturno dos eventos de Horas Normais Noturna e das Horas Extras Noturna.   
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Foi criado no cadastro do turno o campo **Separ Ac Not**. Ele será responsável por realizar a **separação dos minutos de acréscimo noturno gerado nos apontamentos dos eventos de Horas Normais Noturna e de Horas Extras Noturna .** Para que esse campo fique com sim, os campos **Id.Acre.Not** e **Apenas Ac.no** deverão estar com **Sim** também.  
  
Para que o sistema faça o apontamento corretamente dos eventos, será necessário seguir com os procedimentos abaixo:

- Primeiramente, ter atualizado os indicadores no dicionário da base. Seguindo os passos da documentação abaixo:  
[RH - Linha Protheus - PON - Faltam códigos de Identificadores de Ponto na Tabela 20 do Configurador](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410280168983-RH-Linha-Protheus-PON-Faltam-c%C3%B3digos-de-Identificadores-de-Ponto-na-Tabela-20-do-Configurador?source=search)  
  
- Após garantir que os identificadores estão atualizados no dicionário, deverá criar os dois eventos e vincular ao novos IDs do Ponto criados. Segue descrição de cada identificador do ponto:  
  
**Tabelas Genéricas 20 - Identificadores de Ponto:**  
**045A** - Acréscimo Adicional Noturno Hora Extra  
**046A** - Acréscimo Adicional Noturno Horas Normais  
  
Veja na documentação de apoio abaixo referente ao cadastro de eventos:  
[RH - Linha Protheus - PON - Como cadastrar os eventos para Folha de Pagamento ou Banco de Horas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013459532-RH-Linha-Protheus-PON-Como-cadastrar-os-eventos-para-Folha-de-Pagamento-ou-Banco-de-Horas?source=search)  
  
- Após os cadastros dos eventos, faça a configuração do turno de trabalho. Para isto, acesse em A**tualizações > Cadastros Gerais > Turno de Trabalho,** filtre o turno e clique em alterar, na aba Informações Ponto, os campos: **Apenas Ac. No./Id Acre Not e Separ Ac Not** deverão ficar com **S - Sim:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19201127879831)  
  
**Propriedades do Campo no Dicionário:**

**Separ Ac Not - R6\_SPADNOT**

|  |  |
| --- | --- |
| **SX3** | **Conteúdo** |
| X3\_CAMPO | R6\_SPADNOT |
| X3\_TIPO | C |
| X3\_TAMANHO | 1 |
| X3\_DECIMAL | 0 |
| X3\_TITULO | Separ Ac Not |
| X3\_DESCRIC | Separa o acrescimo Not. |
| X3\_PICTURE | @! |
| X3\_RELACAO | "N" |
| X3\_BROWSE | S |
| X3\_VISUAL | A |
| X3\_CBOX | S=Sim;N=Nao |
| X3\_WHEN | If ( FindFunction( "WhenSepAdN" ), WhenSepAdN(), .T. ) |
| X3\_FOLDER | 3 |
| X3\_PYME | S |

Cadastro da **Regra de Apontamento** para gerar as horas normais deverá configurar os campos:

Acesse em A**tualizações > Cadastro do Ponto > Regra Apontamento**, crie a regra ou altere a regra  criada e na aba **Apontamento** deixe o **campo Pg Hrs. Norm.** igual à **S - Sim**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/19201156908311)**  
  
**Exemplo de utilização:**  
  
**1. Acréscimo Adicional Noturno das Horas Normais Noturna:**  
  
Tabela de Horário Padrão:

1E - 22:00  
1S - 01:00  
2E - 02:00  
2S - 05:00  
  
Marcações realizadas pelo funcionário e seus apontamentos:

![](https://tdn.totvs.com/download/attachments/608374451/image2021-4-6_15-39-3.png?version=1&modificationDate=1617734343527&api=v2&effects=drop-shadow)

O funcionário trabalhou ao todo 6 horas noturnas.

Quando o campo **Separ Ac Not estiver com Sim**, teremos o seguinte resultado:  
  
Evento 106 (Adicional Noturno) com 6 horas  
Acréscimo das horas normais noturnas no evento 013 (Id 046A) com 51 minutos referente as 6 Horas Noturna Normais Trabalhadas.  
  
**2.** **Acréscimo Adicional Noturno Hora Extra:**

Tabela de Horário Padrão:

1E - 22:00  
1S - 01:00  
2E - 02:00  
2S - 05:00

Marcações realizadas pelo funcionário e seus apontamentos:

![](https://tdn.totvs.com/download/attachments/608374451/extra.PNG?version=1&modificationDate=1617734641943&api=v2&effects=drop-shadow)

O funcionário trabalhou ao todo 7 horas noturnas, sendo 6 horas normais noturnas e 1 hora extra noturna.

Quando o campo **Separ Ac Not estiver com Sim**, teremos o seguinte resultado:  
  
Evento 106 (Adicional Noturno) com 6 horas  
Eventos 067 e 177 com 1 hora, que seria referente a Hora Extra noturna.  
Acréscimo das horas normais noturnas no evento 013 (Id 046A) com 51 minutos referente as 6 Horas Noturna Normais Trabalhadas.  
Acréscimo da hora extra noturna no evento 012 (Id 045A) com 9 minutos referente a 1 Hora Extra Noturna realizada.

**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)

##
