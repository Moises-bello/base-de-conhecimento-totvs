---
content_hash: ccd36bd24d551270dfc5db3044c57a5f6f8ff033097200c6538c1e30fa45e4c5
fetched_at: '2026-06-29T00:09:16.963236+00:00'
page_id: '421388542'
product: rm
source: tdn-rm
title: FIN - Agendamento de Remessa 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388542
version: 3
---

O Agendamento é utilizado para o processo de remessa, sendo exibido opções para informar data e horário em que a remessa será realizada.   
 Após o agendamento, o processo é iniciado automaticamente pelo sistema, que salva o arquivo no caminho especificado e com o nome indicado no processo.  

O LOG do processo de Agendamento de Remessa pode ser visualizado em Ambiente | Gerenciamento de Jobs.

Para que a opção de agendamento seja exibida pelo sistema, o parâmetro "Permite Agendamento das remessas bancárias" deve ser selecionado. Este se encontra em: Ambiente | Parâmetros |TOTVS Gestão Financeira | Contas a Pagar ou a Receber | Integração Bancaria | Etapa 2 - Integração Bancaria do Financeiro / Permite Agendamento das remessas bancárias.

A utilização dessa opção só está disponível para ambiente 3 camadas.

Deve se atentar a algumas regras para utilizar o agendamento:

* Quando o Parâmetro "Permite agendamento das remessas bancarias" estiver marcado, o sistema considera o caminho informado como o caminho do **Server**.
* Quando o Parâmetro "Permite agendamento das remessas bancarias" estiver desmarcado, o sistema considera o caminho informado como caminho do **Client**.
* Quando o Parâmetro "Permite agendamento das remessas bancarias" estiver marcado ou desmarcado informando caminho de rede, ex.:*\\Servidor\maquina\rede\pasta*, o sistema considera o caminho informado da rede para buscar o(s) arquivo(s).

**Observação**

Deve-se avaliar a hipótese da permissão de acesso para todos os usuários na pasta informada no caminho.

[**Permite agendamento da remessa bancaria na tela do processo de remessa**](http://tdn.totvs.com/pages/viewpage.action?pageId=358455115)

Na tela dos processos de remessas bancárias será apresentada a opção "Salvar arquivo de remessa gerado no servidor de aplicação". Por default o campo na tela do processo será carregado com o valor informado nos parâmetros do sistema, mas permite que o usuário altere. Caso opte por salvar o arquivo da remessa no destino server, será necessário informar um diretório compartilhado.

 Informações Complementares

* [Parametrização para utilização do processo de Agendamento de Remessa](http://tdn.totvs.com/pages/viewpage.action?pageId=269550188)
