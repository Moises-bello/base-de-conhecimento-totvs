---
content_hash: 954b56001e8a0f2ff66b0c5673bf43f784185f46a03ea1e7e3ca90b2c8d84eb0
fetched_at: '2026-06-29T00:05:52.170671+00:00'
page_id: '1058177208'
product: rm
source: tdn-rm
title: TOTVS Construção Gestão de Imóveis - WhatsApp - byWorknow
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1058177208
version: 11
---

Importante

* Será necessária a **contratação do serviço da Worknow** para utilizar a funcionalidade.    
  Entrar em contato com Worknow - <https://worknow.com.br/contato/>  
  Após contratar os serviços de whatsapp juntamente com a worknow você deverá configurar seu ambiente TOTVS para que apareça as funcionalidades Worknow no menu superior do TCGI, assim você conseguirá imputar as informações de servidor onde será enviado as mensagens do whatsapp, numero utilizado para envio como outros dados necessários no processo.
* Conforme Regra de Negócio, o templates sempre devem ser cadastrados para a coligada 1, que é a coligada centralizadora e para a filial 1.

---

Após a contratação deste serviço, no TCGI é preciso acessar o botão executar, no painel às direita da tela, digitar worknow e executar a opção Atualizar Integrações by Worknow:

Na tela que se abre, selecione a opção WorkChat e execute para que esta integração fique ativa:

**Após a execução da ação acima é preciso:**

* Apagar o arquivo \_Broker.DAT, da pasta C:\TOTVS\CorporeRM\RM.Net de onde o sistema está instalado; e
* Parar e reiniciar o HOST, para que as novas bibliotecas desta integração seja mapeadas no novo arquivo \_Broker.DAT que será criado.

Após as ações acima, ao acessar o TCGI, o sistema exibirá a aba *by Worknow*, sendo necessário dar permissão de acesso ao menu 11 - by Worknow, no perfil do usuário:

Na aba *by Worknow*, acesse a opção Parâmetros WorkChat, ative a integração e insira as informações fornecidas pela Worknow:

Após testar a conexão e validar o telefone de envio, verifique com aquela equipe como criar os templates necessários às suas operações e para importá-los utilize o botão sincronizar templates, da aba de mesmo nome, da janela acima:

No TCGI você possui alguns processos que podem utilizar o whatsapp, após ser contratado o serviço, você poderá configurar os processos descritos abaixo:  
  
**1 -**   
**2 -   
3 - [Atendimento - WhatsApp](https://tdn.totvs.com/display/LRM/Novo+Atendimento+-+Cadastros+-+Tipo+Atendimento+TCGI#:~:text=WhatsApp%20%2D%20O%20Tipo%20de%20Atendimento)**
