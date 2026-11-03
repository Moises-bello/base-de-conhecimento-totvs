---
article_id: 360007482371
category: SIGAEST - CUSTOS
content_hash: 0e495e88b26c1eaac8ec751dcafd9f9f47af58be9df215854c4bd299a27ca86a
fetched_at: '2026-06-28T22:39:00.434189+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Qual é o conceito
  de contabilização ONLINE e OFFLINE através do parametro MV_CUSMED
type: support-article
updated_at: '2026-03-31T18:55:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007482371-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Qual-%C3%A9-o-conceito-de-contabiliza%C3%A7%C3%A3o-ONLINE-e-OFFLINE-atrav%C3%A9s-do-parametro-MV-CUSMED
---

O parâmetro MV\_CUSMED define o modo de contabilização do custo médio no TOTVS Protheus: "M" para offline, que requer recálculos manuais e fechamento de saldos, e "O" para online, onde o custo é atualizado a cada movimentação. Não é recomendado usar ambos simultaneamente nem alterar o parâmetro com estoques em aberto, pois pode causar inconsistências. O custo online exige que as movimentações sigam rigorosamente a ordem entrada/saída, e o recálculo do custo médio só é necessário se houver rateio de MOD ou GGF.

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25679369712919)** Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**  
Qual é o conceito de contabilização ONLINE e OFFLINE através do parametro MV\_CUSMED? Eu posso usar os dois simultaneamente?

**Ambiente**

Cross Segmento - TOTVS BackOffice (Linha Protheus) - Estoque/Custos - A partir da versão 12.1.17.

**Solução:**

**MV\_CUSMED = M (Offline)**

Com o fluxo de fechamento de custos **OFF-LINE** deve ser feito da seguinte forma:

* A) Recalculo dos Custos de Entrada MATA190 (no caso de mudanças de TES ou taxa de moedas).
* B) Recalculo do Custo Médio MATA330 (além de atualizar o valor dos movimentos serve para atualizar os campos de valor e quantidade final).
* C) Virada dos Saldos (para criação dos saldos iniciais do período seguinte).

**MV\_CUSMED = O (Online)**

O fluxo de fechamento de custos **ON-LINE** deve ser feito da seguinte forma:

* A) Movimentação do Mês (Notas de Entrada e Saídas e Movimentos Internos)
* B) Saldo Atual para Final MATA350 (para atualizar os campos de valor e qtd final)
* C) Virada dos Saldos (para criação dos saldos iniciais do período seguinte)
* D) Caso o usuário utilize o rateio de MOD (Mão de Obra) pela contabilidade deve executar o Recálculo do Custo Médio (MATA330) também quando utiliza custo On-Line, para obter o valor da MOD. Neste caso pode utilizar o método de Apropriação Sequencial e não é necessário gerar os lançamentos contábeis.

**Ou seja, conceitos diferentes.**

Abaixo segue a imagem da rotina "**Saldo Atual para Final (MATA350)**", responsável por preparar o saldo de fechamento para os campos B2\_QFIM, B2\_VFIM1 e etc.

**Importante**: Esta rotina somente prepara o saldo para virada do mês, para efetivar a virada deve-se executar a rotina de Fechamento Virada de Saldos ou Acompanha Custos.

**Modulo 4 > Miscelanea > Fechar Periodos > Saldo Atual Para Final(MATA350)**

#### **O objetivo deste programa é de transferir os saldos atuais em estoque para saldos finais do período.** **Ela deve ser executada após todas as movimentações do mês estarem digitadas e conferidas, antes que as movimentações do mês seguinte começem a ser digitadas****. Esta rotina deverá ser utilizada apenas por usuários que trabalhem com o custo médio ON-LINE ,caso contrário você deverá rodar o Recálculo do Custo Médio.**

#### **Antes de continuar certifique-se de que näo há nenhum outro usuário atualizando os arquivos de movimentaçäo de estoque.**

**Dúvidas e impactos na utilização da contabilização ONLINE:**

**1 - Podemos alterar o parâmetro MV\_CUSMED com os estoques ainda em aberto?**

**Não.** Todo processo alterado em meio de período, deve ser reavaliado, pois poderão ocorrer de movimentos não serem contabilizados conforme data, lançamentos padronizados (CT5) que atendem somente à contabilização Off-line, devendo ser revisados tais cadastros, conciliação contábil dos itens já registrados na CT2 e falha nos flag's ?\_DTLANC.

**2. Se não podemos, a alteração do parâmetro MV\_CUSMED pode ser feita em que momento?**

**Sugestão:** Realize o fechamento contábil em conjunto ao fechamento de estoque para gerar os registros em equidade no estoque e contábil, à partir de então utilize o cronograma e conforme usual do cliente. Verifique o fluxo operacional do cliente e a possibilidade de execução deste modo e então, após o fechamento sem que haja movimentos executados, altere o parâmetro.

**3 -  Pelo TDN, passando o parâmetro para On-Line significa que a contabilização também será no momento de cada movimentação, correto?**

O parâmetro referência exclusivamente ao modo de Contabilização, quanto ao Custo Médio deve ser atualizado On-Line, conforme o conceito de custo, onde qualquer sacrifício que represente a alteração do estoque deve ser afetado nos resultados.

**4 - E se ocorrer movimentações com data retroativa, o sistema não fará o recálculo? Ou se executarmos a rotina de Custo Médio isso será acertado?**

O conceito de Contabilização On-line é prática de empresas onde não há movimentações retroativas ou Postergadas, obedecendo sempre o ordenamento dos movimentos conforme input do mesmo, não deve ser aplicado em empresas onde a inclusão de notas seja entrada ou saída ou movimentos internos não respeitem a ordem **entrada** **e saída**.

**5  - A rotina de Custo Médio ainda deverá ser executada? Mesmo sem termos produção?**

A rotina MATA330 deve ser executada em processo onde a ordenação não siga o critério entrada e saída (deve ser Apropriação Sequencial), podendo o item ser requisitado então da compra ou empenhado/reservado para processo de modo que o consumo seja visível antes da reposição do item. Por estas circunstâncias a rotina é utilizada para tal ordenação.

**6  - Posso voltar a database com custo online para realizar fechamento?**

Não, acarretara em inconsistencia nos seus saldos. Exemplo:

No custo online (MV\_CUSMED = 'O')  a nota de entrada em 05/03/2026 vai atualizar a qtde atual na SB2 (Qtde 14), Esta nota poderia ser ate com data 31/12/2050 e mesmo assim seria atualizado a qtde atual na SB2.

Ao usar o custo online, o fechamento vai executar a rotina mata350 - Saldo Atual para final e o valor da qtde atual da SB2 (qtde 14) será transferido para a qtde final da SB2, e será o saldo inicial na SB9 (QTDE 14), e ao executar a rotina refaz saldo vai ser usado a qtde inicial da SB9 e adicionado a qtde da nota de entrada novamente (14 + 1) = 15, dando a impressão que o refaz saldos atualizou indevidamente. Por outro lado a nota de 05/03/2026 foi contabilizada e entrou no fechamento de 31/01/2026, sendo que no dia 31/01/2026 não existia o saldo de 14 no estoque, não sendo um erro sistemico, mas sim um erro processual, então não se deve alterar a database vigente, para realizar movimentações ou fechamentos,

**IMPORTANTE****:** Em instituições onde a contabilização é ONLINE e os movimentos do estoque sigam criteriosamente as saídas após as entradas, não deve-se utilizar a rotina MATA330 mas sim o programa MATA350-Saldo Atual para final.

### **INFORMAÇÕES IMPORTANTES:**

**Quando executar o Recálculo do Custo Médio quando o Custo for On-Line:**

Em instituições onde a contabilização é On-Line e os movimentos do estoque sigam criteriosamente as saídas após as entradas, não deve-se utilizar a rotina MATA330 mas sim o programa MATA350 - Saldo Atual para Final.

Somente será necessária a execução da rotina de Custo Médio (MATA330) se utilizar produto MOD ou GGF.

**Sobre Apropriação de Custo (MATA330):**

O sistema permite que o Custo Médio seja recalculado conforme as formas de apropriação descritas abaixo:

**Sequencial -** Todas as movimentações dos estoques são valorizadas exatamente na ordem em que foram digitadas, para tanto, os arquivos SD1, SD2 e SD3 contém o campo D?\_NUMSEQ, que guarda o número sequencial de sua gravação.

**Diária -** Todas as entradas de notas fiscais e devoluções ao estoque do DIA são consideradas para obtenção do custo médio que fará a valorização das requisições e notas fiscais de saídas do mesmo DIA, portanto, a cada dia posso ter uma valorização diferenciada dos meus estoques, dependendo das entradas efetuadas.

**Mensal -** A partir do saldo inicial, notas fiscais de entrada e devoluções ao estoque, do período informado, o sistema calculará o novo custo médio que valorizará as movimentações internas e notas fiscais de saídas do mesmo período informado para o recálculo.

**Observações:**

Toda e qualquer alteração nos conceitos e configurações de Custo deve ser avaliado minuciosamente pela empresa e entendido antes de tal mudança. Pois poderá acarretar danos em seu controle de estoque e custos, por este motivo sugerimos que se há a intenção de mudança que seja solicitado auxilio de consultor TOTVS ou Terceiro, para avaliação e implementação da alteração sistêmica.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)
