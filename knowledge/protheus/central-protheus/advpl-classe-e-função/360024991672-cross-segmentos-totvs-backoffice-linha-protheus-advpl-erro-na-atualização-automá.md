---
article_id: 360024991672
category: ADVPL - Classe e Função
content_hash: a7f33457dc1c5ee2c5130375a6186a7adaf977650fbb7678910ebaa18b816123
fetched_at: '2026-06-28T22:40:18.346902+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: 'Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - Erro na atualização
  automática do TDS 11.3 '
type: support-article
updated_at: '2022-01-06T20:15:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024991672-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Erro-na-atualiza%C3%A7%C3%A3o-autom%C3%A1tica-do-TDS-11-3
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min****Ocorrência**Ao acessar " Verificar Atualizações" no TDS 11.3 gera o erro

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023730952/mceclip0.png)  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 12  
  
**Causa**Existe um link que não está mais disponível **<http://download.eclipse.org/technology/babel/update-site/R0.12.1/luna>**  
  
**Solução**

Acesse "Ajuda"-> "Instalar Novo Programa" -> "Sites de Programas Disponíveis"

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023768791/mceclip1.png)**

Documentação <http://tdn.totvs.com/display/tec/Perguntas+e+Respostas+TDS+11.3> o item 6.

 6. No repository found at <http://download.eclipse.org/technology/babel/update-site/R0.12.1/luna>

Artigo original de [Leo Watanabe](http://tdn.totvs.com/display/~leo.watanabe), migrado da comunidade "TOTVS Developer Studio" (Fluig).

Se ao executarem uma atualização no TDS 11.3 se depararem com o erro:

No repository found at <http://download.eclipse.org/technology/babel/update-site/R0.12.1/luna>.

é porque esta URL foi alterada pelo Eclipse e movida para <http://archive.eclipse.org/technology/babel/update-site/R0.12.1/luna>

Porém para minimizar futuros problemas de referência a UpdateSite Externos foi criada uma URL que substituirá a necessidade de adicionar, alterar e remover estas URL externas.

Abra a lista de "Sites de Programas Disponíveis" clicando em: "Janela > Preferências..." em seguida selecione "Instalar/Atualizar > Sites de Programas Disponíveis".

Remova o site "<http://download.eclipse.org/technology/babel/update-site/R0.12.1/luna>" para que o erro inicial deixe de ser apresentado.

Nesta lista de "Sites de Programas Disponíveis", para o TDS 11.3, serão necessárias apenas três itens:

* Eclipse Luna repository (<http://download.eclipse.org/releases/luna>)
* TOTVS | Developer Studio 11.3 (<http://ds.totvs.com/updates/tds113/>)
* TOTVS | Developer Studio 11.3 External Updatesite Reference (<http://ds.totvs.com/updates/tds113ext/>)

Os dois primeiros já devem existir, então adicione apenas o último, caso ainda não o tenha feito, <http://ds.totvs.com/updates/tds113ext/>

Com isso você não deverá ter mais problemas para adicionar, atualizar ou remover sites da lista de "Sites de Programas Disponíveis".

![](https://lh3.googleusercontent.com/-bbI2_CGH-uA/XIlZbH0efLI/AAAAAAAAAN8/JZIJ1U_A86U6YEevfoFkFeh3tXGwe6nDQCK8BGAs/s0/2019-03-13.png)

**Saiba Mais****[Perguntas e Respostas TDS 11.3](http://tdn.totvs.com/display/tec/Perguntas+e+Respostas+TDS+11.3)**
