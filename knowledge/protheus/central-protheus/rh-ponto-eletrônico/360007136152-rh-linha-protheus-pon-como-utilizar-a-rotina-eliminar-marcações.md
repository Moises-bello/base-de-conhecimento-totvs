---
article_id: 360007136152
category: RH - Ponto Eletrônico
content_hash: efee46f33c01df41f46df38278f2f74e3971fb7420cccedc4b23d90f6acfbbed
fetched_at: '2026-06-28T22:44:58.232586+00:00'
product: protheus
section_id: 206956208
source: central-protheus
title: RH - Linha Protheus - PON - Como utilizar a rotina Eliminar Marcações
type: support-article
updated_at: '2025-10-22T18:14:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007136152-RH-Linha-Protheus-PON-Como-utilizar-a-rotina-Eliminar-Marca%C3%A7%C3%B5es
---

**Dúvida**Como utilizar a rotina Eliminar Marcações?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**A rotina Eliminação das Marcações (PONM050): **Miscelânea>Cálculos>Eliminar Marcações**,tem como objetivo deletar os registros relacionados abaixo, conforme critérios definidos pelo usuário:  
  
- Marcaçöes(SP8)\_\_\_\_\_\_\_\_Acumulado de Marcaçöes(SPG)  
- Apontamentos(SPC)\_\_\_\_Acumulados Apontamentos(SPH)  
- Refeiçöes(SP5)\_\_\_\_\_\_\_\_\_\_Acumulado de Refeiçöes(SPN)  
- Resultados(SPB)\_\_\_\_\_\_\_\_Acumulado de Resultados(SPL)  
- Banco de Horas(SPI)\_\_\_\_Abonos(SPK)  
  
Com o advento da Portaria 1510/2009 e 671/2021, marcações originais não podem ser deletas e deverão constar na base de dados para futuras conferências e fiscalizações.  
  
Para deletar os registros, configure os parâmetros conforme sua necessidade. Segue o conceito de utilização de cada parâmetro:  
- Data Início?/Data Fim? Informe nestes parâmetros um intervalo de datas em que as marcações devem ser deletadas.  
**- Excluir Marcações ?** -> Tem como objetivo excluir as marcações utilizando com base data inicio e fim passada na pergunta anterior validando se estas datas possuem marcações na SP8 período aberto(movimento), SPG período fechado(acumulado) ou nas duas tabelas se optar ambos.Caso opte não, não ocorrerá a exclusão de marcações e percorrerá ao próximo parâmetro.  
**-Excluir Refeições ?** -> Tem como objetivo excluir as marcações utilizando com base data inicio e fim passada na pergunta anterior validando se estas datas possuem marcações na SP5 período aberto(movimento), SPN período fechado(acumulado) ou nas duas tabelas se optar ambos.Caso opte não, não ocorrerá a exclusão de marcações e percorrerá ao próximo parâmetro.  
**-Excluir Apontamentos** **?** ->Tem como objetivo excluir as marcações utilizando com base data inicio e fim passada na pergunta anterior validando se estas datas possuem marcações na SPC período aberto(movimento), SPH período fechado(acumulado) ou nas duas tabelas se optar ambos.Caso opte não, não ocorrerá a exclusão de marcações e percorrerá ao próximo parâmetro.  
**-Excluir Resultados ?** ->Tem como objetivo excluir as marcações utilizando com base data inicio e fim passada na pergunta anterior validando se estas datas possuem marcações na SPB período aberto(movimento), SPL período fechado(acumulado) ou nas duas tabelas se optar ambos.Caso opte não, não ocorrerá a exclusão de marcações e percorrerá ao próximo parâmetro.  
**-Excluir Abonos ?** ->Sim para excluir os abonos da SPK, esta tabela não possui acumulados de período fechado e Não para não excluir.  
**-Excl. Banco de Horas ?** ->Sim para excluir os movimentos de BH da SPI,esta tabela não possui acumulados de período fechado e Não para não excluir.  
**-Limpa Lancamentos ?** ->Informe o tipo de lançamento que deseja eliminar. Validará com base na FLAG do lançamento de cada tabela. As opções a serem escolhidas:   
 Gerado; Informado; Leitura; Marcacao; Classificado  
**-Limpa Todos Tipos ?** ->Informe se deseja limpar Todos os Tipos de Lançamentos. Caso selecione a opção "SIM", esse parâmetro substitui o conteúdo informado no parâmetro anterior, se a opção for "Não", o sistema efetuará a limpeza do Tipo Selecionado no parâmetro anterior.  
**- Considera Data Apontamento**?   
Selecionando a opção "Sim" o sistema considera a data de apontamento ao inves da data de registro da marcacao. Exemplo:  
Funcionário trabalha no noturno, inicia seu turno em um dia e finaliza no outro;  
Data de Apontamento: 05 de maio   
marcações.: 20:00-22:00-00:00-03:00  
Se a eliminação for pela data do apontamento e se a data compreende em 05 de maio, todas as marcações acima serão eliminadas.  
Se a eliminação for pela data da marcação e se a datacompreende em 05 de maio somente as marcacões registradas nesse dia (20:00 e 22:00) serão eliminadas.  
  
Segue as telas da rotina:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35812928754967)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35812942018455)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35812942022807)  
Após a confirmação dos parâmetros será perguntado se deseja continuar com a exclusão total dos dados do ponto eletrônico do funcionário.  
-Caso seja clicado em "Não" a rotina seguirá com a exclusão respeitando as perguntas 'Excluir Marcações', 'Excluir Refeições', 'Excluir Apontamento', 'Excluir Resultados', 'Excluir Abonos', 'Excl. Banco Horas' e 'Limpar Todos Tipos'.  
-Caso seja clicado em "Sim" a rotina seguirá com a exclusão total de todos os registro do ponto eletrônico do funcionário.  
![](https://tdn.totvs.com/download/attachments/1005905635/image-2025-10-16_18-6-30.png?version=1&modificationDate=1760648790093&api=v2)

Caso tenha sido clicado em "Sim" será gerado o log de execução, informando quais funcionários tiveram todo os seus dados apagados e quais possuem uma marcação original e por isso não foi executada a exclusão dos dados.  
![](https://tdn.totvs.com/download/attachments/1005905635/image-2025-10-17_9-14-4.png?version=1&modificationDate=1760703244917&api=v2)  
**Saiba mais,**[Eliminar Todos os Dados do Ponto Eletrônico Para Permitir a Exclusão do Funcionário](https://tdn.totvs.com/pages/releaseview.action?pageId=1005905635)  
[Como eliminar marcações pela rotina PONM050?](https://tdn.totvs.com/pages/releaseview.action?pageId=382549725)  
[Manual do Ponto-PROTHEUS](https://tdn.totvs.com/pages/viewpage.action?pageId=630823373)
