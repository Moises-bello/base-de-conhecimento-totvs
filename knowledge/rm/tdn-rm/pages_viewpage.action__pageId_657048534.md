---
content_hash: efff173d956093928020dbf1a4607be32e49caafc865f2ff7da4c4d7bd162936
fetched_at: '2026-06-29T00:11:13.155330+00:00'
page_id: '657048534'
product: rm
source: tdn-rm
title: Liberar / Cancelar Frequência diária
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=657048534
version: 14
---

Esse processo tem como objetivo permitir que o professor e/ou operador do sistema libere ou cancele a frequência diária na visão: Turma/disciplina através do processo: "Liberar/Cancelar frequência diária", para que os alunos consigam visualizar a frequência no portal.

Essa funcionalidade está disponível apenas no RM.exe.

Criado o processo para que o professor e/ou operador do sistema, possa liberar ou cancelar a frequência diária através do processo: Liberar/Cancelar frequência diária na visão: Turma/Disciplina.

Para liberar essa funcionalidade, é necessário conceder a permissão em: Serviços Globais | Perfil | Educacional | Currículo e Oferta | Oferta | Turmas/Disciplinas | Liberar /Cancelar frequência diária

Essa funcionalidade só será permitido se o parâmetro: *"Justificar as faltas e liberar frequência pelo coordenador definido na turma/disciplina"* **NÃO** estiver marcado.  
Esse parâmetro está disponível em: Configurações | Parâmetros | Educacional | Secretaria | Notas/Faltas.

## **01. EXECUÇÃO DO PROCESSO**

O Usuário pode selecionar uma ou mais Turma(s)/disciplina(s) para a execução do processo.  
Ao iniciar o processo, será exibido uma janela para que o usuário informe um período de datas, para a atualização dos registros do(s) plano(s) de aula da(s) Turma(s)/disciplina(s) selecionada(s) pelo usuário.

* O botão **Executar**, só será habilitado se os campos "Data inicial" e "Data final" forem preenchidos.
* O sistema não permite Liberar/Cancelar a frequência para uma data futura.

Apenas serão processadas a liberação ou o cancelamento da liberação das frequências diárias, caso exista alguma etapa cadastrada com os campos "Data inicial" e "Data final" preenchidas no cadastro da etapa que correspondam ao mesmo intervalo de datas definidas durante a execução deste no processo.

## **Liberar frequência diária**

Para Liberar a Frequência diária, o usuário deverá informar o período desejado e marcar a opção: **Liberar Frequência**, após informar os campos, clicar no botão executar.

Após executar o processo, será exibido um *log* do processo, onde será informado os dados:

* A data iniciar o final (De acordo com a data informada pelo usuário);
* Quantidade de frequência(s) liberada(s);
* O status da liberação, se a mesma já foi liberada ou não;
* Código do Período Letivo;
* Código da Turma;
* Código da disciplina;
* Data em que a frequência foi liberada (de acordo com a data do Plano de aula);
* Código da Aula (Código da Aula do Plano de Aula);
* Horário da Aula;
* Código Coligada e Código da Disciplina.

Após liberar a frequência, o campo de controle "FrequenciaDispWeb" do plano de aula (Campo FREQUENCIADISPWEB da tabela de nome SPLANOAULA terá o valor igual a 1, indicando que a frequência foi liberada).

## **Cancelar liberação de frequência diária**

Esse processo tem como objetivo, cancelar a liberação da frequência diária, isso é, ao executar esse processo, as frequências que estavam liberadas para visualização para os alunos/responsáveis, passam a ficar indisponíveis.

false

Para liberar a frequência para os alunos/responsáveis, basta executar o processo de liberação de frequência através do Portal ( Login do professor) ou pelo RM.exe.

Para Cancelar a Frequência diária, o usuário deverá informar o período desejado e marcar a opção: **Cancelar liberação de frequência diária**, após informar os campos, clicar no botão executar.

Após executar o processo, a frequência diária será cancelada e ficará disponível para uma nova liberação.

Para mais informação sobre outras formas de liberação da Frequência diária: acessar o documento disponível [aqui.](https://tdn.totvs.com/x/LmzNI)

Importante!!!

Caso a Instituição de Ensino utilize a visualização da Frequência após a liberação do professor, ou seja, caso os parâmetros abaixo estejam **MARCADOS** **em Educacional | Secretaria | Notas/faltas |**  
      **- Permitir a visualização das notas e faltas da etapa somente após a liberação do professor**  
**- Permitir a visualização das notas das avaliações e faltas somente após a liberação do professor**

Ao executar o processo de **"Cancelamento de liberação da frequência diária"**,**o contador de faltas** da tabela SNOTAETAPA (Coluna: NOTAFALTA) será **ZERADO**. Para que as faltas digitadas continuem sendo contabilizadas, mesmo após realizar o processo de cancelamento de liberação, os parâmetros citados acima devem estar **DESMARCADOS**.
