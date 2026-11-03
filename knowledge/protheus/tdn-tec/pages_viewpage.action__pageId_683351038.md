---
content_hash: 639cd7da80c38967d3a0e1ebf34cc9710681520d6d9d0f224e613f0588a87601
fetched_at: '2026-07-02T19:24:27.817768+00:00'
page_id: '683351038'
product: protheus
source: tdn-tec
title: Informações sobre a sessão com o servidor balanceado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=683351038
version: 2
---

**A partir da versão 20.3.0.9**.

Informações sobre a sessão com o servidor balanceado

A partir da versão 20.3.0.9 o Broker HTTP retorna mais informações sobre a sessão com o servidor destino do balanceamento.  
Também retorna mais informações quando acontece uma situação de erro no acesso ao servidor balanceado.

Estas informações adicionais ajudam a encontrar no log do broker informações específicas sobre o servidor acessado pelo browser.

Informações sobre situações de erro são mostradas na própria tela do browser.  
Normalmente ocorre que a tela com as informações de erro pode ser reescrita, e as informações serem perdidas.  
Para contornar essa situação as informações de erro são também retornadas em um novo cookie TOTVS\_PROXY\_SH\_LAST\_ERROR.

Informação sobre sessão com o servidor escolhido para balanceamento são retornadas no novo cookie TOTVS\_PROXY\_SH\_SESSION.  
Por motivo de compatibilidade esta informação só é enviada ao browser se a chave USING\_SESSION\_COOKIES estiver habilitada na configuração do broker.

Normalmente o usuário final não sabe como consultar os valores do cookie. Por isso, para essa consulta o usuário final deve ser orientado por uma pessoa técnica (analista).  
Por exemplo, no navegador Firefox a sequência de consulta é: tecla F12, aba Armazenamento, menu Cookies, linha correspondente à URL utilizada.

Exemplo do cookie TOTVS\_PROXY\_SH\_SESSION:  
  client: 192.168.0.37:62344 | server: 192.168.0.40:10000 | ctx:043 | date: 28/04/2022 | time: 13:14:30

Exemplo do cookie TOTVS\_PROXY\_SH\_LAST\_ERROR:  
  [ 28/04/2022, 13:15:29, (no server available for client to connect, client endpoint 127.0.0.1:63313, broker context: ctx:063)

Com estas informações é possível consultar o log do broker para conseguir informações adicionais sobre alguma ocorrência de erro com o usuário final.
