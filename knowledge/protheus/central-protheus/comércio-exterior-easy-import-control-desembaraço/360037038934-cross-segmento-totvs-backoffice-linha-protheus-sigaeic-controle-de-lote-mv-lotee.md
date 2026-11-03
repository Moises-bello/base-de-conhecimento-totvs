---
article_id: 360037038934
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: fb5363590150fb71a90c28e19a104a909e2a7ec129d9dd053478d7734e5829d2
fetched_at: '2026-06-28T22:39:49.832331+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus  - SIGAEIC - Controle de lote
  MV_LOTEEIC
type: support-article
updated_at: '2021-08-18T19:17:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037038934-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Controle-de-lote-MV-LOTEEIC
---

**Dúvida**Como habilitar a inclusão de lote no Processo de Importação?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.  
  
**Solução**Pré-Requisitos:  
  
Os parâmetros devem estar habilitados:  
- MV\_RASTRO  
- MV\_LOTEEIC  
- MV\_EASY

Cadastro do produto deve ter o campo B1\_RASTRO como L - Lote.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048468094/mceclip0.png)

1. Acesse a rotina Desembaraço \ Manutenção (EICDI502)  
2. Posicione no processe e selecione Alterar  
3. Selecione Outras Ações\Lotes  
4. Informe o Nro do Lote e validade (caso utilize o mesmo)  
5. Posicione no item e selecione o mesmo, será apresentada a tela de Qtde.Lote, para informar a quantidade de produto para o lote informado, após selecione confirmar.  
6. Selecione incluir para informar novo lote

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049359573/mceclip1.png)

7. Realize o mesmo procedimento para os demais itens, ao preencher o último item selecione Salvar

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049359833/mceclip2.png)

8. Selecione o Salvar , e os lotes serão gravados no processo.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049359913/mceclip3.png)

**Observação:** Ao gerar a nota para o SIGACOM será gravado os campos D1\_LOTECTL e D1\_DTVALID (caso preenchido). Favor também confirmar se os campos estão como USADO para o módulo SIGAEIC.
