---
content_hash: 8280da5ea56e79982eb4f42110818d0adee637b063d9a6c3d7c0aec50a35ef8e
fetched_at: '2026-06-29T00:06:18.951005+00:00'
page_id: '219694078'
product: rm
source: tdn-rm
title: SAU0060_Como_Realizar_a_Cobrança_de_Medicamentos_Fracionados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=219694078
version: 115
---

# Como realizar a cobrança de medicamento fracionado

|  |  |
| --- | --- |
| **Produto:** | TOTVS GESTÃO HOSPITALAR |
| **Versões:** | Todas as Versões. |
| **Ocorrência:** | Possuí-se, no hospital, um Frasco com 4 mililitros. Destas 4 Mililitros, somente é usada 1 por paciente.  Entretanto, o convênio cobra por Frasco e não por Mililitros. |
| **Passo a passo:** | 1° Passo: Criação das Unidades.  Acesse o menu Cadastros -> Estoque -> Unidades de Medida.  Primeiramente, vamos criar a unidade FRASCO - Código FRT.  Nela, dizemos que 1 Frasco equivale a 4 UN.    Agora, vamos acessar a unidade ML e vamos dizer que ela equivale a 1 unidade.    Sendo assim, 1 FRT (Frasco) equivale a 4 ML (Mililitros).  2° Passo - Ajuste no Produto.  Acesse o menu Cadastros -> Estoques -> Produto.  Acesse o produto.  Na aba "Controle de Estoque", em Unidade de Controle, iremos preencher com ML.  Em unidade de Compra e Venda, colocaremos FRT.  Neste caso, estamos dizendo ao sistema que iremos controlar o estoque através da Unidade ML, entretanto, iremos comprar o produto em Frasco e vendê-lo em Frasco.    3° Passo - Ajuste de Preço  Dentro do próprio cadastro do Produto, presente no 2° Passo, clique em "Anexos" -> Informações TOTVS Saúde.  Clique Novamente em Anexos -> Tabela de Preços  Acesse a tabela de preços correspondente ao convênio o qual deseja realizar a parametrização.  Dentro da tabela, em nosso exemplo, iremos dizer que:  O preço do nosso produto é R$ 20,00 para o paciente.  Quando o paciente realiza o uso do Produto Teste, o uso de 1 Unidade do Produto teste equivale a 1 Unidade ML  Sendo assim, na cobrança do paciente, o valor cobrado pelo uso de 1 unidade do produto, será R$20,00.  Entretanto, o estoque dará baixa de 1 ML.      Situação 2: Caso queiras cobrar somente pelo ML, você deve preencher o campo "Volume" com o valor 4.  Sendo assim, o fator de conversão irá se tornar R$0,25. Assim, na conta do paciente, o sistema cobraria R$5,00 ao convênio. |
| **Observações:** |  |

divs
