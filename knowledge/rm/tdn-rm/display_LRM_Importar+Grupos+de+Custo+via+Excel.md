---
content_hash: eb598aa0c3688087222a10696ebbfaaaa36344cbcf9c13ae1b1ff600032d612c
fetched_at: '2026-06-29T00:10:39.046676+00:00'
page_id: '545645906'
product: rm
source: tdn-rm
title: Importar Grupos de Custo via Excel
type: documentation
url: https://tdn.totvs.com/display/LRM/Importar+Grupos+de+Custo+via+Excel
version: 12
---

Esta tela visa simplificar a importação de Grupos de Custo, sendo feita através de planilhas via Excel.

**Passo a passo:**

Arquivo (Localização + Nome): Informe a localização e o nome do arquivo a ser importado.

Colunas do Excel: Informe a posição das colunas na planilha Excel correspondentes aos campos Código, Descrição, Grupo DNIT, Lei Social, BDI, Condição de Pagamento, Equalizável, Natureza Orçamentária, Percentual Sobre (Grupo DNIT), Percentual Sobre (Custo Unitário), Código Insumo Inicial, Código Insumo Final, Unidade, Jornada, Prazo de Ressuprimento.

O campo Linha Inicial é utilizado devido a necessidade do arquivo Excel ter um cabeçalho ou identificação dos dados da importação, portanto deve ser indicado pelo usuário onde será o início da importação. Este campo é obrigatório seu preenchimento e somente poderá ser inserido números maiores que zero e terá o valor inicial igual a 1.

**Importar Grupo de Custo via Excel:**

A tela para importação esta localizada em Projeto | Importações | Importar Grupo de Custo via Excel.

**Observação**: Os campos Código, Descrição e Grupo DNIT são obrigatórios, e devem ser inseridos sempre de acordo com a planilha.

Se o checkbox "Sobrescrever" estiver marcado, sera atualizado um grupo de custo já cadastrado.

Para executar o Processo deve-se preencher os seguintes campos:

* **Arquivo:** Local onde o arquivo a ser importado se encontra;
* **Linha inicial:** Linha inicial do Excel que o processo irá utiliza para início da leitura dos dados, sendo que, não é um campo obrigatório e caso não haja o preenchimento o sistema utiliza como padrão a linha 1 (um);
* **Código:** Coluna onde se encontra o código do Grupo de Custo;
* **Descrição:** Coluna onde se encontra o nome ou uma breve descrição do Grupo de Custo;
* **Grupo DNIT:** Coluna onde se encontra o Grupo DNIT associado;
* **Lei Social:** Coluna onde se encontra o valor de Lei Social, caso for seu grupo de custo não utilize Lei Social, se passa por padrão o valor 0. Os valores 1 e 2, são respectivamente Lei Social 1 e Lei Social 2, que podem ser parametrizados no sistema através do menu Opções | Parâmetros | RM Solum | Projetos, pasta Cálculo, subpasta Leis - Outros.;
* **BDI:** Coluna onde se encontra o valor BDI, este valor sempre receberá 1, mesmo não sendo preenchido na planilha;
* **Condição de Pagamento:**Coluna onde se encontra a Condição de Pagamento do Grupo de Custo, deve ser preenchida com base nas opções já existentes no projeto;
* **Equalizável:**Coluna onde se encontra o campo Equalizável;
* **Natureza Orçamentária:**Coluna onde se encontra o campo Natureza Orçamentária;
* **% Grupo DNIT:**  Coluna onde se encontra o código referente ao campo a ser importado, estes campos serão fixos de acordo com o percentual sobre Grupo DNIT, sendo necessário o uso do separador ";": Ex. N;A;B;C; etc..;
  + **N -**Nenhum;
  + **A -**Equipamento;
  + **B -** Mão de Obra;
  + **C -**Material;
  + **D -**Atividades Auxiliares;
  + **E -**Tempo Fixo;
  + **F -**Momento de Transporte;
* **% Custo Unitário:**Coluna onde se encontra o código referente ao campo a ser importado percentual sobre Grupos de Custo Unitário, neste campo existe o separador ";", caso seja passado mais de um valor;
* **Cód. Insumo Inicial:**Coluna onde se encontra o código do Insumo Inicial;
* **Cód. Insumo Final:** Coluna onde se encontra o código do Insumo Final;
* **Unidade:**Coluna onde se encontra o código da Unidade referente ao Grupo de Custo;
* **Jornada:**Coluna onde se encontra o valor da Jornada;
* **Prazo de Ressuprimento:**Coluna onde se encontra o valor do prazo de Ressuprimento;

Para informações mais completas sobre os campos dos Grupos de Custo, acesse o link: "".

**Exemplo de planilha a ser importada:**

**Exemplo do log após a execução do processo:**
