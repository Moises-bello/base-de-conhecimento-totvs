---
article_id: 24235150136855
category: Comércio Exterior - Easy Export Control - Cadastros
content_hash: 269a736948f253f7b89835c3a63cfd6e2e6b0f8d63e49f65b6b2ceb184c7ecc1
fetched_at: '2026-06-28T22:36:57.350539+00:00'
product: protheus
section_id: 1500001549302
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - DUE erro: O atributo
  ATT_XXXX para o NCM XXXXXXX ? obrigatório'
type: support-article
updated_at: '2024-11-07T18:29:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24235150136855-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-DUE-erro-O-atributo-ATT-XXXX-para-o-NCM-XXXXXXX-obrigat%C3%B3rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24235160869527) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como corrigir o erro ao transmitir o arquivo DUE: O atributo ATT\_XXXX para o NCM XXXXXXX ? obrigatório ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – *Easy Export Control* – a partir da versão 12.1.2210   
  
**Solução**Houve uma adequação no produto na rotina Cadastro de **Atributos Portal Único** e **Catálogo de Produtos** para a DUE no SIGAEEC. Os passos seriam :  
   
1- Acessar o menu Atualizações-> Portal Único -> **Atributos Portal Único (EICAT140)** e atualizar os atributos. Verificar em qual ambiente esta sendo atualizado no portal único (1- produção ou 2- teste através do parâmetro MV\_EIC0074). Certificar que o ncm e atributo em questão se encontram no cadastro.  
   
2- Acessar o menu Atualizações-> Portal Único -> **Catalogo de Produtos (EECCP400)**, deve-se preencher os seguintes campos:

A) Aba Catalogo de Produtos:

* CNPJ Raiz **(EK9\_CNPJ)**.
* Modalidade = 2 - Exportação **(EK9\_MODALI).**
* NCM **(EK9\_NCM)**.
* ID Manual **(EK9\_IDMANU)**.
* Versão Manual **(EK9\_VSMANU)**.
* Descrição Complementar **(EK9\_DSCCOM)**.

B) Relação de Atributos:

* Será apresentado o(s) atributo(s) da ncm preenchida.

C) Relação de Produtos x Origem/Fabricantes:

* Produto Referencia **(EKA\_PRDREF)**.
* Código de Fabricante **(EKB\_CODFAB) .**
* Loja **(EKB\_LOJA)**.

   
3- Acessa a rotina Embarque de Exportação **(EECAE100)** selecione o processo, clique na opção alterar . selecione o(s) item(ns) para alterar e preencha os campos Id Atual**(EE9\_IDPORT)** e Versão Atual **(EE9\_VATUAL)**.   
   
Após realizar este procedimento ao transmitir a DUE as informações de atributo e destaque são informados no xml atavés das tags *TypeCode* e *Description*.    
 

Exemplo:  
**<TypeCode>ATT\_26</TypeCode>**  
**<Description>01</Description>**
