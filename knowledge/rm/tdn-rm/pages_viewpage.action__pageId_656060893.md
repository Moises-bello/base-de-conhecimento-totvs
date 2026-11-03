---
content_hash: f21f0dd4507ac5734d71db67411160ecb06e34309aac2533eb53581c81244595
fetched_at: '2026-06-29T00:11:12.668333+00:00'
page_id: '656060893'
product: rm
source: tdn-rm
title: Parâmetros existentes no Portal‎ - Backend
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=656060893
version: 10
---

O portal já possui os principais parâmetros para seu funcionamento, definidos como default, mas alguns destes dependem do ambiente do cliente e necessitam ser cadastrados para permitir a operacionalização do Portal de Imóveis. Todos os parâmetros do Portal de Imóveis estão em  **parâmetros (Clique aqui)]]>** e todos são autoexplicativos e de fácil entendimento, portanto nesta seção trataremos somente dos mais importantes para o iniciarmos o Portal de Imóveis, seguem:

#FF9000Sistema

* **Nome da Empresa**: Descreva no nome que deseja que apareça na barra de títulos do Portal de Imóveis.
* **Servidor SMTP Host**:  Nome do servidor SMTP. Após todos os parâmetros SMTP estiverem cadastrados, clique no botão “Testar SMTP” para enviar um e-mail teste para o endereço desejado e validar se a configuração está correta. Para estes parâmetros é importante solicitar estes dados para seu provedor de e-mails.

Os demais parâmetros estão relacionados com o processo de envio de senha e serão preenchidos com as informações disponibilizadas pelo provedor de e-mail:

* Servidor SMTP usuário
* Servidor SMTP senha
* Servidor SMTP servidor requer autenticação
* Servidor SMTP criptografia
* Servidor STMP e-mail de resposta
* Servidor SMTP porta
#FF9000Proposta

* **Validar valor do VPL acumulado**: este parâmetro deve sempre ficar como SIM pois ele garantirá a análise financeira do Portal de Imóveis entre a proposta do cliente e as condições padrões de venda definidas no RM pela tabela de preço e modalidade da venda.  Este parâmetro fará a validação do VPL TOTAL da proposta versus o VPL TOTAL da tabela de vendas da unidade em negociação. Este parâmetro reprova a proposta se o VPL da proposta for menor que o VPL da tabela.
* **Validar valor do VPL até a entrega**: se definido como sim validará o VPL TOTAL da proposta somando as parcelas até a data de entrega do empreendimento, comparando com o VPL TOTAL da tabela também até a data de entrega do empreendimento. Portanto para empreendimentos que se deseja um percentual de receita até a data de entrega, basta construir a modalidade de vendas e ajustar parâmetros dos componentes de venda no Portal de Imóveis para que retratem uma tabela de preços de acordo com o desejado pela incorporadora. Este parâmetro reprova a proposta se  o VPL da proposta for menor que o VPL da tabela até a data de entrega do empreendimento.
* **Validar valor do VPL linear**: este parâmetro, quando sim, validará mensalmente o VPL ACUMULADO parcela a parcela da proposta versus o VPL ACUMUALDO mensal da tabela de vendas e se pelo menos um mês estiver com VPL menor que o esperado pela tabela, a proposta será reprovada.
#FF9000Pessoa

* **Código para o tipo de cliente**: caso no RM, no cadastro de clientes, exista obrigatoriedade para o campo TIPO DE CLIENTE / FORNECEDOR, neste campo deve ser cadastrado o código de tipo de cliente fornecedor que será utilizado quando o Portal de Imóveis cadastrar uma pessoa no RM.
* **Como deseja gravar os clientes**: defina como deseja que o Portal de Imóveis cadastre os clientes no RM, cliente, fornecedor ou cliente e fornecedor (ambos)
* **Permite proposta para prospects de outros corretores:**no Portal de Imóveis é possível limitar o acesso a pessoas que já estão em negociação com outro corretor, portanto este parâmetro tem 3 (três) possibilidades:
  + **Sim** para permitir que todos os corretores possam fazer propostas para qualquer pessoa mesmo aqueles que tiverem sido cadastrados por outros corretores.
  + **Não**para não permitir salvar uma proposta com prospect de outro corretor.
  + **"Sim, avisar e gravar mensagem na proposta"** para permitir salvar a proposta, porém informar ao corretor e gravar a mensagem: "Prospect X vinculado ao usuário Y."

* **Tipo de cliente Global ou Local:**O RM aceita clientes gravados como locais ou globais, este parâmetro define como o Portal de Imóveis cadastrará a pessoa no RM
#FF9000Empreendimentos

* **Tipo de cálculo VPL:**VPL BRUTO define que o cálculo do VPL leva em consideração o valor total da tabela de preços e negociação, este dever ser o parâmetro padrão. O VPL LÍQUIDO elimina do cálculo o valor da comissão do empreendimento, situação em desuso pelas incorporadoras.
#FF9000Integração

* **RD Station:** Possibilita inserir dados no sistema através do RD Station definidos pelo usuário.  
  + **Aplicativos:**
  + **Campos Personalizados:**
  + **Parâmetros:**

***Observação:* ***Para que este menu seja habilitado na visão, será necessário marcar as permissões no grupo associado a este usuário.*****

#FF9000Unidade

* **Adicionar reserva automaticamente para o corretor:**nas ações de reserva ou proposta o Portal de Imóveis irá reservar a unidade para o corretor, desejável que fique sempre SIM.
* **Alterar a unidade para seguinte situação quando reservada:**define qual a situação a unidade terá quando o corretor fizer uma reserva. Estas situações são do cadastro de situações de unidades do Portal de Imóveis
* **Alterar unidade para seguinte situação quando uma proposta for adicionada a ela:**define qual a situação a unidade terá quando o corretor fizer uma proposta. Estas situações são do cadastro de situações de unidades do Portal de Imóveis.
* **Período de retenção de propostas em horas:**quantas horas o Portal de Imóveis irá manter a unidade reservada quando esta for uma proposta. Este parâmetro também poderá ser definido por empreendimento no cadastro de empreendimentos (backend)
* **Período de retenção de reservas em horas:**quantas horas o Portal de Imóveis irá manter a unidade reservada após o corretor executar a ação de reservar unidade. Este parâmetro também poderá ser definido por empreendimento no cadastro de empreendimentos (backend)
* **Período para aumentar a reserva em horas:**quantidades de horas a serem somadas ao tempo da reserva em vigor quando houver a ação de aumentar prazo da reserva.
#FF9000Layout

* **Mostrar nome da empresa em texto ou logo:**se definido em texto, será apresentado na barra de títulos do Portal de Imóveis o nome da empresa que foi definido no parâmetro da aba “sistema”. Se definido como logo, devemos carregar na pasta C:\inetpub\wwwroot\PROTOS-Portal de Imóveis\assets um arquivo com nome “logo.png”.
#FF9000Impressão

* **Logo**: carregue o logo que será utilizado no cabeçalho dos relatórios desenvolvidos no Portal de Imóveis.

*OBS: em versões futuras ao definir LOGO será solicitado o upload do arquivo sem necessidade e acessar o servidor do Portal de Imóveis.*

#FF9000TOTVS

* **WebService TOTVS: URL** **-**coloque a URL fornecida pelo RM para acesso ao WebService do Host RM
* **WebService: Usuário** – cadastre o usuário RM com direitos totais nas funções do TIN, cadastro de clientes e gestão da comunicação com do cliente.
* **WebService: Senha** – cadastre a senha do usuário RM que será usado para o acesso aos WebSercices do Host RM.
* **Código de componentes de valor –**quais são os tipos de componentes de valor usados pelo Portal de Imóveis. Isto é importante pois o Portal de Imóveis demonstra somente os componentes de valor nas simulações de propostas.
* **Informar o número da venda no instante de envio da venda para backoffice -**por default o Portal de Imóveis cria o numero da venda no RM, para isto o parâmetro VENDA SEQUENCIAL, deve estar ligado no TOTVS Incorporação. Caso contrário é possível antes de enviar a venda, dizer ao Portal de Imóveis qual será o número da venda a ser criada no RM.  Para isto deixe este parâmetro como SIM.

* **Separar componente em grupos -**se SIM, ao enviar uma venda do Portal de Imóveis para o RM, o Portal de Imóveis irá separar cada componente em um grupo distinto, exemplo de proposta:

+ Sinal
+ Mensal
+ Semestral
+ Financiamento

 Ao enviar esta venda o Portal de Imóveis irá criar um grupo para cada componente ficando Grupo 1 – Sinal, Grupo 2 – Mensal, Grupo 3 – Semestral e Grupo 4 - Financiamento.

* **Versão do TOTVS RM:**deverá contar a versão do RM com o formato X.Y.Z exemplo: 12.1.21, não deve ser acrescentado no número do patch.
* **Versão do TOTVS RM:**Revitalizada: SIM para versão revitalizada do RM
* **WebService: Banco de Dados:**selecione qual o bando de dados usado pelo RM, Oracle ou SQL Server?

---

Mais Informações:

* [Portal de Imóveis - Backend - Parâmetros](https://tdn.totvs.com/pages/viewpage.action?pageId=563947940)
