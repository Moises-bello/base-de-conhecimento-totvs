---
content_hash: 155f0648630b92a02e252543dfa668f90f8d2ccfad21120f137d69a915daa7c1
fetched_at: '2026-06-29T00:10:07.242005+00:00'
page_id: '452719381'
product: rm
source: tdn-rm
title: Controle de Faltas
type: documentation
url: https://tdn.totvs.com/display/LRM/Controle+de+Faltas
version: 7
---

O Controle de Faltas tem o objetivo de considerar o dia efetivo da falta no cálculo dos avos de férias e 13º salário para os clientes que utilizam máquina de cálculo. Tendo como beneficio:

* Calcular os avos de férias verificando as faltas do primeiro ao último dia do período aquisitivo;
* Considerar corretamente a quantidade de dias de faltas para o funcionário que tem jornada diária diferenciada, e o cliente utiliza o evento do tipo hora no desconto da falta no envelope de pagamento;
* Visualizar detalhadamente os dias das faltas de cada funcionário.
* Estornar o dia real da falta indevida.

Para a utilização do Controle de Faltas, é necessário parametrizar o sistema, podendo o usuário definir se será utilizado o Controle através da Automação de Ponto ou não.   
   
Quando o sistema estiver parametrizado para utilizar o controle de faltas através da Automação de Ponto, será disponibilizado na rotina de Lançamento de Eventos da Automação de Ponto para a Folha de Pagamento um parâmetro onde o usuário poderá definir se grava o Controle de Faltas no momento do lançamento do evento de desconto de faltas.   
   
O evento de desconto de faltas será lançado para a Movimentação Temporária (tabela PFMOVTEMP)  e os dias de faltas serão lançados no Controle de Faltas (tabela PFHSTFALTA).  
   
Sempre for processado o Lançamento de Eventos para a Folha de Pagamento com o parâmetro marcado, a Automação de Ponto irá deletar todas as faltas do período de apuração que não estão bloqueadas e inserir novamente, garantindo desta forma a segurança de não gerar nenhum registro indevido.

**Atenção**  
Caso o usuário faça algum ajuste manual no controle de faltas e este período não esteja bloqueado, este ajuste será perdido quando o processo de lançamento for executado novamente.  
   
**Exemplo**   
O lançamento da Automação de Ponto gravou faltas nos dias 05 e 18 do mês, porém o ponto do funcionário estava errado, o funcionário tem falta apenas no dia 18.  
Se excluirmos a falta do dia 05 no TOTVS Automação de Ponto e processarmos o lançamento novamente e se o sistema não deletar todas as faltas, o dia 05 permaneceria como falta.

Utiliza controle de faltas para cálculo de avos  
O parâmetro Utiliza controle de faltas para avos será utilizado para o Controle de Faltas no cálculo de avos de Férias e 13º Salário.  
   
Com esta opção marcada, o sistema passará a ignorar os códigos de cálculos 8 e 128 a partir da competência informada, e os meses anteriores o sistema continuará fazendo o tratamento verificando os códigos de cálculos 8 e 128.  
   
Ao marcar este parâmetro serão habilitados os campos "Mês" e "Ano" já com o Mês/Ano corrente informado, podendo o usuário alterar se necessário.

Obs: Este parâmetro é encontrado em 'Folha de Pagamento| Configurações| Parametrizador| Folha Mensal| Controle de Faltas'.  
   
Controle de faltas através Automação de Ponto  
Ao marcar este parâmetro será habilitado no processo de Lançamento de Eventos para Folha de Pagamento, do Módulo Automação de Ponto o parâmetro 'Grava controle de faltas para cálculo de avos na folha' possibilitando a geração do controle de faltas no lançamento do evento de desconto de faltas.  
   
Com o parâmetro desmarcado o usuário deverá alimentar o controle de faltas através de importação, quando utilizar outro sistema de ponto, ou através de inclusão manual.

Utiliza fração dia e falta

Este parâmetro só será habilitado caso esteja marcado o "Utiliza controle de faltas para cálculo de avos". Mais informações:

[Parametrizador](http://tdn.totvs.com.br/display/LRM/Parametrizador)  
<<Voltar para tela anterior **Folha Normal**
