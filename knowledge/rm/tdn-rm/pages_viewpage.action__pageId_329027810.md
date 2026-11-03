---
content_hash: 66369648022d2fb5195ba7c25fe6294c02fd8458a3cb9bf16886eee17a87c96b
fetched_at: '2026-06-29T00:08:48.880943+00:00'
page_id: '329027810'
product: rm
source: tdn-rm
title: DT Vinculação de Campus/Polo às Turmas/Disciplinas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=329027810
version: 108
---

# VINCULAÇÃO DE CAMPUS/POLO ÀS TURMAS/DISCIPLINAS

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | **Totvs Educacional** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Cadastro de Turma e Turma/Disciplina* | *Cadastro de Turma e Turma/Disciplina* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Processo - Cadastrar turma e turma/disciplina** | **Processo - Cadastrar turma e turma/disciplina** | | **Processo - Inclusão de disciplinas em turmas** | **Processo - Inclusão de disciplinas em turmas** | | **Processo - Cadastrar turmas/disciplinas** | **Processo - Cadastrar turmas/disciplinas** | |
| **Cadastros Iniciais:** | * *Campus/Polo em Currículo e Oferta | Auxiliares;* * *Para o Processo > Cadastrar turma e turma/disciplina:*   + **Necessário que exista algum Campus/Polo no anexo da Matriz Aplicada.** * **Para os Processos > Inclusão de disciplinas em turmas e **Cadastrar turmas/disciplinas****   + **Necessário que exista turma cadastrada, bem como Campus/Polo no anexo da Matriz Aplicada da Turma.** |
| **Parâmetro(s):** | *N/A* |
| **Ponto de Entrada:** | *N/A* |
| **Tickets relacionados** | *N/A* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | *EDUCACIONAL01-2848* |
| **País(es):** | *Todos* |
| **Banco(s) de Dados:** | *Sql Server e Oracle* |
| **Tabelas Utilizadas:** | *STURMA, STURMADISC e SCAMPUS* |
| **Sistema(s) Operacional(is):** | *Windows 7, 8 e 10* |

## Descrição

Melhoria nos processos que efetuam cadastro de turmas e turmas/disciplinas, para permitir selecionar um campo **Campus/Polo**. Onde ao fim dos processos a turma e /ou turma/disciplina serão criados com o campus/polo preenchido. Os processos que foram alterados são:

* **Cadastrar turma e turma/disciplina** (localizado em: Atividades Acadêmicas | Assistentes);
* **Inclusão de disciplinas em turmas** (localizado em: Atividades Acadêmicas | Assistentes);
* **Cadastrar turmas/disciplinas** (localizado em: Currículo e Oferta | Turmas | Processos).

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações da release 12.1.19.

## Procedimento para Utilização

falseProc-CTTDProcesso - Cadastrar turma e turma/disciplinafalse

* Acessar o Menu | Atividades Acadêmicas | Assistentes | Cadastrar turma e turma/disciplina;
* Selecionar o Período Letivo e a Matriz Aplicada e avançar;

* Neste próximo passo é necessário informar os dados da Turma, sendo que nesta tela é apresentando o campo Campus/Polo para a seleção, sendo este possível selecionar apenas os campus/polo pertencentes à matriz aplicada selecionada no passo anterior. Após informar os dados da turma e informar um campus/polo avançar para o passo seguinte;

* Neste passo é necessário informar os dados da Turma/Disciplina, sendo que nesta tela também será apresentada o campo Campus/Polo para seleção, sendo este possível selecionar apenas os campus/polo pertencentes à matriz aplicada conforme a regra mencionada no passo anterior. Entretanto, é possível selecionar um campus/polo diferente da turma. Após informar os dados da turma/disciplina e informar um campus/polo avançar para o passo seguinte;

* O próximo passo deverá selecionar um período para selecionar as disciplinas, selecione e avance;
* Agora é a hora de selecionar os horários e professores, faça as seleções pertinentes e avance para o processo ser executado;
* O processo então é executado e a turma e as turmas/disciplinas serão criados com os campus/polos informados no processo.
Processo - Inclusão de disciplinas em turmasfalse

* Acessar o Menu | Atividades Acadêmicas | Assistentes | Inclusão de disciplinas em turmas;
* Selecionar uma Turma e avance;
* Selecionar um período para informar quais as disciplinas que serão inseridas e avance;
* Neste passo é necessário informar os dados das turmas/disciplinas, sendo que nesta tela é apresentando o campo Campus/Polo para a seleção, sendo este possível selecionar apenas os campus/polo pertencentes à matriz aplicada da turma selecionada no início do processo. Após informar os dados das turmas/disciplinas e informar um campus/polo avançar para o execução do processo;

* O processo então é executado e as turmas/disciplinas serão criados com os campus/polos informado no processo.
Processo - Cadastrar turmas/disciplinasfalse

* Acessar o Menu | Currículo e Oferta | Turmas | Selecionar uma ou mais turmas | Processos | Cadastrar turmas/disciplinas;
* Selecionar o período que contempla as disciplinas que deseja inserir e avance;
* Selecione o período específico ou todos os períodos e avance;
* Neste passo é necessário informar os dados das turmas/disciplinas, sendo que nesta tela é apresentando o campo Campus/Polo para a seleção, sendo este possível selecionar apenas os campus/polos **comuns** pertencentes à(s) matriz(es) aplicada(s) da(s) turma(s) selecionada(s) no início do processo. Caso não exista nenhum campus/polo **comum** entre as matrizes, não será exibido nenhum item para ser selecionado. Após informar os dados das turmas/disciplinas e informar um campus/polo avançar para o execução do processo;
* O processo então é executado e as turmas/disciplinas serão criados com os campus/polos informado no processo.

divs
