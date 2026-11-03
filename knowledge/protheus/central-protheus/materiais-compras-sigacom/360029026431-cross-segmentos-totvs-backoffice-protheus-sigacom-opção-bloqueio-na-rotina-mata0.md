---
article_id: 360029026431
category: Materiais - Compras (SIGACOM)
content_hash: 0c4347e2757eed441d96f6c540f258f0ec8fe12bb073c83e07e0381d399c860d
fetched_at: '2026-06-28T22:41:22.032991+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Opção Bloqueio na rotina
  MATA020 - Cadastro de Fornecedor não aparece para os usuários, somente para o Administrador
type: support-article
updated_at: '2022-05-18T21:08:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029026431-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Op%C3%A7%C3%A3o-Bloqueio-na-rotina-MATA020-Cadastro-de-Fornecedor-n%C3%A3o-aparece-para-os-usu%C3%A1rios-somente-para-o-Administrador
---

**Dúvida**Opção Bloqueio na rotina **MATA020 - Cadastro** de Fornecedor não aparece para os usuários, somente para o **Administrador**

**Ambiente**Protheus - Compras - A partir da versão 11.08

**Solução**Verificar o Nível do campo se está com o valor igual a **9**

**Acessar o Configurador** - Base de Dados / Dicionário / Base de Dados

Pesquisar pela tabela **SA2** e localizar o Campo **A2\_MSBLQL**, conforme imagem a baixo

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029893132/mceclip1.png)

Verifique na imagem abaixo que com um usuário normal o campo Bloqueio não aparece

Imagem do Configurador

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029893412/mceclip2.png)

Imagem do **MATA020- Cadastro de Fornecedor** após modificar o parâmetro **A2\_MSBLQL**

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029894052/mceclip4.png)

Veja como com o Nível **1** que apresenta o campo

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029893892/mceclip3.png)
