---
content_hash: d9add38e7a4a017dbc2268d4dba2768189f6be51c9636e0abd9474a22f4ade35
fetched_at: '2026-06-29T00:09:23.969420+00:00'
page_id: '422546178'
product: rm
source: tdn-rm
title: Nota Fiscal Eletrônica (NF-e)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422546178
version: 27
---

**Informamos que os dados pessoais contidos nesta entidade foram colhidos para emissão de documentos fiscais e geração de rotinas legais, e são retidos por determinação legal de normas fiscais e de transparência. Os mesmos não poderão ser eliminados em virtude de obrigação legal de retenção. O cumprimento de obrigação legal é hipótese legítima do tratamento dos seus dados conforme a Lei Geral de Proteção de Dados Pessoais (Lei n° 13.709/2018).**

**Para mais informações sobre a LGPD e as soluções oferecidas pela TOTVS, [consulte nossa página aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=514427789).**

## 1. Visão Geral

A Nota Fiscal Eletrônica (NF-e) é um documento de existência exclusivamente digital, emitido e armazenado eletronicamente; utilizado para registrar todas as operações de circulação de mercadorias ou prestação de serviços. A sua validade jurídica é garantida pela assinatura digital de emitente e a autorização de uso é fornecida pela administração tributária da unidade federativa do domicílio do contribuinte.   
Esse modelo nacional de documento fiscal eletrônico substitui a sistemática de emissão do documento fiscal em papel, modelos 1 e 1A, simplificando as obrigações acessórias dos contribuintes e permitindo, ao mesmo tempo, o acompanhamento em tempo real das operações comerciais pelo fisco.

## 2. Sobre a NF-e

A transmissão de NF-e pela Linha RM é realizada através do modulo *Gestão de Estoque, Compras e Faturamento*, onde temos os seguintes aplicativos/arquivos para utilização:

* **Certificado Digital:** O produto RM utiliza o *certificado tipo A1* para transmissão de notas. *Não são contemplados outros tipos de certificados* (por exemplo, certificado A3). Caso seja necessária a utilização de outro tipo de certificado, gentileza entrar em contato com nosso suporte no portal do [cliente](http://suporte.totvs.com/).   
  Para importar um certificado digital, acesse *Backoffice | Gestão Fiscal | Globais | Mais... | Certificado Digital*

  Clique para visualizar a imagem
* **Totvs Sped Services (TSS):** É a solução TOTVS usada para realizar a comunicação entre a Linha RM e a SEFAZ, utilizando web services. É necessário criar um novo banco de dados para o TSS e *não recomendamos* o uso do mesmo banco de dados do RM.
* **TOPConnect:** Solução TOTVS para comunicação entre o TSS e o banco de dados.

Para acessar a visão das Notas Fiscais, acesse *Backoffice | Gestão de Estoque, Compras e Faturamento | Vendas | Documentos Eletrônicos | Nota Fiscal Eletrônica (NF-e/NFC-e)*

Visão das Notas Fiscais Eletrônicas

Esta visão irá mostrar para o usuário todas as NF-e movimentadas por ele. A coluna status (NF-e) poderá assumir os seguintes valores:

| Ícone | Descrição | Sigla |
| --- | --- | --- |
|  | Pendente | P |
|  | Inconsistente | I |
|  | Rejeitada | R |
|  | Autorizada | A |
|  | Cancelada | C |
|  | Contingência | T |
|  | Cancelamento Pendente | K |
|  | Denegada | W |

Na visão da NF-e não serão mostradas notas inutilizadas que tenham sido emitidas e por algum motivo não tenham sido autorizadas pela SEFAZ e nem a inutilização da numeração, mesmo que esta ainda não tenha gerado nota. As inutilizações somente serão apresentadas nos anexos do cadastro de filiais (*Filiais | Anexos | NF-e/NFC-e Inutilizadas*)e podem assumir os seguintes status:

| Ícone | Descrição | Sigla |
| --- | --- | --- |
|  | Pendente | P |
|  | Inutilizada | N |
|  | Rejeitada | R |

Antes de executar qualquer processo da NF-e, certifique-se de que os serviços *TopConnect* e *TOTVS Web Service* estejam iniciados. Para verificar se eles estão ativo, vá até **Painel de Controle | Ferramentas administrativas | Serviços**. Na coluna "status" deve constar o valor "Iniciado".   
***Dica:*** Deixe os dois serviços como automáticos para não ter problemas no envio.

---

Legislação

* [Manual de Orientação do Contribuinte - versão 6.00](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=URCYvjVMIzI=)
* [Nota Técnica 2016.002 - v 1.60](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=Y6Lj7G0uHwc=)
* [Portal da NF-e](http://www.nfe.fazenda.gov.br/portal/principal.aspx)
Parametrizações

* [Instalação e Configuração do TSS](http://tdn.totvs.com.br/pages/releaseview.action?pageId=64652506)
* [Instalação e Configuração do TOP Conect](http://tdn.totvs.com/pages/viewpage.action?pageId=65209013)
