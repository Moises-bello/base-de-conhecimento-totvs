---
article_id: 20714054250391
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: b45f62774a7c3187e01d69c66e4d1db543ca649f2f728bcf7ffcebf896a0742b
fetched_at: '2026-06-28T22:37:56.362433+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA717 - Erro: 500
  InternalServerError'
type: support-article
updated_at: '2024-01-22T18:58:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20714054250391-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA717-Erro-500-InternalServerError
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20714054150679) Tempo aproximado para leitura: **00:10:00 min****Ocorrência**No módulo Financeiro, ao tentar realizar o envio de Boleto Online, está recebendo a mensagem **500 InternalServerError**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20714054157719)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Contas a Receber - A partir da release 12.1.33  
  
**Causa**

O erro **500 InternalServerError** possivelmente, pode ser tratar de um erro de cadastro.

**Solução**

É necessário revisar os seguintes pontos abaixo:

**1 - Cadastro da conta** = Por padrão do sistema Protheus, a conta e digito da conta devem ser separados em seus devidos campos, caso utilize o digito da conta junto ao número da conta **exe... 123456-7**, deve adicionar a conta com dígito separado através da **sub conta** utilizada nos **Parâmetros de bancos (FINA130) - Aba = Outros Banco Oficial** e colocar o digito no campo **EE\_DVCTOFI** Exemplo abaixo:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20714021028759)

2 - **Os dados de Fornecedor na Configuração de Contas** deve conter informações, os campos precisam estar preenchidos com a conta bancária do fornecedor **(Tabela FIL - Outras Ações Bancos)** Exemplo abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20714021031703)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20714054165527)

**Importante**  
Caso o pagamento seja feito através de códigos de barras (**E2\_CODBAR**), não é preciso o preenchimento da **conta do fornecedor.**

**3 - Caso os dados de título e fornecedor possuem caracteres especiais**, deve utilizar a função no layout **FWNOACCENT** para remover caracteres especiais **(não aceito pelo banco)**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20714054169239)

**Saiba mais**  
**[Contas a pagar (Comunicação bancária online)](https://tdn.totvs.com/pages/viewpage.action?pageId=734394071)**
