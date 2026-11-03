---
article_id: 4413305638167
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: bcf3c209a4c721eaefa879b49e9f615a4fc82be007e321262948d823b556d48e
fetched_at: '2026-06-28T22:38:43.804884+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) – SIGAFAT – Conceito dos perguntes
  iniciais de parâmetro na rotina MATA521A Exclusão de Documento de Saída
type: support-article
updated_at: '2022-07-07T11:06:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413305638167-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFAT-Conceito-dos-perguntes-iniciais-de-par%C3%A2metro-na-rotina-MATA521A-Exclus%C3%A3o-de-Documento-de-Sa%C3%ADda
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:25 min**

**Dúvida**

Qual é o conceito e funcionamento dos perguntes iniciais de parâmetro na rotina MATA521A Exclusão de Documento de Saída?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Faturamento - Todas as versões.  
  
**Solução**

Muitas vezes a causa da não visualização provem da configuração inicial que é mostrada a partir da janela de parâmetros que aparece ao entrar na rotina. Cheque os perguntes novamente de acordo com a sua necessidade.

Ao entrar na rotina cheque e averigue a configuração dos perguntes da rotina:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7249284062487/mceclip0.png)

**Modelo de Interface ?**

Como virá o sistema de seleção pelo navegador.

* **Selecao** = Você só consegue excluir um por vez pelo modo ser de posicionar no item pelo navegador.
* **Marcacao** = Você consegue preencher a caixa “dar um flag”, podendo selecionar quantos documentos de saída forem necessários.

**Selecionar itens ?**

Só tem efeito se a opção acima for Marcacao.

* **Sim** = Os documentos que se encaixarem nos perguntes virão marcados.
* **Não** = Os documentos não virão marcados ao entrar na rotina.

**Dt.Emissao de ?**

Só serão mostrados documentos de saída com a data de emissão a partir da data colocada nesse pergunte.

**Dt.Emissao ate ?**

Só serão mostrados documentos de saída com a data de emissão até a data colocada nesse pergunte.

**Serie de ?**

Só serão mostrados documentos de saída com a série a partir da sequência colocada nesse pergunte.

**Serie ate ?**

Só serão mostrados documentos de saída com a série até a sequência colocada nesse pergunte.

**Documento de ?**

Só serão mostrados documentos a partir da sequência colocada nesse pergunte.

**Documento ate ?**

Só serão mostrados documentos até a sequência colocada nesse pergunte.

**Maneira 1: Para que os documentos todos venham marcados:**

* Modelo de Interface ? = Marcacao
* Selecionar itens ? = Sim

**Maneira 2: Para que não venham todos marcados:**

* Modelo de Interface ? = Marcacao
* Selecionar itens ? = Nao

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413298475543/mceclip0.png)

Desta forma, ao dar OK na seleção dos parâmetros, as notas virão desmarcadas:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413291818519/mceclip1.png)

**Maneira 3: Para que não venha no modelo de marcação:**

* Modelo de Interface ? = Selecao
* Selecionar itens ? = Sim/Nao (tanto faz, desconsiderar)

Saiba mais sobre exclusão da nota:

**[MP - FAT - Falta de checkbox no browser de exclusão da nota](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044746454-MP-FAT-Falta-de-checkbox-no-browse-da-exclus%C3%A3o-da-nota)**

**[MP - FAT - Como selecionar várias notas para exclusão na rotina "Exclusão de Documentos de Saída](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058049493-MP-FAT-Como-selecionar-v%C3%A1rias-notas-para-exclus%C3%A3o-na-rotina-Exclus%C3%A3o-de-Documentos-de-Sa%C3%ADda)**

**[MP - FAT - Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Processo de Exclusão da nota Fiscal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009602001-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Processo-de-Exclus%C3%A3o-da-nota-Fiscal)**

**[MP - FAT -](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009602001-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Processo-de-Exclus%C3%A3o-da-nota-Fiscal) [Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - Validação de exclusão do Documento de Saída com uso do JOB FATJOBNFE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115004391207-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Valida%C3%A7%C3%A3o-de-exclus%C3%A3o-do-Documento-de-Sa%C3%ADda-com-uso-do-JOB-FATJOBNFE)**
