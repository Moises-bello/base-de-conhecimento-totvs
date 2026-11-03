---
article_id: 115004726267
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 3a11268b60a8ef8890a87eb4d084425855c2aaea835959368c655c900c789c53
fetched_at: '2026-06-28T22:37:55.170253+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - CNAB - Como utilizar
  o IDCNAB nos layouts de remessas e retorno, modelos 1 e 2
type: support-article
updated_at: '2022-02-04T17:49:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115004726267-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-CNAB-Como-utilizar-o-IDCNAB-nos-layouts-de-remessas-e-retorno-modelos-1-e-2
---

**Dúvida**Como utilizar o IDCNAB nos *layouts* de remessas e retorno, modelos 1 e 2.  
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus – Financeiro – A partir da versão 12  
  
**Solução****CNAB modelo 1**

* O **IDCNAB** deve ser configurado no modelo 1 em uma faixa de posições reservada para a empresa/cedente e essa faixa de posições deve conter no mínimo 10 posições para que o número seja criado.
* A utilização em uma faixa de uso reservada para a empresa é necessário, pois o banco não faz nenhuma validação com o **IDCNAB**, então encaminhando nessa faixa de posições reservada o banco retorna a informação na mesma posição enviada.
* No *layout* de retorno essa faixa de posições referente ao **IDCNAB** deve ser informado no registro de detalhe no campo **TITULO.**

**CNAB modelo 2**

* No caso do **modelo 2** o **IDCNAB** normalmente é configurado na faixa de posições referente ao **Seu Número**.
* No *layout* **de retorno** essa faixa de posições referente ao **IDCNAB** deve ser utilizada a variável **TITULO.**

**Saiba Mais:**Para maiores informações e modelos, acesse: <http://tdn.totvs.com/pages/viewpage.action?pageId=242389515>
