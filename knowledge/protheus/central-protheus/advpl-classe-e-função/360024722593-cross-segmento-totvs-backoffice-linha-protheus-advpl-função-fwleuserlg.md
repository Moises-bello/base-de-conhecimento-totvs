---
article_id: 360024722593
category: ADVPL - Classe e Função
content_hash: 578b7ced76d501df3d3fc04147936ad4d0a6ad21e2b361d306ea75cf5f888fd3
fetched_at: '2026-06-28T22:40:16.754658+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Função FWLeUserlg
type: support-article
updated_at: '2026-05-06T12:43:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024722593-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Fun%C3%A7%C3%A3o-FWLeUserlg
---

**Dúvida**Gostaria de um exemplo para utilizar a função **FWLeUserlg.**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Exemplo de utilização.  
Habilite os campos USERLGI e USERLGA na Tabela utilizando os campos reservados:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360038672773/mceclip1.png)

Escolha os tipo de "*Log*"

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360037836354/mceclip2.png)

Veja que foi incluído na Tabela

![fwleuserlg.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360038671553/fwleuserlg.png)

Coloque a função no campo ou crie uma *user function*

```
Exemplo FWLeUserlg("A1_USERLGI", 1)
```

![fwleuserlg2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360038671613/fwleuserlg2.png)

Visualize a informação no campo

![fwleuserlg3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360038671593/fwleuserlg3.png)

**Nota:** A função **FWLeUserlg**  não retorna informações do usuário logado e sim informações já gravadas em um campo. Ao incluir esta função em um inicializador padrão de uma rotina, caso a rotina seja aberta para inclusão nenhum valor será mostrado, uma vez que não existe valor já carregado no campo.  
Caso seja aberto em uma alteração, o valor pode ser apresentado mas ele vai depender do posicionamento do *browser*. Caso a tabela na qual a função busque a informação não esteja posicionada corretamente pode ser apresentado um registro errôneo ou nenhum registro.  
  
**Observação:** A função **FWLeUserig** deve ser utilizada apenas em campos "virtuais".  
  
**Saiba Mais**[FWLeUserlg - Informações do USERLGIUSERLGA](http://tdn.totvs.com/pages/viewpage.action?pageId=6814934)  
[Rotinas de Logs e Auditoria](http://tdn.totvs.com/display/public/PROT/Rotinas+de+Logs+e+Auditoria)
