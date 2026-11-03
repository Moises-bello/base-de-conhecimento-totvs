---
article_id: 360026101932
category: ADVPL - Classe e Função
content_hash: 2dc2f06b3cf5dfdb0ad3e3fb5926d4937c8c463a6ccdad0f50734e4bb856bd47
fetched_at: '2026-06-28T22:40:15.428473+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Classe MsNewGetDados
type: support-article
updated_at: '2024-02-19T19:41:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026101932-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Classe-MsNewGetDados
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min****Dúvida**A Classe "MsNewGetDados" esta obsoleto, gostaria de saber algum substituto em MVC?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Solução**De Fato a Classe **[MsNewGetDados](http://tdn.totvs.com/display/PROT/MsNewGetDados)** está depreciada, e por conta disso, não recebe mais atualizações e recomendamos a utilização do MVC Protheus.  
Neste caso utiliza-se um componente de grid na interface (*AddGrid*)  
Adicionamos na interface (*View*) um controle do tipo grid (antiga *GetDados*).

Exemplo do método AddGrid.

```
oView:AddGrid( 'VIEW_ZA2', oStruZA2, 'ZA2DETAIL' )
```

Para mais Detalhes segue manual para desenvolvimento MVC.  
  
**Saiba mais**  
[AdvPl utilizando MVC](http://tdn.totvs.com/display/public/PROT/AdvPl+utilizando+MVC)[MVC (Model View Controller)](http://tdn.totvs.com/pages/viewpage.action?pageId=28574107)  
[Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Criação de gatilho](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021876611)
