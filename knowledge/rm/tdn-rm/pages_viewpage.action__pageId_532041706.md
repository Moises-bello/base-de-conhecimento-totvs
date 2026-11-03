---
content_hash: 7244c98660e74c396e6bc9a7720c2f333cb7f82214d4c7407c55dd508fbde9bd
fetched_at: '2026-06-29T00:10:36.409187+00:00'
page_id: '532041706'
product: rm
source: tdn-rm
title: FIN - Valores de Integração Financeiro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=532041706
version: 18
---

Funcionalidade

Os Valores de Integração são campos criados para auxiliar uma ação ou determinado processo que envolve valores entre o sistema de origem e o sistema financeiro (TOTVS Gestão Financeira).

Os valores de integração poderão ser usados também nos lançamentos gerados no financeiro com aplicação de origem igual “F” (Financeiro). Basta cadastrar no Gestão Financeira os valores de integração e parametrizar quais serão considerados nos parâmetros do sistema, essa parametrização será por coligada e o efeito dessa parametrização e uso dos valores de integração serão somente nos lançamentos gerados a parir do Gestão Financeira. A parametrização dos valores de integração do TOTVS Educacional *não será alterada*.

Os valores de integração

O cadastro dos campos de Valores de Integração está disponível no TOTVS Gestão Financeira através do menu Cadastros | Valores de Integração, é necessário que o usuário tenha permissão para manutenção neste cadastro.

Campos

Para incluir os campos de 'Valores de Integração' acione o botão 'Novo': informe uma *'Descrição'* para o campo e defina a *'Ação'* que será interpretada no momento da inclusão e *baixa* do lançamento financeiro podendo ser *Nada, Acrescenta* ou *Desconta*.  Informe também a *'Ordem'* numérica em que valor atribuído ao campo deverá ser aplicado no momento da inclusão e baixa do lançamento.

O campo **Até o Vencimento** estará disponível se a *'Ação'* do campo for 'Desconta'. Com essa opção marcada, o Valor de Integração somente será considerado até a data de vencimento. Quando a opção estiver desmarcada, o Valor de Integração sempre será considerado. O campo **Dias de Atraso** ficará disponível se a *'Ação'* do valor de integração for 'Acrescenta'. Nesse campo pode-se informar o número mínimo de dias de atraso para que a ação seja executada.

Os valores de integração podem ser configurados para usar "Fórmula", com default parametrizado e não permitindo alterar na edição do lançamento financeiro (será calculada no valor líquido), ou configurado para "Valor" permitindo informar no lançamento financeiro com duas casas decimais.

Através do flag "Compõe valor da movimentação do Relatório Extrato Cliente/Fornecedor" é possível definir se um valor de integração do Financeiro ou Educacional, com ação diferente de Nada e sem fórmula, irá compor o valor neste relatório.

Através do flag "Compõe valor do Ajuste Valor a Presente (AVP)" é possível definir se um valor de integração, com ação diferente de Nada e sem fórmula, irá compor o valor futuro no cálculo do Ajuste Valor a Presente (AVP).

Parametrização para uso dos valores de integração no lançamento financeiro

A parametrização dos valores de integração será por coligada através do menu Ambiente | Parâmetros | TOTVS Gestão Financeira | Contas a Pagar\Receber | Valores de Integração.

No parametrizador, ao criar um novo, serão exibidos para seleção os para valores de integração criados para o módulo Financeiro. Basta selecionar qual ou quais serão carregados para o(s) lançamento(s) financeiro em sua inclusão no Gestão Financeira. Somente valores de integração para o módulo Financeiro estarão disponíveis para seleção.

Parametrização dos valores de integração do Financeiro para outros módulos

A parametrização dos valores de integração para outros módulos será por coligada através do menu Ambiente | Parâmetros | TOTVS Gestão Financeira | Contas a Pagar\Receber | Valores de Integração aba "Parâmetros por Módulo".

Quando definido o módulo ao gerar lançamento financeiro neste módulo automaticamente os valores de integração do Financeiro serão carregados para os lançamentos gerados a partir desse módulo.

Cálculo do valor líquido e baixa dos valores de integração do lançamento financeiro

No cálculo do valor líquido serão considerados  os valores de integração, quando o lançamento tiver aplicação origem no Financeiro e quando existir tais valores. Na tela de composição do valor líquido os valores de integração também serão exibidos e irão compor o valor liquido do lançamento.

Na baixa de lançamentos com valores de integração o sistema irá calcular o valor líquido,  quando o lançamento tiver aplicação de origem no Financeiro e existir tais valores.

 Veja Também

* [Valores de integração Financeiro Educaciona](https://tdn.totvs.com/x/E-9bGQ)l
