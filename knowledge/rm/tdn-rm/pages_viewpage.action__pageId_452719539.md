---
content_hash: 321f206eb3979b870c28b053453bb5a17fce71850d905cae00857c8b7b3bd1cb
fetched_at: '2026-06-29T00:10:08.571162+00:00'
page_id: '452719539'
product: rm
source: tdn-rm
title: Períodos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719539
version: 4
---

O período é uma entidade muito forte no sistema e o objetivo dessa organização é guiar para uma correta definição e utilização do período de apuração de ponto. Basicamente, os recursos de Automação de Ponto irão considerar o período aqui definido. Portanto, as alterações e processos aqui executados, poderão impactar no cálculo e movimentação dos funcionários.   
Este menu permitirá a gestão dos períodos de apuração do ponto, exibindo um histórico de todos os períodos existentes no RM Chronus.   
**Atenção**

Para editar ou excluir algum registro (Competência) do histórico de períodos precisamos ter bastante atenção, pois para aquele período excluído pode haver movimentação.

Por isso recomendamos que esse tipo de manutenção seja feita com acompanhamento da equipe de suporte da TOTVS, utilizando os processos de 'Acerto de Inconsistência'

**Competência -**O mês e ano definem a competência a ser considerada no RM Chronus. O sistema permitirá cadastrar mais de um período mensal para o mesmo mês de competência, desde que o intervalo mensal, semanal e quinzenal não esteja em interseção com outro já existente.

**Período Mensal -**O período mensal aqui registrado define o início e o fim em que serão coletadas as batidas do ponto, facilitando o acompanhamento da movimentação para os funcionários com forma de recebimento mensal. Esse intervalo poderá ser de um mês para o outro, variando nesse caso apenas a competência.

**Exemplo:**

Apuração do ponto: 20/12/2009 a 19/01/2010 Nesse caso podemos definir a competência como 12/2009.

**Observação**

Um próximo período mensal deverá ser subseqüente ao anterior. Poderá ser registrado um mesmo período mensal várias vezes, desde que o período quinzenal e semanal não estejam em interseção com outro já existente.

**Período Quinzenal -** O período quinzenal aqui registrado define o início e o fim em que serão coletadas as batidas do ponto, facilitando o acompanhamento da movimentação para os funcionários com forma de recebimento quinzenal.

**Observação -** Um próximo período quinzenal deverá ser subseqüente ao anterior. Poderá ser registrada uma mesma quinzena várias vezes, desde que o período semanal não esteja em interseção com outra já existente.

**Atenção**

Esses campos ficarão disponíveis para edição somente quando houver funcionários cadastrados com forma de recebimento quinzenal.

**Período Semanal -** O período semanal aqui registrado define o início e o fim em que serão coletadas as batidas do ponto, facilitando o acompanhamento da movimentação para os funcionários com forma de recebimento semanal.

**Observação**

Um próximo período semanal deverá ser subseqüente ao anterior. Poderá ser registrada uma mesma semana várias vezes dentro de um mesmo período mensal e/ou quinzenal.

**Atenção**

Esses campos ficarão disponíveis para edição somente quando houver funcionários cadastrados com forma de recebimento semanal.

Apenas o período ativo poderá ser alterado, lembrando que a alteração excluirá a movimentação do período e será necessário recalcular novamente a movimentação dos funcionários.

Não é possível excluir períodos e a criação dependerá do processo Liberar Período.

**Em que momento podemos alterar o período mensal e a competência?**

* Fazer alguma alteração de acerto no período anterior. Caso esta alteração for afetar a movimentação enviada para o sistema RM Labore, devemos lançar a movimentação novamente para a folha de pagamento. Temos que verificar também se esta movimentação já foi paga para os funcionários e se não foram recolhidos tributos.
* Algumas empresas apuram o ponto no período de 21/09/2009 a 20/10/2009, e para fazermos uma rescisão no sistema RM Labore no dia 30/10/2009 temos que apurar o ponto do funcionário até o dia 30/10/2009. Para fazer a apuração do ponto deste funcionário teremos que fechar o ponto do funcionário no período 21/09/2009 a 20/10/2009, liberar o mês para o próximo período (21/10/2009 a 20/11/2009), fechar o ponto do funcionário até a data de demissão, fazer o lançamento da movimentação do funcionário para o RM Labore e voltar a competência e o mês para apurar o ponto dos demais funcionários no período 21/09/2009 a 20/10/2009.  
  **Transfere registros dos períodos oficiais, menor que x mes(es), para o arquivo morto:** Neste parâmetro será considerado a quantidade de meses parametrizado no campo 'Quantidade de meses que não serão migrados para o arquivo morto', disponível no Paramatrizador Inicial.   
  Marcando este parâmetro, ao realizar a Liberação de Período será mantido na Tabela de Produção os dados dos meses parametrizados, os demais meses serão transferidos automaticamente para o Arquivo Morto. Caso a Liberação de Período seja feita sem marcar este parâmetro o sistema não irá alterar as informações da Tabela de Produção nem do Arquivo Morto.

  |  |  |
  | --- | --- |
  |  | Informações Complementares |

  ---

  Definir período futuro Definir período ativo Liberar período Transferir dados para tabelas de produção   
  [Transferência de Período com mais de 6 meses](http://tdn.totvs.com/pages/viewpage.action?pageId=372548518)

  |  |  |
  | --- | --- |
  |  | Como Fazer |

  ---

  [Como Fazer - Transferir dados para tabela de produção](http://tdn.totvs.com/pages/viewpage.action?pageId=185731949)  
     
  HelpWiki - RH - Automação de Ponto
