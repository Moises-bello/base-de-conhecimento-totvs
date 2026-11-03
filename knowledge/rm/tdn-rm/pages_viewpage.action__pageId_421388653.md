---
content_hash: 55ed4f003e6e28fc6028660b0d7719d915c31147e2af7cb9ddcc446f3fd0d208
fetched_at: '2026-06-29T00:09:17.796057+00:00'
page_id: '421388653'
product: rm
source: tdn-rm
title: Importação do Arquivo de Reconciliação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388653
version: 3
---

Através do menu Movimentações Bancárias/ Integração Bancária / Reconciliação Bancária, serão exibidos os registros já importados em processos de captura anteriores e ainda não conciliados, assim como os registros de extrato de caixa do sistema para o período definido pelo usuário.

Através do processo "Importação de Arquivo de Reconciliação",é exibido um wizzard onde o usuário pode importar um arquivo vindo do banco, informando qual o arquivo a ser importado e o banco utilizado. É necessário que o banco seja informado, pois o sistema Financeiro permite o cadastro do mesmo banco (mesmo código FEBRABAN) mais de uma vez, possibilitando a utilização de diferentes layouts para esse banco.

Ao avançar o processo, o sistema apresentará uma tela para que o usuário informe uma conta caixa para cada uma das contas correntes existentes no arquivo de conciliação. Se a conta corrente em questão estiver relacionada a apenas uma conta caixa no cadastro do sistema, essa informação será preenchida automaticamente. A informação da conta caixa irá definir a coligada onde serão procurados os extratos.

A partir dessas informações, os dados importados serão apresentados na tela.  Na parte superior estão os dados importados do arquivo e, na inferior, os extratos gravados na base de dados.
