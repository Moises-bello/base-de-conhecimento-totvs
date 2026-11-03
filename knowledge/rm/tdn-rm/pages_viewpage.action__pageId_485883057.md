---
content_hash: e12c370e37a89a51ef7267cee180fdfa921c5ef6c25e217f3c12c671ac379fa2
fetched_at: '2026-06-29T00:10:20.162348+00:00'
page_id: '485883057'
product: rm
source: tdn-rm
title: Importação de Terceiros-Movimento de Ensino
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=485883057
version: 6
---

**Atenção:**

Os campos deverão ser separados por ponto e vírgula (;).

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Header (1ª Linha) – Pode existir somente um HEADER por arquivo. | | | | | | |
| Nº | Campo | Tipo Campo | Obrigatório | Formato | Descrição | Observações |
| 1 | DATAINICIOPERLET | Data | S | DD/MM/AAAA | Data início do período letivo |  |
| 2 | DATAFIMPERLET | Data | S | DD/MM/AAAA | Data fim do período letivo |  |
|  |  |  |  |  |  |  |
| Detalhe. 2ª e demais linhas: | | | | | | |
| Nº | Campo | Tipo Campo | Obrigatório | Formato | Descrição | Observações |
| 1 | CODCOLIGADA | Numérico | S |  | Código da Coligada | Deverá ter um arquivo para cada coligada, devido o sistema validar a coligada corrente. |
| 2 | CHAPA / CPF | Alfanumérico | S |  | Chapa ou CPF do Funcionário/Professor | Identifica o funcionário na folha de pagamento. Deverá informar o CPF quando o parâmetro Utiliza CPF ao invés da Chapa na importação existente em Opções | Parâmetros | RM Labore | Outros Parâmetros | Parâmetros III estiver marcado, caso contrário informar a CHAPA. O CPF não deverá ter separador. |
| 3 | CODEVENTO | Alfanumérico | S |  | Código do Evento | Caso o campo ‘Compõe Salário’ seja ’S’ o evento informado deverá esta no salário composto do funcionário. |
| 4 | CARGAHORARIA | Hora | S | 000:00  999,99  999 | Carga Horária ou Aulas Semanais | Caso o campo ‘Compõe Salário’ seja ’S’ é obrigatório o preenchimento deste.  Este campo recebe os valores em formato de hora para atividade do tipo E ou C e, inteiro ou decimal para atividade do tipo T. Caso informe um tipo diferente do esperado para atividade, o sistema converte para o formato correto.  Ex.: Campo ORIGEMATIVIDADE = T, Campo CARGAHORARIA = 002:00. No cadastro de movimento de ensino importado, o campo Número de Aula Semanais será = 9,0000 (considerando o fator para cálculo de salário mensal configurado no parametrizador = 4,5). |
| 5 | VALORHORA | Numérico | N | 9999,99 | Valor hora da atividade | Caso o campo ‘Compõe Salário’ seja ‘S’ este campo deverá ser 0 (zero). |
| 6 | ORIGEMATIVIDADE | Alfanumérico | S |  | Origem da atividade | Informe ‘T’ para disciplina/aula Informe ‘E’ para atividade extra Informe ‘C’ para atividade complementar . |
| 7 | DATAINICIO | Data | S | DD/MM/AAAA | Data início da atividade | Este campo é utilizado para calcular o movimento de ensino. |
| 8 | DATAFIM | Data | S | DD/MM/AAAA | Data fim da atividade | Este campo é utilizado para calcular o movimento de ensino. |
| 9 | CODCCUSTO | Alfanumérico | N |  | Código do Centro de Custo no RM Labore | Informar somente centro de custo ‘Ativo’ e se a base estiver parametrizada ‘Usa Centro de Custo’. |
| 10 | COMPOESALARIO | Alfanumérico | N | S ou N | Compõe Salário? (S para ‘Sim’ ou N para’ Não’) | Indica se o registro informado compõe salário do professor, ou seja, se a atividade será considerada na composição do Salário base. Caso não seja informado o default é ‘S’.  Deverá ser ‘S’ quando os campos ‘Valor Fixo’ e ‘Valor Hora’ for igual a zero. Isso porque somente poderá fazer parte do salário do funcionário uma disciplina que utiliza o salário hora do salário composto do funcionário. |
| 11 | VALORFIXO | Numérico | N | 9999,99 | Valor fixo | Caso o campo ‘Compõe Salário’ seja ’S’ este campo deverá ser 0 (zero). |
| 12 | CODFILIAL | Numérico | S |  | Código da filial | Código da filial da turma da disciplina. O sistema irá consistir este campo para localizar a chapa quando a importação for por CPF. Porém sempre será gravado no banco a filial 1. |
| 13 | IDPERLET | Alfanumérico | N\* |  | Identificador do período letivo | Informar somente se a origem da atividade for ‘T’ e neste caso é obrigatório o preenchimento. |
| 14 | CODTURMA | Alfanumérico | S \* |  | Código da Turma | Informar somente se a origem da atividade for ‘T’ e neste caso é obrigatório o preenchimento. |
| 15 | CODDISC ou IDATIVIDADEEXTRA | Alfanumérico | S |  | Código da Disciplina ou Identificação da Atividade Extra | Código da Disciplina ou Atividade Extra. Se a origem da atividade for ‘T’ deverá informar ‘Código da Disciplina’, caso contrário informar ‘Id Atividade Extra’. |
| 16 | QTDALUNOS | Numérico | N |  | Quantidade de Alunos | O sistema irá considerar o valor ‘0’ (Zero) quando não informado. Valor máximo permitido é de 2147483647. |
| 17 | EQUIVHORAAULA | Hora | N | 000:00 | Equivalência de hora aula | Caso este campo não seja informado, será considerado que cada aula tem a duração de 60 min. |
