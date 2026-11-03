---
article_id: 360021111712
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: f25ac26204e6dd0687815a9978d0e653b71e1c9d6d126bb83eef5fddf4013bfb
fetched_at: '2026-06-28T22:42:11.818571+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - NOVAGISS campo
  CD_LOCAL_PRESTACAO
type: support-article
updated_at: '2022-08-18T14:08:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021111712-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-NOVAGISS-campo-CD-LOCAL-PRESTACAO
---

**Dúvida**Como preencher o campo **CD\_LOCAL\_PRESTACAO** da **NOVAGISS**?  
  
 **Ambiente**Protheus – Livros Fiscais – A partir da versão 11.80  
 **Solução**1- Para as Notas de Entrada:  
Verifique se os campos **F1\_ESTPRES** e **F1\_INCISS** estão preenchidos, pois para as entradas esses campos são tratados para que no arquivo o serviço seja recolhido dentro ou fora do município.  
  
Os campos são preenchidos através da aba no **documento de entrada**:![](https://totvssuporte.zendesk.com/attachments/token/tQVRdBFObTzPoXnLV7rYcfKL5/?name=inline1005778317.png)

Validação realizada pelo fonte:

ARQ->ARQ\_LOCPS  := cLocPS

cLocPS := Iif(cCidade == Alltrim(SM0->M0\_CODMUN), "D", "F")

cCidade := Alltrim(UfCodIBGE(SF1->F1\_ESTPRES)+SF1->F1\_INCISS)  
  
2- Para as Notas de Saídas:

Para notas de saídas, a validação é no campo **F3\_ISSST**.

//Local Prestação Serviço (Dentro ou Fora Municipio)

cLocPS := iif(cMunCli == Alltrim(SM0->M0\_CODMUN) .And. (cAlias)->F3\_ISSST == "1", "D", "F")  
  
Importante:   
Para ser considerado o campo **CD\_LOCAL\_PRESTACAO** como "**D = Dentro do município**":

Preencha o campo de Código de Município do **SIGAMAT**, conforme exemplo a seguir:  
  
![](https://totvssuporte.zendesk.com/attachments/token/efIBycSWaugtJmr8x0gO4oTtc/?name=inline-1370501864.png)

Preencha os campos do **Cadastro de Fornecedor**, conforme exemplo a seguir:  
  
![](https://totvssuporte.zendesk.com/attachments/token/uOKgbmQOvR14bFXtOzjbgN70P/?name=inline-986404203.png)

Ou seja, no **SIGAMAT**, informando o Código de Município (exemplo 3550308) terá a mesma validação do **Cadastro do Fornecedor** quando o fonte faz a junção das informações dos campos **A2\_EST** e **A2\_COD\_MUN** (Vide acima).
