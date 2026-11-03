---
content_hash: 13958cb53de849251b96504ed926f30a4cb930593d228cb1e0b27062de201f23
fetched_at: '2026-06-29T00:09:18.147274+00:00'
page_id: '421388688'
product: rm
source: tdn-rm
title: Aba Defaults - Template
type: documentation
url: https://tdn.totvs.com/display/LRM/Aba+Defaults+-+Template
version: 9
---

Impressão da Negociação do Acordo:

Permite informar  neste campo um relatório que irá demonstrar a negociação gerada.

Meio de pagamento obrigatório:

Permite definir que no processo de Acordo o meio de pagamento deverá ser "Não informar", "Informar" ou "Informar obrigatório".

Data default para baixa do acordo:

Quando o template de acordo for parametrizado para Efetivação do acordo como 'Ao Aprovar' ou 'Ao pagar primeira parcela', será possível definir a data da baixa dos lançamentos baixados por acordo que poderá ser a "Data Geração do Acordo" ou "Data Aprovação/Sistema".

Observações

* A partir da versão 12.1.27 a opção Data Aprovação/Sistema foi alterada "Data Sistema" e foi criada outra opção "Data Aprovação/Efetivação".
* Quando a opção de Data Aprovação/Efetivação for selecionada e a Efetivação for definida  "Ao pagar primeira parcela" a data da baixa dos lançamentos origem será a data de baixa do lançamento da primeira parcela do acordo.

Copiar campos complementares:

Os campos complementares do template serão copiados para a tela do processo de acordo, quando marcada essa opção.

Informar default para lançamento na geração do acordo:

Os dados defaults para geração dos lançamentos de Acordo estarão disponíveis para o usuário visualizar / alterar.

Sobrepor defaults do template sobre lançamento:

esse parâmetro terá a seguinte ação:

* Desmarcado: Considera primeiramente os defaults do lançamento de origem se preenchido, caso esteja vazio irá considerar os defaults do template.
* Marcado: Sempre considera os defaults do template caso esteja preenchido, caso contrário, considera os defaults do lançamento.

Defaults para lançamento(s) gerados(s)**:**

Será possível informar defaults para os lançamentos que serão gerados pelo acordo, tais como: Filial, centro de custo, conta caixa, tabelas opcionais, departamento, tipo de documento e histórico. Esses dados serão apresentados no lançamento gerado conforme a parametrização. Vale ressaltar que no histórico a tag [NUM] não funciona para acordo via portal pois neste caso não há iteração do usuário de opções de numeração como ocorre no acordo via módulo Gestão Financeira.

**Observações:**

Para múltiplos lançamento de origem só será considerado o default do lançamento caso tenha o mesmo default entre eles, caso seja diferente então irá considerar o default do template e caso o default do template esteja vazio, o default do lançamento de destino também ficará vazio.

No Portal do Aluno, funcionalidade "Negociação Online" o parâmetro "Sobrepor default do template sobre o lançamento" terá o mesmo efeito, sendo que esses campos não são visíveis para que o aluno possa mudar.

 Informações Complementares

* [DT - Parâmetro data default para baixa do acordo](http://tdn.totvs.com/pages/releaseview.action?pageId=338362818)
