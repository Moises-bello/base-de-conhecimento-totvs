---
content_hash: 3f8a40ecabada97f0cb4d1bc8eae6d04ba0f06b09da2aec99d90d85441e2d395
fetched_at: '2026-06-29T00:09:22.200978+00:00'
page_id: '422545986'
product: rm
source: tdn-rm
title: Controle de Diferimento de PIS e COFINS
type: documentation
url: https://tdn.totvs.com/display/LRM/Controle+de+Diferimento+de+PIS+e+COFINS
version: 10
---

Conforme o parágrafo único da Lei 9.718 de 1998 em seu artigo sétimo, no caso de construção por empreitada ou de fornecimento a preço determinado de bens ou serviços, contratados por pessoa jurídica de direito público, empresa pública, sociedade de economia mista ou suas subsidiárias, o pagamento da COFINS e do PIS poderá ser diferido, pelo contratado, até a data do recebimento do mesmo.   
Este controle foi criado para atender a geração [EFD Contribuições](http://www1.receita.fazenda.gov.br/) nos seus registros M230, M300, M630 e M700.   
Para a correta utilização deste controle alguns pré-requisitos devem ser atendidos:

* Integração do Gestão de Compras com o Gestão Fiscal
* Movimentos escriturados para o período no qual o controle está sendo gerado.
* Integração do Gestão de Compras com o Gestão Financeira.
* Caso não exista integração do Gestão de Compras com o Gestão Fiscal ou não exista licença do mesmo, os Lançamentos Fiscais poderão ser incluídos manual e posteriormente integrados com o Gestão Financeira.
* Em ambos os casos as baixas dos títulos recebidos deverá ter sido executada para o período no qual o controle está sendo feito.
* Em hipótese nenhuma este controle será feito sem a integração com o Gestão Financeira.

Para ativar o controle de diferimento devem ser habilitados os parâmetros Controla Diferimento PIS/COFINS (Versão 11.40 e superiores) e Controla Diferimento PIS/COFINS por contratante (Versão 11.50 e superiores).  
O campo Código da Contribuição Social (Registro M300) nas versões anteriores a 12.0 é tratado como campo complementar no item do lançamento com as seguintes especificações:

|  |  |
| --- | --- |
| **Nome** | CODCONTRIBSOCIAL |
| **Tipo** | ALFANUMÉRICO |
| **Tamanho** | 2 |

Para efeito de cálculo serão considerados:

* Lançamentos Fiscais de saída que tenham sido emitidos para Clientes que sejam do tipo órgão público e possuam em seus itens os Tributos PIS e COFINS.
* Para os créditos, serão considerados os Lançamentos Fiscais de entrada que possuam os Tributos PIS e COFINS em seus itens.

Os lançamentos de Entrada e Saída devem ter o campo Tipo Crédito preenchido no Item Da Situação Tributária.  
Caso algum lançamento de saída não esteja com o Tipo Crédito preenchido o sistema apresentará uma mensagem informando o identificador do lançamento e não executará o processo.

Campo Tipo Crédito

**Total das Vendas:** Somatório do valor contábil (Quantidade x Preço) dos itens dos Lançamentos Fiscais nas condições citadas.  
**Total de Vendas não recebidas:** Calculado subtraindo-se do campo Total das Vendas o valor de todas as saídas emitidas e baixadas no período.  
**Total do Tributo:** Somatório do Tributo (PIS ou COFINS) das saídas emitidas no período do controle.  
**Total do Tributo Diferido:** Calculado subtraindo-se do campo Total do Tributo o valor do PIS ou da COFINS referente ao Total de Vendas não recebidas.  
**Total do Crédito:** Somatório do Tributo (PIS ou COFINS) das entradas no período do controle.  
**Total do Crédito diferido:** Somatório do valor do Tributo (PIS ou COFINS) do item das notas de entrada proporcionalizado em relação à receita diferida.

Exemplo de Cálculo do crédito diferido.  
Total das saídas no período: R$50.000,00  
Total das entradas no período: R$15.000,00  
Total PIS entradas: R$247,50  
Total de vendas não recebidas: R$30.000,00  
Neste caso o Total do Crédito diferido será: (30.000,00/50.000,00) \* 247,50 = R$148,50  
Calcula-se qual o percentual das vendas não recebidas em relação ao total das vendas no mês. Em seguida aplica-se este percentual no valor do tributo das entradas.

---

Legislação

Leia na íntegra a [Lei 9.718](http://www.planalto.gov.br/ccivil_03/LEIS/L9718compilada.htm), que trata, dentre outras informações, do diferimento do PIS e da COFINS.
