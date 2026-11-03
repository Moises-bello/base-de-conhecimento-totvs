---
article_id: 1500012186641
category: NFe - Nota Fiscal Eletrônica
content_hash: 886380ece96a1e9cc914adda77fa4b52a97b7c027ba2831e1984840646662aee
fetched_at: '2026-06-28T22:40:06.807667+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como utilizar o
  MV_DEVSIMP para que não destaque o ICMS no campo próprio na Devolução.
type: support-article
updated_at: '2025-06-25T12:15:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012186641-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-utilizar-o-MV-DEVSIMP-para-que-n%C3%A3o-destaque-o-ICMS-no-campo-pr%C3%B3prio-na-Devolu%C3%A7%C3%A3o
---

**Dúvida**Como utilizar o MV\_DEVSIMP para que não destaque o ICMS no campo próprio na Devolução para fornecedor ou cliente do Simples Nacional ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

**1-** Preencher o parâmetro MV\_DEVSIMP como **.T. (Verdadeiro) no configurador:**

- o valor do ICMS **não será destacado** na TAG **própria do XML;**

- o valor do ICMS **não será destacado** no campo **próprio do DANFE;**

**2 -** Preencher o parâmetro MV\_DEVSIMP como **.F. (Falso) no configurador:**

- o valor do ICMS**será destacado** no campo XML como no **DANFE**

**![MV_.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019272722)**

**2-** Para criar o **parâmetro manualmente** e para acessar o **boletim temos o link abaixo:**

*[Clique Aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=619742950)*

3- Para o funcionamento do parâmetro o fonte do **NFESEFAZ** **Compilar RDMAKE NFESEFAZ** (se emitir NF-e) presente no link abaixo:

[Clique Aqui](https://suporte.totvs.com/portal/p/10098/download?e=1152113)

* **Saiba mais:**

Lembrando que **RDMAKE não possui Release** sendo assim, pode ser aplicada em qualquer uma todos os pacotes.

**4 -** Fazer uma nota de **entrada ou de saída** do **tipo 'D = Devolução'**

**5-** Preencher no cadastro de cliente o campo "**Opt. Simples"**  ***A1\_SIMPNAC = 1 - Sim***

![A1_SIMP.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019278582)

**6-** Preencher no cadastro de fornecedor o campo **"Opt. Simp. Nac."** ***A2\_SIMPNAC = 1 - Sim***

![A2_SIMP.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019278622)

* **Saiba mais:**

*[Parecer da consultoria](https://tdn.totvs.com/pages/viewpage.action?pageId=593729092)*
