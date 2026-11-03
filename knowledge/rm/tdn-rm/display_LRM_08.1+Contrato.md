---
content_hash: 51c0316856fe9a53e32cec5579d92ca6ae8443f52531f3835c567d462ace4127
fetched_at: '2026-06-29T00:08:47.338484+00:00'
page_id: '319787697'
product: rm
source: tdn-rm
title: 08.1 Contrato
type: documentation
url: https://tdn.totvs.com/display/LRM/08.1+Contrato
version: 38
---

**Este Menu está disponível apenas para o contexto ENSINO BÁSICO.**

Este step tem como objetivo de exibir o contrato para que o aluno possa ler e aceitar, para assim finalizar a sua rematrícula.

Para que o contrato seja exibido é necessário que seja disponibilizado para impressão nos parâmetros.

 **Educacional| Configurações| Parâmetros| RM Portal| Matrícula| Contrato Financeiro 1/4**

Contrato - Relatório Fixo

A instituição poderá criar o contrato do jeito que desejar, para saber mais sobre os parâmetros acesse [Portal - Contrato Financeiro 2/3](https://tdn.totvs.com/pages/viewpage.action?pageId=425459703)

Foi evoluído o TOTVS Educacional para que passe a considerar as informações do contrato do aluno quando já existir nas informações da TAG, porém caso o aluno ainda não possua contrato ou esteja modificando o plano de pagamento o comportamento da simulação de valores será pelo plano de pagamento.

No contrato do Portal do aluno, não será mais utilizado os parâmetros de Assinatura e Cabeçalho, para isso foram criadas tags para as informações de Filial e Coligada e a assinatura pode ser incluída no corpo do contrato.

Contrato - Relatório RM Reports 

É possível gerar o contrato financeiro a partir de um relatório parametrizado. Ao acessar a parametrização da matrícula do portal, marcar a opção "Utilizar relatório" e informar qual é o relatório no campo abaixo.

Ao acessar a parametrização da matrícula do portal, marcar a opção "Utilizar relatório" e informar qual é o relatório no campo abaixo.

Para saber mais sobre os parâmetros acesse [Portal - Contrato Financeiro 1/3](https://tdn.totvs.com/pages/viewpage.action?pageId=425458619)

Na execução do relatório será passado parâmetros com informações do contexto selecionado pelo aluno, para que estes dados sejam utilizados crie os parâmetros abaixo nos relatórios:

Nome dos parâmetros:

**CODCOLIGADAPARAM**  
**CODFILIALPARAM**  
**CODTIPOCURSOPARAM**  
**IDPERLETPARAM**  
**IDHABILITACAOFILIALPARAM**  
**RAPARAM**

Observações:

* Se a banda principal do relatório **não** for a tabela SCONTRATO, a utilização dos parâmetros listados anteriormente será **obrigatória** e devem fazer parte da sentença SQL definida como a banda principal do relatório.
* Não é aconselhável criar uma sentença SQL com o mesmo nome de uma tabela da base de dados.

Configuração do Relatório

É possível exibir no relatório as turmas/disciplinas selecionadas, o código do plano de pagamento e os seguintes dados financeiros: valor total do plano de pagamento, valor líquido do plano de pagamento (desconsidera os descontos das parcelas do plano de pagamento), número de parcelas do plano de pagamento e o valor da parcela do plano de pagamento (valor Total / número de parcelas).  para saber mais.

Relatório de Manifesto

Disponível no book de relatórios o relatório **EDUREL0083 - Contrato de Prestação de Serviços - Manifesto**, o mesmo tem a inteligência de ao assinar o contrato por meio do **token** será gerado o manifesto neste relatório.

No portal do aluno será exibido o relatório sem o manifesto como já é mostrado hoje.

Após **assinar o contrato** e **finalizar a matrícula**, será exibido o link para exibir o contrato para aluno já com o manifesto.

Vale lembrar que o manifesto somente é exibido quando o sistema foi parametrizado para utilizar relatório do RM Reports seguindo o modelo do EDUREL0083.

Como pelo sistema é possível visualizar o contrato assinado cadastro do **contrato** anexo **visualizar assinatura de contrato** botão abrir arquivo da assinatura.

Caso prefira utilizar o relatório FIXO basta adicionar a TAG **[MANIFESTO]**.

A TAG irá montar a tabela do Manifesto.

Os dados do Signatário serão do usuário logado no portal, ou seja, aluno, pai, mãe ou responsável.Fórmulas visuais

As fórmulas visuais que estão associadas no processo de matrícula serão executadas na rematrícula online. 

Essa associação é feita através das parametrizações do Educacional que ficam em: **Educacional | Matrícula | Fórmulas Visuais 2/2**, na parte "Cadastrar contrato matrícula". É possível relacionar uma fórmula visual que será executada **antes** e/ou **depois** de cadastrar o contrato, conforme a imagem abaixo:

Importante

Não aconselhamos o uso do componente de Identificador de Relatórios (Certificador de Relatórios) para o contrato da rematrícula web.

Duas questões iniciais:

1 – O cliente aluno, pais e responsáveis, que estiver realizando o processo de rematrícula pode ter acesso ao GUID sem confirmar a matrícula, ser realizar a confirmação do “li e aceito” e depois questionar a instituição que tem um contrato “válido”, diante do código.

2- A engine de execução de relatório do reports para a rematrícula web, em sua jornada única, executa o mesmo relatório 4 vezes, duas antes do “li e aceito” e duas após o “li e aceito”. Isso porque ela gera uma imagem que vai no modal, para que não tenhamos popup e outra que já fica em PDF para impressão, o que pode fazer com que o aluno, pais e responsáveis, que estiverem realizando o processo de rematrícula não tenha a chave válida.

Orientamos o uso do manifesto ou a integração com TAE para o que se propõe a fazer referente a segurança do controle de assinaturas e impressão do contrato.
