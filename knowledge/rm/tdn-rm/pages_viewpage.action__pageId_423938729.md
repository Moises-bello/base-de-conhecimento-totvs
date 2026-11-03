---
content_hash: 9bc89b4b76b26a57f2256b1a924944b59a131330ff173a8699ac96946308f1a3
fetched_at: '2026-06-29T00:09:28.632204+00:00'
page_id: '423938729'
product: rm
source: tdn-rm
title: Demonstração Contábil | Estrutura (Layout)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938729
version: 42
---

Na identificação da Demonstração Contábil é necessário preencher alguns campos:

* **Código** e **Descrição :** São obrigatórios
* **Título Relatório** e **Sub Título Relatório:** deverão ser informados conforme a necessidade do cliente.
* **Comparativo:**deve ser utilizado ao montar uma demonstração, de forma que possibilite a comparação de valores movimentados nas contas contábeis informadas, entre dois ou mais períodos distintos.
* **Consolidado:** Ao marcar este campo é possível associar ao fato contábil contas contábeis de mais de uma coligada. É possível também criar colunas com fatos contábeis que receberão o saldo de contas de mais de uma coligada.

  Saiba mais

  [Demonstrações Consolidadas](https://tdn.totvs.com/x/R2f6Hg)
* **Grupo Empresarial:** Caso a demonstração seja consolidada e este campo esteja preenchido, ao gerar o relatório de demonstração, os cálculos para cada coligada serão feitos levando em consideração a porcentagem de participação que foi informada no cadastro de movimentação dos investimentos societários. Será exibido apenas x (porcentagem de participação) por cento sobre o valor final daquele fato.

  Saiba maisAtenção

  O campo **Consolidado** fica habilitado para alteração apenas se o campo **Comparativo** estiver desmarcado e se não houver nenhum Fato Contábil cadastrado na Estrutura.

  O campo **Grupo Empresarial** fica habilitado para alteração apenas se o campo **Consolidado** estiver marcado e se não houverem Colunas cadastradas na Estrutura. Estarão disponíveis para seleção neste campo apenas os Grupos Empresariais cuja Coligada do Contexto seja a Holding ou seja Investidora de alguma outra Coligada dentro do grupo.
* **"Utilizar máscara no código do Fato Contábil?":** é possível definir uma Máscara para os Fatos Contábeis (linhas horizontais) do relatório a fim de hierarquizar a estrutura do mesmo.

**Após a identificação, devem ser cadastrados:**

---

Templates para DLPA / DMPL / DRE

Existem arquivos Templates pré montados, confira aqui:

Importação / Exportação

**Importação de um Layout** **pré-determinado:** Possível através do ícone Importar Estrutura. Para que o mesmo seja apresentado é necessário primeiramente clicar para Incluir uma nova Demonstração (este ícone localiza-se abaixo do botão de Exclusão da estrutura).  
**Exportação da estrutura:** É possível através do ícone Exportar Estrutura.
