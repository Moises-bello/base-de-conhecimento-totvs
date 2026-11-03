---
article_id: 6152087600023
category: Rescisão
content_hash: 4f1c71844b819c77a056cb3a63f707f845f3d93f478134d6b6fb984590b299c0
fetched_at: '2026-06-28T22:46:54.354407+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: RH - RM - FOP - Erro ao realizar transferência de funcionário "FKPFEMPRT_PCODEMPRT"
type: support-article
updated_at: '2024-06-17T15:12:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6152087600023-RH-RM-FOP-Erro-ao-realizar-transfer%C3%AAncia-de-funcion%C3%A1rio-FKPFEMPRT-PCODEMPRT
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24231643780119) Tempo aproximado para leitura: **00:01:36 min****Ocorrência**Ao realizar transferência de funcionário ocorre o erro:

The INSERT statement conflicted with the FOREIGN KEY constraint "FKPFEMPRT\_PCODEMPRT". The conflict occurred in database "dbo.PCODEMPRT".

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**O erro ocorre pois os códigos de empréstimo na empresa de destino não são os mesmos da empresa de origem.   
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
  
**01.** Acesse na coligada de origem da transferência, **Administração de Pessoal - Cadastros Globais - Tabelas Dinâmicas;**

![](https://totvssuporte.zendesk.com/attachments/token/PJJVXMwLfUtBqZU13WuyDQIgc/?name=inline-149069058.png)  
  
**02.** Selecione **Sistema**: **Folha de Pagamento** e em **Procurar por**: selecione **Código** e digite **INT30** e clique em ocultar registros para buscar;

![](https://totvssuporte.zendesk.com/attachments/token/eIBgrqOtAZGHMl8FsKIcjErys/?name=inline1918466224.png)  
  
**03.**  Após acesse a tabela e a aba; **Item da tabela dinâmica**;

![](https://totvssuporte.zendesk.com/attachments/token/kPkK0eZHuEI4lxEuJjTCDgg6r/?name=inline1692733089.png)  
  
**04.** Os códigos cadastrados devem ser cadastrados iguais na coligada de destino, exemplo, se na coligada origem tiver o código de empréstimo 30 empréstimo especial, na coligada destino também precisa ter o mesmo código cadastrado​​​.  
  
Possui também a opção de copiar toda a tabela e enviar todos os códigos cadastrados para a coligada de destino, para isso; **Selecione todos os códigos e em Processos - Copiar Tabelas Dinâmicas entre Coligadas;**  
![](https://totvssuporte.zendesk.com/attachments/token/nJLeMtzECZnlCnnOALzMQZdlX/?name=inline-1981510563.png)
