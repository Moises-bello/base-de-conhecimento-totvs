---
content_hash: 8e3e247c310b2f0611e7bae22b71e0a87aefb3a5d1c4f4db343bb736b684ff1c
fetched_at: '2026-06-29T00:09:26.811975+00:00'
page_id: '423938434'
product: rm
source: tdn-rm
title: Lançamentos de Detalhamento do RAS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938434
version: 4
---

Cadastro de Lançamentos do detalhamento do Razão Auxiliar de Subcontas. Estes detalhamentos irão compor o RAS na geração do SPED Contábil.

Serão informados alguns dados para a identificação dos lançamentos de detalhamento, tais como:

* Identificador do item do RAS;
* Partida Contábil utilizada;
* Data da partida;
* Valor da partida;
* Natureza da partida contábil;
* Subconta;
* Centro de custo;
* Valor a débito ou a crédito na Subconta.

Seleção da Partida Contábil

* Partida só com um débito ou um crédito preenchido:

1. O campo "Natureza da Partida" será preenchido conforme a conta da partida (Débito ou Crédito);
2. A conta contábil da Partida deve estar cadastrada como uma subconta no sistema; Subcontas (Clique Aqui).

* Débito e crédito na mesma Partida:
  1. O campo "Natureza da Partida" deverá ser preenchido manualmente;
  2. Ao preencher o campo "Natureza da Partida" a subconta será preenchida automaticamente com a conta contábil conforme o indicador selecionado (débito ou crédito);
  3. Uma das contas a débito ou a crédito informada na partida tem que estar cadastrada como uma subconta no sistema. Subcontas (Clique Aqui).

**Observaçoes:**

* - Partidas que possuem detalhamento não poderão ser excluídas;
* - Se a Subconta estiver associada a um detalhamento a mesma não poderá deixar de ser Subconta;
* - Partidas que possuírem detalhamentos não poderão ser agrupadas.

**Visualização dos Detalhamentos**  
   
Aqui serão apresentados os detalhamentos dos lançamentos contábeis incluídos manualmente e também as informações das partidas contábeis que foram classificadas com o tipo "Detalhamento do Item no RAS".

Para que seja exibido os campos referente a valores calculados de (saldos iniciais, saldos finais...) o usuário deve selecionar, conforme sua necessidade, dois botões que foram disponibilizados na tela:

* Mostrar as colunas com os cálculos dos saldos e realizações do item do RAS referentes a conta contábil na qual a subconta esta vinculada;
* Mostra todas as colunas com as informações que irão compor o RAS.

Os botões foram implementados com a finalidade de trazer uma maior performance, calculando os valores apenas quando selecionados pelo usuário.  
   
**Como emitir o RAS?**  
   
Após o detalhamento é preciso que:

* Cadastre uma escrituração contábil com forma de escrituração "Razão Auxiliar" e na aba "Layout do Relatório Razão Auxiliar", informe a origem das informações do relatório como "RAS Razão Auxiliar de Subconta";
* Nos próprios processos da escrituração é possível realizar a emissão do relatório. Também é possível realizar a emissão dentro do menu do RAS presente na aba de obrigações acessórias.

Mais Informações - Escrituração   
   
**Como enviar o RAS para o SPED Contábil?**

* É preciso que o relatório seja gerado em forma de arquivo, já no padrão do layout do SPED contábil;
* Na geração do SPED contábil, selecione uma escrituração que tenha a forma de escrituração "Razão Auxiliar";
* Ainda na geração do SPED, em uma das etapas, insira o arquivo gerado anteriormente no layout do SPED.

Veja também

* Identificador de Item do RAS
* Importação de Informações para o RAS
* Geração Razão Auxiliar
