---
article_id: 360021556152
category: Contabilidade Gerencial - Contabilização txt
content_hash: 4269956201d56e1f91cc49940cbddd1a20ffbeb61c5008b12b543407a0d334ba
fetched_at: '2026-06-28T22:40:55.436669+00:00'
product: protheus
section_id: 1500001537521
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB  :CTBA500 - Contabilização
  TXT com mais de uma Filial
type: support-article
updated_at: '2024-02-16T19:30:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021556152-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA500-Contabiliza%C3%A7%C3%A3o-TXT-com-mais-de-uma-Filial
---

**Dúvida**

É possível realizar Contabilização TXT com mais de uma Filial

**Ambiente**  
Protheus – Contabilidade – A partir da versão P12  
  
  
**Solução**

Necessário configurar o mesmo código de lançamento padrão nas filiais que irão receber o lançamento

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018440751)

Pergunta na rotina de contabilização TXT:

* Considera Filial no arquivo texto?
  + Sim
  + Não

Para que a contabilização seja  executada, as primeiras posições do arquivo texto deverão conter o código da filial, em seguida o código do lançamento padrão onde será executada a leitura do arquivo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018560532)

[Considerar filial no arquivo texto](https://tdn.totvs.com/pages/viewpage.action?pageId=348293358)

Para esta funcionalidade é necessário configurar os parâmetros abaixo:

* [MV\_CTBTPAT](https://tdn.totvs.com/pages/viewpage.action?pageId=312160877): Caminho do arquivo texto.
* [MV\_CTBTERR](https://tdn.totvs.com/pages/viewpage.action?pageId=312160877): Diretório onde serão copiados os arquivos texto após o processamento que não foram importados.
* [MV\_CTBTRES](https://tdn.totvs.com/pages/viewpage.action?pageId=312160877): Diretório onde serão copiados os arquivos texto após o processamento que foram importados com sucesso.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12608458269463)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12608352841623)

Exemplo:

* Considera Filial no arquivo texto?
  + Sim
    - Arquivo Texto: (em negrito filial de um ambiente com gestão corporativa)
    - **D MG 01**10011001...
    - **D MG 01**10011001...
    - **D MG 01**10011001...

* Não
  + Arquivo Texto: (em negrito filial de um ambiente com gestão corporativa)
  + 10011001...
  + 10011001...
  + 10011001...

Caso o parâmetro “Quebra linha em Doc” estiver configurado como “não” o sistema irá gerar um documento a cada troca de filial.

Exemplo:

* **D MG 01**100...
* **D MG 01**100...
* **D MG 01**100...
  + **Gera um documento na filial D MG 01**
  + **D MG 02**100...
  + **D MG 02**100...
  + **D MG 02**100...
    - **Gera um documento na filial D MG 02**
    - **D MG 01**100...
    - **D MG 01**100...
    - **D MG 01**100...
      * **Gera um documento na filial D MG 01**

Para utilizar essa funcionalidade, o lançamento padrão de contabilização TXT deve levar em contas 12 Posições de filial + 3 posições no código do LP para as funções LerVal e LerSTR.

O sistema deve validar o campo de filia

<https://tdn.totvs.com/pages/releaseview.action?pageId=234611889>

Veja mais

[MP SIGACTB - CONTABILIZAÇÃO TXT](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007149031-MP-SIGACTB-CONTABILIZA%C3%87%C3%83O-TXT?source=search)

[MP - SIGACTB - Validação arquivo txt CTBA500](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019339412-MP-SIGACTB-Valida%C3%A7%C3%A3o-arquivo-txt-CTBA500?source=search)
