---
content_hash: af0595e0388f50808188377d80152b4514ac2e8c4e6087ff24d867730d74eaf1
fetched_at: '2026-06-29T00:09:29.115821+00:00'
page_id: '423938813'
product: rm
source: tdn-rm
title: Processo Produtivo Simples (Estoque)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938813
version: 16
---

Este processo baseia-se no cadastro simplificado de estruturas, componentes e atividades.   
A estrutura contém a informação do produto que possui itens como componentes e atividades produtivas com o intuito de obter o produto citado na estrutura.

Exemplo:

* Estrutura código "KitBasico" para o produto com descrição "Kit Escolar Básico";
* Atividades código "Separar" ("Separação de Itens") e "Montar" ("Montagem do Kit");

**Componentes (itens que compõem o produto da Estrutura)**: Além dos cadastros citados acima, será necessário parametrizar através do "Assistente de Implantação de Processos", os movimentos do tipo:

|  |  |  |  |
| --- | --- | --- | --- |
| **Item** | **Qtde** | **Estrutura** | **Atividade** |
| Caneta Esferográfica Azul | 01 Un. | KitBasico | Separar |
| Caneta Esferográfica Vermelha | 01 Un. | KitBasico | Separar |
| Caneta Esferográfica Preta | 01 Un. | KitBasico | Separar |
| Lapiseira 0,7 | 01 Un. | KitBasico | Separar |
| Régua Transparente 30cm | 01 Un. | KitBasico | Separar |
| Borracha Branca | 01 Un. | KitBasico | Separar |
| Caderno Espiral 120fls capa dura | 04 Un. | KitBasico | Separar |
| Mochila Modelo "X" | 01 Un. | KitBasico | Montar |

Além dos cadastros citados acima, será necessário parametrizar através do "Assistente de Implantação de Processos", os movimentos do tipo:

2.1.XX – como "Ordem de Produção", processo 04.04.08, parametrizar no tópico "Mov – Identificação" com a classificação "Produção (Gestão de Estoque)", habilitar no tópico "Produção" o parâmetro "Gera Ordem de Produção no RM Factor";  
2.2.XX – de "Baixa de Matéria-Prima", processo 04.04.05, parametrizar no tópico "Mov – Identificação" com a classificação "Produção (Gestão de Estoque)", habilitar no tópico "Produção" o parâmetro "Baixa de Matéria Prima a Partir do RM Factor";  
1.2.XX – para "Entrada de Produto Acabado", processo 04.09, parametrizar no tópico "Mov – Identificação" com a classificação "Produção (Gestão de Estoque)", habilitar no tópico "Mov – Outros Dados" o parâmetro "Usar Cópia de Movimentos por referência" com motivo "Produção", e no tópico "Produção" habilitar o parâmetro "Entrada de Produtos Acabados a Partir do RM Factor  
***Observações***: Para os tipos de movimentos acima deve ser observada a seguinte parametrização:

* Tópico "Mov – Identificação": Numeração / Edita Numeração: Mostra
* Tópico "Mov – Datas 2/2": Data Entrega / Edição da Data de Entrega: Edita
* Tópico "Item – Identificação 2/2": Unidade de Medida Padrão: Unidade de Controle
* Critério para Alteração: Ter a mesma Unidade Base

**Como utilizar o Processo de Produção Simples:**Inserir movimento do tipo "2.1.XX – Ordem de Produção" e incluir como item o produto cadastrado como Estrutura;

* Realizar o faturamento do movimento de "Ordem de Produção" em movimento do tipo "Baixa de Matéria-Prima" (este possuirá os componentes da Estrutura como itens);
* O movimento do tipo "Entrada de Produto Acabado" será gerado através de cópia por referência (menu "Movimentos | Gerar Mov. Por Referência"), terá como origem o movimento de "Ordem de Produção" e conterá o produto da Estrutura como item.

IMPORTANTE

Abaixo regras importantes para utilização do Processo Produtivo Simples:

* O movimento de "Ordem de Produção" deve conter apenas **um** item "Estrutura para Produção".
* No processo produtivo simples, o item "Estrutura para Produção" **não** **deve ser expandido** pois esse processo só é interpretado corretamente para o "Produção Conjunta".
* O faturamento da "Ordem de Produção" para realização da "Baixa de Matéria-Prima" **não suporta o faturamento automático**.
* Todos os movimentos só podem ser recebidos em sua totalidade, ou seja, **não é possível realizar baixas parciais.**
* Deverá ser validado os registros gerados para o **bloco K** referente o processo produto simples se atendem a empresa. Para mais informações dos registros gerados consulte a documentação: [Bloco K](https://tdn.totvs.com/display/public/LRM/SPED+Fiscal+-+Bloco+K#BLOCOK-K200)
* **Não poderá ser alterado** os cadastros de Estrutura, Componente e Atividade no mês de produção, isso se faz necessário para não gerar erros no validador do SPED Fiscal.
Informações Adicionais

* A partir da versão de patch **12.1.2602.137**, ao realizar a baixa de matéria-prima e faturamento do movimento gerado a partir de uma estrutura, a Tabela de Classificação considerada no item do movimento deve ser obtida a partir dos produtos componentes da estrutura (itens consumidos), e não da estrutura (produto pai).
* Detalhamento de como parametrizar [Processo Produtivo Simples](https://tdn.totvs.com/pages/viewpage.action?pageId=889099305)
* [Produtos Compostos](https://tdn.totvs.com/display/public/LRM/Produtos+Compostos)
