---
article_id: 360035277613
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: f90e187fc1857fc2182794311a039580d10786a211e591ebd6c563fab60458e9
fetched_at: '2026-06-28T22:42:03.874673+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: 'MP- FIS - Apuração de ISS - EFD ICMS/IPI - Bloco B:  Como o sistema define
  onde o ISS é devido?'
type: support-article
updated_at: '2021-04-30T13:42:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035277613-MP-FIS-Apura%C3%A7%C3%A3o-de-ISS-EFD-ICMS-IPI-Bloco-B-Como-o-sistema-define-onde-o-ISS-%C3%A9-devido
---

**Dúvida**Como o sistema define onde o ISS é devido?  
   
 **Ambiente**  
Microsiga Protheus a partir da 12.1.17

**Solução**

**Nas aquisições:**

Se o serviço for configurado como “EP” (B1\_MEPLES = 1 ou Branco), ou seja, ISS devido no estabelecimento do prestador, o ISS será considerado devido no município do fornecedor do documento (A2\_COD\_MUN).

Se o serviço for configurado como “LES” (B1\_MEPLES = 2), ou seja, ISS devido no local de execução do serviço, primeiramente serão avaliados os campos F1\_ESTPRES e F1\_INCISS, que podem ser informados no momento da digitação do documento de entrada. Se estes campos estiverem preenchidos, o ISS será considerado devido no município ali definido.

Caso contrário, o ISS será considerado devido no município do SIGAMAT (M0\_CODMUN).

**Nas prestações:**

Se o serviço for configurado como “EP” (B1\_MEPLES = 1 ou Branco), ou seja, ISS devido no estabelecimento do prestador, o ISS será considerado devido no município do SIGAMAT (M0\_CODMUN).

Se o serviço for configurado como “LES” (B1\_MEPLES = 2), ou seja, ISS devido no local de execução do serviço, primeiramente serão avaliados os campos F2\_ESTPRES e F2\_MUNPRES, preenchidos através dos campos C5\_ESTPRES e C5\_MUNPRES no pedido de venda. Se estes campos estiverem prenchidos o ISS será considerado devido no município ali definido.

Caso contrário o ISS será considerado devido no município do cliente de faturamento (A1\_COD\_MUN).

 No sistema, “EP” significa **Estabelecimento do Prestador**, “LES” significa **Local de Execução do Serviço.**

Esta configuração é feita no cadastro de produto, por meio do campo **Exec. Serviço(B1\_MEPLES)**, a opção “1” indica EP e opção “2” indica LES, e caso este campo esteja vazio, será adotada “EP” como padrão.

Informações adicionais:

<https://tdn.totvs.com/pages/viewpage.action?pageId=500292737>
