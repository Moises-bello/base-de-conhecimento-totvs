---
article_id: 40266657578519
category: SIGAEST - CUSTOS
content_hash: 15bf51e803a64840edc5f12c20899fdaa71ef1cb6e0eb79b4592efac37bac69b
fetched_at: '2026-06-28T22:39:00.608839+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Cadastro de produto
  iniciando com a palavra "MOD" apresenta o HELP NAOMVMOD ao incluir Documento de
  Entrada
type: support-article
updated_at: '2026-05-06T12:16:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40266657578519-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Cadastro-de-produto-iniciando-com-a-palavra-MOD-apresenta-o-HELP-NAOMVMOD-ao-incluir-Documento-de-Entrada
---

**[Remover as instruções entre colchetes e altere o tempo aproximado para leitura]**  
  
![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40266657576471) Tempo aproximado para leitura: **00:02:45 min**  
  
**Dúvida**

Cadastro de produto iniciando com a palavra **"MOD"** apresenta o **HELP NAOMVMOD** ao incluir Documento de Entrada.

![naomvmod.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40266837770903)  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**

O Help **NAOMVMOD** é apresentado ao incluir um Documento de Entrada vinculando um **produto Mão-de-Obra**.

No Protheus padrão os **produtos MOD (Mão-de-Obra)** são identificados das seguintes formas:

* O código (B1\_COD) é iniciado pela sigla **"MOD" + o código do Centro de Custo**;
* Também quando os campos **B1\_CCCUSTO** **e/ou B1\_GCCUSTO** estiverem preenchidos.

A rotina **não** aceita esse tipo de produto, devido seu Custo ser obtido somente através do rateio dos movimentos vinculados as ordens de produções (SD3).  
  
Caso seja necessário que a informação de Centro de Custo esteja no cadastro de Produto, informe na Aba Cadastrais, no campo **Centro de Custo (B1\_CC)** e no campo **Conta Contábil (B1\_CONTA)**.

Sobre esse conceito veja o **PDF anexo** explicativo sobre a funcionalidade dos produtos MOD com e sem Integração Contábil. [**Nesse link**](https://tdn.totvs.com/x/zrZEGQ) constam mais detalhes sobre a construção padrão dessa funcionalidade no Protheus.

**Importante:**Os cadastros de produtos que iniciam com a palavra "MOD" **são reservados apenas para essa funcionalidade**, impedindo que sejam criados códigos de produtos que iniciam com esse Termo. **Ou seja, qualquer produto que iniciar com essa palavra o Sistema entende que trata-se de um produto "MOD" (Mão-de-Obra)**.

Nesse  cenário, é adequado a criação de códigos de produtos que iniciem com a palavra diferente de MOD, **por exemplo**: **\_*****MOD**, ou também **M\_*****OD.**

***Saiba Mais:***

[Clique aqui e veja mais artigos sobre CADASTROS E CONFIGURAÇÕES GERAIS no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)

[Clique aqui e veja mais artigos sobre CUSTOS no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)

[Backoffice (Linha Protheus) - SIGACOM - Help NAOMVMOD ao incluir um Documento de Entrada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9324451218839-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGACOM-Help-NAOMVMOD-ao-incluir-um-Documento-de-Entrada)

[Fluxo de processo de um produto MOD sem integração com o contábil](https://tdn.totvs.com/x/zrZEGQ)

[Backoffice (Linha Protheus) - SIGAEST - Processo de configuração de MOD e GGF "Sem" e "Com" integração contábil](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402062082071-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Processo-de-configura%C3%A7%C3%A3o-de-MOD-e-GGF-Sem-e-Com-integra%C3%A7%C3%A3o-cont%C3%A1bil)
