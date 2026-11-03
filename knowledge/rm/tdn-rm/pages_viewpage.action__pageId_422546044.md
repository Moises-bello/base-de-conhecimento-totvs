---
content_hash: 93dc34c7c2353f081fccc11848b53b7cc01ea73be98375c27603761b46292b35
fetched_at: '2026-06-29T00:09:23.085640+00:00'
page_id: '422546044'
product: rm
source: tdn-rm
title: Parâmetros da ECF (Lucro Real)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422546044
version: 5
---

Forma de tributação Lucro Real Trimestral ou Lucro Real Anual com levantamento de Balanço de suspensão/redução  
 Este item deverá ser habilitado nos casos em que a apuração do tributo não coincide com a suspensão do balanço.  
 Ex.: Balanço encerrado anualmente e apuração do tributo trimestral. Neste caso os valores de Débitos X Créditos no Ativo e Passivo não irão fechar. Este recurso é utilizado para gerar no registro K155 uma linha com o valor do encerramento trimestral para que as colunas de Ativo e Passivo fechem ao importar e declaração no PVA da ECF. Este processo não irá gerar lançamentos contábeis. Estes valores só existirão em tempo de execução da rotina para a geração do arquivo corretamente. Para os períodos que houver a suspensão do balanço estes valores não serão gerados.

**Origem do Resultado Contábil apurado no Trimestre ou Mês**

**Apuração virtual:** Ao gerar o registro K155 o sistema vai executar a apuração virtual que calculará o resultado contábil gerando o mesmo na conta de lucro ou prejuízo parametrizada no molde da Apuração Virtual.  
 **Apuração do Período do TOTVS Gestão Fiscal:** Ao gerar o registro K155 o sistema vai carregar o resultado contábil utilizado no módulo TOTVS Gestão Fiscal (Evento Tributário) para apurar o imposto, gerando o mesmo na conta de lucro o prejuízo a ser parametrizada.  
 Se for informada que a origem do Resultado é a Apuração Virtual o código da estrutura a ser utilizada deverá ser informado no campo correspondente.  
 **Contas de Lucro e de Prejuízo:**Será gerada uma linha em cada período de apuração do tributo no registro  K155 com a conta de Lucro ou Prejuízo com o  valor calculado pela Apuração Virtual ou TOTVS Gestão Fiscal para o resultado. Se a conta de Lucro ou Prejuízo for a mesma ela deverá ser gravada nos dois campos.  
    
 **Método de Avaliação do Estoque Final (Registro L200)**

Informe para cada período de apuração o método utilizado para fazer a avaliação final do estoque.

**Informativo de Composição de Custos (Registro L210)**

Através deste registro serão geradas as informações da composição de custos. Esta informações são originadas nas contas contábeis. Para que isto ocorra corretamente deverá ser criado um Plano de Contas Paralelo, porém deve ser importada a tabela correspondente e associadas as contas de custos.
