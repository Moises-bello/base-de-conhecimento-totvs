---
content_hash: f19c52ec2d70282282dd9387647ef2eb199e9030887860b172093bec7a916f97
fetched_at: '2026-06-29T00:11:16.940214+00:00'
page_id: '674548749'
product: rm
source: tdn-rm
title: Integração TOTVS x SAP
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=674548749
version: 3
---

Módulo do sistema TOTVS Folha de Pagamento, por meio da qual será possível realizar a integração com o SAP, sendo controlada a integração contábil da folha de pagamento e possíveis estornos de documentos já integrados.  
   
O processo de contabilização da folha de pagamento e os dados para envio na integração contábil serão gerados por meio de uma consulta executada no banco de dados. Este envio será através de uma aplicação WebService que permitirá enviar dados em formato XML.   
   
Desta forma, a integração atenderá os seguintes objetivos:

* Integração contábil da folha de pagamento: a contabilização é gerada no TOTVS Folha de Pagamento e enviada para o sistema SAP.
* Estorno da integração contábil da folha de pagamento: após integração contábil, existe a necessidade de reprocessar a contabilidade e enviar novamente para o SAP.

Através deste módulo será possível visualizar os lotes a serem integrados, realizar a integração destes lotes, estornar integrações realizadas e ainda, consultar status e logs de integração.  
   
No parametrizador do TOTVS Folha de Pagamento deverá ser marcado o parâmetro "Utiliza integração TOTVS x SAP da Contabilização da Folha de Pagamento" dentro de Folha de Pagamento | Folha Normal | Contabilização.  
   
Com este parâmetro marcado deixa de existir a integração com o TOTVS Gestão Contábil e passa a ser considerada a integração com o SAP.  
Para os lançamentos contábeis da folha de pagamento, serão identificados os tipos de Integração (Evento, Provisão e Encargo) da folha de pagamento através do campo "código do lote" (CODLOTE).   
   
Será verificado se o código do lote digitado no módulo de Geração de Lançamentos da Contabilização contém a máscara abaixo:  
1º Caractere: valores iguais a "1", "2" ou "3", que corresponderá ao tipo de integração.

* Código do lote iniciado com "1", será do tipo 'ENC - Encargo'.
* Código do lote iniciado com "2", será do tipo 'EVE - Evento'.
* Código do lote iniciado com "3", será do tipo 'PRO - Provisão'.

Do 2º ao 5º caractere: valores no formato ano "aaaa", que será o "ano" da competência da contabilização. (Data da Contabilização)  
Do 6º ao 7º caractere: valores no formato mês "mm", que será o "mês" da competência da contabilização. (Data da Contabilização)  
   
Na geração dos dados para integração, serão controlados o limite de 999 linhas através do campo "LOTE", que a cada 998 linhas será auto-incrementado.  
   
**ATENÇÃO OBRIGATÓRIO:** O Código de externo do cadastro de coligadas deve conter apenas 4 caracteres para o layout do documento que será enviado ao WebService.  
   
Nesta integração, haverá um filtro, por onde serão selecionados os dados de contabilização da folha de pagamento através da base de dados por exercício, período da empresa corrente e Tipo de Integração.

* Por default, o **exercício e o período** serão sempre preenchidos com a competência selecionada no TOTVS Folha de Pagamento, podendo ser alterado manualmente pelo usuário. Lembrando que a relação referente ao filtro selecionará de acordo com o mês e ano da data da contabilização e que somente o default será a competência do TOTVS Folha de Pagamento.
* **Tipo de Integração:** Como "default" será apresentado o filtro "Todos", porém, poderá ser alterado para: "ENC – Encargo", "EVE – Evento" ou "PRO- Provisão" e conforme a seleção serão filtrados os registros que possuem o tipo de integração pertencente à empresa, exercício e período selecionados. Na integração estará disponível apenas realizar consultas, não sendo permitida nenhuma manutenção (inserir/alterar/excluir) nos mesmos.

Abaixo segue descritivo de cada campo apresentado na tela:

* + **Campo de "referência":** O número de referência de cada lançamento contábil (registro) é composto por meio das seguintes informações: EMPRESA + EXERCICIO + PERIODO + TIPOINTEGRACAO + LOTE.
  + **Campo de "status":** Conforme processo de integração e estorno da integração, para cada "referência" apresentada na tela, será exibido um "status", sendo definido das seguintes formas:

    |  |  |
    | --- | --- |
    | **Status** | **Motivo** |
    | **A integrar** | Foi realizada a contabilização, os dados estão disponíveis na consulta, porém, não foi feita a integração com o SAP. |
    | **Integrando** | Foi solicitada a integração, porém, ainda não foi recebida a resposta (retorno) do SAP. |
    | **Integrado** | Contabilização integrada no SAP, retornado número contábil gerado no SAP para cada referência. |
    | **Estornando** | Foi solicitado o estorno de uma contabilização (referência) realizada no SAP, porém, ainda não foi recebida resposta (retorno) do SAP. |
    | **Estornado** | Estorno realizado no SAP. |
    | **Erro integração** | Foi solicitada a integração, porém, retornaram sem número de documento e com mensagens de erro, essas informações serão armazenadas em tabela customizada de log. |
    | **Erro estorno** | Foi solicitado o estorno, porém, o SAP retornou sem número de documento de estorno e com mensagens de erro, essas informações serão armazenadas em tabela customizada de log. |
  + **Campo de Documento SAP:** O número do documento do SAP será preenchido para cada "referência" da tela de integração, assim que o sistema SAP retornar que a integração foi realizada com sucesso ("status" igual a "integrado").

Para a seleção dos registros, haverá a opção de marcar todos os registros exibidos na tela, ou selecionar de forma individual cada registro.  
**Atenção:**  
Serão apresentados todos os itens listados na Partida do lote contábil e selecionando um item será selecionado todos os itens de mesma referência.  
Então no processo de integração além do envio da referência marcada, serão enviados os demais lotes que possua a mesma base de referência selecionada.  
   
**Exemplo:**  
EMPRESA (1100) + EXERCICIO (2011) + PERIODO (11) + TIPOINTEGRACAO (ENC).  
Dessa forma, seguindo a mesma base de referência, teremos: "1100201111ENC", portanto, será enviado mais um arquivo XML com os dados da referência:   
"1100201111ENC001", "1100201111ENC002", "1100201111ENC003", etc...  
   
Os processos disponíveis serão:  
Integrar – para status: "A integrar", "Erro integração", "Integrando" e "Estornado";  
Estornar – para status: "Integrado", "Estornando" e "Erro estorno";  
LOG - As informações serão geradas após o retorno do SAP referente ao processo de Integração e Estorno contábil.
