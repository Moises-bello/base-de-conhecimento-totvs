---
content_hash: 61e09685f15671ad545306d8a9fea844673db428b689dc6ec7e361dbaca432a4
fetched_at: '2026-06-29T00:11:03.494630+00:00'
page_id: '623893586'
product: rm
source: tdn-rm
title: Parâmetros - Pessoas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=623893586
version: 11
---

| Parâmetro |
| --- |
| **Enviar e-mail para o corretor ao atribuir um corretor no cadastro da pessoa?** Informe **Sim** para que seja enviado um e-mail ao vincular um corretor no cadastro da pessoa ou informe informe não **Não** para que e-mail não seja enviado. |
| **Grava mensagem de acompanhamento ou anotação ao registrar interesse ou uma proposta?** Informe **Sim** para que seja registrado uma anotação ou uma mensagem de acompanhamento todas às vezes em que for registrado um interesse ou uma proposta para o cliente. Informe **Não** para que não seja registrado uma anotação ou uma mensagem de acompanhamento. |
| **API SERPRO - Ambiente (Tipo de Licença)** Ambiente de operação da API de Integração com SERPRO. **Importante** Para usar em modo de produção é necessário que seja contratado do SERPRO uma licença de uso do serviço. O custo de contratação de serviço do SERPRO **NÃO** é de responsabilidade da PROTOS Sistemas e Projetos. |
| **API SERPRO - Consumer Key** Chave do consumidor (Consumer Key) adquirida e configurada com SERPRO para validação de CPF via integração. Para maiores detalhes veja às orientações do [changelog](https://www.dropbox.com/s/57e4nen2i10gupg/changelog.pdf?dl=0) da versão **v2.12.391** |
| **API SERPRO - Secret Key** Chave Secreta (Secret Key) adquirida e configurada com o SERPRO para validação de CPF via integração. Para maiores detalhes veja às orientações do [changelog](https://www.dropbox.com/s/57e4nen2i10gupg/changelog.pdf?dl=0) da versão **v2.12.391** |
| **Cadastro de clientes global** Caso seja global, ao enviar a venda para o backoffice a coligada será 0. Se não for global a coligada do cliente será a coligada do empreendimento. |
| **Cadastro de fornecedores global** Caso seja global, ao enviar a venda para o backoffice a coligada será 0. Se não for global a coligada do fornecedor será a coligada do empreendimento. Em ambos os casos, o vendedor deverá existir no backoffice antes de enviar a venda caso um CNPJ/CPF esteja cadastrado no cadastro de usuário. |
| **Clientes com interesses perdidos ou ganhos vão para o banco de clientes?** Informe **Sim** para que o cliente seja enviado para o banco de cliente toda vez que um interesse for ganho ou perdido. Informe **Não** para que nenhuma ação de envio do cliente para o banco de clientes aconteça. **Importante** Se o cliente possuir pelo menos um interesse em aberto ele continuará como em atendimento. |
| **Código para o tipo de cliente** Se nas configurações do sistema o tipo de cliente/fornecedor for obrigatório, o código padrão para o tipo de cliente tem que ser informado aqui ou a importação da venda falhará. |
| **Como deseja gravar os clientes** Informe se deseja gravar os cliente como: CLIENTE, FORNECEDOR ou CLIENTE/FORNECEDOR OBS: Se selecionado a opção Fornecedor, quando uma proposta for integrada com o Backoffice, o registro da Pessoa será gravado como Fornecedor (Ambos) no cadastro de Cli\For do RM. |
| **CPF/CNPJ obrigatório no cadastro de pessoas?** |
| **Enviar SMS para alertar sobre um compromisso?** Enviará um SMS 30 minutos antes do compromisso vencer. |
| **Interesses: Obrigatório informar motivo do interesse quando a situação(do interesse) atribuída for "perdido"** Selecione uma opção para sistema fazer a validação quando necessário. |
| **Número máximo de prospects por usuário** Informe 0 ou nulo para sem limite. |
| **Obrigatório cadastro de cônjuge** Informe se o sistema deve obrigar o cadastro do cônjuge quando o prospect for casado. |
| **Período de vínculo de prospects (em dias)** Quanto tempo um prospect fica vinculado à um corretor antes que este volte para o banco de dados. Coloque 0 para desativar essa função. |
| **Permite proposta para prospects de outros corretores** Selecione ***Sim*** para permitir que todos os corretores possam fazer propostas para qualquer prospect mesmo aqueles que tiverem sido cadastrados por outros corretores. Selecione ***Não*** para não permitir salvar uma proposta com prospect de outro corretor. Selecione "Sim, avisar e gravar mensagem na proposta" para permitir salvar a proposta, porém informar ao corretor e gravar a mensagem: "Prospect X vinculado ao usuário Y.". |
| **Salvar Dados dos Prospects em Maiúsculo** Mudando este parâmetro para Sim, fará com que os dados dos prospects sempre sejam salvos em maiúsculo. **Nota:** Somente afetará novos prospects ou prospects editados. |
| **Tipo de cliente Global ou Local** Define se a coligada do campo/atributo **tipo de cliente/fornecedor** do TOTVS é local ou global (campo/atributo: FTCF.CODCOLIGADA) |
| **Usuário quem cadastra prospect deve ser associado automaticamente como corretor do prospect cadastrado** Sim: se não for atribuído o corretor no instante do cadastro, o usuário quem cadastra será o corretor responsável automaticamente Não: se não for atribuído o corretor no instante do cadastro, o sistema não irá atribuir o usuário quem cadastrou o prospect como o corretor responsável |
| **Vínculo de Prospect - Enviar um e-mail para o corretor antes que um prospect seja enviado para o banco de prospect** Configurando este parâmetro com 2 irá enviar um e-mail para o corretor e seu superior informando que que não foi feita atualização no cadastro do prospect nos últimos 2 dias. Digite 0 para desativar |
| **Utiliza a nova interface de prospect (A partir da versão 12.1.2302)**  Ao marcar este parâmetro como Sim, será habilitada [a nova tela de prospects,](https://tdn.totvs.com/pages/viewpage.action?pageId=701668855#M%C3%A3o-C_5) mais moderna e com interface mais fluída. Experimente! |

Considerações sobre o parâmetro **Como deseja gravar os clientes?**

Este parâmetro possui as seguintes opções que irão afetar o modo como a pessoa é salva no backoffice

**Caso seja global, ao enviar a venda para o backoffice a coligada será 0. Se não for global a coligada do cliente será a coligada do empreendimento.**

* **Caso seja definido para Cliente:** Ao enviar a venda ao backoffice o cliente fornecedor nascerá com o seu tipo definido como cliente.
* **Caso seja definido para Fornecedor:**Ao enviar a venda ao backoffice o cliente fornecedor nascerá com o seu tipo definido como ambos.
* **Caso seja definido para Ambos:** Ao enviar a venda ao backoffice o cliente fornecedor nascerá com o seu tipo definido como ambos.

É importante salientar que um cliente / fornecedor já cadastrado no RM não poderá ter seu tipo alterado para somente cliente quando já possuir lançamentos a pagar no backoffice.

Da mesma forma, não é possível alterar este cliente / fornecedor já cadastrado para somente fornecedor quando já possuir lançamentos a receber no backoffice.

O Portal de Imóveis irá emitir uma mensagem de alerta informando, ao enviar a venda que já existem lançamentos para o cli/for caso este cenário for verdadeiro.
