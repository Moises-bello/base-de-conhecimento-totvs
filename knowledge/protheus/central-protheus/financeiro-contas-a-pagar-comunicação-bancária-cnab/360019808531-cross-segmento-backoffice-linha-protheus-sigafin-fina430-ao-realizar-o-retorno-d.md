---
article_id: 360019808531
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: c4d0238d8366b076fb6d5a672726484b36d58f3f9d7eee2cf3d49bd4385a7ac1
fetched_at: '2026-06-28T22:37:55.205197+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA430 - Ao realizar
  o retorno de CNAB de pagamento é apresentado mensagem que o arquivo está corrompido
type: support-article
updated_at: '2026-01-19T13:53:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019808531-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA430-Ao-realizar-o-retorno-de-CNAB-de-pagamento-%C3%A9-apresentado-mensagem-que-o-arquivo-est%C3%A1-corrompido
---

**Ocorrência**  
Ao realizar o retorno de pagamento CNAB através da rotina **FINA430** é apresentado a informação de que o arquivo está corrompido de acordo com os **Parâmetros de Bancos**.  
  
**Ambiente**  
Cross Segmento - Backoffice Linha Protheus – Financeiro – A partir da versão 12.1.17  
  
**Causa**  
A mensagem é apresentada pois a rotina realiza validação do arquivo de retorno e do cadastro de **Parâmetros de Bancos** deste **banco, agencia, conta** e **subconta**. Ou seja, caso o arquivo de configuração utilizado esteja com número de bytes diferente do que foi configurado no cadastro **Parâmetros de Bancos** para o Banco informado nos parâmetros da rotina, o sistema exibirá a mensagem "Arquivo Corrompido".

Por exemplo: Quando o arquivo de retorno é modelo 2 (240 bytes) e no cadastro de **Parâmetros de Bancos** o número de bytes está com o conteúdo 400(modelo 1) ou 200 bytes.  
  
**Solução**  
Verificar se o cadastro **Parâmetros de Bancos** foi configurado com o **numero de Byte**s correto e se o **Banco, agencia, conta** e **subconta** informados na rotina de processamento de retorno CNAB (**FINA430**) estão corretos (de acordo com o arquivo modelo utilizado).

**Saiba mais:**

[**FINA473 - Erro ao importar: Arquivo de Extrato Invalido**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19820730113943-Cross-segmentos-TOTVS-BackOffice-Linha-Protheus-FINA473-Erro-ao-importar-Arquivo-de-Extrato-Invalido)

[**FINA430 - Retorno CNAB a Pagar**](https://tdn.totvs.com/pages/viewpage.action?pageId=312166838)
