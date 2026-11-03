---
article_id: 4418344329879
category: Meu RH - Login
content_hash: 82d7233ad10d130ce9bc0b802276d0458e655c051115b6b053aac1efd6f07966
fetched_at: '2026-06-28T22:47:27.298995+00:00'
product: rm
section_id: 37725850167319
source: central-rm
title: RH - RM - Meu RH -  Não havia um ponto de extremidade em escuta SOAP incorreta
type: support-article
updated_at: '2026-01-16T15:20:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418344329879-RH-RM-Meu-RH-N%C3%A3o-havia-um-ponto-de-extremidade-em-escuta-SOAP-incorreta
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22322230103447) Tempo aproximado para leitura: **00:04:27 min**  
  
**Ocorrência**  
Ao acessar o Meu RH é apresentada o erro "Não havia um ponto de extremidade em escuta".

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - Todas as versões  
  
**Causa**  
A falha apresentada pode ocorrer quando em um ambiente 3 ou N camadas existem versões diferentes instaladas. Por exemplo, servidor de aplicação executando a versão 12.1.2402.151 e máquina *client* executando a versão 12.1.2402.130, ao acessar o sistema na máquina *client* a inconsistência será apresentada.

A recomendação é que tanto a Biblioteca RM quanto o RM Portal estejam utilizando a mesma versão, por exemplo:

BibliotecaRM (Patch) 12.1.2402.151.exe  
TOTVSRMPortal (Patch) 12.1.2402.151.exe

Poderá ocorrer também quando simplesmente há uma falha na comunicação entre o IIS e o Host do RM.

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

**Caso esteja em versões diferentes o RM e o RM Portal**

1. Verifique qual máquina está com a versão diferente;
2. Desinstale ou atualize as versões no ambiente 3 ou N camadas de modo que seja utilizada a mesma versão;
3. Após a atualização do Servidor de Aplicação, *Job* e *Client* corretamente, este erro não mais será apresentado.
4. Considerando o ambiente de servidor do Meu RH, verifique se a versão da Biblioteca RM e RM Portal estão idênticas. Caso estejam divergentes, atualize a versão de ambos.

**Caso RM e RM Portal estejam na mesma versão**

Poderá recriar o *broker* conforme orientações abaixo e reiniciar o IIS utilizando o comando **iisreset** no CMD (Prompt de comando).  
[RM - Frame - Reinstalar Host](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115010413428-RM-Frame-Reinstalar-Host)

1. Clique desinstalar o serviço:   
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/22322390988951)
2. Na pasta RM.Net após parar os serviços de host, remova o arquivo \_broker.dat da pasta e então inicie novamente os serviços de hosts.

**Importante**  
Poderá apresentar também o erro "O formatador gerou uma exceção ao tentar desserializar a mensagem:  
Erro ao tentar desserializar o parâmetro" ou "*The formatter threw an exception while trying to deserialize the message: There was an error while trying to deserialize parameter*.", os procedimentos a serem adotados são os mesmos descritos neste documento.
