---
content_hash: ac3be26246b1485ac15b0f8b9413928fd29983da9ba0c81ab5d6278c45830efb
fetched_at: '2026-06-29T00:09:37.399701+00:00'
page_id: '425459604'
product: rm
source: tdn-rm
title: Backoffice RM x Protheus SigaMNT - Parâmetros Protheus SigaMNT
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459604
version: 6
---

**Backoffice RM x Protheus SigaMNT - Parâmetros Protheus SigaMNT**

---

**Configuração de Parâmetros EAI Protheus**

O envio e o comportamento das mensagens, geradas pelos processos do Protheus SigaMNT, obedecem as parametrizações feitas no módulo SigaCFG.

**Passos para a configuração dos Parâmetros.**

**Passo 1-** Acesse: Protheus SigaCFG/ Base de Dados/ Dicionario de Dados/ Base de Dados

**Passo 2-** Expandir a árvore do menu localizado ao lado esquerdo.

**Passo 3-** Acesse: Parâmetros

**Passo 4-** Clique sobre o Ícone "Pesquisar" representado por uma LUPA.

**Passo 5-** Informe o nome do Parâmetro que deseja configurar e clique no botão Pesquisar.

**Passo 6-** Selecione o Parâmetro e clique em Editar(Representado graficamente por um papel com um lapis).

**Passo 7-** Informe os valores  de acordo com o parâmetro e clique em confirmar para salvá-lo.

**Parâmetros:**

**1- MV\_NGCORPR**

Informa se o sistema pode gerar Solicitações de compra para Manutenções Corretivas.

**Valores:**

**S:** Gera Solicitações de compra para Manutenções Corretivas

**N:** Não gera Solicitações de compra para Manutenções Corretivas.

**2- MV\_NGGERSA**

Indica se o Protheus SigaMNT deve gerar Solicitação de Armazém ao invés de Solicitação de Compras.As solicitações de compra serão geradas somente se a quantidade de insumos previstos em uma Ordem de Serviço excederem a quantidade disponível em estoque.

**S:** Gera Solicitação de Armazém e não gera Solicitação de Compra.

**N:** Gera Solicitação de Compra  e não gera Solicitação de Armazém.

**3- MV\_NGINTER**

Parâmetro que informa o tipo de integração. Este parâmetro pode receber os valores  L= SistemaLogix, R= Sistema RM  e M = Mensagem única.  
**Valor :** M

**4- MV\_NGMNTAT**

Integração Manutenção (MNT) c/ Ativo (ATF). Informar "" ou "N" não integra; 1= alterações no ATF replicarão no MNT; 2= MNT p/ ATF; 3= MNT p/ ATF e ATF p/ MNT.  
**Valor: 3**

**5- MV\_NGMNTCM**

Integração do Manutenção de Ativos (SigaMNT) com Compras (COM). Informar S para sim e N para não.  
**Valor:** S

**6- MV\_NGMNTCP**

Indica se a numeração dos itens da solicitação de compras será a mesma. Este parâmetro sobrepõe o processo padrão de geração do Compras.  
**Valor:** N

**7- MV\_NGMNTES**

Integração com Estoque.  
**Valor:** S

**8- MV\_NGMNTFI**

Integração do Manutenção de Ativos (SigaMNT) com Financeiro (FIN). Informar S para sim e N para não.  
**Valor:** S

**9- MV\_NGMNTPC**

Integração com PCP.  
**Valor: S**

**10- MV\_NGMNTRH** I

Integração Manutenção (SigaMNT) com Recursos Humanos (RH).  
**Valor: S**

**11- MV\_NGMULOS**

Permite a abertura de mais de uma Ordem de Serviço(O.S) por SOlicitação de Serviço(SS).  
**Valor: S**

**12- MV\_NGPNEUS**

Indica se utiliza complemento de pneus.  
**Valor: S**

**13- MV\_NGPRSB2**

Busca preço médio da tabela SB2.  
**Valor: S**

**14- MV\_NGSALHO**

Define se o campo salário do funcionário da manutenção é integrado com o SigaGPE.  
**Valor: S**

**15- MV\_RASTRO**

Determina a utilização ou não da rastreabilidade dos lotes de produção (S para „sim‟ ou N para „não‟).  
**Valor: N**

**16- MV\_PRODFER**

Item de estoque que indica ferramentas no SIGAMNT.

**Valor: FERRAMENTA**

**17- MV\_PRODTER**

Item de estoque que indica  Serviço de Terceiros no SIGAMNT.

**Pré-condições:** **1-** Sincronizar um produto com a descrição Serviço de Terceiros.  
**Valor: Código do  produto.**

**18- MV\_PRODTRX**

Item de estoque que indica multas no SigaMNT.  
**Pré-condições:** **1-** Sincronizar um produto com a descrição Multa  
**Valor: Código de um produto.**

**19- MV\_PRODTS2**

Item de estoque que indica documentos no SigaMNT.  
Pré-condições:**1-** Sincronizar um produto com a descrição Documento

**Valor: Código de um produto**.

**20- MV\_PRODTS8**

Item de estoque que indica Honorários de Despachante no SigaMNT.

**Pré-condições:** **1-** Sincronizar um produto com a descrição Honorário de Despachante  
**Valor: Código de um produto.**

**21- MV\_NGSECON**

Código do Serviço utilizado para conserto de pneus. Pode ser informado mais de um código de serviço, porém eles devem ser separados por ponto e vírgula(   
**Pré-Condição:** **1-** Ter Sincronizado um Serviço  
**Valor: Código do serviço**

**22- MV\_NGSEREF**

Serviço utilizado para Reforma de Pneus  
**Pré-Condição:** **1-** Ter Sincronizado um Serviço  
Valor: Código do serviço

**23- MV\_NGMNTFR**

Indica que a empresa utiliza o sistema Gestão de Frotas.  
**Valor: S**

**24- Cadastrando um Status no Protheus SigaMNT**

**Passo 1-** Acesse: Protheus SigaMNT/ Atualizações/ Controle de Oficina/ Bens/ Status. **Passo 2-** Incluir um novo registro para os status:

* Aguardando Análise Técnica
* Aguardando Conserto
* Aguardando Reforma
* Aplicado
* Estoque Novo
* Estoque Reformado
* Estoque Usado
* Removido de Serviço

**25- MV\_NGSTAAT**

Parâmetro que define o valor para o status Aguardando Análise Técnica

**Valor: Codigo do status Aguardando Análise Técnica**

**26- MV\_NGSTAEN**

Parâmetro que define o valor para o status Estoque Novo

**Valor: Codigo do status Estoque Novo**

**27- MV\_NGSTAER**

Parâmetro que define o valor para o status Estoque Reformado **Valor: Codigo do status Estoque Reformado**

**28- MV\_NGSTAEU**

Parâmetro que define o valor para o status Estoque Usado **Valor: Codigo do status Estoque Usado**

**29- MV\_NGSTAGC**

Parâmetro que define o valor para o status Aguardando Conserto **Valor: Codigo do status Aguardando Conserto**

**30- MV\_NGSTAGR**

Parâmetro que define o valor para o status Aguardando Reforma **Valor: Codigo do status Aguardando Reforma**

**31- MV\_NGSTAPL**

Parâmetro que define o valor para o status Aplicado **Valor: Codigo do status Aplicado**

**32- MV\_NGSTARS**

Parâmetro que define o valor para o status Removido de Serviço **Valor: Codigo do status Removido de Serviço**

**33- MV\_ESTHOME**

Parâmetro MV\_ESTHOME responsável por controlar o envio  de mensagens de baixa de estoque ou pedidos de compra dos processos de Abastecimento Manual, Abastecimento em Lote e Conciliação de Abastecimento. De acordo como valor informado ao parâmetro, que pode ser S ou C, o sistema apresentará um comportamento diferente  para cada um dos  processos citados anteriormente

**S:** O Parâmetro MV\_ESTHOME com Valor S controlará  o envio dos cadastros de Abastecimento Manual e Abastecimento em Lote.

**C:** O Parâmetro MV\_ESTHOME com Valor C controlará o envio dos cadastros de Conciliação de Abastecimentos.

**N:** não baixa estoque. Nesta parametrização não existe integração com BackOffice RM.

**34- MV\_NGPNEUS**

Parâmetro que indica se utilizará Complemento de Pneus **Valor: S**

**35- MV\_NGPNEST**

Parâmetro que indica se a empresa utilizará Identificação do Bem no Controle de Estoque. **Valor:  S**   **37- MV\_NGPSATI** Parâmetro que indica se utiliza pesquisa de satisfação das solicitações de serviços.

**Valores: S  e N**

**36- MV\_NGSSWRK**

Parâmetro que indica se no módulo de Solicitação de Serviços utilizará o envio de mensagens por workflow online aos solicitantes. **Valores: S  e N**  
**37- MV\_WFWEBEX**

Parâmetro que indica a utilização de web servisse para o workflow.

**Valor:  .F.**   (Ao inserir não esquecer do ponto antes  e depois da Letra F)

**38- MV\_NGWFLG**

Parâmetro que indica se gera log especifico do processamento do workflow (0 - Desabilita; 1 - Habilita)  
**Valores : 0 ou 1**

**39- MV\_EAIMETH**

Parâmetro que informa o método que receberá o xml com as mensagens dos processos enviados pelo Protheus SigaMNT

**Valor: receiveMessage**

**40- MV\_NGWFHT**

Parâmetro que identifica o servidor e porta HTTP

**Valor Exemplo: "**[{\*}{+}](http://127.0.0.1:8080/)[http://127.0.0.1:8080+\*](http://127.0.0.1:8080+*)**"     (Não esquecer das aspas)**

**41- MV\_EAIUSER**

Parâmetro que identifica o usuário do Webservice do EAI que receberá as mensagens dos processos do Protheus SigaMNT

**Valor: mestre**

**42- MV\_EAIPASS**

Parâmetro que identifica a senha do Webservice do EAI que receberá as mensagens dos processos do Protheus SigaMNT

**Valor: totvs**

**43- MV\_EAIURL2**

informa qual o endereço para acessar o webservice do EAI que receberá as mensagens dos processos do Protheus SigaMNT

**Valor: http:// IP do computador em que o TBC foi instalado/TOTVSBusinessConnect/wseaiservice.asmx**

Para mais detalhes sobre as configurações do Protheus , acese os Boletins Técnicos.

---

**Recursos Adicionais**

**TDN - Boletins Técnicos :**   
   
[Configurar Parametros no SigaCFG.pdf](http://tdn.totvs.com/download/attachments/76251246/BT+-+Configurar+Parametros+no+SigaCFG.pdf?version=1&modificationDate=1380031997000)  
[Configurar Webservice TBC no Protheus SigaCFG.pdf](http://tdn.totvs.com/download/attachments/76251246/BT+-+Configurar++Webservice+TBC++no+Protheus+SigaCFG.pdf?version=1&modificationDate=1380031996000)
