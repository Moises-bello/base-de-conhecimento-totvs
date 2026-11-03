---
article_id: 11077842459543
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: caec1b5db55886bd1889e20dd571f486eb0a83e19aa7dcc00045660c89bcbbc6
fetched_at: '2026-06-28T22:37:22.968061+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Help OBRIGAT2 / ENTIDOBRIG
  de Centro de Custo ou outra Entidade Contábil Obrigatório não Preenchido ao tentar
  gerar o Titulo no Encerramento da Medição
type: support-article
updated_at: '2026-05-11T13:44:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11077842459543-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Help-OBRIGAT2-ENTIDOBRIG-de-Centro-de-Custo-ou-outra-Entidade-Cont%C3%A1bil-Obrigat%C3%B3rio-n%C3%A3o-Preenchido-ao-tentar-gerar-o-Titulo-no-Encerramento-da-Medi%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39442226725271) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**

Ao encerrar uma medição ocorre o Help OBRIGAT2 ou ENTIDOBRIG de campo de Centro de Custo ou outra Entidade Contábil Obrigatório não Preenchido ao tentar gerar o Titulo no Encerramento da Medição

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11078075296151)      ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39442240383383)

**AJUDA:OBRIGAT2**  
Um ou alguns campos obrigatórios não foram preenchidos no objeto Grid.  
Lançamentos  
Campo: Classe de Valor  
Linha: 1

Ou

**AJUDA:ENTIDOBRIG**

Obrigatório o preenchimento da seguinte entidade contábil:

C Custo

Falha na Gravação automática do Título!

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contrato - Todas as versões

**Solução**

A mensagem em questão está relacionada a no ambiente em questão haver um campo na tabela de títulos que está sendo gerado, que está marcado como "Obrigatório" em seu cadastro no Configurador e o mesmo não estar sendo preenchido.

No caso, pode-se retirar a obrigatoriedade do campo em questão da tabela (Onde na mensagem aparece a descrição/nome do campo, na imagem acima destacado em vermelho)

Pelo padrão do sistema, os campos de Entidades Contábeis dos títulos não são obrigatórios, e no encerramento de uma medição que gera títulos a rotina de medição de fato não leva informação, ou preenche a informação de entidades contábeis no título gerado, bem como para demais campos que não são obrigatórios por padrão.

Caso se deseje preencher o campo no encerramento da medição que não é obrigatório por padrão, este deve ser realizado através de customização, conforme informações do artigo abaixo:

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Centro de Custo e outras Entidades Contábeis não são levadas para o Título gerado pela Medição - CNTA121](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7753942435991-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Centro-de-Custo-e-outras-Entidades-Cont%C3%A1beis-n%C3%A3o-s%C3%A3o-levadas-para-o-T%C3%ADtulo-gerado-pela-Medi%C3%A7%C3%A3o-CNTA121?source=search)

***Saiba Mais:***

* [Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Centro de Custo e outras Entidades Contábeis não são levadas para o Título gerado pela Medição - CNTA121](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7753942435991-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Centro-de-Custo-e-outras-Entidades-Cont%C3%A1beis-n%C3%A3o-s%C3%A3o-levadas-para-o-T%C3%ADtulo-gerado-pela-Medi%C3%A7%C3%A3o-CNTA121?source=search)
* [Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
