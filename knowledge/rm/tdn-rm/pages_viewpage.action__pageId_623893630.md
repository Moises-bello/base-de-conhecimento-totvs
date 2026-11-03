---
content_hash: 3bb593d78b7fc72729432b01b6afbcf45bf6b46595d7b29ab5dc3bb6a461ec2a
fetched_at: '2026-06-29T00:11:03.502600+00:00'
page_id: '623893630'
product: rm
source: tdn-rm
title: Parâmetros - TOTVS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=623893630
version: 8
---

| Parâmetro |
| --- |
| **WebService TOTVS: URL** Informe a URL do WebService do TOTVS.  **Disponível apenas para clientes sem base unificada. Para alterar este parâmetro com sua base unificada, [veja a documentação aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=801997247)** |
| **WebService: Usuário** Digite aqui o usuário do TOTVS a ser usado para acesso aos webservices do TOTVS. Este usuário será usado apenas para leitura.  **Disponível apenas para clientes sem base unificada. Para alterar este parâmetro com sua base unificada, [veja a documentação aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=801997247)** |
| **WebService: Senha** Digite aqui a senha do usuário do WS do TOTVS. **Nota:** Após salvar a senha, a mesma será criptografada e o parâmetro ficará em branco, ou seja, é normal que o campo esteja em branco.  **Disponível apenas para clientes sem base unificada. Para alterar este parâmetro com sua base unificada, [veja a documentação aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=801997247)** |
| **API REST TOTVS: URL** URL base para acessar as APIS da TOTVS **Nota:** A porta será informada na TAG: ApiPort do arquivo de configuração do Host:  *Exemplo: <add key="ApiPort" value="8052" />*  **Disponível apenas para clientes sem base unificada. Para alterar este parâmetro com sua base unificada, [veja a documentação aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=801997247)** |
| **Código do tipo dos componentes de valor** Informe os códigos dos tipos de componentes classificados como componentes de valor.  Para o Portal de Imóveis só importa apresentar na tela de simulação de vendas os componentes de valor, ou seja, o corretor não necessita ver os componentes de correção, portanto neste parâmetro devemos informar os números dos tipos de componentes de valor do RM, exemplo: 1 = Entrada, 2 = Principal, etc.  OBS: para MCMV os componentes de subsídio, FGTS, financiamento CEF possuem tipos a partir de 50. Portanto para que estes componentes apareçam em uma proposta é importante seus tipos estarem associados neste parâmetro do Portal de Imóveis. |
| **Grupo de produtos para brindes** Informe o código do grupo de produtos para serem utilizados como brindes. Por exemplo: Grupo definido como 02. Os produtos para brindes serão 02.001, 02.002, 02.001.01, etc. |
| **Informar o número da venda no instante de envio da venda para backoffice** Sim: Esta opção forçará o usuário informar o número da venda que será gerado no backoffice Não: O envio da venda será sequencial, ou seja, o backoffice que se encarrega de salvar a venda e atribuir o número da venda automaticamente |
| **Separar componente em grupos** **Sim:** Irá separar 1 componente por grupo. **Não:**Irá agrupar os componentes no mínimo de grupos possíveis sem repetir os componentes. |
| **URL Servidor TOTVS de atualização** Informe a URL do Servidor TOTVS para downloads de atualizações. |
| **Venda: Efetivar venda automaticamente?** Se definido como SIM após o envio da venda, se não ocorrerem erros, a venda será automaticamente efetivada. Para seu funcionamento o parâmetro Criar plano de financiamento no backoffice tem que estar definido como SIM |
| **Versão do TOTVS RM** **Usar o seguinte formato:** x.x.x. ex. 12.1.13 |
| **Versão do TOTVS RM - Revitalizada** |
| **WebService: Banco de Dados** Banco de dados do RM. |
| **Gravar arquivos de Request e Response do RM** Gravar na pasta tmp os arquivos referentes à troca de mensagens entre o RM. |
