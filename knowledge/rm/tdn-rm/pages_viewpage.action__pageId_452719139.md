---
content_hash: 8d5a1d1ba09fbb8c5d1bd84c2e15063e0061e3eb2a6b03fb28b8e483ff51c177
fetched_at: '2026-06-29T00:10:03.710410+00:00'
page_id: '452719139'
product: rm
source: tdn-rm
title: Lançar Calculados por Fórmula
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719139
version: 2
---

**Lançar Calculados por Fórmula**

Este processo é utilizado para que os eventos calculados por fórmula, código de cálculo 0040, cadastrados em Configurações | Parâmetros Gerais | Eventos, sejam lançados no movimento.

Este evento deve também ser cadastrado no parâmetro Sindicato do funcionário em Configurações | Parâmetros Gerais | Parametrizador.

Embora o recálculo já faça essa funcionalidade, pelo parâmetro 'Calcula Eventos por Fórmula no Movimento', esta tela tem a particularidade de poder alterar eventos pontuais, lançando ou excluindo, garantindo melhor desempenho para este processo.

**Seleção de Funcionários**

A seleção de funcionário é a padrão dos processos do TOTVS Automação de Ponto. Através deste componente são determinados os funcionários que terão a fórmula lançada no movimento.

**Opção de Lançamento:**

* **Lançar:** Marque esta opção para lançar no movimento do período do funcionário o evento calculado por fórmula.
* **Excluir:** Marque esta opção para retirar do movimento do período do funcionário o evento calculado por fórmula.

**Eventos do Ponto:**  
Listará todos os eventos calculados por fórmula, código de cálculo 0040.

* **Todos:** Utilize esta opção para marcar/desmarcar todos os eventos a serem considerados no lançamento que estão na janela de "Eventos do Ponto".

**Gera arquivo de Log Técnico -** Gera o arquivo "RMCHRONUS\_LancaEventoFormula\_LOG.TXT", na pasta C:\Totvs\CorporeRM\RM.Net, depois da execução do cálculo. É utilizado pela equipe de desenvolvimento Totvs para detectar problemas de desempenho ou até mesmo erros específicos na execução do cálculo.

**Considera Funcionários com Alteração Manual/Compensação do Banco -**Este parâmetro deve ser marcado caso queira realizar o lançamento de eventos calculados por fórmula para funcionários com alterações manuais ou Compensação / Lançamento de banco de horas.
