---
content_hash: ae6394e6c594aa6b3875561b981438b57144284b7aa6996a8fb1df66e77fdca2
fetched_at: '2026-06-29T00:09:48.445001+00:00'
page_id: '435105156'
product: rm
source: tdn-rm
title: Gerar e associar contas gerenciais
type: documentation
url: https://tdn.totvs.com/display/LRM/Gerar+e+associar+contas+gerenciais
version: 8
---

Este processo foi criado para facilitar e agilizar a implantação e a configuração de cada empreendimento, automatizando a geração das Contas Gerenciais e associando-as automaticamente, para cada subunidade do empreendimento selecionado.

Atenção

Para utilizar este processo, a [máscara](https://tdn.totvs.com/pages/releaseview.action?pageId=423938635) das [Contas Gerenciais](https://tdn.totvs.com/display/LRM/Plano+Contas+Gerencial) deve ser atualizada para, no mínimo, "#.###.###.####", com 4 níveis, e uma Conta Gerencial Sintética deve ser criada previamente, para que as contas dos empreendimentos, que são analíticas, sejam subordinadas a ela.

É necessária essa máscara para a execução do processo automático, para que sejam preenchidos os dados do empreendimento, da unidade e da subunidade.

Cada grupo de contas gerenciais poderá ter uma máscara diferente. E também é possível alterar a [máscara](https://tdn.totvs.com/pages/releaseview.action?pageId=423938635).

Este processo só será executado corretamente se o **código reduzido** para **contas gerenciais** estiver parametrizado para gerar de forma automática, ou seja, não edita.

* Para utilizar o POC, a conta gerencial, no plano contábil deve ser sempre a de **código 9**.

* O cadastro das contas gerenciais irá respeitar os parâmetros da conta pai. Portanto se este cadastro for global, todas as contas gerenciais associadas serão Globais.

* Como serão preenchidas as contas gerenciais? O preenchimento das contas gerencias é realizado automaticamente pelo processo de **Gerar e Associar Contas Gerencias,** desde que a parametrização da máscara esteja correta.

**#**.###.###.#### - Primeiro nível - Fixo "9" - Definição de conta gerencial do TCGI

#.**###**.###.#### - Segundo nível - Empreendimento - Esse nível será preenchido com o número do empreendimento.

#.###.**###**.#### - Terceiro nível - Unidade - Esse nível será preenchido com o número da unidade.

#.###.###.**####** - Quarto nível - Subunidade - Esse nível será preenchido com o número da subunidade.

Caso sejam utilizadas mais casas para os números do empreendimento, unidade e subunidade, a máscara deverá ser adaptada para respeitar o tamanho utilizado.  
Se o valor cadastrado for menor, será preenchido com zeros à esquerda.

As contas são incluídas automaticamente pelo processo, seguindo a regra acima, considerando a máscara, que deverá obrigatoriamente ser configurada com 4 níveis.

* Caso a [apuração](https://tdn.totvs.com/pages/viewpage.action?pageId=435105027) seja realizada considerando as subunidades e seu respectivo rateio gerencial, e já exista saldo nas Contas Contábeis utilizadas na apuração, será necessário efetuar o [*rateio gerencial*](https://tdn.totvs.com/display/LRM/Rateio+Gerencial+-+Processo), utilizando as ferramentas já disponibilizadas no módulo de [Contabilidade](https://tdn.totvs.com/display/LRM/Processos+-+Gerencial) que é a *[distribuição gerencial](https://tdn.totvs.com/pages/viewpage.action?pageId=423938663)*.
* A distribuição deverá ser feita considerando a situação de cada conta;

Exemplo:      Uma conta de custo, que deve ser rateada para as contas gerenciais de cada subunidade, considerando a fração ideal.

Já nas contas de resultado, caso considere apenas subunidades vendidas, uma maneira que pode ser feito o rateio, é multiplicando o total apurado pela fração do preço da subunidade pelo somatório de preços das subunidades vendidas.

Depois do processo já executado, caso seja incluída uma nova subunidade ou uma nova unidade no empreendimento, a associação das contas gerenciais deverão ser feitas manualmente em seus respectivos cadastros.

Importante!

Após realizada a apuração do POC, não será possível gerar novamente ou alterar as contas gerenciais das Subunidades envolvidas na apuração.

Este comportamento se justifica , pois estas ações poderia causar divergências no fechamento das apurações realizadas.

Outra validação realizada é que caso uma subunidade for vendida e tenha uma conta gerencial associada, esta conta gerencial também não poderá ser alterada, podendo a mesma ser alterada somente caso a apuração não tenha sido realizada e a subunidade não estiver vendida.

Acesse: Regras de Apuração  do POC para obter mais informações.
