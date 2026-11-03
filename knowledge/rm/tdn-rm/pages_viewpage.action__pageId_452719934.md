---
content_hash: 9f71fa55084dcf08f22950b221b01c08c872f6c5b4497864783ff264b944d2b9
fetched_at: '2026-06-29T00:10:11.083592+00:00'
page_id: '452719934'
product: rm
source: tdn-rm
title: Enviar e-mails para Funcionários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719934
version: 21
---

Essa rotina é utilizada para enviar e-mails aos funcionários de forma global. Pode-se enviar e-mails com relatórios e também enviar mensagens personalizadas (livres).  
Pode-se filtrar por chefes, supervisores, funcionários e ainda utilizar o filtro de seleção de funcionários.

DICA

Acesse o link [COMO FAZER - Configuração de envio de E-mail para Funcionário](https://tdn.totvs.com/pages/releaseview.action?pageId=162169916) para ver mais detalhes.

### Filtro de Destinatários

Nesta seleção, você deve escolher para quem você irá enviar o e-mail desejado.

Selecionando apenas a flag **Envia p/ Funcionário**, será enviado para os funcionários da base, de acordo com o filtro de seleção de funcionários, passando como parâmetro para geração do relatório apenas os dados do próprio funcionário (Selecionando esta opção não será enviado para chefes e supervisores da seção).

Selecionando apenas a flag **Envia p/ Chefes**, será enviado para apenas os funcionários que forem chefes das seções e que estiverem com a flag **Recebe e-mail de alerta** marcada, no cadastro de [chefes/supervisores](http://tdn.totvs.com.br/display/LRM/Chefes+e+Supervisores), e de acordo com o filtro de seleção de funcionários, passando como parâmetro para geração do relatório apenas os dados do próprio chefe.

Selecionando apenas  a flag **Envia p/ Supervisor**, será enviado para apenas os funcionários que forem supervisores das seções e que estiverem com a flag **Recebe e-mail de alerta** marcada, no cadastro de [chefes/supervisores](http://tdn.totvs.com.br/display/LRM/Chefes+e+Supervisores), e de acordo com o filtro de seleção de funcionários, passando como parâmetro para geração do relatório apenas os dados do próprio supervisor.

ATENÇÃO:

* Caso queira realizar o envio para todos da seção, é necessário que seja marcadas as três flags acima.
* Para enviar e-mails de subordinados para os seus respectivos chefes ou supervisores, deverá ser feito a implementação no próprio relatório:

### Relatório .NET

Ao marcar esta opção, serão exibidos os relatórios disponíveis no **RMReports**.  
Ao habilitá-la, o parâmetro **“Relatório do SmartView”** será automaticamente desabilitado, conforme demonstrado abaixo.

**1 – Como elaborar o contracheque de funcionário a ser enviado ao chefe**

Para o envio de contracheques de funcionários, é necessário criar um relatório específico para essa finalidade.  
Abaixo, apresentamos um exemplo de modelo de contracheque.

Inclua, no relatório, textos descritivos nas bandas, explicando a estrutura e a construção do layout, de forma a facilitar o entendimento e a manutenção do relatório.

Se quiser, posso detalhar **o que descrever em cada banda** (cabeçalho, detalhes, rodapé etc.) ou ajustar o texto para um **manual passo a passo**.

**2 – Como elaborar uma listagem de subordinados para envio aos chefes**

Para a geração da listagem de subordinados, o relatório deverá ser estruturado com **bandas pai e filha**:

* + **Banda pai:** deve conter a *chapa dos funcionários chefes*.
  + **Banda filha:** deve listar os funcionários subordinados ao respectivo chefe.

A banda filha deverá ser alimentada por uma *query* semelhante ao exemplo abaixo, na qual o usuário poderá definir as regras de filtro dos subordinados conforme a necessidade:

`SELECT CODSECAO,
CHAPA,
NOME
FROM PFUNC
WHERE CODCOLIGADA = :CODCOLIGADA
AND CODSECAO IN (SELECT CODSECAO
FROM PSUBSTCHEFE
WHERE CODCOLIGADA = :CODCOLIGADA
AND CHAPASUBST = :CHAPA)
AND CODSITUACAO <> 'D'`

Além disso, podem ser incluídas restrições adicionais conforme o tipo de relatório desejado.  
Como exemplo, para a geração de um relatório de **Programação de Férias**, pode-se aplicar o filtro por período de início das férias:

`AND INICIOFERIAS >= :DATA1
AND INICIOFERIAS <= :DATA2`

Esse modelo permite flexibilidade na criação de relatórios, possibilitando a adaptação das regras de negócio de acordo com o cenário apresentado.

### Relatório de SmartView

Ao habilitar o parâmetro **“Relatório do SmartView”**, o parâmetro **“Relatório .NET”** será automaticamente desabilitado, conforme demonstrado abaixo.

O relatório anexado deverá conter, obrigatoriamente, os filtros de **Coligada** e **Chapa**, os quais serão utilizados internamente pelo sistema. O filtro de **Coligada** será obtido por meio do **contexto**, enquanto o filtro de **Chapa** utilizará o **filtro de seleção**.

### Informações do e-mail

**Opção de Envio**

Nesta opção, deverá selecionar se o e-mail enviado é Mensagem livre ou Relatório do sistema.

* Mensagem livre, escrita no corpo do e-mail, com opção do envio de documentos como anexo. Caso marque a opção **Envia destinatários como Cópia Oculta,** os destinatários do e-mail se tornam ocultos, ou seja, os destinatários não conseguirão visualizar outras pessoas para qual o e-mail também foi enviado.
* Relatório do sistema, gerado com os dados do funcionário como parâmetro.

**Mensagem de alerta caso não tenha dados nos relatórios**

Nesse campo poderá escrever uma mensagem para enviar em caso de o relatório não retornar dados para seu respectivo destinatário.

Caso este campo não for utilizado e a consultar não retornar dados não será encaminhado o e-mail.

Exemplo:

**Escolha o tipo do relatório em anexo**

Caso selecione enviar relatório como anexo, será habilitada a opção de saída do relatório, nos formatos abaixo:

### DEMAIS INFORMAÇÕES

* [DT - Enviar e-mails para Funcionários - Smart View](https://tdn.totvs.com/pages/viewpage.action?pageId=906833930)
