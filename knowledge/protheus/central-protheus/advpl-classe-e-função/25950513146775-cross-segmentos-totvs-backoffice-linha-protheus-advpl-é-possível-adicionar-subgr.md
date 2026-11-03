---
article_id: 25950513146775
category: ADVPL - Classe e Função
content_hash: bb08c7265a222501addf6b9bb2e7b889387e1211fc45020e630690e247d001fa
fetched_at: '2026-06-28T22:40:21.591373+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - É possível adicionar
  subgrupo em outras ações na enchoicebar?
type: support-article
updated_at: '2024-08-28T19:04:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25950513146775-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-%C3%89-poss%C3%ADvel-adicionar-subgrupo-em-outras-a%C3%A7%C3%B5es-na-enchoicebar
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25950513126423) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**

É permitido adicionar subgrupo em outras ações na enchoicebar?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Todas as versões  
  
**Solução**

Sim, é possível adicionar subitens, subgrupos no botão Outras Ações da Enchoicebar.

**Exemplo**

Criar uma nova posição (posição 7) no array aButtons utilizado na criação da EnchoiceBar, essa posição deverá ser opcional e suportar um array bidimensional que conterá as definições para criação de cada submenu. Este array deverá seguir o mesmo modelo do menu pai.

```
Add(aButtons,{/*<Resource (Depreciado)>*/,/*<Action>*/, "MenuPai", "MenuPai",,,{{/*<Resource (Depreciado)>*/,{|| Alert("Filho1")}, "MenuFilho1", "MenuFilho1" },{/*<Resource (Depreciado)>*/,{|| Alert('Filho2')}, "MenuFilho2", "MenuFilho2" } }} )
```

O método AddUserBtn da classe FWFormBar também deverá aceitar um array com submenu, este será o 10º parâmetro do método.

```
oFormBar:AddUserBtn( /*<resource>(depreciado)*/, "Menu1", /*<action>*/,,,.F.,,,,{{"Menu11", {||alert(11)},,,.F.}, {"Menu12", {||alert(12)},,,.F.}})
```

**Saiba mais:**

[SubGrupo enchoicebar](https://tdn.totvs.com/display/public/framework/ER_PCREQ-7464_Subgrupo_em_Outras_Acoes_da_EnchoiceBar)
