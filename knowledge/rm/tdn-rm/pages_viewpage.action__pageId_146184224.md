---
content_hash: 20d48c80e758acd7fe71df8d80e74d777ffd0feabf2bc27803526457c0a3cec4
fetched_at: '2026-06-29T00:05:55.824585+00:00'
page_id: '146184224'
product: rm
source: tdn-rm
title: Utilizando a atividade "Enviar E-mail"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=146184224
version: 29
---

# Índice:

---

.\*ndice:

# Objetivo:

---

      Exemplificar a criação de uma Fórmula Visual que utilize a atividade "Enviar E-mail".

# Criando a Fórmula Visual:

---

No exemplo, criaremos uma Fórmula Visual que enviará um E-mail com uma imagem anexo.

falseCriando a Fórmula VisualAtividade "Enviar E-mail"

      Primeiramente é necessário arrastar a atividade "Enviar E-mail" para o "fluxo de trabalho" sequencial em sua Fórmula Visual.

      Depois adicionar a atividade ao fluxo de trabalho. É necessário configurar suas propriedades.

      Nas **Propriedades** da atividade, preencha os campos conforme o exemplo, onde:

**Assíncrono:** Permite que os gatilhos e processos da Fórmula Visual que enviam e-mails, não sejam, gargalos de performance, porém é importante ficar atento, pois com os envios assíncronos habilitados, a fórmula visual e o processo principal não são interrompidos em caso de falha no envio.

**Assunto:** Deve ser preenchido com o assunto do e-mail.

**Texto do e-mail:** Deve ser preenchido com o corpo do e-mail.

**Destinatários:** Lista de e-mails dos destinatários.

**Remetente:** Quem enviará o e-mail.(Usuário/Coligada/ColigadaGlobal)

Quando utilizado a opção de remente "Custom" é necessário informar senha e usuário para que a autenticação no SMTP seja realizada.

Atividade "Executar Consulta SQL"

      No exemplo abaixo foi utilizado a atividade **"Executar Consulta SQL"**, onde a consulta sql associada a atividade retornará uma imagem do banco de dados.Para mais informações sobre esta atividade acesse [Consulta SQL](http://tdn.totvs.com/x/hJi2C).

      Informe o nome da Consulta SQL que será utilizada, conforme exemplo abaixo

Informando Anexo

      Depois adicione e configure a atividade **"Consulta SQL"** no fluxo de trabalho. É necessário configurar suas propriedades **"Anexar Arquivo"** e **"Nome do Arquivo"** da atividade **"Enviar E-mail"**.

      A propriedade "Nome do Arquivo" deve conter a extensão que o arquivo receberá ao ser anexado ao e-mail. Conforme exemplo o arquivo terá a extensão **".JPG"**

      Como a consulta sql retornará a imagem, é necessário associar a propriedade "Anexar Arquivo" aos atributos desta atividade. Para esta associação, dê um duplo clique no ícone  na propriedade "Anexar Arquivo".

      Expanda a atividade "Consulta SQL" e informe as opções:

      Clique em OK para que o atributo seja inserido na propriedade da atividade.

Observação

A propriedade Item foi setada como Item["Imagem"] pois é este o campo que é retornado na consulta SQL vinculada a atividade "Executar Consulta SQL".

      

       Salve e execute a Fórmula Visual

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.15 ou Superiores

false

**Processo:** Utilizando a atividade "Enviar E-mail"

falsefalse

**Status:** Finalizado

false

**Data:** 22/02/2017

false

**Autores:**
