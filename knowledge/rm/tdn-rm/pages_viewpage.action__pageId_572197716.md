---
content_hash: fabf67570e7c1861df64270fed44cd309777f055f07c111dfb0ff09501deffb3
fetched_at: '2026-06-29T00:10:52.368960+00:00'
page_id: '572197716'
product: rm
source: tdn-rm
title: 'Propostas - Contrato: Assinatura Eletrônica'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=572197716
version: 26
---

# **Introdução**

---

O processo de assinatura eletrônica no Portal de Imóveis consiste em enviar documentos para portais de assinatura digital, possibilitando a assinatura digital dos mesmos através destes portais. Hoje o Portal de Imóveis possui integração com o DocuSign e TOTVS Assinatura Eletrônica (TAE).

Importante: O Portal de Imóveis somente irá trabalhar com o DocuSign caso não exista integração com o TAE ativa. Se houver integração com o TOTVS Assinatura Eletrônica, a integração com o DocuSign será desabilitada.

### **TOTVS Assinatura Eletrônica**

---

Para que o TAE esteja disponível é necessário primeiro que o [RM esteja parametrizado para tal](https://tdn.totvs.com/pages/viewpage.action?pageId=562963400). Sendo assim, após a [sincronia](https://tdn.totvs.com/display/LRM/PVI+-+Backend+-+Sincronizar) deste serviço, ao acessar o menu de ***Propostas / Contrato: Assinatura Eletrônica***,

Além disso, ao acessar a visão de assinatura eletrônica, devemos primeiro fazer login no portal do TAE, para que possamos enviar os documentos.

O Portal de Imóveis irá mostrar a tela de login assim que clicarmos na opção ***Contrato: Assinatura Eletrônica***,

A visão de Contrato: Assinatura Eletrônica é uma visão que possibilitará ao corretor, gerenciar assinantes, documentos, bem como criar ou adicionar novas solicitações de assinaturas digitais ao TAE.

**Solicitar Assinatura:** Clique neste botão para iniciar o processo de assinatura digital, conforme demonstrado abaixo.

A opção **TOTVS Assinatura Eletrônica** será destacada pela tag **TAE** em azul. A seguir, apresentamos os passos necessários para concluir a assinatura no Portal de Imóveis.

#### **Proposta e Contrato**

---

Nesta etapa, apresentamos o número da proposta e a tag **TAE**, que indica que o envio ao **TOTVS Assinatura Eletrônica** está em andamento.   
Além disso, é necessário selecionar as minutas que serão enviadas ao **TOTVS Assinatura Eletrônica**, sendo esse envio obrigatório.

Abaixo das minutas, o sistema agora apresenta a seção **Documentos da Unidade**. Nesta etapa, é possível visualizar e selecionar automaticamente os documentos vinculados à unidade que devem compor o envelope para assinatura.

**Importante:** Esta seção listará automaticamente os documentos que foram previamente anexados àquela unidade específica no Backend do sistema (em *Empreendimentos > Unidades > [Documentos](https://tdn.totvs.com/pages/viewpage.action?pageId=563947962)*).

#### **Documentos**

---

Na etapa de documentos, faremos o upload dos arquivos que precisam ser enviados ao **TAE**.

Como ilustrado na imagem acima, além da minuta no primeiro passo, foram carregados dois documentos adicionais que também serão enviados ao **TAE**.

#### **Signatários**

---

Aqui, devemos incluir os assinantes responsáveis pelos documentos. Por padrão, o Portal de Imóveis exibirá o nome e o e-mail do comprador principal da proposta. É possível alterar ou excluir esse e-mail e adicionar novos signatários.

Neste exemplo, adicionamos dois assinantes para os documentos.

#### **Confirmação**

---

Agora, devemos confirmar os documentos, dar um nome ao Envelope e clicar em **Concluir**.

O conceito de **Envelope**, como o nome sugere, agrupa todos os documentos carregados na etapa anterior em um único envio, tornando o processo de assinatura eletrônica mais ágil e eficiente.

Importante

O nome para o envelope é **obrigatório** e o processo não poderá ser concluído sem este campo preenchido.

Ao clicar em "**Concluir**", os documentos serão unificados através do Envelope e estarão prontos para o envio.

#### **Enviar**

---

Ao clicar em "**Enviar**" os documentos serão enviados de forma definitiva ao **TOTVS Assinatura Eletrônica** e serão disparados e-mails a todos os assinantes, referentes a assinatura pendente.

O processo pode ainda ser interrompido ao clicar em "**Cancelar**".

Importante

Os assinantes ou validadores automáticos cadastrados no Empreendimento através do RM, também irão receber o e-mail com o documento para efetuar a assinatura.  
Mais informações sobre como cadastrar os assinantes automáticos, acesse o link: .

### **Consultando o status da assinatura digital no TOTVS Assinatura Eletrônica:**

---

Para realizar a consulta do status das assinaturas, basta acessar novamente o menu de Contrato: Assinatura Eletrônica. Após o primeiro envio, o sistema irá automaticamente redirecionar para este menu. Portanto, devido a sincronia dos envelopes com o TAE o sistema poderá levar alguns segundos para carregar a tela.

Verifique que, para uma proposta que já teve documentos enviados, no menu de "Assinatura de documentos" os envelopes serão listados como a imagem abaixo. Cada envelope pode possuir um ou mais documentos unificados.

Os campos desta região são:

* **ID**: ID do documento no TAE;
* **Documento**: Nome do envelope;
* **Qtd. Assinantes**: Quantos assinantes estão associados ao envelope enviado.
* **Ações**: Aqui podemos consultar o status da assinatura clicando no botão assinantes, bem como excluir um envelope através do botão excluir. Note que ao excluir um envelope, o Portal de Imóveis não irá verificar se o mesmo já foi assinado. Ao excluir um envelope, **todos** os documentos deste envelope serão excluídos.

Exemplo da tela de Assinantes, consultando o status dos mesmos no TOTVS Assinatura Eletrônica:

Além de consultar o status dos assinantes na tela a cima, também é possível incluir um novo assinante informando o nome e o e-mail conforme imagem a seguir.

Também é possível excluir um assinante específico do envelope. Através do botão de lixeira que é apresentado ao lado da situação. O sistema não permite excluir todos os assinantes de um envelope. Ao menos um assinante deve permanecer.

Conforme é mostrado em , quando estiver um usuário cadastrado no TAE- Assinantes Automáticos, será possível visualizar na tela da imagem acima os usuários que tiveram sua assinatura automática.

### **Visualizar Envelope assinado através do TOTVS Assinatura Eletrônica**

---

Para visualizar a assinatura digital, adicionada ao envelope, basta acessar novamente o menu de Contrato: Assinatura Eletrônica. Os envelopes enviados utilizando o processo Solicitar Assinatura, serão listados na seção Assinatura de Documentos.

Navegue até o botão Visualizar.

  Finalizando o clique sobre o botão, é possível visualizar o envelope com todas as suas Assinaturas Digitais. (Devido a sincronia dos documentos com o TAE, o sistema poderá levar alguns segundos para carregar a tela).

Importante:

* Assinaturas solicitadas pelo DocuSign ainda não são possíveis de acompanhamento direto pelo portal de vendas. Quando todos documentos forem assinados o DocuSign enviará notificação por e-mail ao solicitante da assinatura.
* Ao enviar a proposta de venda ao backoffice, o Portal de Imóveis irá também enviar estes documentos associados à proposta para a venda criada. Os documentos e seus status de assinatura, podem ser consultados via botão TOTVS Assinatura Eletrônica na barra de ferramentas de contratos de venda.
* Após o envio da proposta ao backoffice, o Portal de Imóveis não irá permitir qualquer alteração no documento, como inclusão e exclusão de assinantes, inclusão e exclusão de documento.
* A partir da versão 12.1.33, caso exista um [relatório RM parametrizado nas minutas do empreendimento](https://tdn.totvs.com/display/LRM/PVI+-+Backend+-+Empreendimentos), o Portal de Imóveis irá automaticamente incluir este relatório nas opções de envio de minuta do TOTVS Assinatura Eletrônica. Caso não tenha minutas parametrizadas do empreendimento, o sistema irá utilizar a minuta padrão do sistema.
* Caso o RM esteja parametrizado para realizar a assinatura automática de documentos, o cadastro desses assinantes devem ser do tipo "Portal de Imóveis". Para entender como realizar assinaturas automáticas, [clique aqui.](https://tdn.totvs.com/pages/viewpage.action?pageId=630574349)
