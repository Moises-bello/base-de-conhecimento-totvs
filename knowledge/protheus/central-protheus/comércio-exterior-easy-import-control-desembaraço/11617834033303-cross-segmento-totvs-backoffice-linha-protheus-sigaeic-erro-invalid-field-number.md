---
article_id: 11617834033303
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: abb8d5008bc0f0f1f160fc6364d2c12aa1b69daa06df96a2cf1789f2056f82e7
fetched_at: '2026-06-28T22:39:50.057271+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Erro invalid
  Field number : 0 - statement ignored (Last FieldPos that returned 0 received parameter:
  AUTIMPIP).'
type: support-article
updated_at: '2023-01-12T13:55:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11617834033303-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Erro-invalid-Field-number-0-statement-ignored-Last-FieldPos-that-returned-0-received-parameter-AUTIMPIP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura:**02:00 min** **Dúvida**Ao incluir/gerar a pre-nota de importação na rotina **EICDI154**, está retornando o erro:  
**"invalid Field number : 0 - statement ignored (Last FieldPos that returned 0 received parameter: AUTIMPIP)".**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  –*Easy Import Control*– a partir da versão12.1.27  
  
**Solução** O erro é em virtude da falta de conexão com o *TelNet* e/ou com a impressora de rede (**SIGAACD**).

Será necessário ter um impressora física instalada ou compartilhada na máquina e fazer a configuração por *NET USE* da impressora para impressão em terminais;

Outra opção é configurar o campo "**Ident.Prod."** (**A2\_IMPIP**) para **"3-Não Imprime"** ou para **"4-Documento de Entrada"**, bem como alterar o conteúdo do parâmetro **MV\_IMPIP** para **3** ou **4**. É necessário alterar ambos.  
Assim será possível prosseguir com a geração da pré-nota de importação.

**Saiba mais:**

[Guia do Módulo Automação em Coleta de Dados - SIGAACD](https://centraldeatendimento.totvs.com/hc/pt-br/article_attachments/1500017323122/ACD_Guia_Pratico_-_Automa__o_e_Coleta_de_Dados.pdf,)
