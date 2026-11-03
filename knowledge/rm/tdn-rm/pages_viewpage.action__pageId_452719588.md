---
content_hash: 771e3ab2468f8d6fb9c7e6c4edc217c6a59fe4583d3e6eba5bea137203821779
fetched_at: '2026-06-29T00:10:08.825906+00:00'
page_id: '452719588'
product: rm
source: tdn-rm
title: Salário Composto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719588
version: 3
---

Estes dados serão disponibilizados se a empresa utilizar, para algum funcionário, este tipo de remuneração, que consiste em compor o salário com diversos tipos de proventos específicos da categoria profissional ou da política de pessoal da empresa.   
   
Os dados cadastrados permitem a diferenciação entre o funcionário que recebe um só salário e o outro que recebe salário composto por eventos.   
   
**Observação:**  
1.     Ao excluir um determinado salário composto, o sistema abrirá uma janela solicitando a data da mudança e o motivo de alteração para inserir um registro no histórico salarial do funcionário com o salário composto e jornadas iguais a zero.  
2.     Os botões Incluir\Excluir\Editar serão habilitados respeitando primeiramente o acesso a menus.   
   
Se o acesso estiver habilitado. O procedimento será da seguinte forma para quem tiver integração com Educacional:  
**Eventos:**

* Inserir: Sempre estará habilitado.
* Editar: Não estará disponível. Deverá ser editado o evento por centro de custo. Somente ficará habilitado se não existir     registro na janela de Salário composto.
* Excluir: Somente será habilitado se não existir evento por centro de custo.

**Eventos por centro de custo:**

* Inserir: Estará habilitado somente se existir um evento cadastrado.
* Editar: Estará habilitado somente se existir um evento cadastrado.
* Excluir: Estará habilitado somente se existir um evento cadastrado e se não existir evento relacionado.

**Eventos relacionados:**

* Inserir Estará habilitado somente se existir um evento por centro de custo cadastrado
* Editar: Estará habilitado somente se existir um evento relacionado. (Não será possível alterar o centro de custo do evento)
* Excluir: Estará habilitado somente se existir um evento relacionado.

   
Para integração dos sistemas de Folha de Pagamento (Folha de Pagamento) e sistema de Gestão Educacional (Educacional), haverá as seguintes  
observações:  
1.   Quando o evento relacionado for calculado por fórmula e não existir na pasta de eventos relacionados do funcionário, o sistema buscará o centro de custo pelo evento principal da tabela PFSALCMPCC.  
2.    Quando existir um evento relacionado calculado por fórmula e esse retornar zero, o evento será apagado da pasta Salário Composto, incluindo todo o processo no log de cálculo da Gestão Educacional em Reprogramação Salarial.   
   
**Jornada Semanal**  
Esta informação somente ficará visível quando o parâmetro "Utiliza importação do movimento de ensino de sistema acadêmico de terceiros" existente em Parâmetros do sistema estiver marcado e a função do funcionário estiver cadastrada em Gestão Educacional em Reprogramação Salarial.   
   
O cálculo da jornada mensal do funcionário será realizado pela multiplicação da jornada semanal com o fator para cálculo da jornada mensal que está parametrizado em Gestão Educacional nos Parâmetros do Sistema.   
O resultado da multiplicação será o valor em horas apresentado no campo Jornada Mensal do cadastro de funcionário.  
   
**Utilização de tabela salarial com Salário Composto**  
   
Para visualizar os campos relativos a tabela salarial, os parâmetros de funcionário "Utiliza Tabelas Salariais para evento de Salário Composto e "Edita Tabelas Salariais nos Eventos de Salário Composto" devem estar marcados.  
   
Foi vinculado a tabela salarial do Vitae permitindo que o modulo de Alteração salarial busque o valor atual da tabela salarial para atualizar o salário do funcionário.  
   
Na tela de criação/edição de eventos de Salário Composto, é possível alterar Tabela, Nível e Faixa salarial do funcionário. Após inserir estas informações, ao salvar  o registro, os valores Hora e Mensal são atualizados de acordo com as novas informações.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Funcionários
