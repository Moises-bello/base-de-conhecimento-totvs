---
article_id: 41052794384407
category: RH - Banco De Horas
content_hash: 786260a8b82ab8c838419f553a80d1c2ce373f2c8d3d2f8658194e0b90b13d8a
fetched_at: '2026-06-28T22:44:54.175980+00:00'
product: protheus
section_id: 32405029751063
source: central-protheus
title: RH - Linha Protheus - PON -  Fechamento do Banco de Horas por Vencimento
type: support-article
updated_at: '2026-06-08T14:38:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41052794384407-RH-Linha-Protheus-PON-Fechamento-do-Banco-de-Horas-por-Vencimento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41052794337303) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Como realizar o fechamento do banco de horas por Vencimento?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Foi disponibilizado no modulo 16 Ponto Eletrônico, o fechamento do Banco de Horas por vencimento.

Em **Miscelânea> Fechamentos> Banco de Horas** foi adicionada a opção "Vencimento" na Pergunta "Fechamento por?":  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/41052763877015)

**Importante**: Quando utilizada a opção Fechamento por Vencimento algumas perguntas apresentadas não serão consideradas para o fechamento.

**Funcionamento do Fechamento por Vencimento**

Serão baixados os eventos com data de vencimento menor que a Data de Fechamento.  
Os eventos que ocorreram antes da data de vencimento, mas não estão vencidos, podem ser usados para compensar os eventos vencidos.

Exemplo:   
Data do fechamento: 31/05/2024

Os eventos vencidos, em azul, serão baixados;  
Os eventos anteriores a data de fechamento, mas que não estão vencidos, em verde, serão utilizados para compensar os eventos vencidos;  
Os eventos que ocorreram após a data de fechamento, em preto, não serão considerados para o fechamento;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/41052794339735)

Após executar o fechamento temos os eventos baixados:

* **Apenas eventos do mesmo Centro de Custo são utilizados na compensação.**
* A Hora Extra do dia 02/05/2024 foi utilizada parcialmente para compensar a Falta do dia 04/01/2024, com isso foi gerado um novo registro separando o que foi utilizado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41052794340503)

Nos resultados foi gerado o saldo do centro de custo 000000002.  
Não foi gerada nenhuma verba para o centro de custo 000000001, pois todos os eventos vencidos foram compensados.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/41052794340759)

**Horas Valorizadas**

Ao selecionar a opção "Valorizadas" na pergunta "Utilizar Horas?" o sistema usará as horas valorizadas para realizar o fechamento:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/41052794341015)

Exemplo:

No Banco de Horas temos um atraso de 1h vencido  
e 1 Hora Extra com +50% de valorização, resultando em 1h e 30min  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/41052794342039)  
Ao realizar o fechamento utilizando as horas valorizadas temos:

Foram utilizados 40min (ou 1h se considerando a hora valorizada) da Hora Extra para compensar o atraso  
O restante da Hora Extra foi mantido no Banco de Horas  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/41052763883543)

**Fechamento para Rescisão**

Quando realizado o fechamento para rescisão todos os eventos que ocorreram antes da data de fechamento serão baixados, a data de vencimento será utilizada para realizar a compensação  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/41052763885335)

Exemplo:

Data de Fechamento: 31/05/2024  
Fechamento para Rescisão: Sim

Todos os eventos que ocorreram antes da data de fechamento serão baixados, destacados em azul na imagem abaixo;  
Os eventos que ocorreram após a data de fechamento não serão considerados no fechamento.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/41052794349719)

Após realizar o fechamento temos:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/41052763886871)

Verbas geradas nos resultados:

Nesse exemplo a HE do dia 06/05/2024 não foi utilizada para compensar a falta do dia 04/01/2024 pois a HE ocorreu após a data de vencimento da falta  
Gerando assim as verbas de provento e desconto nos resultados  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/41052794351255)  
  
**Saiba Mais:**  
<https://tdn.totvs.com/pages/releaseview.action?pageId=852886609>  
[RH - Linha Protheus - PON - Como efetuar o fechamento do banco de horas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013670411-RH-Linha-Protheus-PON-Como-efetuar-o-fechamento-do-banco-de-horas)  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
