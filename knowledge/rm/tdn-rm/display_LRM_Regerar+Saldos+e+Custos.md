---
content_hash: 9e49beb426926d0c3a33117d8a980d1fac4efbc54891c6caec2aebbb156d02f0
fetched_at: '2026-06-29T00:09:29.250582+00:00'
page_id: '423938852'
product: rm
source: tdn-rm
title: Regerar Saldos e Custos
type: documentation
url: https://tdn.totvs.com/display/LRM/Regerar+Saldos+e+Custos
version: 17
---

O processo de Regerar Saldos e Custos, tem por finalidade regravar todas movimentações inclusas em tipos de movimentos parametrizados para afetar saldo em estoque e que tenham data de movimentação "superior" a data de fechamento de estoque.   
A data de fechamento de estoque é definida pelo usuário, onde pode ser informada uma data que será comum a todos os 10 saldos da base, ou colocar uma data pertinente a cada um.

Este processo é executado quando há necessidade de recompor os saldos e custos dos produtos inclusos em data retroativa à atual ou quando existe alguma alteração na parametrização do tipo de movimento que deve afetar os saldos e custos na base.   
Ao executar esta rotina, será considerada parametrização atual da base de dados fazendo com que a informação de saldo físico e financeiro sejam refeitos.

Além de acerto dos saldos, o processo também monta os dados da ficha física financeira do produto, que só é atualizada quando a rotina é executada. O processo depois de executado é irreversível, sendo sugerido que seja feito um backup de segurança.   
Outra verificação a ser feita é em relação ao volume de produtos e movimentações na base, visto que, a execução da rotina para todos os itens pode levar até horas.

A regeração é feita sequencialmente, um produto de cada vez. Porém é possível realizá-la de forma paralela, quando selecionada a opção **Execução paralela** nos parâmetros gerais do processo. Assim será feita a regeração de N produtos de uma só vez, conforme a capacidade do servidor de aplicação.   
O tempo de cálculo é diretamente relacionado ao poder de processamento do ambiente onde está sendo executado.   
Quanto mais processadores e memória o servidor de aplicação tiver, mais produtos serão calculados simultaneamente e menos tempo levará o processo, entretanto isso vai exigir mais do servidor de banco de dados, já que cada cálculo abre uma conexão.   
Com isso ganha-se em performance ao realizar o processo.  
Ao habilitar o parâmetro de execução paralela é apresentado o campo "**Número máximo processos paralelos**", através dessa opção é possível limitar a quantidade de processos que serão executados em paralelo, podem ser definidos valores de 0 a 100.  
Em casos de erros de time out e/ou alocação de recursos recomenda-se diminuir esse valor gradativamente, para que o mesmo fique dentro da capacidade do servidor.

Ao habilitar o parâmetro **Usar Log Detalhado** o Log será gerado com informações adicionais, especificando as movimentações do produto e o tempo gasto durante a regereção de cada produto.  
***Observação***: com esta opção marcada a performance poderá diminuir.

Ao habilitar o parâmetro **Gravar Arquivo de Log**, para cada produto regerado o Log do processo será atualizado com as informações da regeração do produto informando se ocorreu algum erro ou sucesso. Ao término do processo o Log será gravado fisicamente no diretório definido pelo administrador do sistema.   
***Atenção!*** para utilizar este recurso é necessário definir a tag *FileServerPath*. Em ambiente  N Camadas, é recomendado que o antivírus não aplique restrições no diretório onde serão salvos os arquivos de log do processo.

É indispensavel a realização do processo **Regerar Saldos e Custos** no menu **Estoque | Processos**, antes de emitir a Ficha Fisica Financeira que alimenta a tabela TRELSLD.

Informações Adicionais

* [Processo de Regerar Saldos e Custos](http://tdn.totvs.com/pages/releaseview.action?pageId=237373704)
* [Configuracao das Tags FileServerPath e LogPath](http://tdn.totvs.com/display/LRM/Configuracao+das+Tags+FileServerPath+e+LogPath)
* [Melhoria de Performance - Paralelismo](https://tdn.totvs.com/display/public/LRM/TUDCK9+DT+Regerar+Saldos+e+Custos+-+Melhoria+de+Performance)
