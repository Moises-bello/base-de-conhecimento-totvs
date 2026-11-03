---
content_hash: e29e67996ef98d6dde7bf1b6ccfb6917bcda9a76fc107aa3609f88a448cf1875
fetched_at: '2026-06-29T00:09:14.330481+00:00'
page_id: '421385201'
product: rm
source: tdn-rm
title: Identificação Parâmetros Gerais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385201
version: 5
---

---

**Subdivisões do Projeto**

Informe a descrição para o 1º nível das tarefas.

**Moeda Corrente**

Informe a moeda corrente dos projetos. Caso a moeda do Projeto não seja informada nos parâmetros do projeto, essa moeda será considerada.

**Lista de Documentos**

Informar algum modelo de documento.

**Descrição da Natureza do Insumo**

Este campo representa a natureza do insumo, antes, conhecido como Grupo DNIT. Todas as telas do sistema, onde antes tinham o campo Grupo DNIT passará a aceitar a descrição informada pelo usuário.  A descrição definida será replicada para todos os projetos de todas as coligadas. Incluindo projetos de revisão, licitação, modelo e global.

**Integrado com o Protheus**

**Permitir data retroativa no faturamento de contratos**

**Abrir anexo de projetos de revisão múltipla automaticamente na visão de projetos:**São duas as possibilidades de abertura automática de anexos na visão de projeto, os Projetos Recentes utilizados pelo usuário e os Projetos de Revisão Múltipla.

**Permite realinhamento sobre o total do contrato**

O contrato será calculado considerando os valores atuais, ou seja, o somatório do valor total dos itens.  
Onde valor total do item = Qtde Contratada \* Valor unitário atual

**Obriga fechar telas abertas do calculo do projeto**  
   
**Pasta padrão do backup agendado (Caminho Compartilhado)**

Nesse campo deve ser informado um caminho com uma pasta compartilhada, onde os arquivos que serão exportados utilizando Excel ou no Backup do Projeto serão salvos. Verifique todas as configurações para  para que o processo seja executado.

**Cálculo do projeto valida a quantidade dos insumos da tarefa com as quantidades pedidas e consumidas do mesmo.**

Ao marcar este parâmetro, quando for calculado o projeto ou alterado a quantidade de tarefas, faz com que seja validado a quantidade necessária de insumos e a quantidade pedida de cada tarefa. Caso exista divergência, será mostrado uma mensagem de erro.

Ex.: Tarefa A: Insumo B quantidade necessária X e já possui Y de quantidade pedida.

Ao executar o cálculo onde a quantidade necessária de um insumo é diferente da quantidade pedida em uma das tarefas, é exibido o seguinte erro:

O erro também é exibido ao salvar caso a quantidade seja alterada diretamente na grid da planilha de atividades:

---
