---
article_id: 15923820729495
category: Materiais - Compras (SIGACOM)
content_hash: ee0a9587e15017b7165db816a4950264bcff456689cc9c6883bae3135ad0de7d
fetched_at: '2026-06-28T22:41:12.816547+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus  - Legenda "Docto Pendente de Revisão
  Cadastral" - Automação Cadastral
type: support-article
updated_at: '2025-01-02T15:12:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15923820729495-Cross-Segmentos-Totvs-Backoffice-Protheus-Legenda-Docto-Pendente-de-Revis%C3%A3o-Cadastral-Automa%C3%A7%C3%A3o-Cadastral
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15923791199895) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**

Qual a funcionalidade da Nova Legenda Automação Cadastral ?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15924035221655)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - A partir da Versão 12

**Solução**

O objetivo dessa funcionalidade é realizar o cadastro automático de fornecedor/cliente, a amarração entre produto e fornecedor ou produto e cliente, além de facilitar o processo de cadastro e/ou seleção de produtos.

Ao realizar a Integração um dos cadastros por meio da funcionalidade, o documento poderá ser inserido no Monitor com o Legenda marrom "**Docto Pendente de Revisão Cadastral**". Nesse caso, será necessária a revisão cadastral do fornecedor/cliente para prosseguir com o andamento do documento.

Quando o cadastro for inserido por meio da funcionalidade, é necessário revisar o documento no Monitor para corrigir as informações.

Segue abaixo um exemplo de revisão cadastral: informei o produto que estava em branco, verifiquei se as informações do **cadastro de fornecedor** e da **amarração Produto x Fornecedor** estavam corretas, e confirmei para validar a automação cadastral.

![Exemplo de Revisao Cadastral.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/19869174631447)

Ao validar todas as mensagens na aba "**Ocorrências**" e confirmar, a Legenda foi alterada para "**VERDE**", "**Documento Normal**", conforme a imagem abaixo. Dessa forma, é possível prosseguir com o processo e gerar o documento.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19869155665943)

**Observação 1** : Caso não valide todas as ocorrências, ao tentar gerar o documento na tela do Monitor, a legenda do documento permanecerá com a legenda "**Docto. Pendente Rev Cadastral**" e será exibido o alerta abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19869174649623)

Foi disponibilizada a melhoria no link abaixo, permitindo que o cadastro de fornecedor/cliente seja incluído automaticamente, com as informações básicas e obrigatórias, na rotina do Monitor:

[Automação Cadastral - Importador XML x TOTVS Transmite](https://tdn.totvs.com/pages/releaseview.action?pageId=773517403)

**IMPORTANTE:** A funcionalidade de automação cadastral estará disponível apenas na integração entre o Importador XML e o TOTVS Transmite.

***Saiba Mais*****:**

[Cross Segmento - Backoffice (Linha Protheus) - SIGACOM - Integração Importador XML x TOTVS Transmite](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7557934491159-Cross-Segmento-Backoffice-Linha-Protheus-SIGACOM-Integra%C3%A7%C3%A3o-Importador-XML-x-TOTVS-Transmite)

[Automação Cadastral - Importador XML x TOTVS Transmite](https://tdn.totvs.com/pages/releaseview.action?pageId=773517403)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
