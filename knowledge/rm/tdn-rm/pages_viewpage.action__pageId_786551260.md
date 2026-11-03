---
content_hash: c1d7ca6b7bd066bdbb8d163b55bab9a33deac8246595fbb45e168703e05bd367
fetched_at: '2026-06-29T00:11:39.010813+00:00'
page_id: '786551260'
product: rm
source: tdn-rm
title: Histórico de atendimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=786551260
version: 26
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
   1. **Visualização da triagem**
   2. **Propriedades Exibidas no Grid**
3. **Filtros avançados**
4. **Impressão**
5. **Parâmetros utilizados**
6. **Filtro de tela**
   1. **Filtro de Período**
   2. **Filtro de Tipo de Atendimento**
   3. **Filtro de Atendimentos**

Histórico de atendimentoVisão Geral

## **01. VISÃO GERAL**

Esta tela tem como objetivo mostrar de maneira centralizada o histórico de todas as informações registradas para o paciente.

Exemplo de utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

1. Ao acessar a tela, virá carregada com os 100 primeiros registros do paciente ordenados de forma decrescente;
2. Somente serão exibidas os registros que foram '**finalizados'**;
3. Botão **"Carregar mais registros"** carrega mais 100 registros na *timeline* de histórico;
4. Botão **"Expandir"** exibe o resumo das informações contidas em cada registro;
5. Botão "Visualizar" encaminha o usuário ao registro abrindo uma nova guia no navegador; Caso o registro aberto pertença a outro atendimento, o contexto do prontuário será automaticamente alterado para o atendimento correspondente ao registro selecionado no histórico clínico. Com isso, o usuário poderá manipular os dados desse atendimento, incluindo a criação de novos registros dentro desse mesmo contexto.

## **02.1 VISUALIZAÇÃO DA TRIAGEM PELO HISTÓRICO DE ATENDIMENTO**

A visualização da triagem via histórico de atendimento segue algumas regras específicas conforme descrição abaixo:

**Triagem Legada ou Externa (PEP1, PEP2 ou Versão < 2410)**

* Não deve abrir nova aba ou tela externa.
* A visualização é permitida **exclusivamente** através da expansão da "aleta" (accordion) no próprio grid do Histórico.
* Exibição de alerta em tela

**Triagem em versão >2410**

* Ao clicar no ícone de visualização ("olhinho"), o usuário deve ser redirecionado para a tela oficial de Classificação de Risco.
* Ao expandir a aleta no histórico, o sistema deve carregar e exibir fielmente os dados capturados durante a triagem (Sinais vitais, queixa principal, etc.).

**Triagem Legada ou Externa (PEP1, PEP2 ou Versão < 2410)**

* Não deve abrir nova aba ou tela externa.
* A visualização é permitida **exclusivamente** através da expansão da "aleta" (accordion) no próprio grid do Histórico.
* Exibição de alerta em tela

## **02.2 PROPRIEDADES EXIBIDAS NO GRID DE HISTÓRICO DE ATENDIMENTO**

A partir da versão 12.1.2602, foi adicionada a coluna de grupo profissional do prestador na timeline de histórico de atendimento. O campo foi adicionado ao lado do prestador, assim como mostrado na imagem a seguir.

A coluna lista a sigla do conselho profissional e o número vinculado ao usuário que realizou o registro. Exemplo:  CRM: 93XXXX/RJ

Foram feitas também modificações na descrição de propriedades nessa tela:

* A coluna com a nomenclatura "Médico(a) responsável" foi modificado para "Responsável".
* O filtro com a nomenclatura "Profissional" foi modificado para "Responsável"
* O filtro com a nomenclatura "Categoria" foi modificado para "Descrição do item"

Agora é permitido ordenar a listagem de histórico de atendimento por grupo profissional clicando no cabeçalho da tabela (colunas **Data, Responsável, Descrição do Item e Grupo Profissional)**. Assim o usuário pode listar por ordem alfabética ou por data os registros conforme cada campo.

Outra inovação em histórico de atendimento implementada a partir da versão 12.1.2602 foi o recurso gerenciar as colunas apresentadas. É possível acessar clicando na engrenagem na parte superior da tabela, conforme indicado na imagem a seguir:

Nessa atualização é possível abrir o gerenciador de colunas e ocultar/ordenar os itens apresentados.

O exemplo a seguir foi ocultado o responsável, e alterada a ordenação trazendo primeiro o Grupo Profissional:

Filtros avançados

## **03. FILTROS AVANÇADOS**

É possível realizar o filtro do histórico pelos seguintes valores, sendo o primeiro sempre disponível, já os demais ficarão disponíveis ao utilizar a função filtros avançados.

* Atendimento(s); (**Obs:** Por padrão exibe os atendimentos dos últimos 3 anos, porém é possível filtrar por tipo e período)
* Grupo profissional;
* Profissional; (**Obs:** Caso grupo profissional estiver preenchido será apresentado somente os respectivos profissionais do grupo)
* Especialidade; (**Obs**: Profissional ou Registro)
* Categoria(s);
* Data inicial;
* Data final;

Por  padrão o filtro é realizado automaticamente, mas caso seja utilizado a função **"Filtros avançados"** esse comportamento é desabilitado e a função **"Filtrar"** é disponibilizada;  
Ao utilizar qualquer filtro dentro do formulário será exibido a quantidade de filtros aplicados junto ao botão de **"Filtros avançados";**

Impressão

## **04.** **IMPRESSÃO**

Exibe em tela uma janela onde será possível realizar a impressão utilizando os mesmos filtros disponíveis no histórico, ao imprimir uma guia será apresentada com o resultado final em pdf;

Parâmetros utilizados

## **05. PARÂMETROS UTILIZADOS**

É possível alterar o comportamento do filtro de histórico, tornando ele automático ou manual.

* Automático:  
  A função "Filtros avançados" fica disponível para exibir os demais filtros;   
  Ao abrir o menu ou alterar filtro a listagem é atualizada automaticamente;
* Manual:  
  A função "Filtrar" fica disponível para aplicar os filtros selecionados;  
  Ao abrir o menu ou alterar filtro a listagem não é afetada até que a opção filtrar seja acionada;  
  Os filtros avançados ficam sempre visíveis;
Filtros de tela 

## **06. FILTRO DE TELA NO HISTÓRICO DE ATENDIMENTO**

Melhoria disponível a partir da versão 2506.175

A melhoria realizada tem como objetivo otimizar a **usabilidade e o desempenho** da tela de histórico de atendimentos, garantindo que os filtros sejam **mais intuitivos**, apresentem **comportamento dependente** entre si e utilizem **carregamento incremental** para evitar lentidão.

## **Filtro de Período**

Permite definir o intervalo de tempo dos atendimentos exibidos.

### Opções rápidas:

* Últimos **30 dias**
* Últimos **3 meses**
* Últimos **6 meses**
* **1 ano**
* **2 anos**
* **3 anos** (opção padrão)
* **Personalizado** (com data inicial e final)

**Padrão de sistema:** ao abrir a tela, o sistema traz automaticamente **os últimos 3 anos** selecionados.

## **Filtro de Tipo de Atendimento**

Define o escopo dos atendimentos que serão exibidos.

### Opções disponíveis:

* **Internação**
* **Pronto Atendimento**
* **Ambulatório**

**Padrão de sistema:** todos os tipos de atendimento vêm **selecionados por padrão**.

Este filtro é **dependente do Período** e **influencia os próximos filtros**:

## **Filtro de Atendimentos**

Exibe a listagem dos atendimentos disponíveis conforme as seleções anteriores.

Funcionalidades:

* **Busca direta** por número, data ou nome do paciente.
* **Listagem resumida**, apresentando:

  + Iniciais do tipo de atendimento (ex.: INT, PA, AMB)
  + **Data de início e fim** do atendimento
* Caso **nenhum atendimento seja selecionado**, o sistema **carrega todos os disponíveis** conforme os filtros aplicados.

## **Filtros dependentes adicionais**

Esses filtros refinam a busca conforme o **Tipo de Atendimento** selecionado.

| **Filtro** | **Descrição** |
| --- | --- |
| **Especialidade** | Exibe apenas as especialidades associadas ao tipo de atendimento escolhido. |
| **Tipo de Documento** | Lista apenas documentos cadastrados para o tipo de atendimento selecionado. |
| **Profissional** | Apresenta somente profissionais que realizaram atendimentos do tipo escolhido. |
| **Classe Profissional** | Filtra conforme as classes profissionais habilitadas para o tipo de atendimento. |

## **6.1 IMPRESSÃO**

As informações de filtro para impressão são iguais aos filtros de tela, respeitando a padronização de usabilidade.

Registros exibidos

## **07. REGISTROS EXIBIDOS**

Listagem dos módulos que são exibidos no histórico clínico.

* Anamnese
* Anotação clínica
* Aprazamento/Checagem Enfermagem
* Aprazamento/Checagem Médica
* Atestados e Documentos
* Cirurgia
* Controle de Enfermagem
* Evolução
* Formulários dinâmicos
* Histórico de enfermagem
* Interconsulta Ambulatorial
* Justificativa da Prescrição Médica
* Plano Terapêutico
* Plano Terapêutico Ambulatorial
* Prescrição de Enfermagem
* Prescrição de Especialidade
* Prescrição Médica
* Prescrição Médica Consolidada
* Prescrição Quimioterapia
* Receita
* Resposta de Parecer
* Resultado de Exames
* Solicitação de Exames
* Solicitação de Parecer
* Solicitação de Procedimentos
* Triagem

* Anamnese (PEP1)
* Anamnese/Formulários especiais (PEP1)
* Atestados e Documentos PEP2
* Evolução (PEP1)
* Evolução Prof (PEP1)
* Histórico clínico PEP2
* Prescrição de Enfermagem (PEP 1 / PEP 2)
* Prescrição Médica (PEP1)
* Receita (PEP1)
* Receituário PEP2
* Solicitação de Parecer (PEP1)
