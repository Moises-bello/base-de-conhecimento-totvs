---
content_hash: b492e9c74966365a4d70f0649a590fadb954ac9f7cc5211512a81f33235a8b61
fetched_at: '2026-06-29T00:10:42.814449+00:00'
page_id: '547861135'
product: rm
source: tdn-rm
title: 2.1 Geração de Lançamentos em Lote
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=547861135
version: 23
---

Para gerar os lançamentos financeiros no Sistema (TOTVS Educacional), o usuário deve acessar o Módulo Educacional e realizar os seguintes procedimentos:

Para isso acessar: *Menu TOTVS - Linha RM | Educacional | Módulo Gestão Educacional*

Após acessar o Módulo Educacional, o usuário deve selecionar na aba “Financeiro/Contábil” a opção “Financeiro” para iniciar o assistente de geração dos lançamentos financeiros.

No assistente, preencha os campos com seus respectivos dados para selecionar as parcelas que vão ser gerados os lançamentos:

* **Período Letivo:** Selecionar um ou mais períodos letivos que deseja gerar lançamentos financeiros;
* **Intervalo de Parcelas:** Que pode ser definido por parcela ou data de vencimento, neste passo será definido quais parcelas serão geradas o lançamento;
* **Tipo de Contrato:** Selecionar quais os tipos de contratos que serão gerados;
* **Tipo de Agrupamento:** Não agrupar serviços diferentes em um boleto.
* **Tipo de Agrupamento:** Agrupar no mesmo boleto lançamentos de outros Filiais.
* **Tipo de Parcela:** Selecionar quais os tipos de parcelas que serão geradas.

Selecione os dados comuns dos lançamentos a serem gerados/regerados.

Selecione o filtro de alunos mais adequado à sua necessidade. Os alunos poderão ser filtrados ou adicionados. Caso realize a opção de adicionar alunos, está manterá os alunos filtrados anteriormente.

* **Seleção de aluno**, selecione qual o aluno
* **Seleção de alunos por filtro**, neste caso você pode definir um filtro buscando todos os alunos que pertencem ao curso, habilitação, matriz curricular, turno e turma
* **Seleção de alunos por consulta SQL**, neste caso crie uma consulta SQL para filtrar os alunos que serão gerados os lançamentos
* **Seleção de aluno por Arquivo:** neste caso será possível selecionar arquivos do tipo texto (.txt), CSV (.csv) e planilhas Excel (.xls, xlsx) para filtrar os alunos que serão gerados os lançamentos

Importante

Se utilizada a **seleção de alunos por consultas SQL**, o retorno da consulta não deve retornar registros com o conjunto de registros: **"CODCOLIGADA" e "RA"** duplicados.

Caso hajam registros com valores duplicados, será apresentada uma mensagem informando que houve uma falha ao ativar restrições, por conter valores que violam a sua unicidade.

Selecione as situações de matrícula dos alunos, nas quais deseja realizar a geração de lançamentos em lote. Caso deseje personalizar a sua execução. Caso não sejam selecionadas, todas serão consideradas. Somente as situações de matrículas existentes nos períodos letivos selecionados serão consideradas.

Selecione os serviços a serem considerados no processo. Os serviços listados nesta tela dependem dos alunos e períodos previamente selecionados;

Selecione os planos de pagamentos a serem considerados no processo. Os planos de pagamento listados dependem dos períodos letivos previamente selecionados;

Selecione as matrizes aplicadas a serem consideradas no processo, nesta tela é apresentada a opção de selecionar as matrizes de contratos que não possuem matriz aplicada associada;

Executar

A partir da versão **12.1.2306**, o processo de geração de lançamento em lote poderá ser configurado para utilizar o fracionamento de Jobs, conforme a documentação disponibilizada, abaixo, e utilizando a classe de job *"EduGeraLancSliceableData"*:

* [Configuração de fracionamento de jobs.](https://tdn.totvs.com/x/lpR-I)
Veja também

* [DT Geração de lançamentos - Seleção de alunos por arquivo](https://tdn.totvs.com/pages/viewpage.action?pageId=334348063)
* [TOTVS Educacional - Educacional - EDU - Geração de lançamento pelo Educacional a partir de um filtro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022753651-TOTVS-Educacional-Educacional-EDU-Gera%C3%A7%C3%A3o-de-lan%C3%A7amento-pelo-Educacional-a-partir-de-um-filtro)
* [TOTVS Educacional - Educacional - EDU - Gerar lançamentos em lote](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047541113-TOTVS-Educacional-Educacional-EDU-Gerar-lan%C3%A7amentos-em-lote)
* [TOTVS Educacional - Educacional - EDU - Geração de lançamento pelo Educacional para um aluno especifico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046559233-RM-EDU-Gera%C3%A7%C3%A3o-de-lan%C3%A7amento-pelo-Educacional-para-um-aluno-especifico)
