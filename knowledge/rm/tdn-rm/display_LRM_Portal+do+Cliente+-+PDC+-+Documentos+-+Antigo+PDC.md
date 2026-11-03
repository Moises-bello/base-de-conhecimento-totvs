---
content_hash: 1c087611f7ebcd15456059909c10bbc544b8f937c6a01799992ecd2490936e09
fetched_at: '2026-06-29T00:09:48.315985+00:00'
page_id: '435105120'
product: rm
source: tdn-rm
title: Portal do Cliente - PDC - Documentos - Antigo PDC
type: documentation
url: https://tdn.totvs.com/display/LRM/Portal+do+Cliente+-+PDC+-+Documentos+-+Antigo+PDC
version: 19
---

# **1) Introdução**

---

Esta funcionalidade permite ao administrador anexar à venda ou aluguel, cópias de contratos e documentos em geral para o usuário final acessar através do portal.

# **2) Como Fazer**

---

**2.1) Gestão**

O administrador do sistema irá armazenar os documentos somente através do executável RM.

* No menu Contratos de Venda, o usuário deve ir em anexos e selecionar a opção **Contratos - Documentos**.
* Para documentos de aluguel o usuário poderá cadastrá-los através do .

Na visão do anexo, o usuário consegue visualizar todos os documentos cadastrados para aquela venda / contrato de aluguel. Os arquivos e os seus dados podem ser alterados.

Ao criar ou editar um documento a seguinte janela é abertaDocumento por Empreendimento!

# Documento por empreendimento

**Esta funcionalidade será liberada da versão 12.1.2302 em diante!**

Existem casos, em queum determinado documento é o mesmo para diversos contratos, como por exemplo ( Planta, manual de garantias e etc ). Obrigado o usuário entrar em diversos contratos para associar o mesmo tipo de documento repetidamente gerando um trabalho extra. Agora será possível inserir determinado documento para vários contratos ao mesmo tempo pelo empreendimento.

Habilitar o perfil do usuário para que possa utilizar esta funcionalidade.

Habilitar o perfil do usuário para utilizar a funcionalidade.

01.02.13 – Documentos do Empreendimento

Dentro do cadastro do Empreendimento | Anexos

Documentos.

Todos contratos que fazem parte deste empreendimento , terão acesso ao Documento anexado.

Ao cadastrar um novo documento, o usuário deverá obrigatoriamente inserir o nome do documento e o arquivo. O arquivo deverá ser do tipo PDF.  
O limite de 5MB existente fixo no sistema, passa a ser configurável a partir da versão 12.1.2205. Para configurar acima de 5MB deverá ir nos parâmetros de incorporação na etapa "Geral" e moficar para o tamanho limite desejado.

Além desses dois campos, o usuário pode definir se o documento está ativo (vigente) ou não. Por exemplo: A venda possui um contrato de compra e venda, contudo após uma negociação, um aditivo foi feito e sobrepõe todos os termos do primeiro contrato e assim gerando um novo documento. Neste exemplo, caso o administrador deseja manter o histórico ele pode transformar o contrato antigo para inativo, e o novo contrato ele atribui como ativo. Esta informação (ativo / inativo) é apresentada para o comprador do imóvel no Portal. A mesma lógica pode ser seguida para documentos associados à contratos de aluguel.

Outro campo passível de alteração é o "Publicar no Portal". Este campo informa se o documento estará visível ou não para o comprador / locatário no Portal do Cliente.

Ainda na tela de criação / edição do documento, o usuário conseguirá visualizar e baixar o documento salvo no sistema.

**2.2) Cliente**

Atenção!

* Para que o menu de documentos fique disponível para o usuário no Portal do Cliente, a seguinte permissão deve ser concedida no perfil: **[13.02.09] Documentos.**
* Para que a lista de documentos habilitadas para serem visualizadas no portal seja visualizada, a permissão deve ser concedida também no perfil: **[01.01.01] Contratos de Venda | [01.01.01.2] Contratos: Documentos - Visualizar**

Na visão de documentos, o comprador ou locatário, consegue visualizar todos os documentos divididos por cada venda / contrato de locação. Na listagem, o Portal exibe o status do documento (ativo/inativo) e o nome cadastrado para o documento. Ao clicar no botão Visualizar ou sobre a linha, uma nova aba no browser é criada e o documento é exibido em formato PDF.

A partir da versão 12.1.33, foi implementado um log de abertura dos documentos. Este log visa armazenar as informações:

* Documento aberto
* Usuário
* Data de abertura
* Sistema (portal ou mobile).
* IP de cliente.

Desta forma, todo documento aberto irá salvar na tabela XDOCUMENTOSLOGACESSO as informações acima.

# **3) Documentos do TOTVS Assinatura Eletrônica**

---

A partir da versão 12.1.33, com a disponibilização da integração com o TOTVS Assinatura eletrônica, todos os documentos associados à contratos de venda ou de aluguel, que foram enviados ao TOTVS Assinatura Eletrônica, poderão ser vistos no menu de documentos, como qualquer outro documento associado aos contratos.

Importante!

Para apresentar os Documentos ao usuário, o PDC consulta pelo menos 3 entidades: Contrato de Venda, Empreendimento e uma tabela de integração com o TOTVS Assinatura Eletrônica (TAE).

Caso ocorra alguma exceção em alguma destas entidades, o sistema não apresentará nenhum documento no PDC.

Em cenários como este, entre em contato com a equipe de Suporte, para análise.

# **4) Veja Também**

---

* Gerar Contrato
