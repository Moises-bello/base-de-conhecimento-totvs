---
article_id: 360043030894
category: ' RH - Funcionários'
content_hash: a8d2cdbd4a86f3120397c7c8e3a3278039ef975f2792e4e601b10da88ceadada
fetched_at: '2026-06-28T22:44:48.238870+00:00'
product: protheus
section_id: 32419218165783
source: central-protheus
title: RH - Linha Protheus - PON - Utilização de exceção por funcionário para escalas
  de trabalho
type: support-article
updated_at: '2025-12-26T12:46:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043030894-RH-Linha-Protheus-PON-Utiliza%C3%A7%C3%A3o-de-exce%C3%A7%C3%A3o-por-funcion%C3%A1rio-para-escalas-de-trabalho
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34954159683735) Tempo aproximado para leitura: 00:04:00 min**  
  
**Dúvida**  
Como tratar os cenários onde os colaboradores trabalham aos domingos e tem os DSRs durante a semana?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Existem muitos clientes que têm colaboradores que trabalham aos domingos como sendo um dia normal, e o DSR do mesmo acontece em um dia de semana ou sábado.

Para esses cenários, muitos clientes utilizam o processo de troca de turno, porém o processo se torna oneroso, pois a cada troca de turno um evento **S-2206** é gerado e deve ser transmitido ao **eSocial** para que outra troca seja realizada.

A melhor e mais rápida tratativa para o caso é a utilização das exceções por funcionários, onde é possível programar a escala mensal de trabalho do colaborador, informando os sábados e domingos que serão trabalhados (pagando as horas de um dia normal) e tornando um dia normal em um dia compensado, não trabalhado ou DSR.

**Exemplos:**

**Como tornar um domingo em um dia trabalhado?**

Para realizar o processo, basta acessar o módulo 16 - Ponto Eletrônico em **Atualizações> Cadastro de Funcionário> Exceções por Funcionário**.

Já dentro da rotina, deve-se observar a coluna Trabalhado, selecionar o domingo desejado e marcar a opção **S - Sim**. Dessa forma, o domingo passará a ser um dia trabalhado normal.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058950853)

O próximo passo é inserir o motivo da geração da exceção para o colaborador.  
Por padrão, o sistema trará a descrição \*\***EXCECAO TRABALHADA\*\***, porém ela pode ser alterada por qualquer outra descrição.

**Exemplo:**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058951073)

Seguindo adiante, por padrão o sistema trará os tipos de hora extra de DSR caso o domingo esteja marcado como DSR na tabela de horário padrão, dessa forma:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058951093)

Caso os campos não sejam alterados, se o colaborador ultrapassar os horários previstos para trabalho, o sistema gerará as horas extras pertinentes a um domingo trabalhado.

No meu exemplo, quero que o sistema gere as horas extras iguais a de um dia normal, para que isso ocorra, terei que alterar esses dois campos da seguinte forma:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058951173)

Os demais campos podem ser deixados no padrão, ou alterados conforme o desejo do cliente.

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058952173)

Após informarmos que o Domingo 02/02/2020 é um dia trabalhado e que as horas serão pagas conforme as horas extras normais, o próximo passo é cadastrar os horários esperados para o colaborador no dia na aba horário, conforme exemplo abaixo:

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058952973)

No meu exemplo, o horário esperado para o colaborador é das 08:00 às 12:00 e das 13:00 às 17:00.

O próximo passo é realizar o cadastro de Intervalos para o colaborador, no meu exemplo vou informar que a primeira saída para o colaborador trata-se de Intervalo:

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058066334)

Agora vamos verificar a quantidade de horas na tela de total de horas:

No meu exemplo são 4 horas antes do intervalo + 1 hora de intervalo + 4 horas após o intervalo, ou seja, 9 horas.

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058066454)

Na rotina de marcações pressionando a tecla **F10** é possível verificar se a exceção está cadastrada corretamente.

A **legenda para exceções é azul escuro**, verifiquei também que foram gerados os horários para a exceção e o nome atribuído a ela na coluna exceção:

![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058953433)

Legendas:

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058953393)

Vou realizar um teste atribuindo um horário para o colaborador no dia, forçando a geração de 2 horas extras na saída:

![mceclip14.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058953553)

Agora vou mostrar um cenário onde é necessário que um dia de semana normal seja um DSR utilizando os conceitos explicados no primeiro exemplo:

![mceclip15.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058066934)

Nesse caso, como o dia não será trabalhado não será necessário informar horário de trabalho e intervalo. Ao consultar o dia na rotina de marcações pressionando a tecla **F10** o dia é demonstrado da seguinte forma:

Conforme a legenda anexada acima, o dia agora será um dia de **Exceção DSR**.

![mceclip16.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058067074)

Se a pergunta **Pg. DSR** estiver marcada com **Sim** na regra de apontamento, o pagamento de DSR será demonstrado no apontamento do colaborador:

![mceclip17.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058953873)

![mceclip18.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058067314)

Se por um acaso o colaborador trabalhar no dia, o sistema se comportará da seguinte forma:

![mceclip19.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058954033)

**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[RH - Linha Protheus - PON - Como informar um Afastamento no Ponto Eletrônico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050591573-RH-Linha-Protheus-PON-Como-informar-um-Afastamento-no-Ponto-Eletr%C3%B4nico?source=search)  
[RH - Linha Protheus - PON - Como aumentar tamanho da letra nas rotinas do Ponto Eletrônico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011274701-RH-Linha-Protheus-PON-Como-aumentar-tamanho-da-letra-nas-rotinas-do-Ponto-Eletr%C3%B4nico?source=search)
