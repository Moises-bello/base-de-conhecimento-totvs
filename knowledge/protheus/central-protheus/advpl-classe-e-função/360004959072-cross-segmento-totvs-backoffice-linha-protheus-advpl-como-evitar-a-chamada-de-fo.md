---
article_id: 360004959072
category: ADVPL - Classe e Função
content_hash: c428dc7cbd5293861e27ed08868ea28fd6b1993b42a5980a6db87a89f16178a3
fetched_at: '2026-06-28T22:40:15.520009+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Como evitar a chamada
  de fontes não encontrados durante o Debug
type: support-article
updated_at: '2022-01-04T19:59:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004959072-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Como-evitar-a-chamada-de-fontes-n%C3%A3o-encontrados-durante-o-Debug
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**  
Como evitar a chamada de fontes que não possuo ou não tenho acesso durante o debug?Quando ativamos o debug para analisar os fontes em algumas linhas solicita estes arquivos

FWBROWSE.PR?  
FWMBROWSE.PR?  
FWPREEXECUTE.PR?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**No TOTVS | Developer Studio, para habilitar este recurso você deve proceder da seguinte maneira:

* Acesse o menu **Window**
* Em seguida, o item **Preferences**
* Na janela que será aberta, localize o item **Configurações do Servidor**(*pode-se utilizar a busca como apoio*)
* Por fim, basta marcar a opção **Ignorar arquivos não encontrados no Debug**

Com esta opção habilitada você não terá problemas com a chamada de funções, métodos e classes que estejam em fontes aos quais vocês não possui e/ou não tem acesso.  
Abaixo uma imagem exibindo a opção supracitada:

<http://tdn.totvs.com/display/tec/Perguntas+e+respostas>

**Versão 11.2**

![](https://totvssuporte.zendesk.com/attachments/token/Xh5tDRnZ5Y1jUx6pnl2EfZaUU/?name=inline-1928838443.png)

**Versão 11.3**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360012774651/mceclip2.png)
