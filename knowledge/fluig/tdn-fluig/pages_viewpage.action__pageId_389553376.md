---
content_hash: f22702d5905ed47a0b26d0e00091499ec3abea92119087c6544b3cb1a58a5198
fetched_at: '2026-06-28T21:35:26.674911+00:00'
page_id: '389553376'
product: fluig
source: tdn-fluig
title: BPM 097 - Por que dados de formulários são perdidos em atividades paralelas?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=389553376
version: 9
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**Fluig

# Ocorrência

Ao preencher um formulário de forma simultânea em atividades paralelas, a informação enviada por um dos usuários é perdida.

# Causa

Há uma regra para formulário em atividades paralelas a qual valida as versões do mesmo, onde quando há usuários preenchendo o formulário simultaneamente e um usuário envia suas informações, os demais usuários ao tentar o envio receberão uma mensagem informando que houve alteração e que será necessário atualizar seu formulário, a fim de que os usuários visualizem o que foi atualizado.

Tendo em consideração que o fluig não possui formulário onde as informações são salvas em tempo real, e sim quando os dados são populados (enviados ao banco de dados), essa validação foi criada para que não sejam perdidas informações durante o processo.

Sabendo do funcionamento dessa validação, quando há um formulário com versão única não é possível aplicar a mesma, pois toda vez que há uma movimentação a versão é sobreposta, diferente de quando há um formulário versionado, onde os registros são salvos separadamente sendo possível aplicar a validação.

# Solução

Criar o formulário versionado para esse cenário. Caso seu projeto já esteja em funcionamento será necessário retirar a versão única do mesmo e liberar versão/exportá-lo para o servidor.

Na web, acesse **Configuração de Processo**, acione **Propriedades** e acesse a aba **Formulário**:

No Studio, acesse **Propriedades** e acione a aba**Formulário:**

Importante!

Vale lembrar que, para solicitações em andamento não será possível a alteração através da conversão, pois não é possível a conversão de formulários.
