---
article_id: 360033673914
category: SIGAEST - CUSTOS
content_hash: 734c7fafd8c743c96deefd6ef53e681f2db91f7d4e76fc70529c09ced7e8202d
fetched_at: '2026-06-28T22:39:02.083977+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 -  Quais são
  os Métodos de Apropriação para execução do Recálculo do Custo Médio?
type: support-article
updated_at: '2026-03-17T14:49:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033673914-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Quais-s%C3%A3o-os-M%C3%A9todos-de-Apropria%C3%A7%C3%A3o-para-execu%C3%A7%C3%A3o-do-Rec%C3%A1lculo-do-Custo-M%C3%A9dio
---

O recálculo do custo médio no Protheus pode ser feito por três métodos de apropriação: Mensal (considera todas as entradas e saídas do mês), Diário (calcula o custo por dia) e Sequencial (segue a ordem de digitação dos movimentos), cada um impactando de forma distinta o valor do estoque.

**Dúvida**  
Quais são os Métodos de Apropriação para execução do Recálculo do Custo Médio e como funciona cada uma delas?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
O módulo de Estoque, por meio da rotina de **Recálculo do Custo Médio (MATA330)**, permite que os movimentos sejam recalculados conforme o método de apropriação definido na parametrização da rotina, sob 3 metodos existentes. No entanto, a escolha do método deve considerar a forma como a empresa necessita organizar os movimentos, a fim de garantir que o resultado obtido esteja alinhado com suas expectativas de calculo/ordenação e apuração.

|  |
| --- |
| **IMPORTANTE:** O método de apropriação de custos **é definido no momento da implantação dos custos da empresa**, após uma análise detalhada de toda a sua regra de negócios.  Caso haja necessidade de alteração, é fundamental entrar em contato com o gerente de contas ou com a unidade responsável pela implantação para solicitar a atuação de um analista consultor especialista em estoque e custos.  Esse profissional conduzirá uma nova análise da regra de negócios para validar se a alteração atenderá às novas expectativas do cliente.  Ressaltamos que essa modificação **não deve ser realizada sem o devido conhecimento sobre os custos e os impactos que a mudança poderá causar no cálculo de suas movimentações/ordenações/apurações.** |

**Métodos**:

- **Mensal**: A partir do saldo inicial, notas fiscais de entrada e devoluções ao estoque, do período informado, o sistema calculará o novo custo médio que valorizará as movimentações internas e notas fiscais de saídas do mesmo período informado para o recálculo;

**Da apropriação Mensal**, note que para essa apuração, é o método mais usado no Brasil e consiste em avaliar o estoque pelo custo médio apurado de todas as **notas fiscais de compra** sendo apuradas, antes das **notas fiscais de saida**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27712768341655)

**- MÉTODO DIARIO:** Todas as entradas de notas fiscais e devoluções ao estoque do DIA são consideradas para obtenção do custo médio que fará a valorização das requisições e notas fiscais de saídas do mesmo DIA, portanto, a cada dia posso ter uma valorização diferenciada dos meus estoques, dependendo das entradas efetuadas;

**Da apropriação Diaria****,**note que as notas do "dia 06/09" **não são mais sequenciadas**, pois a sua apropriação respeita a ordenação por "**Dia**", lembrando assim do conceito da normativa ([Parecer Normativo CST nº 6/1979](https://tdn.totvs.com/pages/releaseview.action?pageId=789992253)) Primeiro os documentos **fiscais de compra** antes das **notas fiscais de venda**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27712795577495)

- **MÉTODO SEQUENCIAL**: Todas as movimentações dos estoques são valorizadas exatamente na ordem em que foram digitadas, para tanto, os arquivos SD1, SD2 e SD3 contém o campo **D?\_NUMSEQ**, que guarda o número sequencial de sua gravação.

**Da apropriação Sequencial****,** Observe que, conforme o sequenciamento apresentado na tabela abaixo, independentemente de as notas fiscais serem de entrada ou saída, ou mesmo no caso de alteração da **database para inserção de movimentos esquecidos com datas distintas do que deveriam ter sido efetuadas naquele dia, essa ação não surtirá efeito**. Isso ocorre porque a apropriação foi definida para ser sempre sequencial, garantindo que o método adotado ordene e processe o cálculo das movimentações de forma contínua e estruturada, toda sua apuração vai ser respeitada conforme **D?\_NUMSEQ** da movimentação, ou mais conhecido como "sequencial de digitação do usuario".

**Se eu efetuo uma nota de entrada, após efetuo uma requisição desse saldo para OP, mas depois vem uma nota de complemento para essa entrada, entenda que como sua forma é sequencial o custo da requisição não tera o custo do complemento, pois ele veio após a requisição.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27712795581719)

**Saiba mais:**

[*MP - SIGAEST - Recálculo do Custo Médio (MATA330) - Conceito e Informações*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013945671)

[*MP - SIGAEST - Rotina MATA330 - Perguntas do Recálculo do Custo Médio*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024805291)

[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000049222-SIGAEST-CUSTOS)
