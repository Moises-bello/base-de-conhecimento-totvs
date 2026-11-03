---
content_hash: d8159455fbd09e6ed4307dab35bd803cb827a7714c4a3b6a86c2b71e130b244c
fetched_at: '2026-06-29T00:11:55.955232+00:00'
page_id: '864986742'
product: rm
source: tdn-rm
title: Custos do Período – SIGAMNT
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=864986742
version: 1
---

* Opção de Menu: Projetos \ Construção e Projetos \ Controle \ Básico \ Mobilidade \ Equipamentos \ Custos do Período \ Custos Diretos;
* Opção de Menu: Projetos \ Construção e Projetos \ Controle \ Básico \ Mobilidade \ Equipamentos \ Custos do Período \ Custos Indiretos;
* O parâmetro “Integrado com o SIGA-MNT” deve estar HABILITADO;
* A integração “TOTVS Construção Obras e Projetos x Manutenção de Ativos” deve estar ativa no modulo de integração do RM. Para certificar é necessário acessar “Integração -> Integração -> RM Conector -> Mensagem Única -> Integrações”. Caso não esteja ativa é necessário ativá-la através da funcionalidade de configuração disponível em “Integração -> Ferramentas -> Ferramentas -> Configurar”;
* Os apontamentos realizados pelo coletor móvel são enviados ao SIGA-MNT, conforme descrito em Enviar. Os custos diretos e indiretos dos equipamentos são agrupados e enviados de volta ao TOP para apropriação e revaloração. Este envio é feito através da mensagem única “AssetMonthlyCosts”;
* São enviados ao TOP os custos diretos e indiretos dos equipamentos, assim como todos os apontamentos realizados (via coletor móvel ou Pointer);
* Os custos enviados são agregados ao projeto que tenha o mesmo centro de custos e filial do equipamento. São considerados somente projetos com a situação de andamento, execução e negociação.
* **Visão de Custos Diretos**

* + São exibidas informações relativas aos custos diretos que são compostos por apontamentos produtivos e improdutivos. Os apontamentos e os custos diretos (das horas trabalhadas) são agrupados por Filial/Equipamento/Ano-Mês/Frente de Trabalho;
  + No anexo de Apontamentos de equipamentos é disponibilizado o processo de associar tarefa, que simplifica a definição de tarefas para apontamentos. Estas tarefas são as utilizadas no momento da apropriação que deverá ser realizada na visão de apontamentos indiretos.
* **Visão de custos Indiretos**

* São exibidas informações relativas aos custos indiretos (manutenção corretiva, preventiva, abastecimento e outros) são agrupados por Filial/Equipamento/Ano-Mês;
* O processo de apropriar custos de equipamentos, realiza a apropriação dos apontamentos (custos diretos) de equipamentos;
* O cálculo do valor da apropriação é realizado da seguinte forma:
  + Para cada equipamento calcula-se o valor do ticket médio acrescido dos custos indiretos. O valor do Ticket Médio será calculado dividindo-se o custo total pelo volume de horas (produtivas e improdutivas);
  + Os custos indiretos serão rateados proporcionalmente, conforme o número de horas de cada frente de trabalho;
  + É considerada a parametrização de quais custos indiretos devem ser considerados para compor o custo final do equipamento. O parâmetro é “Custo Indiretos – Equipamentos.

* + - Ticket Médio = (SOMA 03 + SOMA 01) / SOMA 02

* **Apropriação de Serviços / Insumos**  
  + **Revalorar Custos de Equipamentos - SIGAMNT**
    - Opção de Menu: Projetos \ Construção e Projetos \ Controle \ Básico \ Apropriações de Insumos / Serviços \ Processos \ Mobilidade \ Revalorar Custos de Equipamentos;
    - O parâmetro “Integrado com o SIGA-MNT” deve estar HABILITADO;
    - Esta funcionalidade deve ser executada após recebimento dos apontamentos e custos do Manutenção de Ativos do PROTHEUS;
    - Após a seleção do período para o qual deseja efetuar a revaloração é exibida uma mensagem de confirmação informando a data em que foi realizada a última apropriação de apontamento importado do SIGA-MNT para o período informado. Prosseguindo com a execução os valores das apropriações existentes serão atualizados;
    - O calculo do Valor é realizado utilizando a mesma regra da apropriação de apontamentos de equipamentos e ravaloradas todas as apropriações relativas ao bem e centro de custos que estão contempladas dentro do mês e ano informados.
