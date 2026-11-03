---
article_id: 19357524772375
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: f101683a4bcb6e68571d0e816796282405f0789f9c68080d0f6170b866d323ff
fetched_at: '2026-06-28T22:37:21.508169+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como funciona o Rateio
  de Entidades Contabeis no Gestão de Contratos ?
type: support-article
updated_at: '2026-01-12T16:41:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19357524772375-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-funciona-o-Rateio-de-Entidades-Contabeis-no-Gest%C3%A3o-de-Contratos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19357550939799) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como funciona o Rateio por Entidadees Contabeis no Gestão de Contratos ?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões

**Solução**  
O cadastro do Contrato possui uma aba referente a "Rateio Contabil por Item" (Tabela CNZ) da imagem abaixo em que podem ser vinculados os rateios das entidades contábeis pra cada item da planilha no contrato:

![](https://totvssuporte.zendesk.com/attachments/token/18HlLU52DfxRNdtXKZJK2cgs2/?name=image.png)

Ao ser incluído o rateio no contrato, posteriormente este será levado automaticamente para as medições a serem realizadas para o contrato, numa aba semelhante de "Rateio Contabil do Item" existente na rotina de Medição (imagem abaixo):

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34677669161495)

E ao encerrar a medição em que for gerado um Pedido de Compras, este rateio inserido nesta aba da rotina de medição será levado para o Rateio de Centros de Custos do Pedido de Compras gerado (Tabela SCH), na opção da imagem abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19357656503063)

***Obs1:***

Ao incluir o rateio é alimentado o campo CNB\_RATEIO com conteúdo 1 , não é possível visualizar esse campo em Tela apenas via consulta na base de dados.

No pedido de compras é preenchido em Outras ações>Rateio o mesmo rateio informado na medição e o campo C7\_RATEIO é preenchido com "Sim".

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36819537973655)

***Obs2:***

**P:** O campo CNZ\_ITEM pode ser aumentado o seu tamanho ?

**R:** Na tabela CNZ de "Rateio Contabil por Itens" do Gestão de Contratos, o campo CNZ\_ITEM não possui a possibilidade de ter o seu tamanho alterado para que comporte um numero maior de itens na aba de "Rateio Contabil do Itens".

O campo possui no SIGACFG inibida a alteração, que é uma restrição das regras de negócio dos módulos e assim não é recomendada a alteração via manipulação de registros de Dicionário de Dados.

***Saiba Mais:***

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
