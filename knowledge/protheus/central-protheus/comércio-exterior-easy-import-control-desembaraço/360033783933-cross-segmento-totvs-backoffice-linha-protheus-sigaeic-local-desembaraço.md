---
article_id: 360033783933
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: d4b6183c2caebf8b61e433ce6a5a462b08f5db41b4a5b23f18ec88f4f1493c59
fetched_at: '2026-06-28T22:39:50.109155+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Local Desembaraço
type: support-article
updated_at: '2022-03-15T12:14:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033783933-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Local-Desembara%C3%A7o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Na transmissão de uma NFe de importação do SIGAEIC esta apresentando falha no schema na tag <xLocDesemb>, gostaria de saber onde devemos preencher esta informação no sistema afim de ajustar esta divergencia?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – *Easy Import Control* – A partir da versão 11.80  
  
**Solução**A informação deve ser preenchida no Desembaraço na aba Cadastrais.  
Ao informar o campo Local (W6\_LOCAL) será gatilhada a descrição do Local para o campo "Descr.Local"(W6\_LOCALN) e "UF Desembaraço" (W6\_UFDESEM) a sigla do estado na aba outros, para o campo "descrição do local" é gatilhado ao informar W6\_LOCAL. ![](https://totvssuporte.zendesk.com/attachments/token/YhUWFHyJkalQ4AN7LjvmJFteL/?name=inline-323809080.png)​

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042635594/mceclip0.png)

Local onde será a mercadoria desembaraçada.

Selecione através do F3 o cadastro de portos/aeroportos ou digite a sigla previamente cadastrada.  
Após informar o conteúdo do campo estorne a nota e gere novamente.
