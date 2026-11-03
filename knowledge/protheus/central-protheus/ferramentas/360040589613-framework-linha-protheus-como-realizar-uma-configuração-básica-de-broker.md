---
article_id: 360040589613
category: Ferramentas
content_hash: 71671edcf89a67dc1e08a32d6de26cbca35c1601f872d6f21baa62a3199e9723
fetched_at: '2026-06-28T22:42:18.006838+00:00'
product: protheus
section_id: 360000075448
source: central-protheus
title: Framework - Linha Protheus - Como realizar uma configuração básica de Broker
  ?
type: support-article
updated_at: '2025-12-09T14:27:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040589613-Framework-Linha-Protheus-Como-realizar-uma-configura%C3%A7%C3%A3o-b%C3%A1sica-de-Broker
---

**[Remover as instruções entre colchetes]**  
 **Dúvida**Como realizar uma configuração básica de Broker ?  
   
 **Ambiente**Protheus – Frame – A partir da versão 12  
   
**Solução**O Broker é utilizado e recomendado sempre que o cliente de problema de queda do smartclient por erro de sincronismo, ou seja, a transação de dados do smartclient com o appserver ficou desincronizada e por este motivo acabou caindo, o Broker consegue segura uma conexão em até 90 segundos para que o smartclient consigo sincronizar novamente a transição de dados evitando a queda da conexão, para uma configuração básica do Broker iremos seguir os passos abaixo:

1. Será necessário uma instalação apartada do appserver somente para uso do Broker, portanto podemos criar uma nova pasta appserver dentro do servidor apontando para o mesmo banco de dados do appserver original ;  
 2. Nesta nova instalação do appserver iremos editar o arquivo appserver.ini e apagar todas as informações do arquivo;  
 3. Adicionar as seguintes chaves ao arquivo appserver.ini:

[GENERAL]  
CONSOLELOG=1  
   
[BALANCE\_SMART\_CLIENT\_DESKTOP]  
   
; porta onde este broker server atende pedidos de conexão dos broker clients  
LOCAL\_SERVER\_PORT = 4000  
   
; hostname ou endereço ip, e porta TCP dos servidores Protheus ERP que serão destino  
; das conexões vindas dos broker clients  
REMOTE\_SERVER\_01 = 172.16.50.42 5000  
REMOTE\_SERVER\_02 = 172.16.50.42 5001  
REMOTE\_SERVER\_03 = 172.16.50.42 5002  
; etc  
; esta chave aceita letras e números para identificar servidores,  
; por exemplo REMOTE\_SERVER\_0A, REMOTE\_SERVER\_XY, etc, e as chaves  
; podem estar em qualquer ordem  
   
; nome do serviço, pode ser qualquer nome que não contenha espaços  
; só tem importância se o broker server for instalado como um serviço Window  
SERVICE\_NAME = XXX\_TOTVS\_BALANCE\_SC\_001  
   
; opcional, "display name" do serviço Windows  
SERVICE\_DISPLAY\_NAME = "BROKER SERVICE"

4.Deve-se configurar corretamente as portas e os ips conforme o servidor em questão para que o smartclient consiga acessar corretamente o appserver do Broker.

5.Adicionar a dll totvsbrocker a pasta smartclient (link no final do artigo)

6.Adicionar a linha de comando de execução do appserver -d -balance\_smart\_client\_desktop

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054094113)

Executar o smartclient em seguida e verificar se o broker esta subindo corretamente para execução.

7.Adicionar a chave brokerproxy=1 a tag de conexao do smartclient

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360053222814)

Links importantes:

<https://tdn.totvs.com/display/tec/Balanceamento+entre+Smart+Client+desktop+e+servidor+Protheus> (possui a dll totvsbroker para download)

<https://tdn.totvs.com/display/tec/Balanceamento+de+carga+com+broker>
