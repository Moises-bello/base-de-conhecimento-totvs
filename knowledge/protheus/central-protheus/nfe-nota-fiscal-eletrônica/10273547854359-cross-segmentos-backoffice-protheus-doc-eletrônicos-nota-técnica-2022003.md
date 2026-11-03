---
article_id: 10273547854359
category: NFe - Nota Fiscal Eletrônica
content_hash: 27e1dcf3cd0e2a984a6a087270e7f210004d24d2f09f704cc212ad460ccd555d
fetched_at: '2026-06-28T22:40:07.049150+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Nota técnica 2022.003
type: support-article
updated_at: '2025-10-23T14:46:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10273547854359-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Nota-t%C3%A9cnica-2022-003
---

**Dúvida**Quais são as atualizações e procedimentos necessários para configuração da NT 2022.003  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.27

Cross Segmentos - TSS - a partir da versão 12

**Solução**

**Prezados Clientes,**

* **Importante:**

**O prazo previsto para a Nota Técnica 2022.003 v1.11 é:**

* Ambiente de Homologação (ambiente de teste das empresas): até **07/02/2022**
* **Ambiente de Produção: 03/04/2023**

Para solucionar essa dúvida, realize os seguintes passos:

**1. Atualização do ambiente TSS (repositório e schemas)**

**[MP - TSS - Atualização do Repositório (RPO) do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981)**

2. Atualizar a pasta **SCHEMAS** presente na estrutura do TSS através do link:

[TSS - Atualização dos SCHEMAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025103552)

**1. Atualização do ambiente Protheus:**

1. Aplicar o **Pacote Documentos eletrônicos**

<https://tdn.totvs.com/pages/releaseview.action?pageId=525010692>

      2. **Compilar RDMAKE NFESEFAZ** (se emitir NF-e) presente no link abaixo

<https://suporte.totvs.com/portal/p/10098/download?e=1083729>

**2. Criação do Parâmetro:**

1. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /** **Cadastros / Parâmetros** clicar em **incluir** **MV\_NFESIG Tipo: 1 - Caractere.**

Preencher no configurador o valor do parâmetro **MV\_NFESIG**contendo a **UF** do emitente da nota que deseja que a nota referenciada vá com o **código numérico zerado**.

**1.** A UF do emitente que deseja o envio da *tag* <refNfeSig> contendo a chave com o código numérico zerado.

Exemplo: MV\_NFESIG = SP

![MV_NFESIG_SP.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/13509303435159)

**2.** Informar **ALL**, para que qualquer UF de emitente seja considerada para o envio da *tag* <refNfeSig>.

Exemplo: MV\_NFESIG = ALL

![MV_NFESIG_ALL.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/13509405971095)

**3.** Caso deseje que mais de uma UF seja considerada, mas não todas, separar as UF por pipe "|"

**Exemplo: MV\_NFESIG =** SP|RJ

![MV_NFESIG_SPRJ.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/13509472616215)

**Exemplo:  MV\_NFESIG =** SP, para NF-e do tipo Normal (finnfe=1), emitidas pela UF SP e que possua nota referenciada do tipo 55 (NF-e), essa nota será informada através da*tag*<refNfeSig>, contendo o seu o código numérico zerado.

**4.** Verificar se a nota foi **referenciada ao documento**de origem corretamente:

D2\_ITEMORI, D2\_SERIORI, D2\_NFORI **(nota de saída)**

![referecia_nt_saida.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17788979083287)

D1\_ITEMORI, D1\_SERIORI, D1\_NFORI **(nota de entrada)**

**![referecia_nt_entrada.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17788979086871)**

**Importante:**

Lembrando que a nota só é **referenciada no XML** caso exista no sistema.

Se a mesma for referenciada manualmente deve se preencher os campos **NF . Ori , Serie Ori e Item Ori** .   
  
Se for preenchido automaticamente pelo gatilho **F4 (Nota de saída) ou F7 (Nota entrada)** os campos são alimentados automaticamente.

Caso precise referenciar mais de uma nota, na nota que deseja que destaque a tag refsig, vai precisar incluir a nota que deseja referenciar no modulo 09 Livros Ficais - Atualizações - Movimentos - Nota manual de saída ou entrada.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35832287468951)

Selecione a nota e va em Outras Ações - Complemento.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35832287474967)

**Clique em documentos fiscais e no campo Docto. Ref selecione a nota que deseja vincular a nota principal e depois em salvar.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35832278626583)

**5. Acessar o link abaixo para mais informações da criação do parâmetro:**

[Clique Aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=747333552)
