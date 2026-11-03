---
content_hash: a7b76c5552ad7c51df71ad08bc30c871f47255c7cfef781fc13ffe335d035be9
fetched_at: '2026-06-29T00:11:55.643560+00:00'
page_id: '862605886'
product: rm
source: tdn-rm
title: Integração Laboratorial DB Diagnóstico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=862605886
version: 22
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **DB DIAGNÓSTICOS**
3. **Tela DB DIAGNÓSTICOS**
4. **Exemplo de utilização**

## **01. VISÃO GERAL**

IntegraçãoVisão Geral

1. **Visão Geral**Integrar o RM saúde com o Laboratório de apoio DB Diagnóstico
Parâmetros 

Cadastro > Prestador> Novo

Cadastrar o Laboratório DB diagnóstico como um prestador do tipo Laboratório de Apoio

Cadastro > Prestador> Novo > Anexos> Endereço de envio de prestador

Ainda na tela de cadastro ir em Anexos > Endereço de envio do Prestador, a razão social já vem preenchida com o nome do prestador, o cliente deverá preencher:

* Layout (DB Diagnósticos), Usuário (fornecido pela DB Diagnóstico), Senha (fornecido pela DB Diagnóstico), Tipo (Login), Ação (Autenticação) e Url (fornecido pela DB Diagnóstico, quando testado foi utilizado em homologação: <https://cirhomprd.diagnosticosdobrasil.com.br/dbsync/wsrvProtocoloDBSync.dbsync.svc> e para produção: <https://wsmb.diagnosticosdobrasil.com.br/dbsync/wsrvProtocoloDBSync.dbsync.svc>)
* **Observação: Só deve ser informado uma url na lista de ações, caso contrário irá gerar um erro ao tentar enviar;**

Cadastros> Unidade de Diagnóstico > Locais de execução externa

Cadastrar o Laboratório DB como um local de execução externa

Cadastro > Unidade de Diagnóstico > Exames e Serviços > Configurações do Exame

Configurar os exames laboratoriais que tem peso, altura e local do corpo de coleta do material biológico obrigatórios para o envio do pedido para a DB

Cadastro > Unidade de Diagnóstico > Cadastro de Exames para Integração laboratorial

Esse cadastro é necessário para realizar a integração , a DB diagnóstico tem uma tabela de exames própria. 

Dados da tela:

Local Padrão -  por default vem como Não, caso o usuário  deseje que o local de execução externa como DB Diagnóstico, no pedido de exames seja preenchido automaticamente, essa flag deve ser habilitada.  

Importação de resultados :  por default vem como Não, caso o retorno do exame seja em PDF, essa flag deve ser habilitada.

Mnemônico  Exame  (obrigatório): preencher mnemônico do exame conforme tabela da DB Diagnóstico

Mnemônico Material: para essa integração não é obrigatório

Material: para essa integração não é obrigatório

Exame (obrigatório): descrição do exame no RM saúde

Local (obrigatório) : Laboratório DB , conforme cadastro de prestadores 

Descrição de conservantes: descrição do conservante cadastrado no RM saúde

Nro Etiquetas Identifi. Material Externo: quantidade de etiquetas a ser impressa, no caso da DB, deixar como 1 pois a quantidade é administrada pela DB

Tempo Min Execução: tempo mínimo em horas, que o Laboratório DB precisa para  analisar o exame

Entrega (dias): tempo em dias para liberação do resultado  após a data da coleta

## **02. DB DIAGNÓSTICOS**

O módulo do DB Diagnósticos está localizado em Unidade Diagnósticos> Integrações Laboratoriais > Laboratórios de Apoio > DB Diagnósticos.

## **03. TELA DB DIAGNÓSTICOS**

Nessa tela são exibidos somente os exames que possuem o local de execução externo cadastrado como DB Diagnósticos

* Ao abrir a tela ão será exibido a opção de filtro, a terá sempre irá abrir com os exames da Db Diagnóstico. Mas o usuário poderá utilizar o filtro se desejar;

## **Exemplo de utilização**

As solicitações de exames pode ser realizadas através do Prontuário Eletrônico (PEP), menu de Pedidos de Exames no Registro de Atendimento ou no menu Pedidos de Exames da Unidade de Diagnóstico

  Na tela de solicitação de exames o local ser DB Diagnóstico

Se no cadastro do exame estiver configurado a obrigatoriedade de peso e altura será exibido uma mensagem impedindo o usuário de salvar o exame

Na aba "Informações do paciente", temos os campos "Peso", "Altura" e "Local do corpo de coleta de material biológico" eles devem ser preenchidos conforme configurado no cadastro de exame, tornando obrigatório ou não. Se o peso e/ou altura já tiverem sido informados em outro pedido de exames para o mesmo atendimento, esses dados serão preenchidos automaticamente.

Após clicar em Ok para confirmar o pedido de exames, esses itens serão visualizados em Unidade Diagnósticos> Integrações Laboratoriais > Laboratórios de Apoio > DB Diagnósticos

 os exames ficam com status T - Execução externa, ao ir executando as mudanças de status 

  Os exames com  status AR podem ser enviados para integração através do menu Integrações > Processo de Envio de Pedidos de Exames, os exames enviados com sucesso terão seu status alterado para EE, nesse status não é permitido alterar o pedido de exames e a tela de resultados fica bloqueada para digitação.

 Os exames que não foram integrados por algum motivo no final do processo é informado o que precisa ser ajustado para enviar novamente

O processo de resultado de exames é somente para exames com status EE, os exames que ja possuírem resultado liberado, passam para o status L, ao finalizar o processo é exibida uma mensagem de sucesso ou falha na busca desses resultados

O retorno de resultados pode ser por PDF , onde será exibido um link dentro exame e ao clicar é direcionado para o PDF

Ou resultado estruturado  que é exibido na tela os valores de referencia e resultados importados da DB

Informações complementares:

* Após o envio é retornado a etiqueta da amostra, esta etiqueta é gravada na tabela e coluna SZLOGINTEGRACAOPACSLAB.ETIQUETA, abaixo mais informações sobre:
  + Ocorre que algumas amostrar é necessário apenas 1 amostra para realizar 2 ou mais exames, neste caso para cada exame é gravado a mesma etiqueta de amostra;
  + Se for necessário imprimir apenas uma etiqueta, será necessário ajustar a impressão para não primir etiquetas duplicadas, fazendo o tratamento do campo SZLOGINTEGRACAOPACSLAB.ETIQUETA para imprimir apenas etiquetas distintas.
