---
content_hash: fbea84a84887aa1c5b59a3548db575b57d694c723b5258356d73617bf2bf2d54
fetched_at: '2026-06-29T00:11:45.799544+00:00'
page_id: '821579588'
product: rm
source: tdn-rm
title: Configuração do Layout
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=821579588
version: 5
---

Após as definições de Fatos Contábeis e Colunas, na aba Configurações do Layout, é possível visualizar como ficou a pré-montagem da Estrutura, e será possível realizar as parametrizações do layout.  
A **parametrização do layout** consiste em definir a origem/composição dos valores que serão visualizados no Fato Contábil x Coluna, ou seja, para cada célula da coluna em que o Fato Contábil deva processar um valor, o usuário deverá clicar sobre a célula e do lado direito parametrizar como o valor será composto (contas contábeis, Origem do Valor e Sinal).

**Origem do Valor:** possibilita a definição de qual valor será buscado para a informação da célula, sendo possível a seleção de Saldo Inicial, Movimentação (Débito - Crédito), Saldo Final, Total Débito, Total Crédito, Filtro Genérico, Outra Coluna e Expressão.

**Sinal:** possibilita a definição de como o valor da conta será emitido no relatório, podendo ser o valor Original, com Efeito Positivo (Aumenta), ou com Efeito Negativo (Diminui).  
Após as definições de campo é **necessário Confirmar**, para que as configurações realizadas sejam salvas.  
  
**Contas Contábeis**: possibilita a seleção de uma, várias ou um intervalo de contas contábeis para a demonstração no relatório.  
  
**Filtro Complementar**: Recurso disponível para Estruturas que não consolidam (Opção "Consolidado" na identificação da estrutura).  
Permite a inclusão de filtros complementares que serão utilizados para trazer o resultado do fato contábil que está sendo configurado, na geração da demonstração.  
Nessa aba ainda, é possível **pré visualizar** Partidas por lote ou lote zero, após informar o filtro global.  
Utilização de campos complementares no filtro:   
  -Só é permitido a utilização de campos complementares no filtro, caso a **Origem do Valor** seja do tipo Movimentação. Caso seja configurado de forma diferente, não será possível gerar a demonstração.  
  -Para a utilização das funcionalidades de pré visualização de partidas, é necessário que o parâmetro "Exibir campos complementares na visão de lançamento", localizado nas Preferências de Usuário, esteja **marcado**.  
  -Na geração da demonstração, caso a opção "Buscar do histórico contábil" esteja marcada, os filtros complementares informados devem ser filtros cadastrados no sistema antes do fechamento do período. Caso contrário, não será possível gerar a demonstração buscando do histórico.

---

Legenda de ícones na configuração do Layout:

 - Rótulo;

 - SubTotal;

 - Totalizador sintético;

 - Totalizador analítico;

 - Parametrização necessária;

 - Coluna parametrizada;

 - Parametrização iniciada, porém com pendências;
