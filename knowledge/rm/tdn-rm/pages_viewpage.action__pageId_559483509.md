---
content_hash: 7ed9cb97e9373f37906be95dd014413631ec59be84ac5d7ac5bc17f78ef39ef1
fetched_at: '2026-06-29T00:10:47.571661+00:00'
page_id: '559483509'
product: rm
source: tdn-rm
title: DT Liberação de frequência diária na Turma/Disciplina
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=559483509
version: 7
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Educacional |
| Linha de Produto: | Linha RM |
| Segmento: | Educacional |
| Módulo: | Turma/disciplina |
| Função: | Processo: Liberar Frequência |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DEDUMOBILE-3324](https://jiraproducao.totvs.com.br/browse/DEDUMOBILE-3324) |

## **02. SITUAÇÃO/REQUISITO**

Permitir que o professor e/ou operador do sistema libere a frequência diária na visão: Turma/disciplina através do processo: "Liberar frequência diária", para que os alunos consigam visualizar a frequência no portal.

Essa funcionalidade está disponível apenas no RM.exe.

## **03. SOLUÇÃO**

Criando o processo para que o professor e/ou operador do sistema, possa liberar a frequência diária através do processo: Liberar frequência diária na visão: Turma/Disciplina.

Para liberar essa funcionalidade, é necessário conceder a permissão em: Serviços Globais | Perfil | Educacional | Currículo e Oferta | Oferta | Turmas/Disciplinas | Liberar frequência diária

Essa funcionalidade só será permitido se o parâmetro: *"Justificar as faltas e liberar frequência pelo coordenador definido na turma/disciplina"* **NÃO** estiver marcado.  
Esse parâmetro está disponível em: Configurações | Parâmetros | Educacional | Secretaria | Notas/Faltas.

# Execução do processo

O Usuário pode selecionar uma ou mais Turma(s)/disciplina(s)pra a execução do processo.  
Ao iniciar o processo, será exibido uma janela para que o usuário informe um período de datas, para a atualização dos registros do(s) plano(s) de aula da(s) Turma(s)/disciplina(s) selecionada(s) pelo usuário.

Informar o período desejado, e em seguida clicar no botão executar.

Após executar o processo, será exibido um *log* do processo, onde será informado os dados:

* A data iniciar o final (De acordo com a data informada pelo usuário);
* Quantidade de frequência(s) liberada(s)
* O status da liberação, se a mesma já foi liberada ou não;
* Código do Período Letivo;
* Código da Turma;
* Código da disciplina;
* Data em que a frequência foi liberada (de acordo com a data do Plano de aula);
* Código da Aula (Código da Aula do Plano de Aula);
* Horário da Aula;
* Código Coligada e Código da Disciplina.

Após liberar a frequência, o campo de controle "FrequenciaDispWeb" do plano de aula (Campo FREQUENCIADISPWEB da tabela de nome SPLANOAULA terá o valor igual a 1, indicando que a frequência foi liberada).

## **04. ASSUNTOS RELACIONADOS**

Para mais informação sobre outras formas de liberação da Frequência diária: acessar o documento disponível [aqui.](https://tdn.totvs.com/x/LmzNI)
