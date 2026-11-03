---
content_hash: 2256f904da701ca22ab80fcfd9c40debf250dd794b12c27147c7559c9be1a327
fetched_at: '2026-06-29T00:08:04.670481+00:00'
page_id: '235576138'
product: rm
source: tdn-rm
title: CTR0001_vinculo_entre_ctrc_e_nota_fiscal_de_entrada
type: documentation
url: https://tdn.totvs.com/display/LRM/CTR0001_vinculo_entre_ctrc_e_nota_fiscal_de_entrada
version: 2
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão de Estoque, Compras e Faturamento |
| **Versões:** | Todas |
| **Ocorrência:** | Processo de Vínculo entre CTRC e Nota Fiscal de entrada |
| **Ambiente:** | Movimentação de Conhecimento de transporte com a existência de Vínculo entre o CTRC e a Nota. |
| **Passo a passo:** | **Movimento de CTRC:(Cadastra CTRC)**    Exemplo de Fórmula:    No movimento:  Informa-se o valor das Notas e da sua quantidade neste movimento. Campos: - Quantidade de Notas do CTRC - Valor das Notas do CTRC    Isso significa que, ao incluir as notas e associá-las a este Conhecimento de transporte, ao final da inclusão da 2ª nota (Que é a quantidade informada neste exemplo) deverá bater com o valor total informado. Essa consistência será realizada a qualquer momento que realizar um vínculo, caso uma das duas informações ultrapasse os totais vinculados ou quando todas as notas tiverem sido vinculadas mas ainda restar valor de nota a ratear.  O cálculo da nota é feito de acordo com a fórmula informada nos parâmetros do CTRC (*Fórmula do Valor* *do CTRC a Ratear*), e não pelo valor do movimento da nota. Ou seja, a nota pode ter um valor diferente, mas se a execução da fórmula do CTRC fechar os valores o sistema não irá criticar.  **Observação:** O valor líquido do movimento de CTRC deverá ser o valor do Frete. Que será distribuído entre as notas associadas.  **Movimento de Nota que aponta um CTRC: (Indica CTRC)**    Informa-se os dados normais do movimento e associa-se o CTRC desejado:    Observe que o valor do frete total é R$ 55,00, mesmo valor liquido informado no CTRC, e o valor rateado depende do resultado da fórmula executada de acordo com o parâmetro. Neste caso, será associado ao CTRC o valor de 250,00 e 1 nota.  O sistema não emite nenhuma mensagem de erro pois os valores são aceitáveis.  Incluindo a 2ª nota, de acordo com o que foi informado no CTRC, o sistema seguirá o mesmo conceito.    Novamente, o valor rateado depende do resultado da fórmula executada de acordo com o parâmetro. Neste caso, será associado ao CTRC o valor de 500,00 e 1 nota.  Somando os valores da nota e a quantidade da nota, teríamos o valor correto, fechando os valores apontados no CTRC (2 | 750,00).  - Quantidade de Notas do CTRC = 1 + 1 => 2 - Valor das Notas do CTRC = 250,00 + 500 => 750    Observe que, se o valor resultado da fórmula não fechar com o CTRC, apresentará a mensagem de erro: *“O valor desta nota somado aos valores já rateados é menor que o valor total do CTRC de número* *XXXXX”*  Veja que o valor da nota será de 450,00. Este valor somado ao total já associado não fecha (250,00 + 450,00 = 700,00). Neste caso, deve ser tratado corrigindo o valor do movimento de nota, ou corrigindo o valor informado no movimento de CTRC ou corrigindo a “Fórmula do Valor do CTRC a Ratear” para que os totais fechem. |
| **Observações:** | Para mais informações:    [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
