---
article_id: 360035730393
category: RH - Funcionários
content_hash: b6aa20614a88089324f71d8f38767f48f04758c0fd16715d78e191080adcb767
fetched_at: '2026-06-28T22:43:27.686046+00:00'
product: protheus
section_id: 360011909593
source: central-protheus
title: RH - Linha Protheus - GPE - Como retirar validação da tabela SA6 - Bancos/Agências
  do campo RA_BCDEPSA
type: support-article
updated_at: '2025-08-18T18:56:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035730393-RH-Linha-Protheus-GPE-Como-retirar-valida%C3%A7%C3%A3o-da-tabela-SA6-Bancos-Ag%C3%AAncias-do-campo-RA-BCDEPSA
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16091541086743)** Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como retirar validação da tabela SA6 - Bancos/Agências do campo RA\_BCDEPSA, para que o usuário possa informar o conteúdo?   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Acesse o Módulo **Configurador**;  
2. Acesse **Base de Dados - Dicionários - Arquivos** e busque pela tabela **SRA**;  
3. Abra a visualização dos campos, localize o campo **RA\_BCDEPSA** e clique em **Alterar**;  
4. Na aba **Opções,**deixe em branco o conteúdo do campo **Cons. Padrão;  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045820294)**5. Na aba **Validações,**retire o conteúdo do campo **Val. Usuário  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045820454)**6. Após esses ajustes, clique em **Salvar;**7. Clique em **Confirmar**, no ícone ![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046680073);  
8. Clique em **Atualizar Base de Dados**, no ícone ![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046680113);  
9. Avance as telas para que o sistema efetive o ajuste no campo e ao final, clique em **Finalizar.**Após esses procedimentos, o campo ficará livre para edição, sem validação com a tabela de Bancos/Agências - SA6 do Financeiro.

**Atenção:**

* Os campos: **banco, agência e conta** são desconsiderados no grupo de campos do Configurador (SIGACFG), pois podem ou não estar vinculados ao cadastro de bancos (SA6). O vínculo obrigatório ao cadastro de bancos, implicaria em uma série de validações do módulo Financeiro (SIGAFIN), que poderia não atender a todos os clientes.
* A alteração do campo é caracterizada como customização, portanto a sua alteração e validação é de responsabilidade do cliente.

**Saiba Mais:**

[Picture dos Campos - Dicionário de Dados](https://tdn.totvs.com/pages/viewpage.action?pageId=22479526)  
[GPE006OUTROS\_GPEM680\_Alteração\_da\_picture\_no\_campo\_RA\_BCDEPSA](https://tdn.totvs.com/pages/viewpage.action?pageId=233752727)  
[RH - Linha Protheus - GPE - Como cadastrar banco/agência com dígito verificador X](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwh6QdTUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBm2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1Mjk2NTc1NC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1jYWRhc3RyYXItYmFuY28tYWclQzMlQUFuY2lhLWNvbS1kJUMzJUFEZ2l0by12ZXJpZmljYWRvci1YBjsIVDoOc2VhcmNoX2lkSSIpZTU0NjQ2NTUtMjRmYy00NzQ1LThiMTEtNDRmZWI5NDBkZmQxBjsIRjoJcmFua2kJOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIPUkFfQkNERVBTQQY7CFQ6EnJlc3VsdHNfY291bnRpAoUB--90b95ddb210031508a2b38f7626ae1be1d2610fa)  
[RH - Linha Protheus - GPE - Quais variáveis que podem ser utilizadas para desenvolver um CNAB de Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwi%2B%2FDrTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBuGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyNjE0MzkzNC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtUXVhaXMtdmFyaSVDMyVBMXZlaXMtcXVlLXBvZGVtLXNlci11dGlsaXphZGFzLXBhcmEtZGVzZW52b2x2ZXItdW0tQ05BQi1kZS1Gb2xoYS1kZS1QYWdhbWVudG8GOwhUOg5zZWFyY2hfaWRJIillNTQ2NDY1NS0yNGZjLTQ3NDUtOGIxMS00NGZlYjk0MGRmZDEGOwhGOglyYW5raQc6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIg9SQV9CQ0RFUFNBBjsIVDoScmVzdWx0c19jb3VudGkChQE%3D--b342786acac31ad8e5ebaa1c8b86c8a3e7decf0d)
