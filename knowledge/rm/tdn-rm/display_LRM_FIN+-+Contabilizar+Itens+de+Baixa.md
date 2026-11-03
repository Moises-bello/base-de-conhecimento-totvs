---
content_hash: 48dd29989a51bf612093fbd902da5c248303d8965c203bfb6d12ecd5233f5d87
fetched_at: '2026-06-29T00:09:58.133197+00:00'
page_id: '451261743'
product: rm
source: tdn-rm
title: FIN - Contabilizar Itens de Baixa
type: documentation
url: https://tdn.totvs.com/display/LRM/FIN+-+Contabilizar+Itens+de+Baixa
version: 8
---

## Descrição

Este processo fará a contabilização dos lançamentos baixados (baixa total, baixa parcial e baixa por acordo) com a opção 'Contabilizar posteriormente' que ainda não foram contabilizadas (tipo contábil "Baixa a Contabilizar" e "Contábil com Baixa a Contabilizar"). É possível filtrar esses lançamentos, informar qual a data da contabilização, salvar o log de contabilização dos lançamentos, inserir endereço (s) de e-mail para que determinado usuário receba as informações sobre o que foi contabilizado na execução do processo.  
  
Procedimento para Utilização

CardstrueContabilizar Itens de Baixa

Acesse o menu Contas a Pagar / Receber | Operações Financeiras | **Contabilizar Itens de Baixa**

Deve ser informado os seguintes parâmetros:

* Filtro: Informe um filtro que será usado para selecionar os itens de baixas para contabilização
* Data de contabilização: Informe a opção mais adequada para o seu processo para definir a data da contabilização da baixa
* Pasta compartilhada para salvar o log do processo: Informe um diretório que será gravado o log do processo.
* Enviar e-mail para: Lista de e-mails, separados por ponto e virgula. Caso o sistema esteja parametrizado corretamente para [envio de e-mail](https://tdn.totvs.com/display/LRM/Envio+de+email+-+LINHA+RM) e seja informado endereço (s) válido (s), será enviado um e-mail com as informações do processo e o caminho onde foi gerado o log.

**Importante**: Esse processo pode ser agendado caso seja utilizado o [ambiente em N camadas](https://tdn.totvs.com/pages/viewpage.action?pageId=236432384#Configura%C3%A7%C3%A3oNCamadas-Instala%C3%A7%C3%A3oemNcamadas:). Neste caso, a pasta onde será gravado o log deverá ser uma pasta compartilhada e com permissão para o conta/usuário que esta executando o RM.Host.Service.exe ou RM.Host.exe.

Contabilizar Itens de Baixa (Processamento Distribuido)

É necessário acessar o menu Ambiente | Processos | **[Segurança de Jobs Fracionáveis](https://tdn.totvs.com/pages/viewpage.action?pageId=547231277)** e incluir a classe de job "***FinFiltroContabilizacaoItensBaixaFracionadoProcess***" para parametrizar o uso do processamento distribuído ao contabilizar os itens de baixa do (s) lançamento (s) financeiro (s). Exemplo:

Em seguida, para realizar o processo, acesse o menu Contas a Pagar / Receber | Operações Financeiras. Clique na seta para baixo que aparece ao lado direito da opção "Contabilizar Itens de Baixa" para expandir a funcionalidade. Selecione a opção **Processamento Distribuido**.

Deve ser informado os seguintes parâmetros:

* Filtro: Informe um filtro que será usado para selecionar os itens de baixas para contabilização
* Data de contabilização: Informe a opção mais adequada para o seu processo para definir a data da contabilização da baixa
* Enviar e-mail para: Lista de e-mails, separados por ponto e virgula. Caso o sistema esteja parametrizado corretamente para [envio de e-mail](https://tdn.totvs.com/display/LRM/Envio+de+email+-+LINHA+RM) e seja informado endereço (s) válido (s), será enviado um e-mail com as informações do processo. Vale ressaltar que neste processo não existe a possibilidade de definir um diretório para gravação do log. No e-mail que é enviado constará o Id do job deste processo, possibilitando uma consulta posterior para mais detalhes. No corpo do e-mail constará o id do job, status do processo, data/hora de início e fim da execução do processo e o tempo total de execução. Caso o processo tenha sido concluído com alguma falha, no e-mail será exibida uma lista das baixas que apresentou algum problema com o detalhamento do (s) motivo (s).

**Importante**: Obrigatoriamente o ambiente deve estar em [N camadas](https://tdn.totvs.com/pages/viewpage.action?pageId=236432384#Configura%C3%A7%C3%A3oNCamadas-Instala%C3%A7%C3%A3oemNcamadas:) para que seja possível utilizar o processamento distribuído e o agendamento da execução automática deste processo.
