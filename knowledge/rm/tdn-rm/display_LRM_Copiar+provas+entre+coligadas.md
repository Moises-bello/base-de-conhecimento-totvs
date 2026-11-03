---
content_hash: f015e4177ed4d238e456512d7f68a7ceaa207efd8a18d7488b08d531a0f5dc47
fetched_at: '2026-06-29T00:09:34.081344+00:00'
page_id: '425459136'
product: rm
source: tdn-rm
title: Copiar provas entre coligadas
type: documentation
url: https://tdn.totvs.com/display/LRM/Copiar+provas+entre+coligadas
version: 3
---

Este processo permite ao usuário selecionar uma ou mais provas da coligada corrente e realizar a cópia dessa prova para uma coligada de destino. Essa cópia irá levar os demais cadastros que envolvem uma prova, tais como: Área de conhecimento, Matéria, Questões, Níveis de dificuldade, Classificação, Grupo e Período.  
   
Ao executar o processo é preciso definir as seguintes informações:

* Coligada(s) de destino: Neste campo, devemos informar para qual(is) coligada(s) o sistema irá copiar as provas;
* Copiar questões vinculadas à prova (Tabela BDEFQUESTAO): Este parâmetro deverá ser marcado quando desejamos copiar as questões vinculadas às provas normais;
* Copiar configurações das questões vinculadas à prova dinâmica (Tabela BCONFIGPROVA): Este parâmetro deverá ser marcado quando desejamos copiar a configurações definidas para a proava dinâmica de área, matéria e quantidade de questões por grau de dificuldade;
* Copiar grupos vinculados à prova: Este parâmetro deverá ser marcado quando desejamos copiar os grupos contidos nas provas para a coligada de destino;
* Copiar períodos vinculados à prova: Este parâmetro deverá ser marcado quando desejamos copiar os períodos contidos nas provas para a coligada de destino;

Durante a execução do processo é exibido os seguintes passos:  
   
**Seleção de provas -** são apresentadas todas as provas (ativas) para que seja informado o código da prova de destino (novo). Se o sistema não encontrar um código igual na coligada de destino, ele irá sugerir o mesmo código, mas caso encontre, o usuário deverá informar manualmente o novo código para coligada de destino.

**Seleção de áreas -** são apresentadas as Áreas de conhecimento para que seja informado o código na coligada de destino. Se o sistema não encontrar um código igual na coligada de destino, ele irá sugerir o mesmo código, mas caso encontre, o usuário deverá informar manualmente ou utilizar o já existente marcando o parâmetro "Não criar novas áreas de conhecimento, desejo utilizar as áreas já cadastradas na coligada de destino com mesmo nome".

**Seleção de matérias -** são apresentadas as Matérias para que seja informado o código na coligada de destino. Se o sistema não encontrar um código igual na coligada de destino, ele irá sugerir o mesmo código, mas caso encontre, o usuário deverá informar manualmente ou utilizar o já existente marcando o parâmetro "Não criar novas matérias, desejo utilizar as matérias já cadastradas na coligada de destino com o mesmo nome".

**Seleção de classificações -** são apresentadas as Classificações para que seja informado o código na coligada de destino. Se o sistema não encontrar um código igual na coligada de destino, ele irá sugerir o mesmo código, mas caso encontre, o usuário poderá selecionar uma classificação já existente da coligada de destino através da lookup ou informar um novo código para a classificação. Importante: o usuário somente conseguirá visualizar as classificações da coligada de destino se houver permissão nelas.

Ao final o usuário terá todas as provas copiadas para a coligada de destino de acordo com o log de execução do processo.

**Observação**

Para executar o processo é preciso que tenha pelo menos uma prova ativa.

Se as questões da prova forem copiadas e esta(s) possui(rem) nível de dificuldade vinculada, será verificado se já existe o nível com o mesmo nome na coligada de destino, caso exista, a questão na coligada de destino passa a consistir com o nível já cadastrado. Caso não exista este nível, um novo nível será inserido e vinculado a questão na coligada de destino.
