---
article_id: 360024915551
category: Escrita Fiscal - Error.log
content_hash: 4258e630b4fe6bbe6f7fd329e8db375b849c7bc1a65608da61974e3c86dd5648
fetched_at: '2026-06-28T22:39:32.860089+00:00'
product: protheus
section_id: 1500001549782
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Nome de coluna 'CE5_TPLANC'
  inválido.
type: support-article
updated_at: '2021-07-08T13:07:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024915551-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Nome-de-coluna-CE5-TPLANC-inv%C3%A1lido
---

**Dúvida**

Ao gerar apuração de ICMS (MATA953) está ocorrendo a seguinte mensagem :

    Nome de coluna 'CE5\_TPLANC' inválido.

    Invalid column name 'CE5\_TPLANC'.

**Ambiente**

Protheus – Livros Fiscais– A partir da versão 12.1.17  
  
**Solução**

Para solucionar essa dúvida, realize os seguintes passos:

1. Fazer backup da sua CE5;

2. Deletar registros que o X3\_ARQUIVO=CE5

3. Appendar arquivo que se encontra no arquivo em anexo;

4. Entrar no sistema, abrir a**rotina  FISA034,** para criação da CE5;

5. Appendar sua tabela CE5 que fez backup;

6. Refazer processo.

 Arquivo em anexo:
