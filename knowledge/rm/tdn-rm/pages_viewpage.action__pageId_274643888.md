---
content_hash: 4213822306ab00c90dc9e11bf6af15dffe34b8394d24662840db96809eb0cd45
fetched_at: '2026-06-29T00:08:34.081031+00:00'
page_id: '274643888'
product: rm
source: tdn-rm
title: CNT0002_Gerar_Financeiro_de_Acordo_com_a_Data_de_Faturamento_do_Contrato.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274643888
version: 3
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão de Estoque, Compras e Faturamento |
| **Versões:** | 11.83, 12.1 e superiores |
| **Ocorrência:** | Gerar Financeiro de acordo com a data de faturamento do contrato. |
| **Ambiente:** | Faturamento de Contrato. |
| **Passo a passo:** | **Objetivo:** Gerar Financeiro de acordo com a data de faturamento do contrato.    **Necessidade:** Ao faturar um contrato inteiro (geralmente periódico), o sistema gera o financeiro de todos os movimentos da mesma forma. Para que isto não ocorra deverá seguir os procedimentos listados a seguir.    **Parâmetros de Contrato.**  Menu Ambiente | Parâmetros | TOTVS Gestão de Estoque, Compras e Faturamento | Contratos | Faturamento | Avança:      **Etapa Definições Fat. Contrato 1/3**  Copiar Data de Venc/Medição p/Mov: Informar para qual data será carregada a data de faturamento do contrato. Opções:   * + Data de Entrega   + Data de Entrada/Saída   + Data Extra 1   + Data Extra 2       **Parâmetros do tipo de movimento a ser gerado.**  Menu Ambiente | Parâmetros | TOTVS Gestão de Estoque Compras e faturamento | Localizar o tipo de movimento no parametrizador | Parametrizar o tipo de movimento desejado:    **Etapa Mov- Datas 1/2 ou 2/2 (dependendo da data selecionada no contrato).**  - Edição da data = Edita ou Mostra  - Definir o Nome da data (caso esteja disponível)  - Copiar valor Default = Nenhum        **Etapa Fin- Faturamento 2/6**   * + Vencimento a Partir: Informar a mesma data definida no contrato (Data de Entrega, Data de Entrada/Saída, Data Extra 1 ou Data Extra 2).  * + Data de Emissão: Informar a mesma data definida no contrato (Data de Entrega, Data de Entrada/Saída, Data Extra 1 ou Data Extra 2).         **Processo:**  Ao Gerar o faturamento do contrato, o lançamento financeiro irá considerá a data alternativa que foi configurada para definir o vencimento das parcelas, e não mais a data de emissão (que será a mesma em todos os movimentos). Veja o exemplo.    **Contrato Periódico com 3 faturamentos, sendo 1 a cada mês. Utilizando a "Data Extra 1" como a data de faturamento.**    - Data Início do contrato = 01/01/2000  - Data em que o contrato foi faturado = 10/01/2000  - Condição de pagamento = 30 Dias  - Movimentos gerados: 3    **Movimento 1:**  - Data de emissão do movimento = 10/01/2000  - Data Extra 1 = 01/01/2000  - Data Emissão (financeiro): 01/01/2000  - Data Vencimento (financeiro): 01/02/2000    **Movimento 2:**  - Data de emissão do movimento = 10/01/2000  - Data Extra 1 = 01/02/2000  - Data Emissão (financeiro): 01/02/2000  - Data Vencimento (financeiro): 01/03/2000    **Movimento 3:**  - Data de emissão do movimento = 10/01/2000  - Data Extra 1 = 01/03/2000  - Data Emissão (financeiro): 01/03/2000  - Data Vencimento (financeiro): 01/04/2000 |
| **Observações:** | Para mais informações:    [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |

[Curtir](http://tdn.totvs.com/display/LRM/FAT0001_Faturamento_Parcial_Por_Valor)Seja o primeiro a gostar disto

* [base\_de\_conhecimento](http://tdn.totvs.com/label/LRM/base_de_conhecimento)
* [faturamento\_parcial](http://tdn.totvs.com/label/LRM/faturamento_parcial)
* [faturamento\_parcial\_por\_valor](http://tdn.totvs.com/label/LRM/faturamento_parcial_por_valor)
* [versao\_11\_83](http://tdn.totvs.com/label/LRM/versao_11_83)
* [versao\_12\_1](http://tdn.totvs.com/label/LRM/versao_12_1)
* [rmnucleus](http://tdn.totvs.com/label/LRM/rmnucleus)
* [totvs\_gestao\_de\_estoque\_compras\_e\_faturamento](http://tdn.totvs.com/label/LRM/totvs_gestao_de_estoque_compras_e_faturamento)
* [desdobramento](http://tdn.totvs.com/label/LRM/desdobramento)
* [movimento](http://tdn.totvs.com/label/LRM/movimento)
* [movmovfaturamento](http://tdn.totvs.com/label/LRM/movmovfaturamento)
