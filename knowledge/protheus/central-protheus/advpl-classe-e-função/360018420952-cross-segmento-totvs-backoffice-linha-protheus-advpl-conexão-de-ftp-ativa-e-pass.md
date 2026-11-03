---
article_id: 360018420952
category: ADVPL - Classe e Função
content_hash: c500704a2c3081cbb8d3a4016273539d369b6af0d6519cb2ed5553eb855d32de
fetched_at: '2026-06-28T22:40:15.632034+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Conexão de ftp ativa
  e passiva
type: support-article
updated_at: '2022-01-05T13:59:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018420952-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Conex%C3%A3o-de-ftp-ativa-e-passiva
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**O que é e como realizar uma conexão FTP (*File Transfer Protocol*) ativa ou passiva utilizando a linguagem ADVPL (*Advanced Protheus Language*)?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.8  
  
**Solução**O que é uma conexão FTP ATIVA ou PASSIVA?  
Uma conexão pelo protocolo FTP pode ser realizada em dois estados: PASSIVO e ATIVO.  
No modo ativo, o cliente requisita o servidor usando uma porta aleatória (por exemplo: a porta 1026), endereçando o pacote à porta 21 do servidor. O servidor imediatamente contata o cliente de volta, usando a porta seguinte (do lado cliente) para enviar dados. Assim sendo, se o cliente usou a porta 1026 para abrir uma conexão, então o servidor enviará os dados na porta 1027.   
A questão principal é que o modo ativo não funciona quando o cliente acessa através de uma conexão compartilhada, pois ao tentar responder, o servidor cairia na porta 1027 do *gateway* da rede, sem conseguir chegar ao cliente.  
No modo passivo, o cliente também abre a conexão contatando a porta 21 do servidor, entretanto, ao invés de iniciar a conexão imediatamente, o servidor responde avisando que o cliente pode contatá-lo numa segunda porta, escolhida aleatoriamente (a 2026, por exemplo). Então, o cliente inicia uma nova conexão na porta especificada e o servidor responde enviando os dados.  
A vantagem da conexão ativa é a segurança, pois uma vez feita e atendida a requisição, a conexão com o serviço FTP é encerrada, contudo torna-se limitada para transferência de diversos arquivos. Já uma conexão passiva, ao manter a comunicação com o serviço, pode-se solicitar diversos arquivos e redirecioná-los para diversas outras portas (lado cliente), aumentando a quantidade de arquivos por conexão, todavia por este processo não se há um controle primário da quantidade de solicitações.  
  
Como realizar a conexão utilizando a linguagem ADVPL  
Para controlar se a requisição FTP que a ser realizada será ativa ou passiva, utilize a classe TFTPClient() em conjunto a propriedade bFirewallMode.  
  
**Saiba mais**  
[Classe TFTPCLIENT - Tecnologia](http://tdn.totvs.com/display/tec/Classe+TFtpClient)
