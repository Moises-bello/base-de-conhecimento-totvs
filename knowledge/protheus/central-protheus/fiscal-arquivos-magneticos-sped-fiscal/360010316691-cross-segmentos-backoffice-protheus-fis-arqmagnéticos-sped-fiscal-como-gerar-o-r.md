---
article_id: 360010316691
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 583152a8ceb610a57cb420ac8feaeff8333972d78a6525a2b5c6a4195239861f
fetched_at: '2026-06-28T22:42:03.586740+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Sped Fiscal
  - Como gerar o registro E530 no Sped Fiscal?
type: support-article
updated_at: '2024-03-14T18:24:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010316691-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Sped-Fiscal-Como-gerar-o-registro-E530-no-Sped-Fiscal
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 02:00 min**

**Dúvida**

Como gerar o registro **E530** - **Ajustes da apuração do IPI**?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões

**Solução**

**REGISTRO E530: AJUSTES DA APURAÇÃO DO IPI**

Estes ajustes são os códigos de subitens lançados manualmente na **Apuração de IPI**, que serão transportados para o meio magnético.

**Parâmetro**

**MV\_USASPED=T**

*Wizard* **Apuração de IPI**

**Livro Selecionado = \***                         -> Será gerado apuração de todos os livros

**Apuração = Mensal**                            -> Apuração do mês

**Período = 1º**                                      -> Período Mensal

Deve ser selecionado linha onde será realizado ajuste efetuado **duplo *click*** na **coluna Cod. Ajuste** para ser visualizado a tela abaixo:

![](http://tdn.totvs.com/download/attachments/238035285/image2016-6-18%2022%3A59%3A50.png?version=1&modificationDate=1466297625000&api=v2)![](http://tdn.totvs.com/download/attachments/238035285/image2016-6-18%2023%3A20%3A8.png?version=1&modificationDate=1466298843000&api=v2)![](http://tdn.totvs.com/download/attachments/238035285/image2016-6-18%2023%3A21%3A10.png?version=1&modificationDate=1466298905000&api=v2)

Deverá ser gerado arquivo txt do **SPED FISCAL** com a pergunta da *Wizard*

**Tipo de Atividade = 0- Industrial ou Equiparado**

![](http://tdn.totvs.com/download/attachments/238035285/image2016-6-18%2022%3A30%3A34.png?version=1&modificationDate=1466295869000&api=v2)

Será apresentado o registro **E530** gravado na tabela **CDP** no arquivo TXT.

![](http://tdn.totvs.com/download/attachments/238035285/image2016-6-18%2023%3A25%3A39.png?version=1&modificationDate=1466299174000&api=v2)

**Importante:**

**Ao campo 5 do registro E530 “Indicador da origem do documento vinculado ao ajuste” do registro E530 foi acrescida a opção “3 – Documento Fiscal”, além disso o preenchimento do campo passará a ser obrigatório.**

**Quando a opção escolhida pelo contribuinte for documento deverá ser apresentado o registro E531.**

Para mais informações sobre o Sped Fiscal acessar:

<http://tdn.totvs.com/pages/releaseview.action?pageId=238035285>
