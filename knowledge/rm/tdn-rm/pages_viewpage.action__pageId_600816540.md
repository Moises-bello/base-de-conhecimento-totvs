---
content_hash: d1503c525810f0fef70c64be21c744754b528f61ddef3e49eba37440c934067a
fetched_at: '2026-06-29T00:10:57.927889+00:00'
page_id: '600816540'
product: rm
source: tdn-rm
title: Exames e Serviços
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=600816540
version: 12
---

## **ÍNDICE**

1. **Exemplo de Utilização**
2. **Funcionamento do parâmetro "Agrupar Exame"**

itensExemplo de utilização

## **01. Exemplo de Utilização**

* Acesse pelo caminho Cadastros > Unidade de Diagnósticos > Exames e Serviços

* Selecione o filtro desejado
* Clique duas vezes no exame desejado

Será exibido a seguinte tela.

* O checkbox 'Utiliza laudo pré-impresso' desabilita automaticamente caso o setor seja para exames Laboratoriais.  
   Caminho: Cadastro >> Unidade de Atendimento

* Utilização de Materiais do Exame/ Preparações / Vasilhame / Conservante

* A aba Preparo de Exames permite que o usuário edite textos para informar qual a forma de preparo para o exame.   
  Observação: Somente será permitido salvar alterações caso haja mudanças no conteúdo do texto.

SZPREPAROEXAME: PK CODCOLIGADA, CODEXAME

Para enviar ao paciente as instruções de preparo pelo e-mail é necessário definir o relatório de instrução de preparo nos Parâmetros Gerais no DELPHI.

Parâmetros Gerais > Unidades Diagnóstico > Relatório de Instrução de Preparo

Feito isso, agora será enviado um email com o relatório preenchido com as informações do agendamento selecionado. Este email é enviado de dentro do agendamento, na agenda, ao clicar no botão **Enviar Email**, como mostrado abaixo:

O relatório também é enviado ao email fornecido de forma automática ao criar os agendamentos através do Assistente de Agendamento (a partir do RM versão 12.1.2302).

Exemplo de email:

Agrupar Exame

## **02.** **Funcionamento do parâmetro "Agrupar Exame"**

Quando o exame tiver o parâmetro ligado, ele irá agrupar o resultado no mesmo relatório com os outros exames do mesmo pedido (que tiverem o parâmetro ligado também).

**OBS**.: O parâmetro só vai funcionar caso os exames estejam no MESMO PEDIDO. Caso estejam em pedidos diferentes, ele sempre deve imprimir os relatórios separadamente.

Exemplo:

Cadastro do Colesterol Total

Cadastro do Glicose de Jejum

Ao emitir o resultado dos dois exames NO MESMO PEDIDO, vai gerar somente UM relatório com os dois exames. **Será formatado de acordo com o que for selecionado primeiro no grid da tela de resultados laboratoriais**.

Caso eu desmarque o parâmetro para o exame Glicose de Jejum, por exemplo, como o pedido só tem os dois exames, ele vai emitir DOIS relatórios: um para o Colesterol Total e outro para o Glicose de Jejum (que não agrupa no mesmo relatório).

**OBS**.: Ele só vai gerar o relatório 2 a partir do momento que eu fechar a aba do relatório 1.
