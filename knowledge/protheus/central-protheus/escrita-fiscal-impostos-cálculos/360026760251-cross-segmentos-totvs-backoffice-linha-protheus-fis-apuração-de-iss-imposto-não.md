---
article_id: 360026760251
category: Escrita Fiscal - Impostos - Cálculos
content_hash: 18b94fdb7a2216208418263d19395c4f736912a01b64301d05f37b75c4b341b7
fetched_at: '2026-06-28T22:39:30.650077+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Apuração de ISS -
  Imposto não é gerado na linha "Imposto a Recolher" e sim em "Imposto a recolher
  em outros municípios" ou Deduções
type: support-article
updated_at: '2021-07-29T13:33:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026760251-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Apura%C3%A7%C3%A3o-de-ISS-Imposto-n%C3%A3o-%C3%A9-gerado-na-linha-Imposto-a-Recolher-e-sim-em-Imposto-a-recolher-em-outros-munic%C3%ADpios-ou-Dedu%C3%A7%C3%B5es
---

**Dúvida**Como fazer o imposto de ISS ser apresentado na apuração na linha "Impostos a recolher" em vez de "Imposto a recolher em outros municípios ou Deduções".

**Ambiente**  
Protheus – Livros Fiscais – A partir da versão 12.1.17  
   
**Solução**

Apuração de ISS trabalha com o conceito de ISS por município. O valor do imposto não é considerado na linha “Imposto a Recolher”, pois, o cliente não é do mesmo município do prestador, ou seja, o código de município do SA1 está diferente do município informado no Sigamat.

Diante disso entra o conceito que o Imposto deve ser pago no local de prestação do serviço e o sistema entende que o serviço foi prestado no município do cliente em questão, porém, a prestação do serviço não necessariamente deve ocorrer no município do cliente.

Para que o valor do ISS - Devido seja considerado na linha de “Imposto a Recolher” o processo abaixo deverá ser seguido:

* Configurar o parâmetro MV\_MUNIC com o fornecedor padrão para o recolhimento do seu ISS. O sistema automaticamente cria o fornecedor “MUNIC”, basta alterar o cadastro e informar no campo “Município” o mesmo código do município do Sigamat (Cadastro de empresas).

* Configurar o parâmetro MV\_ISSXMUN = .T.

* Ao realizar o pedido de vendas, informar o fornecedor MUNIC no campo “C5\_FORNISS” e também informar onde o serviço foi prestado (neste caso, o município do prestador), através dos campos:

* Uf. Prest (C5\_ESTPRES)
* Mun. Prest (C5\_MUNPRES)

* O valor a recolher do ISS será devidamente gerado na linha 012  - “Imposto a Recolher”

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026083651/mceclip0.png)

Para melhorar o controle sobre os serviços prestados por município, é possível conferir estes valores através da última aba - “Por Município – Saídas”.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026083691/mceclip1.png)
