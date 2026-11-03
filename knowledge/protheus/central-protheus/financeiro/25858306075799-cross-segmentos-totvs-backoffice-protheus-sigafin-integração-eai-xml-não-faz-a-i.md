---
article_id: 25858306075799
category: Financeiro
content_hash: b56ce265925d3df8074432ecab2f7022d536a5c486438a0cc90d4bc14518f276
fetched_at: '2026-06-28T22:38:04.191924+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAFIN - Integração EAI XML
  - Não faz a integração, o que devemos coletar?
type: support-article
updated_at: '2024-08-23T15:05:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25858306075799-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAFIN-Integra%C3%A7%C3%A3o-EAI-XML-N%C3%A3o-faz-a-integra%C3%A7%C3%A3o-o-que-devemos-coletar
---

**[Remover as instruções entre colchetes e altere o tempo aproximado para leitura]**  
![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25858306012695) Tempo aproximado para leitura: **00:10:00 min** **Dúvida**Integração EAI via XML - Não faz a integração, o que devemos coletar para enviar para uma análise?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões]  
  
**Solução**

Faça o procedimento A, B e C**A -** Ative a chave FwTraceLog=1 no appserver.ini do ambiente do WS

**B -** Envie o exporta dados que possui as datas dos fontes

**C -** Envie todos os XML envolvidos no processo até o último que dá o erro

**A - Ative a chave FwTraceLog=1 no appserver.ini do ambiente do WS**

Na maioria das empresas tem mais de 1 appserver.ini, logo a empresa deve ativar a chave no ambiente do WS.

Segue um exemplo de um ambiente WS que geralmente irá possuir as TAG´s abaixo que realiza a comunicação EAI.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25858306015127)

Então neste appserver.ini que terá as chaves do WS, irá realizar o procedimento do link abaixo

[RM - Como habilitar e gerar o Fwtracelog no console.log do protheus?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026026133-RM-Como-habilitar-e-gerar-o-Fwtracelog-no-console-log-do-protheus)

Após isso, faça uma nova simulação e nos encaminhe os LOG´s **console.log, e console.bak** informando a data e hora da simulação.

**B - Envie o exporta dados que possui as datas dos fontes**

Segue o procedimento para  gerar o arquivo \*.csv com datas, e nos encaminhe  
[How To | Exportar Dados - TOTVS Backoffice (linha Protheus)](https://www.youtube.com/watch?v=j1Zfbuej99k)

**C - Envie todos os XML envolvidos no processo até o último que dá o erro**

Esse procedimento também poderá ser realizado no outro ERP que está se comunicando com o protheus, e que está enviando ou recebendo o XML exemplo: RM, Multiclubes e entre outros, porém vamos mostrar como se faz pelo protheus

Encaminhe todos os XML´s envolvidos no processo em sequência numerada  
**Exemplo:** Em um processo que tenho a inclusão do título, faço uma renegociação baixando um registro e criando um outro, e depois faço o pagamento. Neste exemplo possivelmente terei 4 XML´s envolvidos no processo, sendo:

1 XML de inclusão do registros

2 XML a baixa do título da renegociação (baixa **sem** movimentação bancária)

3 XML a Inclusão do novo título referente a renegociação

4 XML o pagamento do título que foi realizado a baixa (baixa **com** movimentação bancária)

1. Acesse o **Monitor EAI** através da opção **Schedule** do **Configurador**;  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25858306017431)  
2. Em **Visões**, acesse na opção **EAI**;  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25858306019735)  
3. Faça um filtro utilizando o campo **Data Transação** informando a data atual e aplique o filtro, dessa forma somente os registros da fila referente a esse dia serão exibidos;  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25858315912599)  
4. Posicione no XML que apresentou o erro, em nossa exemplo o erro é na transação que apresenta o erro **Start tag expected, '<' not found** e clique na lupa no canto superior esquerdo, em seguida escolha a opção **Visualizar mensagem de resposta**;  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25858306028183)

5. Salve o erro ou a informação com o XML, e nos encaminhe.  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25858315924887)

**Importante**O **Monitor EAI** que fica no SIGAADV / SIGAMDI, também pode ser acessado através do menu **Miscelânea** de qualquer modulo do **Protheus.**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25858315929751)
