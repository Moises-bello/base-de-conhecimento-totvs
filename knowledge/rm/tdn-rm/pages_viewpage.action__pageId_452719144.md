---
content_hash: 4627348cae152afc25cb4f8fe35feee719df14c2bb075041f7caab82bc4bbfb1
fetched_at: '2026-06-29T00:10:03.721039+00:00'
page_id: '452719144'
product: rm
source: tdn-rm
title: Lança Eventos para Folha de Pagamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719144
version: 3
---

**Lança Eventos para Folha de Pagamento**

Por este módulo, os eventos calculados no RM Chronus poderão ser selecionados e lançados para a folha de pagamento. Os eventos lançados serão gravados em uma tabela temporária (PFMOVTEMP), para permitir ao RM Labore controlar o que será gerado no envelope de pagamento e gerenciar a movimentação dos funcionários de acordo com o código de recebimento (semanalistas, quinzenalistas e mensalistas). Após a execução desse módulo, para que os eventos calculados no RM Chronus sejam lançados para a movimentação dos funcionários no RM Labore, deverá ser executado o módulo "Lançamento de grupos de eventos" utilizando o parâmetro "Lançar eventos da integração com outros aplicativos" no RM Labore.

**Observação**

Para que um evento seja lançado no RM Labore, ele deverá estar incluído na pasta "Eventos a serem lançados no RM Labore" no Sindicato do RM Chronus. Para cada Sindicato, deverão ser cadastrados os eventos que, se presentes no movimento do funcionário, serão lançados para o RM Labore através desta opção.

**Para o grupo de funcionários:** **Código de quebra** Informe o código de quebra da seção a qual pertencem os funcionários que terão os eventos lançados.

**Seleção de Funcionários** Clique no botão "Seleção de Funcionários" para acessar a janela que irá selecioná-los por situação, tipo, código de recebimento ou Chapa

**Ações:**

**Ignorar** Mantém o valor do evento caso ele já exista (Inclui se não existir).

**Somar** Soma o valor constante no movimento com o valor do evento já lançado, caso o evento já exista (inclui se não existir).

**Substituir** Substitui o valor do evento já lançado, caso o evento já existia (inclui se não existir).

**Parâmetros:**

**Grava controle de faltas para cálculo de avos na folha** Selecionando essa opção, o sistema lançará as faltas do funcionário para o RM Labore, inserindo os dados da tabela AFALTAPARAFOLHA na tabela PFHSTFALTA. Essas faltas serão utilizadas posteriormente para a gestão de férias do RM Labore.

**Observação**

 Utilizando esse parâmetro o RM Chronus apenas lançará a falta para uma tabela auxiliar do RM Labore e não lançará o evento de Falta, para isso deverá ser selecionado o evento nos "Eventos a serem lançados".

**Lança eventos para funcionários demitidos** Ao habilitar este parâmetro o sistema irá lançar os eventos para os funcionários demitidos no período vigente. Caso o usuário não deseje lançar os eventos para os funcionários demitidos é só não marcar o parâmetro.

**Eventos a serem lançados** Selecione aqui os eventos que serão lançados para o RM Labore.

**Eventos de refeição** Selecione aqui os eventos de refeição que serão lançados para o RM Labore.
