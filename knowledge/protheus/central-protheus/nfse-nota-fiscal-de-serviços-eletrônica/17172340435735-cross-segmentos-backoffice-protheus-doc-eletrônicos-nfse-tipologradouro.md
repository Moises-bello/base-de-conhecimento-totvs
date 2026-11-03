---
article_id: 17172340435735
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 99b64e1edaa9cc95b4ee09b44031a6b410d0e134524748b20165cf88b5f5a9b1
fetched_at: '2026-06-28T22:39:58.678260+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe: TipoLogradouro'
type: support-article
updated_at: '2023-08-31T12:23:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17172340435735-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-TipoLogradouro
---

**Dúvida**O tipo de logradouro está sendo enviado também na tag Logradouro do remessa gerado pelo rdmake, que causa duplicidade na nota gerada pela prefeitura.  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Solução**O parâmetro MV\_TIPLOGR foi criado para determinar se retira o tipo do logradouro do endereço.   
Caso não tenha o parâmetro no Protheus, faça a criação conforme abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17172280380567)  
Exemplo de configuração do parâmetro:  
  
Parametro =**.T.** = Sim

**A1\_END**='AV. BRAS LEME , 1000'   **XML**= ' BRAS LEME , 1000'

Parâmetro = **.F.** = Não

**A1\_END**='AV. BRAS LEME , 1000'   **XML****=**'AV. BRAS LEME , 1000' // **NÃO MUDA.**

Para que seja retirado o tipo de logradouro a mesma devera obedecer a tabela abaixo sendo valido:

**1- Primeira letra maiúsculo e o restante minúsculo (Av)**

**2 -Tudo Maiúsculo (AV) .**

**3 - Tudo Minúsculo (av).**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17172673220247)
