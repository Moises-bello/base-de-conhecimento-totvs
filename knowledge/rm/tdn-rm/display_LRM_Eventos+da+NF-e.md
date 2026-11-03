---
content_hash: cf88c262a8ff1d2d60ee35e7baa283fdaca5f2f93c882b6ceab03041b2938dbf
fetched_at: '2026-06-29T00:12:06.261436+00:00'
page_id: '914790591'
product: rm
source: tdn-rm
title: Eventos da NF-e
type: documentation
url: https://tdn.totvs.com/display/LRM/Eventos+da+NF-e
version: 87
---

Conteúdo:

Conteúdo:

# 1. Sobre

Os eventos da NF-e (Nota Fiscal Eletrônica) são ocorrências registradas após a emissão da nota fiscal para documentar fatos relevantes no seu ciclo de vida. Esses eventos permitem ao emissor, destinatário ou transportador comunicar informações adicionais ou atualizações à Secretaria da Fazenda (SEFAZ), garantindo a integridade e a rastreabilidade das operações fiscais.

Desde situações como a Carta de Correção Eletrônica para corrigir erros específicos até ocorrências logísticas como o Comprovante da Entrega ou Insucesso na Entrega, cada evento possui um propósito específico e deve ser enviado conforme as regras definidas pela legislação. O uso correto dos eventos proporciona maior segurança jurídica, transparência nas operações e facilita a comunicação entre empresas e órgãos fiscais.

Para visualizar os Eventos, acesse o menu: **anexos | Eventos**na tela de emissão da NF-e

# 2. Parametrizações Necessárias

Para que os usuários possam utilizar corretamente a funcionalidade de eventos da NF-e é necessário realizar algumas configurações no sistema. Siga os passos abaixo para garantir a configuração adequada.

ParametrizaçõesPermissões de Usuário

Certifique-se de que os usuários tenham permissão para emitir e consultar eventos da NF-e. Para isso:

1. Acesse o menu: **Cadastros > Segurança > Perfis**.
2. Edite o perfil dos usuários que necessitam dessa permissão.
3. Navegue até a aba **Acesso a Menus**.
4. Conceda permissão nos seguintes menus:
   * **Enviar Evento**
   * **Consultar Autorização Evento**

ExemploParametrização da Filial

Além das permissões, é necessário parametrizar a filial para habilitar o ambiente de operação adequado para os Eventos:

1. Acesse o menu: **Opções > Parâmetros > Gestão de Estoque, Compras e Faturamento > Integrações > Fiscal > Parâmetros por Filial**.
2. Selecione a filial desejada e clique em **Parametrizar**.
3. No menu de parametrização, vá para a **Ambiente Evento** e configure os campos de acordo com a necessidade

# 3. Como enviar um Evento?

O envio de eventos da NF-e é um processo assíncrono, ou seja, após o envio, o usuário deve executar uma consulta para verificar se o evento foi autorizado pela SEFAZ. É importante destacar que apenas notas fiscais já **autorizadas** podem ter eventos vinculados.

false

## 3.1 Envio de Eventos

Siga os passos abaixo para enviar um evento:

1. Acesse o menu: **Utilitários > SPED > NF-e Estadual**.
2. Selecione a NF-e desejada.
3. Clique em **Processos > Envio de Evento**.
4. Uma nova visão chamada **"Envio de Eventos"** será aberta.
5. Selecione o **Tipo de Evento** desejado (por exemplo, Carta de Correção, Cancelamento, Insucesso na Entrega, etc.).
6. Preencha os campos obrigatórios solicitados.
7. Execute o processo para enviar o evento.

> **Dica:** É possível selecionar várias notas fiscais simultaneamente. O sistema criará um evento separado para cada uma, facilitando o envio em lote.

#FFA500#FFFACD#FFE766dashedAviso Importante:

Informamos que processo de **Envio de Eventos no movimento** está sendo desenvolvido gradualmente. Algumas funcionalidades que não são suportadas atualmente, estarão disponíveis nas próximas Releases. Essa mudança é parte do nosso compromisso com a evolução tecnológica e a otimização de nossas soluções, proporcionando maior estabilidade e alinhamento com as atualizações mais recentes do mercado.

No Movimento é possível **Enviar os Eventos das notas de entrada** para o TSS ou para o TPF. Siga os passos abaixo para enviar um evento:

1. Acesse o menu: **Compras > Recebimentos de Materiais > selecione o tipo de movimento de entrada**.
2. Selecione a NF-e desejada.
3. Clique em **Processos > Envio de Evento**.
4. Uma nova visão chamada **"Envio de Eventos"** será aberta.
5. Selecione o **Tipo de Evento** desejado (por exemplo, Solicitação de crédito presumido Apropriação de crédito presumido, etc.).
6. Preencha os campos obrigatórios solicitados.
7. Execute o processo para enviar o evento.

> **Dica:** É possível selecionar várias notas fiscais simultaneamente. O sistema criará um evento separado para cada uma, facilitando o envio em lote.

false

## 3.2 Consulta de Eventos

Após o envio de um evento (seja por NF-e ou Movimento de Entrada), o status de autorização junto à SEFAZ deve ser consultado.

1. #### A. Consulta de Eventos (Pela NF-e)

   1. Acesse o menu: Gestão de Compras, estoque e faturamento > Vendas > Nota Fiscal Eletrônica > Anexo Eventos >Processos > Consulta Eventos.
   2. **Selecione** uma ou mais **Notas Fiscais Eletrônicas (NF-e)** enviadas.
   3. O sistema consultará o status dos **Eventos pendentes** para cada NF-e selecionada.
   4. O resultado será retornado, informando se o evento foi **Autorizado** ou **Rejeitado** pela SEFAZ.
   > **💡 Dica:** É possível selecionar **várias NF-e simultaneamente**. O sistema consultará todos os Eventos pendentes associados a cada uma das notas.

   #### B. Consulta de Eventos (Pelo Movimento de Entrada)

   #### Regra de Execução Específica

   * **Ao consultar eventos a partir de um Movimento de Entrada**, serão processados **somente** os eventos cujo tipo de emitente do movimento seja **Fornecedor**.
   * Acesse o menu: Gestão de Compras, estoque e faturamento > Compras/Movimentações > Anexo Eventos > Processos > Consulta Eventos.
   1. **Selecione** o **Movimento de Entrada** enviado.
   2. O sistema consultará o status dos **Eventos pendentes** para cada Movimento de Entrada selecionado.
   3. O resultado será retornado, informando se o evento foi **Autorizado** ou **Rejeitado** pela SEFAZ.
   > **💡 Dica:** É possível selecionar **vários eventos simultaneamente**. O sistema consultará todos os Eventos pendentes associados a cada um.

# 4. Tipos de Evento

O sistema oferece suporte aos principais eventos relacionados à NF-e, cada um com uma finalidade específica, garantindo a correta comunicação com a SEFAZ e a rastreabilidade do documento fiscal. Veja abaixo os tipos de eventos disponíveis:

EventosCarta de Correção Eletrônica (CC-e)

Permite corrigir erros em campos específicos da NF-e, desde que não alterem informações essenciais, como valores totais, dados cadastrais do emitente e destinatário, ou a data de emissão. A CC-e ajuda a evitar cancelamentos desnecessários e mantém a validade do documento.

**Observação:** Para enviar este evento, é obrigatório informar um texto explicativo com pelo menos **15 caracteres** que descreva a correção realizada.

Cancelamento de NF-e

Este evento estará disponível somente se na parametrização do tipo de movimento ambos emitente e destinatário estiverem configurados como Empresa.

Imagem

Esse evento possibilita o cancelamento de uma nota fiscal já emitida, desde que a operação não tenha sido concluída e esteja dentro do prazo permitido pela legislação (geralmente 24 horas após a emissão). O cancelamento garante a anulação formal do documento junto à SEFAZ.

Ao selecionar o tipo **Cancelamento**, o sistema verifica se há alguma **pendência** que possa impedir o cancelamento do movimento associado.

* **Caso exista pendência**, o sistema exibirá uma mensagem informativa, questionando se o usuário deseja **interromper o processo**.

  + Ao clicar em **Sim**, o envio do evento será **abortado**, e o usuário poderá ajustar a pendência existente antes de tentar novamente.
  + Ao clicar em **Não**, o evento será gerado normalmente. No entanto, será necessário resolver a pendência posteriormente para que o processo de **consulta de autorização** seja concluído com sucesso.
* **Caso não exista pendência** ou o usuário opte por prosseguir clicando em **Não**, será necessário informar um texto justificando o cancelamento com **mais de 15 caracteres** para concluir o envio do evento.

Comprovante de Entrega

Utilizado para registrar a confirmação de que a mercadoria foi entregue ao destinatário. Esse evento é importante para assegurar a conclusão da operação logística e fornecer evidências formais da entrega realizada.

Para este tipo é possível gerar o **Comprovante de Entrega da NF-e** ou o **Cancelamento do Comprovante de Entrega da NF-e** Para mais informações consulte:

Siare - Módulo de Registro de Saída

O evento **Siare** tem como objetivo permitir o registro eletrônico da data da efetiva saída da mercadoria, quando essa informação não foi informada no arquivo digital da NF-e transmitido ao fisco e autorizado pela **Secretaria de Estado de Fazenda**.

Como o arquivo digital da NF-e não pode ser modificado após sua autorização, o **Módulo de Registro de Saída** possibilita ao contribuinte registrar essa data posteriormente, quando, por questões logísticas, não for possível precisar a data da efetiva saída no momento da transmissão da NF-e.

Insucesso na Entrega

Esse evento informa a SEFAZ que a tentativa de entrega não foi bem-sucedida. Motivos comuns incluem destinatário ausente, endereço incorreto ou recusa de recebimento. O registro desse evento ajuda a documentar problemas na logística e prevenir questionamentos futuros.

Para mais informações consulte: [Evento Insucesso na Entrega da NF-e](https://tdn.totvs.com/display/LRM/Evento+Insucesso+na+Entrega+da+NF-e)

Informação de efetivo pagamento p/ crédito presumido

**Evento: 112110 - Informação de efetivo pagamento integral para liberar crédito presumido do adquirente****Função:** Permitir que o emitente da NFe informe o efetivo pagamento integral da operação a fim de liberar crédito presumido do adquirente.

Campos:

* Selecione o Tipo do Autor: Valor default: 1=Empresa Emitente - Valores disponíveis: 1=Empresa Emitente, 2=Empresa destinatária; 3=Empresa; 5=Fisco; 6=RFB; 9=Outros Órgãos;
* UF do Autor: Estado do Autor;
* Indicador de efetiva quitação: Valor default 1

ImagemAtualização da Data de Previsão de Entrega#FFA500#FFFACD#FFE766dashedAviso Importante:99%

Informamos que o **Evento 112150: Atualização da Data de Previsão de Entrega** está sendo desenvolvido gradualmente. Algumas funcionalidades que não são suportadas atualmente, estarão disponíveis nas próximas Releases. Essa mudança é parte do nosso compromisso com a evolução tecnológica e a otimização de nossas soluções, proporcionando maior estabilidade e alinhamento com as atualizações mais recentes do mercado.

**Evento: 112150 - Atualização da Data de Previsão de Entrega****Função:** Permitir ao fornecedor atualizar a data da previsão de entrega ou disponibilização do bem ao adquirente, de forma a remover o débito do mês em que foi previsto inicialmente  
  
Ao executar o processo para enviar o evento 112150, o mesmo permite ao fornecedor atualizar a data da previsão de entrega ou disponibilização do bem ao adquirente, de forma a remover o débito do mês em que foi previsto inicialmente.

Modelo: NF-e modelo 55  
Autor do Evento: emitente da NF-e  
Código do Tipo de Evento: 112150

**Campos:**

* Selecione o Tipo do Autor: Valor default: 1=Empresa Emitente - Valores disponíveis: 1=Empresa Emitente, 2=Empresa destinatária; 3=Empresa; 5=Fisco; 6=RFB; 9=Outros Órgãos;
* UF do Autor: Estado do Autor;
* Data da previsão de entrega: Valor informado pelo usuário.

**Regras da consulta deste evento:**

* Durante a consulta do evento Data de Previsão de Entrega, caso o status do evento for **autorizado** e o movimento estiver **escriturado,** será alterado automaticamente a data no Lançamento Fiscal.

Execução do processoSolicitação de Apropriação de crédito presumido

**Evento: 211110 - Solicitação de Apropriação de crédito presumido**

**Função:** Evento a ser gerado pelo destinatário da NF-e em relação às notas fiscais de aquisição de emissão de terceiros e que lhe gerem o direito à  
apropriação de crédito presumido.  
  
Verifique as parametrizações necessárias para realizar o envio:

Evento a ser gerado pelo adquirente em relação às notas fiscais de aquisição de emissão de terceiros e que lhe gerem o direito à apropriação de crédito presumido.

**Processo e regras:**

**Exibição de Eventos e execução:**  
• Ao enviar eventos a partir de um movimento de entrada, serão exibidos e processados **somente** os eventos de **entrada (1.2.XX)** e tipo emitente do movimento for de **Fornecedor**.

**Regras de Geração do Evento e Status:**  
• A rotina **deve permitir** a geração do evento em lote (com vários Movimentos selecionados).  
• O sistema **não deve permitir** a geração deste evento (211110) se já existir um evento do mesmo tipo com status Autorizado, Pendente ou Cancelamento Pendente para o Movimento.

• **Status de Gravação:**  
◦ Em caso de **erro** durante a execução, o Evento deve ser gravado com o status Inconsistente.  
◦ Em caso de **sucesso** na execução (envio para o TSS/TPF), o Evento deve ser gravado com o status Pendente.  
• Ao final do processo, um **histórico** deve ser registrado com o resultado do envio do Evento.

**Regra de Geração dos Grupos de Tributos (gIBS e gCBS):**  
• Se o item **não tiver o tributo** (IBS ou CBS) parametrizado, o respectivo grupo de tributo (gIBS ou gCBS) **NÃO** deve ser exibido no XML do evento.  
• Se o item **tiver o tributo** parametrizado, mesmo que seus valores estejam zerados, o respectivo grupo (gIBS ou gCBS) **DEVE** ser gerado no XML.

Execução do processo

Anexo:

ImagemImobilização de Item#FFA500#FFFACD#FFE766dashedAviso Importante:1%99%

Informamos que o **Evento 211130 - Imobilização de Item** está sendo desenvolvido gradualmente. Algumas funcionalidades que não são suportadas atualmente, estarão disponíveis nas próximas Releases. Essa mudança é parte do nosso compromisso com a evolução tecnológica e a otimização de nossas soluções, proporcionando maior estabilidade e alinhamento com as atualizações mais recentes do mercado.

**Evento 211130 - Imobilização de Item**

**Função:** Evento a ser gerado pelo adquirente de bem, quando este for integrado ao seu ativo imobilizado, a fim de viabilizar a adequada identificação, pelos sistemas da administração tributária, de prazo limite para apreciação de eventuais pedidos de ressarcimento do respectivo crédito, nos termos do art. 40, I da LC 214/2025. Modelo: NF-e modelo 55 Autor do Evento: Destinatário da NF-e (Adquirente)

Verifique as parametrizações necessárias para realizar o envio: [Parametrizações - Envio de evento no movimento](https://tdn.totvs.com/pages/viewpage.action?pageId=1015560568)

O usuário deve selecionar a quantidade de cada item do movimento sobre os quais será solicitado a apropriação dos créditos de IBS e CBS.

**Processo e regras:**

**Exibição de Eventos e execução:** Ao enviar eventos a partir de um movimento de entrada, serão exibidos e processados **somente** os eventos de **entrada (1.2.XX)** e tipo emitente do movimento for de **Fornecedor**.

**Regras de Geração do Evento e Status:**

* Depois de informar a quantidade consumida, será feito o cálculo automático do IBS e CBS que será enviado: (valor IBS base / quantidadeItemMovimento) \* quantidade consumida
* A quantidade consumida não deve exceder o valor da quantidade do movimento.
* A rotina **não permite** o envio do evento em lote (com vários Movimentos selecionados).
* O sistema **não permite** o envio deste evento (**211130**) se já existir um outro evento do mesmo tipo com status Pendente ou Cancelamento Pendente para o Movimento.
* **Status de Gravação:**

◦ Em caso de **erro** durante a execução, o Evento é gravado com o status Inconsistente.

◦ Em caso de **sucesso** na execução (envio para o TSS/TPF), o Evento é gravado com o status Pendente.

◦ Ao final do processo, um **histórico** é registrado com o resultado do envio do Evento.

Execução do processoSolicitação de Apropriação de crédito de Combustível#FFA500#FFFACD#FFE766dashedAviso Importante:1%99%

Informamos que o evento ****Evento 211140: Solicitação de Apropriação de Crédito de Combustível**** está sendo desenvolvido gradualmente. Algumas funcionalidades que não são suportadas atualmente, estarão disponíveis nas próximas Releases. Essa mudança é parte do nosso compromisso com a evolução tecnológica e a otimização de nossas soluções, proporcionando maior estabilidade e alinhamento com as atualizações mais recentes do mercado.

****Evento: 211140 - Solicitação de Apropriação de Crédito de Combustível******Função:** Evento a ser gerado pelo adquirente de combustível listado no art. 172 da LC 214/2025 e que pertença à cadeia produtiva desses combustíveis, para solicitar a apropriação de crédito referente à parcela que for consumida em sua atividade comercial, observada exceção do art. 180 da LC 214/2025  
  
Verifique as parametrizações necessárias para realizar o envio:

O usuário deve selecionar a quantidade de cada item do movimento sobre os quais será solicitado a apropriação dos créditos de IBS e CBS. 

**Processo e regras:**

**Exibição de Eventos e execução:**  
• Ao enviar eventos a partir de um movimento de entrada, serão exibidos e processados **somente** os eventos de **entrada (1.2.XX)** e tipo emitente do movimento for de **Fornecedor**.

**Regras de Geração do Evento e Status:**

• Depois de informar a quantidade consumida, será feito o cálculo automático do IBS e CBS que será enviado: (valor IBS base / quantidade) \* quantidade consumida  
• A quantidade consumida não deve exceder o valor da quantidade do movimento.  
• A rotina **não** **permite** o envio do evento em lote (com vários Movimentos selecionados).  
• O sistema **não permite** o envio deste evento (211140) se já existir um outro evento do mesmo tipo com status Pendente ou Cancelamento Pendente para o Movimento.  
• É possível enviar o evento novamente mesmo que já exista um registro de envio com o status Autorizado.

• **Status de Gravação:**  
◦ Em caso de **erro** durante a execução, o Evento é gravado com o status Inconsistente.  
◦ Em caso de **sucesso** na execução (envio para o TSS/TPF), o Evento é gravado com o status Pendente.  
◦ Ao final do processo, um **histórico** é registrado com o resultado do envio do Evento.

Execução do processoPedido de Prorrogação de Remessa 1° Prazo

**Evento: 111500 - Pedido de Prorrogação de Remessa 1° Prazo  
Função:** Este evento substitui a necessidade de petição em papel para prorrogar o prazo de 180 dias para retorno de mercadorias remetidas para conserto, reparo ou industrialização. 

Imagem 01

**Processo e Regras:**

* **Exibição de Eventos e Execução:**

  + Ao enviar eventos a partir de um movimento de saída, serão exibidos e processados os movimentos que possuam o tipo de operação compatível com remessa e tipo emitente **Empresa**.
  + **Execução Individual:** A rotina **não permite** a geração deste evento em lote. Deve ser selecionado apenas uma nota por processo de envio para garantir a integridade da seleção dos itens.
* **Regras de Geração do Evento e Status:**

  + O sistema **não deve permitir** a geração deste evento (111500) se já existir um evento do mesmo tipo com status **Pendente**. O sistema não faz consistências referentes a quantidade de itens já prorrogadas ou se já existe um evento autorizado. Estas consistências são de responsabilidade da SEFAZ.
  + **Edição de Itens:** Ao carregar os itens do movimento, a coluna **Quantidade Prorrogada** é preenchida automaticamente com a quantidade total do item contido na NF-e. O usuário pode editar para um valor menor ou igual à quantidade original, ou excluir itens que não serão objeto da prorrogação.

    Imagem 02
* **Consulta de Autorização e Retorno da SEFAZ:**

  + **Atualização da Data de Retorno:** Após a autorização, o sistema atualiza a data de retorno nos itens de movimento autorizados caso o campos esteja preenchhido. A regra utiliza o prazo configurado na **Natureza de Operação**; caso esteja em branco, será aplicado o prazo padrão de **180 dias**. A atualização ocorre apenas se o campo de data de retorno no item não estiver vazio.
* **Status de Gravação Envio:**

  + Em caso de **erro** durante a execução, o Evento deve ser gravado com o status **Inconsistente**.
  + Em caso de **sucesso** na execução (envio para o TSS), o Evento deve ser gravado com o status **Pendente**.
* **Status de Gravação Consulta:**
  + Em caso de **Rejeição**, o Evento deve ser gravado com o status **Rejeitado**.
  + Em caso de **Autorização**, o Evento deve ser gravado com o status **Autorizado**.
  + Caso a **Data de Retorno de Remessa** esteja preenchida no item de movimento, é gravado o log de alteração no **histórico da NF-e.**
Pedido de Prorrogação de Remessa 2° Prazo

**Evento: 111501 - Pedido de Prorrogação de Remessa 2° Prazo  
Função:** Este evento substitui a necessidade de petição em papel para prorrogar o prazo de 180 dias para registros que já enviaram o evento:  **Pedido de Prorrogação de Remessa 1° Prazo**

Imagem 01

**Processo e Regras:**

* **Exibição de Eventos e Execução:**

  + Ao enviar eventos a partir de um movimento de saída, serão exibidos e processados os movimentos que possuam o tipo de operação compatível com remessa e tipo emitente **Empresa**.
  + **Execução Individual:** A rotina **não permite** a geração deste evento em lote. Deve ser selecionado apenas uma nota por processo de envio para garantir a integridade da seleção dos itens.
* **Regras de Geração do Evento e Status:**

  + O sistema **não deve permitir** a geração deste evento (111500) se já existir um evento do mesmo tipo com status **Pendente**. O sistema não faz consistências referentes a quantidade de itens já prorrogadas ou se já existe um evento autorizado. Estas consistências são de responsabilidade da SEFAZ.
  + **Edição de Itens:** Ao carregar os itens do movimento, a coluna **Quantidade Prorrogada** é preenchida automaticamente com a quantidade total do item contido na NF-e. O usuário pode editar para um valor menor ou igual à quantidade original, ou excluir itens que não serão objeto da prorrogação.

* + Imagem 02
* + **Consulta de Autorização e Retorno da SEFAZ:**

    - **Atualização da Data de Retorno:** Após a autorização, o sistema atualiza a data de retorno nos itens de movimento autorizados caso o campos esteja preenchhido. A regra utiliza o prazo configurado na **Natureza de Operação**; caso esteja em branco, será aplicado o prazo padrão de **180 dias**. A atualização ocorre apenas se o campo de data de retorno no item não estiver vazio.
  + **Status de Gravação Envio:**

    - Em caso de **erro** durante a execução, o Evento deve ser gravado com o status **Inconsistente**.
    - Em caso de **sucesso** na execução (envio para o TSS), o Evento deve ser gravado com o status **Pendente**.
  + **Status de Gravação Consulta:**
    - Em caso de **Rejeição**, o Evento deve ser gravado com o status **Rejeitado**.
    - Em caso de **Autorização**, o Evento deve ser gravado com o status **Autorizado**.
    - Caso a **Data de Retorno de Remessa** esteja preenchida no item de movimento, é gravado o log de alteração no **histórico da NF-e.**
Não Fornecimento com Pagamento AntecipadoNão Fornecimento com Pagamento Antecipado

**Evento: 112140 - Fornecimento não Realizado com Pagamento Antecipado**

**Função:** Esta inovação permite que as empresas comuniquem à SEFAZ o desfazimento total ou parcial de negócios que tiveram pagamentos antecipados, garantindo a conformidade da empresa com a Reforma Tributária (LC 214/2025 e NT 2025.002) e viabilizando o estorno e a recuperação correta dos tributos de IBS e CBS recolhidos.

**Processo e Regras:**

* **Exibição de Eventos e Execução:**

  + **Execução Individual:** A rotina **não permite** a geração deste evento em lote. Deve ser selecionado apenas uma nota por processo de envio para garantir a integridade da seleção dos itens.
* **Regras de Geração do Evento e Status:**

  + O sistema **não deve permitir** a geração deste evento se já existir um evento do mesmo tipo com status **Pendente**. O sistema não faz consistências referentes a quantidade de itens já prorrogadas ou se já existe um evento autorizado. Estas consistências são de responsabilidade da SEFAZ.
  + **Edição de Itens:** Ao carregar os itens do movimento, as colunas de Valores do IBS e CBS são preenchidas automaticamente com a quantidade dos Itens de Estorno do item contido na NF-e. O usuário pode editar para um valor menor ou igual à quantidade original, ou excluir itens que não serão objeto da prorrogação.
* **Status de Gravação Envio:**

  + Em caso de **erro** durante a execução, o Evento deve ser gravado com o status **Inconsistente**.
  + Em caso de **sucesso** na execução (envio para o TSS), o Evento deve ser gravado com o status **Pendente**.
* **Status de Gravação Consulta:**
  + Em caso de **Rejeição**, o Evento deve ser gravado com o status **Rejeitado**.
  + Em caso de **Autorização**, o Evento deve ser gravado com o status **Autorizado**.
Perda de Isenção ZFM/ALMImportação em ALC/ZFM não Convertida em isenção

**Evento: 112120 - Importação em ALC/ZFM não Convertida em isenção**

**Função:** Atendendo à **NT 2025.002** e à legislação da Reforma Tributária **(LC 214/2025)**, deve efetuar a confissão do débito de IBS e CBS para mercadorias importadas em áreas incentivadas que não cumpriram os requisitos de isenção, evitando multas por sonegação.

**Processo e Regras:**

* **Exibição de Eventos e Execução:**

  + **Execução Individual:** A rotina **não permite** a geração deste evento em lote. Deve ser selecionado apenas uma nota por processo de envio para garantir a integridade da seleção dos itens.
* **Regras de Geração do Evento e Status:**

  + O sistema **não deve permitir** a geração deste evento se já existir um evento do mesmo tipo com status **Pendente**. O sistema não faz consistências referentes a quantidade e valores de itens já informado ou se já existe um evento autorizado. Estas consistências são de responsabilidade da SEFAZ.
  + **Edição de Itens:** Ao carregar os itens do movimento, as colunas de Valores **IBS** e **CBS** devem ser informadase **Quantidade Sem Benefício** o usuário pode editar para um valor menor à quantidade original, ou excluir itens que não tiveram perda de isenção.

* **Status de Gravação Envio:**

  + Em caso de **erro** durante a execução, o Evento deve ser gravado com o status **Inconsistente**.
  + Em caso de **sucesso** na execução (envio para o TSS), o Evento deve ser gravado com o status **Pendente**.
* **Status de Gravação Consulta:**
  + Em caso de **Rejeição**, o Evento deve ser gravado com o status **Rejeitado**.
  + Em caso de **Autorização**, o Evento deve ser gravado com o status **Autorizado**.
Solicitação Apropriação de Crédito Bens e ServiçosSolicitação Apropriação de Crédito Bens/Serviços - Atividade do Adquirente

**Evento: 211150 - Solicitação de Apropriação de Crédito para bens e serviços que dependem de atividade do adquirente**

**Função:** De acordo com a **LC 214/2025 (Art. 57)** e **NT 2025.002**, itens de uso e consumo específico não geram crédito automaticamente. A empresa compradora precisa emitir o evento **211150** comprovando a relação com sua atividade para ter o benefício legal do crédito de IBS e CBS, reduzindo seu custo operacional de forma lícita.

**Processo e Regras:**

* **Exibição de Eventos e Execução:**

  + **Execução Individual:** A rotina **não permite** a geração deste evento em lote. Deve ser selecionado apenas uma nota por processo de envio para garantir a integridade da seleção dos itens.
* **Regras de Geração do Evento e Status:**

  + O sistema **não deve permitir** a geração deste evento se já existir um evento do mesmo tipo com status **Pendente**. O sistema não faz consistências referentes a quantidade e valores de itens já informado ou se já existe um evento autorizado. Estas consistências são de responsabilidade da SEFAZ.
  + **Edição de Itens:** Ao carregar os itens do movimento, as colunas de **Valores** **IBS Solicitado** e **Valores** **CBS Solicitados** devem ser informadaso usuário não pode editar para um valor menor que zero ou maior que o valor original.

* **Status de Gravação Envio:**

  + Em caso de **erro** durante a execução, o Evento deve ser gravado com o status **Inconsistente**.
  + Em caso de **sucesso** na execução (envio para o TSS), o Evento deve ser gravado com o status **Pendente**.
* **Status de Gravação Consulta:**
  + Em caso de **Rejeição**, o Evento deve ser gravado com o status **Rejeitado**.
  + Em caso de **Autorização**, o Evento deve ser gravado com o status **Autorizado**.

Exemplo de Rejeição

| Mensagem | Descrição Erro |
| --- | --- |
| 575 | Autor do evento diverge do destinatário da NF-e |
| 1096 | Número de item não existe na NFe |
| 1097 | O valor do crédito de IBS do item não pode ser maior que o valor do IBS do respectivo item na NFe. |
| 1098 | O valor do crédito de CBS do item não pode ser maior que o valor da CBS do respectivo item na NFe. |

# 5. Cancelamento de Evento

Cancelamento de EventoCancelamento de Evento NFe

**Evento: 110001 - Cancelamento de Evento  
Função:** Permitir que o autor de um Evento já autorizado possa proceder o seu cancelamento..

Ao executar o processo **Cancelamento do Evento**, o sistema verifica se há alguma **pendência** que possa impedir o cancelamento do evento selecionado, caso contrário o processo é executado e o registro do cancelamento é gerado com status "Pendente". Ao Consultar o cancelamento, caso autorizado, o sistema atualiza o status para autorizado e o status do registro do evento pai é alterado para "Cancelado", caso o evento seja rejeitado o sistema atualiza o status para "Rejeitado", volta o status do registro pai para "Autorizado" e apresenta o motivo da rejeição no log do processo.

**Caso o status do evento a ser cancelado seja diferente de autorizado**, o sistema exibirá uma mensagem informando que só é permitido o cancelamento de um evento autorizado.

O evento **110001** **(Cancelamento de Evento)** pode ser utilizado para cancelar **todos os novos eventos previstos na Nota Técnica 2025.002, com exceção do próprio evento de cancelamento (110001)**.

Para facilitar o entendimento foi dividido a lista dos eventos que podem ser cancelados de acordo com o **autor** responsável pela sua emissão:

**Eventos emitidos pelo Fornecedor (Emitente da NF-e)**

Estes eventos devem ser emitidos (e cancelados) utilizando o Certificado Digital da empresa que emitiu a nota fiscal de saída. 

* **112110** - Informação de efetivo pagamento integral para liberar crédito presumido do adquirente.
* **112120** - Importação em ALC/ZFM não convertida em isenção.
* **112130** - Perecimento, perda, roubo ou furto - durante o transporte contratado pelo fornecedor (Frete CIF).
* **112140** - Fornecimento não realizado com pagamento antecipado.
* **112150** - Atualização da Data de Previsão de Entrega.

**Eventos emitidos pelo Adquirente (Destinatário da NF-e)**

Estes eventos devem ser emitidos (e cancelados) utilizando o Certificado Digital da empresa destinatária da nota fiscal.

* **211110** - Solicitação de Apropriação de crédito presumido (Pode ser emitido pelo emitente ou destinatário).
* **211124** - Perecimento, perda, roubo ou furto - durante o transporte contratado pelo adquirente (Frete FOB).
* **211128** - Aceite de débito na apuração por emissão de nota de crédito.
* **211130** - Imobilização de Item (Para controle do prazo-limite de ressarcimento de crédito).
* **211140** - Solicitação de Apropriação de Crédito de Combustível (Para atividades produtivas).
* **211150** - Solicitação de Apropriação de Crédito para bens e serviços que dependem de atividade do adquirente.

Detalhe Cancelamento do Evento 112150

Ao cancelar o Evento 112150: Atualização da Data de Previsão de Entrega, caso o movimento já esteja escriturado, o sistema atualiza a data de entrega conforme o último evento autorizado de alteração da data de previsão de entrega, caso não exista nenhum evento anterior o sistema atualiza a data de entrega com a data do movimento, segue exemplo abaixo, na imagem 02:

Cancelamento de Evento de Prorrogação

**Evento:** 111502, **- Cancelamento de Evento de Prorrogação 1º Prazo**

**Evento:** 111503, **- Cancelamento de Evento de Prorrogação 2º Prazo**

****Função:****Permitir que o cancelamento de um Evento de Solicitação de Prorrogação, já autorizado, possa ser realizado.

Ao cancelar o Evento 111500 e 111501 (Evento de prorrogação de primeiro e segundo prazo), caso os itens envolvidos no movimento possuam o campo: Data de Retorno de Remessa preenchido, o mesmo será atualizado, removendo o prazo que foi adicionado anteriormente no envio do evento de prorrogação de prazo. 

Imagem

# 6. Histórico do Evento

Cada evento da NF-e possui um histórico detalhado, que registra todas as etapas pelas quais o evento passou desde o seu envio. Esse histórico inclui informações essenciais para o acompanhamento, como:

* **Data e Hora do status:** quando o evento foi registrado/atualizado no sistema.
* **Status de Processamento:** indica se o evento foi aceito, rejeitado ou está pendente.
* **Xml Enviado e xml retornado da SEFAZ:** demonstra o xml completo que foi enviado para a SEFAZ e o retorno dela.

O histórico é uma ferramenta indispensável para auditoria e rastreabilidade, permitindo ao usuário consultar o ciclo completo do evento e solucionar possíveis problemas de forma ágil.

Para visualizar o histórico, acesse o menu: **anexos | Eventos | selecione o evento desejado | Histórico do Evento**
