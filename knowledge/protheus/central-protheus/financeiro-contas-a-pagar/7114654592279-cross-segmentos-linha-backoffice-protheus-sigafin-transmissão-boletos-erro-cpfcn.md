---
article_id: 7114654592279
category: Financeiro - Contas a Pagar
content_hash: 5d7391ef1e211540ec06f7a0ec0807e2dbd11f6bcb9f247bc4bac207fc18d389
fetched_at: '2026-06-28T22:38:09.853084+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Linha BackOffice Protheus - SIGAFIN - Transmissão Boletos
  - Erro CPF/CNPJ Beneficiário Inválido!
type: support-article
updated_at: '2022-10-05T22:57:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7114654592279-Cross-Segmentos-Linha-BackOffice-Protheus-SIGAFIN-Transmiss%C3%A3o-Boletos-Erro-CPF-CNPJ-Benefici%C3%A1rio-Inv%C3%A1lido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:10:00 min****Ocorrência**No módulo Financeiro, ao tentar realizar a transmissão de boletos pela FINA710, ocorre a mensagem pelo Monitor de Pendencias:  **Erro CPF/CNPJ Beneficiário Inválido!  
  
![FINA710.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7114653234839/FINA710.png)**  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**Esse incidente ocorre, pois no cadastro dos bancos e clientes envolvidos na transmissão, não possui o CPF/CNPJ cadastrado.   
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acessar o cadastro de banco e cadastrar o **CNPJ** da agencia ao qual voce tem conta pagadora / recebedora **A6\_CGC**  
2. Acessar o cadastro do cliente e informar o **CPF/CNPJ** do Cliente **A1\_CGC**  
3. Realizar novamente a transmissão e validar no Monitor se a mensagem não exibi mais.

Saiba mais:

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA710 - Configuração e Funcionalidade do Novo Gestor Financeiro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7019775569047)
