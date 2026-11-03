---
content_hash: ef84be8f5abf3faf9cf5b8d6737312ee204a53994b04658180ed9c9f9718a476
fetched_at: '2026-06-29T00:09:27.309634+00:00'
page_id: '423938498'
product: rm
source: tdn-rm
title: Geração Automática de Orçamentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938498
version: 3
---

O processo que permite a geração de orçamento de forma automática, está disponibilizado no menu Orçamento | Geração Automática de Orçamentos. A partir desse menu é possível a geração de novos orçamentos baseados na movimentação das contas selecionadas.  
Os orçamentos gerados serão apresentados no menu Orçamento | Orçamento. Para cada combinação de conta contábil com cada filial, departamento, conta gerencial e centro de custo parametrizados o sistema irá gerar um cadastro ou mais. Esses orçamentos serão criados com o primeiro e segundo valor.

**Data Inicial e Data Final** Esses campos deverão ser preenchidos obrigatoriamente, com o período para qual existe a movimentação a ser considerada na geração do orçamento, não podendo exceder ao limite de 12 meses. Podendo compreender meses de um mesmo ano ou não.

**Ano do novo orçamento** Ano para o qual o novo orçamento será gerado. De preenchimento obrigatório.

**Filial/Departamento** Permite selecionar as movimentações de determinadas filiais e departamentos, que servirão como origem para a geração do novo orçamento. Para que sejam consideradas as movimentações que não tem departamento, é necessário marcar a opção "Incluir departamentos nulos no filtro",  que é apresentada dentro da janela de seleção. Se não for marcado nenhum departamento o sistema irá considerar o movimento geral das contas, não levando em consideração o rateio dos valores por departamento.

**Conta Contábil** Permite selecionar individualmente as contas contábeis desejadas ou faixa de contas. Estas contas, juntamente com suas combinações (filial/departamento, contas gerencias e/ou centros de custo), servirão como origem para a geração do novo orçamento. É obrigatório informar as contas contábeis e é recomendável usar somente contas analíticas.

**Conta Gerencial** Através dessa aba é possível selecionar individualmente as contas gerenciais desejadas ou faixas de contas. Se nenhuma conta gerencial for informada o sistema irá considerar o movimento geral das contas, não levando em consideração o rateio dos valores por contas gerenciais. Se alguma conta gerencial for informada o sistema irá fazer duas considerações:  
1 - Considerar os movimentos das contas contábeis, rateados pelas contas gerenciais selecionadas, apenas para as contas contábeis que exigirem rateio gerencial. 2 - Para as contas contábeis que não exigirem rateio o sistema irá considerar a movimentação sem rateio gerencial. Desta forma as contas gerenciais selecionadas só farão efeito para contas contábeis que exigirem rateio gerencial.  
Se a opção "Gerar orçamento de acordo com a distribuição gerencial das contas" for marcada o filtro de contas gerenciais ficará desabilitado. Com essa opção selecionada serão gerados orçamentos para todas as contas gerenciais existentes na distribuição gerencial das contas contábeis que exigem rateio.

**Centro de custo** Permite selecionar individualmente os centros de custo desejados ou faixas de centros de custo. Para considerar os movimentos sem centros de custo a opção "Considerar movimentos sem centros de custo (Centros de custo nulos)" deverá ser marcada. Se algum centro de custo for informado, inclusive os centros de custo nulos, o sistema irá considerar somente os movimentos dos centros de custo informados. Se não for informado nenhum centro de custo o sistema irá considerar o movimento geral das contas, não levando em consideração o rateio dos valores por centros de custo.  

**Observação:**  
No cadastro do orçamento os valores de natureza credora serão gerados com o sinal negativo.
