---
content_hash: df1093288282fab59183f6c0602dfda46c02cacd70901c13c0fa680881686fd4
fetched_at: '2026-06-29T00:11:28.185285+00:00'
page_id: '730532434'
product: rm
source: tdn-rm
title: Novo Atendimento - Cadastros - Tipo Atendimento TCGI
type: documentation
url: https://tdn.totvs.com/display/LRM/Novo+Atendimento+-+Cadastros+-+Tipo+Atendimento+TCGI
version: 14
---

Para acessar o cadastro dos ***Tipos de Atendimento***, no contexto do módulo TOTVS Construção Gestão de Imóveis, doravante TCGI, acesse a aba de *Atendimento* e no agrupador de nome *Atendimento Revitalizado*, o menu ***Cadastro | Tipos Atendimentos TCGI***:

Ao acessar o cadastro acima, o sistema exibirá a Visão dos Tipos de Atendimentos criados para o TCGI.

Para incluir um novo Atendimento acione o ícone Incluir (símbolo de +) e na tela que se abre, são apresentados os campos abaixo, conforme as abas:

* **Aba *Identificação*:**

**Tipo de Atendimento:** Este campo não é editável e apresenta o Código de Identificação do Tipo de Atendimento criado. Sendo que no momento de inclusão de um novo registro, o mesmo apresenta o valor padrão 0, que será substituído posteriormente, pelo Código de Identificação gerado automaticamente pelo sistema ao salvar este registro;

**Descrição:** Neste campo o sistema apresenta a Descrição do Tipo de Atendimento definido pelo usuário. O preenchimento do mesmo é obrigatório;

**Coligada Etapa do Tipo Atendimento:** Informe a Coligada no qual as *Etapas* deste Tipo de Atendimento estão cadastradas. o cadastro destas ***[Etapas](https://tdn.totvs.com/display/LRM/Etapas)*** é herdado do *TOTVS Aprovações e Atendimento,* doravante *TAA*. Etapas são fases que o atendimento possui, juntamente com as atividades que devem ser realizadas em cada uma delas. Este campo é obrigatório;

**Grupo de Atendimento:** Informe o Grupo de Atendimento ao qual os Atendimentos deste Tipo serão associados. Basicamente, os Grupos de Atendimentos agregam de maneira macro assuntos que podem ser relevantes para a empresa. O cadastro do ***[Grupo de Atendimentos](https://tdn.totvs.com/display/LRM/Grupos+de+Atendimentos)*** deve ser realizado previamente no *TAA*. Este campo é obrigatório.

**Tipo de Atendimento:** Informe o Código do ***[Tipo de Atendimento](https://tdn.totvs.com/pages/viewpage.action?pageId=425459518)***, do *TAA,* ao qual este Tipo de Atendimento do TCGI está associado. Esta entidade é utilizada para classificar o Atendimento, definir suas Etapas (situação atual do atendimento) e verificar o Fluxo de Etapas (passagem de uma etapa para outra) que o mesmo percorrerá no sistema. O preenchimento deste campo é obrigatório.

Importante!

* WhatsApp - O Tipo de Atendimento define se irá utilizar também o whatsapp para interagir com o atendimento.  
  **[Configurar Whatsapp no tipo de atendimento](https://tdn.totvs.com/pages/viewpage.action?pageId=425459518#:~:text=Minhas%20Aprova%C3%A7%C3%B5es%20/%20WhatsApp)**

**Tipo de Atendimento:** Informe a finalidade deste Tipo de Atendimento. Esta informação é fundamental no Processo de Geração de Atendimento, pois este processo irá seguir a parametrização deste cadastro para definir os campos do Atendimento. As opções disponíveis são:

* + **Outros:**  Os Atendimentos deste Tipo podem ser vinculados diretamente a um *Condomínio*, ou a um *Empreendimento*, ou uma *Unidade,* ou a uma *Subunidade*, sem necessariamente estarem vinculados a nenhum *Contrato de Venda* ou de *Locação*.

Os Atendimentos deste Tipo podem ser utilizados em algumas situações como, por exemplo:

* + - Abertura de atendimento pelo síndico para manutenção de áreas comuns;
    - Manutenção de unidades que ainda não foram vendidas (própria incorporadora);
    - Atendimentos do condomínio.

Lembrando que é importante definir o Cliente, já que não existe contrato

* + **Garantia:** Os Atendimentos vinculados a este Tipo são relativos às [Coberturas de Garantias](https://tdn.totvs.com/display/LRM/Contratos+de+Venda+-+Anexos+-+Atendimento+ao+Cliente+-+Cobertura+de+Garantia) estipuladas no Contrato de Venda/Locação da Subunidade/Imóvel. Este *Tipo de Atendimento* também se aplicam aos *Condomínios* e *Empreendimentos*, uma vez que a *garantia* também pode ser acionada para estas Entidades;
  + **Entrega de Chaves:** Os Atendimentos deste Tipo são vinculados ao procedimentos e trâmites relativos à [Entrega de Chaves](https://tdn.totvs.com/display/LRM/Contratos+de+Venda+-+Processo+-+Entrega+de+Chaves) das Subunidades/Imóveis. Este campo é obrigatório; e
  + **Aprovação de WorkFlow:** Os Atendimentos deste Tipo são relativos a realização de aprovação dos Aditivos, Vendas e Distratos dos contratos de venda utilizando o TAA;

**Tipo de Contrato:** Selecione o Tipo de Contrato ao qual a Subunidade/Imóvel, ou as Subunidades/Imóveis ao qual este Tipo de Atendimento se refere. As opções apresentadas são:

* + **Venda:** Selecione esta opção para tratar cenários específicos relativos aos Contrato de Venda, uma vez que os Atendentes, os Processos e as Etapas, poder ser diferentes, em relação às demais opções abaixo;
  + **Aluguel:** Selecione esta opção para tratar Contratos de Locação ou Itens relativos ao contexto do Aluguel em si;
  + **Condomínio/Empreendimento:** Selecione esta opção para tratar cenários e itens relativos aos Condomínios ou aos Empreendimentos.

**Exibir Tipo de Atendimento no Portal do Cliente / App Meu Imóvel:** Marque esta opção para que este Tipo de Atendimento seja disponibilizado no *Portal do Cliente* e no app *Meu Imóvel*, para que o seu Cliente possa gerar os [**Atendimentos** através destas Soluções](https://tdn.totvs.com/display/LRM/Portal+do+Cliente+-+PDC+-+Atendimento);

* + **Permite notificações push da abertura de atendimento pelo atendente:** Ao marcar esta opção o sistema enviará uma ***[notificação push](https://tdn.totvs.com/pages/viewpage.action?pageId=867823930)***, diretamente ao app Meu Imóvel do Cliente, informando a abertura de um novo Atendimento para ele;
  + **Permite notificações push da inclusão de uma discussão atendente:** Ao marcar esta opção o sistema permitirá ao Atendente, o envio de uma [***notificação push***,](https://tdn.totvs.com/pages/viewpage.action?pageId=867823930) diretamente ao app Meu Imóvel do Cliente, informando que houve uma nova interação no Atendimento existente para ele, caso no momento da inserção desta discussão, o Atendente também marque a opção para publicar no fórum.

**Exibir Preferências do Período de Visitas no Atendimento:** Marque esta opção para exibir as Preferências de Dias da Semana (domingo a sábado) e Períodos do Dia (manhã, tarde, noite) para sinalizar a preferência do Cliente em relação ao [Turno](https://tdn.totvs.com/pages/viewpage.action?pageId=616226405) para as Visitas de Inspeção do Atendimento; e

**Exigir o Envio de Anexo no Portal do Cliente / App Meu Imóvel:** Marque esta opção para exigir que o Cliente envie pelo menos um arquivo de anexo, no momento da abertura deste Tipo de Atendimento. Sendo suportados arquivos de até 5MB, nos formatos abaixo:

* + Imagem: jpg, jpeg, png;
  + Vídeo: flv, mov; e/ou
  + Documento: pdf.

Após Salvar este cadastro, o sistema apresenta a aba de ***[Etapas do Tipo de Atendimento](https://tdn.totvs.com/display/LRM/Novo+Atendimento+-+Cadastros+-+Tipo+Atendimento+TCGI+-+Etapas)***, que também pode ser acessada através do menu *Anexos*.
