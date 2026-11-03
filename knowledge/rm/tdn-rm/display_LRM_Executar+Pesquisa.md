---
content_hash: b6a590a7f36c4a55a16339f55d5d4c5ec95b67064c3b1fe9e06a1650247153c6
fetched_at: '2026-06-29T00:09:59.865893+00:00'
page_id: '452718429'
product: rm
source: tdn-rm
title: Executar Pesquisa
type: documentation
url: https://tdn.totvs.com/display/LRM/Executar+Pesquisa
version: 2
---

**Executar Pesquisa**

Após parametrizado, o LNTD deverá ser executado este processo para calcular as demandas de treinamento, onde serão apresentados os cursos recomendados para cada característica/competência a ser treinada.

As regras utilizadas como critérios para definições de cursos recomendados são as seguintes:

* Competências: Verifica qual o curso que treina o maior número de requisitos vinculados à competência encontrada como demanda de treinamento;
* Características Pessoais: Verifica qual o curso que treina a característica pessoal a ser treinada. Neste caso, não existe uma regra para diferenciar um curso dos demais que a treina, sendo recomendado o primeiro da lista.

Após o cálculo do LNTD, poderá verificar o resultado de todas as características pessoais/competências com necessidades de treinamento e os cursos recomendados clicando no botão: **"Visualizar o resultado do LNTD"**.

Na tela de visualização do LNTD, será possível "Aprovar", "Negar" ou "Limpar" uma sugestão de treinamento por  um processo. ara executar o processo, acesse o resultado do LNTD, selecione as sugestões de treinamento desejadas, e execute um dos processos de acordo com a necessidade.

Haverá um status indicando se a pessoa já fez ou não o treinamento, ou se já está inscrita em um treinamento para mesma característica/competência.

Será possível também gerar um plano de treinamento a partir de um LNTD, ou ainda mesclar o LNTD em um plano de treinamento já existente. Este poderá gerar turmas ou apenas orçamento do treinamento. As turmas poderão ser propostas com os participantes ou apenas reservar a vaga por centro de custo da pessoa selecionada.

Para executar o processo acesse: Desenvolvimento | LNTD, escolha o registro desejado e execute o processo: "Gerar Plano de Treinamento" e informe se deseja criar um novo plano de treinamento, ou complementar um plano já existente.

Caso opte por gerar turmas para orçamento, o sistema gera um orçamento no anexo "Orçamento do treinamento" para cada curso levantado anteriormente para que sejam utilizados no planejamento de despesas.

Caso opte por gerar turmas propostas, o sistema informa se deseja inscrever os participantes selecionados ou reservar vaga para o centro de custos dos participantes selecionados.

**Quanto ao centro de custo:**

Caso selecione na caixa de opções de centro de custo, a opção "Centro de custo da seção do funcionário", será utilizado o centro de custo vinculado à seção do funcionário.  
Caso selecione a opção "Fórmula", poderá escolher uma fórmula que definirá onde buscar o centro de custo.
