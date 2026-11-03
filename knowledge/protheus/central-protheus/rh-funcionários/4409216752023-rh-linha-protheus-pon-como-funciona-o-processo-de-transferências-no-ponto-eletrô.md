---
article_id: 4409216752023
category: ' RH - Funcionários'
content_hash: 4262c748ead0658f3e63e3309122a8145d0f57ede39ae542f6a3091158018ae3
fetched_at: '2026-06-28T22:44:48.245985+00:00'
product: protheus
section_id: 32419218165783
source: central-protheus
title: 'RH - Linha Protheus - PON - Como funciona o processo de transferências no
  Ponto Eletrônico Versão 12 '
type: support-article
updated_at: '2025-06-13T19:43:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409216752023-RH-Linha-Protheus-PON-Como-funciona-o-processo-de-transfer%C3%AAncias-no-Ponto-Eletr%C3%B4nico-Vers%C3%A3o-12
---

**Dúvida**Como funciona o **processo de transferência entre filiais, empresas, centro de custo, entre outras opções?**  
 **Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões

**Solução**

O Sistema disponibiliza os seguintes tipos de transferências:

* **Transferências entre Empresas/Filiais:** neste tipo de transferência, toda movimentação do funcionário permanece na Empresa/Filial de origem e será feita uma inclusão do funcionário na Empresa/Filial destino.
* **Transferências entre Centro de Custo:** o Sistema utiliza o mesmo registro do Cadastro de Funcionários (origem) para o funcionário destino, efetuando apenas a troca do centro de custo.
* **Transferências entre Matrículas:** este tipo de transferência é permitida apenas no mês de admissão do funcionário, e enquanto não houver movimentação acumulada. Além disso, será permitido apenas quando não foi efetuado outro tipo de transferência ou movimentação do funcionário.
* **Transferência de Funcionários por Departamentos:** permite a transferência de um funcionário ou de vários funcionários de uma vez, por Departamento ou Centro de Custo.

Para efetuar a transferência, acesse:

**Ponto Eletrônico -> Atualizações -> Transferências -> Transferências** 

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409225072279/mceclip0.png)

Em Outras Ações, selecione a opção **Transferir**.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409225248151/mceclip4.png)

O Sistema apresenta uma janela para seleção dos funcionários que serão transferidos. Nessa tela estão disponíveis as seguintes opções para seleção dos funcionários:

**Pesquisar**: permite pesquisar os dados dos funcionários cadastrados.

**Filtro**: permite elaborar um filtro, para apresentar somente os funcionários cujos dados atendam à solicitação do filtro.

**Marcar/Desmarcar Todos:** permite selecionar até 50 funcionários por vez ou desmarcar todos os que já tenham sido selecionados.   
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409225136535/mceclip1.png)

Confirmados os funcionários para a transferência, o Sistema apresenta nova janela onde a tela é dividida em duas pastas:

* **Dados Transferência:** informações para transferência como Empresa, Filial, Matrícula, Centro de Custo, Departamento, Processo.
* **Dados Cadastrais:**outros dados cadastrais dos funcionários, que podem ser configurados através da opção Config. campos, como por exemplo a função, cargo, o qual passamos um exemplo ao final do artigo.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409225181463/mceclip2.png)

Nas duas pastas, os campos estão dispostos em dois grupos.

**Origem -** São os dados atuais do funcionário. Por isso não é possível alterá-los.

**Destino -** Deve-se informar os novos dados que o funcionário terá após a transferência.

Após conferir os dados, clique em Confirmar:   
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409225191831/mceclip3.png)

Ao final do processamento da Transferência, é **emitido um log** com as alterações efetuadas e um histórico da movimentação é gerado no Arquivo de Transferência. A partir deste histórico, procedem os devidos tratamentos nas rotinas: CAGED, PROVISÃO DE FÉRIAS/13º, RAIS, DIRF, etc.

**Configuração de Campos:**

Ao acessar a rotina de Transferências, clique em Outras Ações e selecione a opção Config. campos.   
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409216630551/mceclip5.png)

Na tela seguinte, é mostrado uma lista com os campos, onde estão disponíveis as seguintes opções em Outras Ações:

**Marca Todos:**permite selecionar todos os campos apresentados na lista.

**Desmarcar Todos:**permite desmarcar todos os campos que já tenham sido selecionados.

Confira os dados e clique em Confirmar.
