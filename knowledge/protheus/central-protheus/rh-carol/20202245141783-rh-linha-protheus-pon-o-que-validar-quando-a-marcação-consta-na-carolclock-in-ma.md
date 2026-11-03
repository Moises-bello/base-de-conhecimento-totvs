---
article_id: 20202245141783
category: RH - Carol
content_hash: bed59cf1288f3c8a1acce506b426e7a03ff2cd5b85badebd5935fa951a24988d
fetched_at: '2026-06-28T22:44:56.601574+00:00'
product: protheus
section_id: 19035556880407
source: central-protheus
title: RH - Linha Protheus - PON - O que validar quando a marcação consta na Carol/Clock
  In mas não foi para o Protheus
type: support-article
updated_at: '2025-12-04T16:42:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20202245141783-RH-Linha-Protheus-PON-O-que-validar-quando-a-marca%C3%A7%C3%A3o-consta-na-Carol-Clock-In-mas-n%C3%A3o-foi-para-o-Protheus
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20202276690071) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
O que validar quando a marcação consta na Carol/Clock In mas não foi para o Protheus?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Nestes casos, é importante avaliarmos os passos abaixo:  
  
**1 -** Na **Carol**, ir em **Explore - Clock In Records:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20202245089815)  
  
 Avaliar se a marcação que não foi integrada no Protheus, consta nesta tela com **NSR gerado**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20202245091095)  
**Importante:** o Protheus só consegue consumir a marcação quando ela aparece nesta tela, ou seja, se ela aparece no Mapa de Marcações mas não consta aqui, o sistema não consegue localizar este dado. Para que a marcação apareça aqui, é necessário que ela tenha passado pelo processo de geração de NSR, validação de fraudes, e etc.  
  
Cabe ressaltar que esta opção só fica disponível no menu da Carol para um usuário que seja **Tenant Admin.**  
  
**2 -** É importante avaliar se o **cadastro do dispositivo** que o funcionário usou para fazer a marcação de Ponto está habilitado para **integração com o RH**, caso contrário, mesmo tendo NSR a marcação não seria integrada. Para validar este cadastro, retorne ao menu da Carol e clique em **Carol Apps - TOTVS RH Clock In Backoffice:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20202245093399)  
  
Clique no link gerado no **Web App:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20202276698007)  
  
No menu à esquerda, clique na opção **Dispositivos:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20202245094935)  
  
Faça a busca pelo **código do dispositivo** que o funcionário utilizou para fazer a marcação de Ponto, e veja se a opção **Integra RH está como SIM**, desta forma, garantimos que o Protheus conseguirá localizar o dado e consumir essa marcação:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20202245096215)  
  
**3 -** Com os dados da Carol corretos, podemos partir para as validações no Protheus.  
Inicialmente, verifique se a marcação realmente não consta na tabela **RR1** ou **MSA\_CONTROL\_MARCAC** (só recomendamos a gravação dos dados na MSA\_CONTROL\_MARCAC se você também utilizar a integração com o Suricato via WS).   
Em caso negativo, recomendamos que execute a rotina **PONAPI01** no menu do SIGAPON, pois esta rotina é a responsável por fazer a busca das marcações na Carol e gravação na tabela do Protheus:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20202245096983)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20202276701847)  
  
Neste exemplo, após a execução da rotina, a marcação de NSR 138058 não consta na RR1:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20202276702999)  
  
Neste caso, recomendamos que altere o conteúdo do parâmetro **MV\_APICLOB para .T.**  
Este parâmetro existe para que seja possível fazer uma varredura em todos os registros existentes nos Clock In Records da Carol com NSR, ou seja, se existir qualquer marcação/NSR nesta rotina da Carol que não exista ainda na tabela do Protheus, este dado será gravado independente da data ou número do NSR.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20202245110679)  
**IMPORTANTE:** o parâmetro onera a performance do Protheus, visto que será feita uma varredura completa em todos os registros da Carol, portanto, recomendamos o uso do parâmetro como .T. somente nos casos pontuais onde a marcação consta na Carol mas não foi gravada na tabela do Protheus. Após a execução da PONAPI01 e gravação do dado na tabela, retorne o conteúdo do parâmetro para .F.  
  
Após a alteração no conteúdo do parâmetro e uma nova execução da rotina PONAPI01, a marcação foi gravada com sucesso na tabela RR1:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20202245112087)  
  
Caso exista alguma marcação que mesmo com o MV\_APICLOB = .T. não seja gravada na tabela do Protheus, recomendamos então que o parâmetro **MV\_APICLOC** fique com conteúdo **.T.** também, para que durante a execução da PONAPI01, seja gravado um ***log*** **em TXT** dentro da pasta ***System***do ambiente, chamado **Integração Carol ou** ***Carol Integration*****:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20202245115159)  
  
Neste log, é possível fazer uma busca pelo código do dispositivo + NSR para verificar se a Carol enviou o dado para o Protheus ou não:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20202276715927)  
  
Caso o NSR/dispositivo **não apareça** neste *log*, será necessário o suporte por parte do time de Carol/Clock In, para avaliarem diretamente no ambiente se existe alguma inconsistência.  
  
O **MV\_APICLOC** com conteúdo **.T.** também onera a performance do Protheus, portanto, recomendamos que após a geração do log para buscar as informações necessárias, o conteúdo dele fique como .F.  
  
**4 -** Com a marcação na tabela do Protheus, para que seja possível executar a Leitura dos dados é necessário que seja feito o **cadastro de um relógio** que integre com a Carol, conforme [esta documentação.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052083354-RH-Linha-Protheus-PON-Como-cadastrar-um-rel%C3%B3gio-para-integra%C3%A7%C3%A3o-do-Clock-In-com-o-Ponto-Eletr%C3%B4nico)  
  
Com todos os passos conferidos, basta executar a rotina de **Leitura/Apontamento** no SIGAPON.  
  
**Saiba mais**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[Integração Protheus x Carol](https://tdn.totvs.com/pages/releaseview.action?pageId=515294516)
