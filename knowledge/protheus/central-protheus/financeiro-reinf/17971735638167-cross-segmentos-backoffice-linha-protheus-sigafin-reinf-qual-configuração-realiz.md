---
article_id: 17971735638167
category: Financeiro - Reinf
content_hash: ab33a192335015b290bbfff7a4a37d6286701466403bcfd2820f79abceaa52f7
fetched_at: '2026-06-28T22:37:51.852359+00:00'
product: protheus
section_id: 17886892336407
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - REINF - Qual configuração
  realizo para os títulos de fornecedor estrangeiro serem apresentados no Extrator
  Fiscal
type: support-article
updated_at: '2024-09-03T18:04:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17971735638167-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-REINF-Qual-configura%C3%A7%C3%A3o-realizo-para-os-t%C3%ADtulos-de-fornecedor-estrangeiro-serem-apresentados-no-Extrator-Fiscal
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18008063784215)**Tempo aproximado para leitura:**00:05:00 min  
  
Dúvida**

Na integração do bloco 40 com o TAF (rotina Extrator Fiscal) os títulos de fornecedor estrangeiro não são apresentados.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - REINF - A partir da versão 12.1.33

**Solução**

Quando o fornecedor é estrangeiro, alguns campos precisam ser preenchidos, para que os títulos sejam apresentados no **Extrator Fiscal**.

01 - Acesse o **Cadastro do Fornecedor ->**aba **Cadastrais,** preencha os campos:

**Estado** = EX

**Tipo** = Outros

**Município** = 999999

![4.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/23144872953367)  
![3.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/23144843526295)

02 - Aba **Residente no Exterior**, preencha o **Campo Código Pais**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17971187685015)

03 - Acesse o **Cadastro de Participantes**, preencha os campos com os dados do cliente, sendo obrigatórios.

**ID Pais**

**ID UF**

**Cod.Part.**

**Tipo. Pessoa**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17971236050839)

O campo no **TAF C1H\_RELFON** é corresponde ao campo **Benef. Rend** na **A2\_BREEX**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23144843537303)  
  
04 - Acesse o **Cadastro de Participantes ->** aba **Informações Residentes/Domiciliados no Exterior**, preencher o campo:

**Id. País Ext.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26103822920727)

**Importante**

**Preenchimento de impostos realizado de forma manual não serão validados pelo painel do TAF. Serão considerados apenas as informações de impostos no cadastro de natureza e fornecedor (neste cadastro deve ser vinculado o cadastro de natureza)**

**Saiba mais**

**[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - MATA020 - COMO CADASTRAR FORNECEDOR ESTRANGEIRO NO PROTHEUS ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019752011-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-MATA020-COMO-CADASTRAR-FORNECEDOR-ESTRANGEIRO-NO-PROTHEUS-?source=search)**

**[Gerar Dirf para fornecedores residentes no exterior](https://tdn.totvs.com/display/PROT/Gerar+Dirf+para+fornecedores+residentes+no+exterior)**
