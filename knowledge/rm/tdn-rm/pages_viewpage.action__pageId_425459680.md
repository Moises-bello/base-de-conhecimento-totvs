---
content_hash: e5610c5a44bb6cabc910bb6b52c608bb02fec1fae4f1db0485f65c609a6afac5
fetched_at: '2026-06-29T00:09:38.024916+00:00'
page_id: '425459680'
product: rm
source: tdn-rm
title: Integração TOTVS Folha de Pagamento x BackOffice Logix
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459680
version: 21
---

**Totvs Folha de Pagamento x Logix (BackOffice)**

---

A integração entre Totvs Folha de pagamento e Logix (BackOffice) possibilitará a realização dos procedimentos relacionados à folha de pagamento compartilhando entidades do Logix e Totvs Folha de pagamento, reportando e processando cálculos e cadastros relacionados a rotina de folha de pagamento.

**Arquitetura da integração**

A arquitetura dessa integração é baseada em Mensagem única. Para utilização da integração será necessário utilizar o "TOTVS Business Connect. Execute o instalador "TOTVS Business Connect - \[versão\].msi" e patchs disponíveis, se houver. Este pacote cria uma aplicação no IIS e copia os arquivos necessários para a utilização dos Web Service.

**Configuração da integração 1020 - TOTVS Folha pagamento RM x Backoffice Logix:**

Para utilizar a integração Totvs Folha de Pagamento e Logix (1020) é necessário executar o assistente de integração em Integração | Ferramentas | Configurar. Executar a integração.   
Após executar o configurador, a integração será criada com o código 1020. Ao realizar a instalação, juntamente a ela será criado o mapeamento de entidades relacionadas a integração. Essas entidades serão os cadastros e informações utilizadas para troca de mensagens no processo de integração.   
Acesse Integração| Mensagem única | Integrações para verificar a instalação da integração realizada. Para avaliar as entidades criadas, acesse a integração com o código 1020 (TOTVS Folha pagto RM x BackOffice Logix), clique em Anexos| Mapeamento de entidades. Neste submenu são listadas todas as entidades que serão usadas para executar o processo da integração com suas respectivas versões. Abaixo maiores detalhes das entidades no tópico Itens Integrados.  
A integração também dispõe de alguns parâmetros opcionais relacionados as entidades. Esses parâmetros também serão instalados juntamente com a integração e por default, terão valor nulo ou false que podem ser modificados de acordo com a necessidade da integração. Os parâmetros de cada entidade serão detalhados no tópico Itens integrados.   
Após executar o procedimento de criação da integração, será necessário realizar as parametrizações para comunicação entre os sistemas.   
  
NOME INTEGRAÇÃO: Este é o nome completo da integração. Trata-se de um campo meramente informativo.  
NOME REDUZIDO: Este é o nome reduzido da integração. Trata-se de um campo apenas informativo.  
SISTEMA INTEGRADO: Este é um mnemônico que identifica a aplicação de origem e será enviado no atributo "name" da tag <Product> no XML trafegado. Ex: "Logix".  
SIGNIFICADO DE COLIGADA: Define qual o limite da identificação da coligada, se representa a companhia ou a unidade de negócio.  
URL WEB SERVICE: Informe o endereço do WebService Logix para envio de mensagens. Utilize o formato http://\[servidor\]:\[porta\]/EAIService.apw.  
USUÁRIO AUTENTICAÇÃO: Informe o nome do usuário para autenticação pelo WebService.  
SENHA AUTENTICAÇÃO: Informe a senha para autenticação pelo WebService.  
  
**Configuração Integração com Folha de Pagamento**

Após a etapa anterior, será necessário configurar o sistema TOTVS Folha de Pagamento para integrá-lo com o sistema Logix. Esse procedimento é executado da seguinte maneira: RH | Folha de Pagamento | Configurações | Parametrizador | Integrações > Outros BackOffice.

Na Etapa 1 - Outros BackOffice deverá marcar o parâmetro "Usa integração com outros backoffice". Habilitando este parâmetro será possível realizar integração com sistemas backoffice de terceiros. Será habilitado também um checkbox com parâmetro relacionado ao processo contábil.

**C****onsiderações relacionadas a parametrização de De-Para:**

O cadastro De-Para é criado durante o próprio processo de integração das entidades. No entanto, no início do processo de integração dois cadastros de De-Para devem ser feitos manualmente: GCOLIGADA E GFILIAL.  
  
Abaixo estão disponíveis informações das entidades integradas. Clique nos links abaixo para maiores detalhes:

**[Integração processos contábeis e financeiros](http://tdn.totvs.com.br/pages/viewpage.action?pageId=425459638)**  
**[I](http://wikihelp.totvs.com.br/WikiHelp/CON3/INT.FolhadepagamentoxLogixFuncoes.aspx)[ntegração cadastro de funções](http://tdn.totvs.com.br/pages/viewpage.action?pageId=425459596)**  
**[Integração cadastro de funcionários](http://tdn.totvs.com.br/pages/viewpage.action?pageId=425459665)**  
**[Integração cadastro de seções](http://tdn.totvs.com.br/pages/viewpage.action?pageId=425459600)**  
**[Integração processo de transferência de funcionários](http://tdn.totvs.com.br/pages/viewpage.action?pageId=425459630)**  
**[Integração processo de turno e escala de funcionários](http://tdn.totvs.com.br/pages/viewpage.action?pageId=425459168)**  
**[Integração pagamento de comissões](http://tdn.totvs.com.br/pages/viewpage.action?pageId=425459222)**  
**[Integração pagamento de autônomos externos](http://tdn.totvs.com.br/pages/viewpage.action?pageId=425459174)**

---

**Veja Também**

[Documento técnico Integração Totvs Folha de Pagamento x Logix](http://tdn.totvs.com/display/INT/TOTVS+Folha+de+Pagamento+RM+X+BackOffice+Logix)
