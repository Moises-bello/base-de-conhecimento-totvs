---
content_hash: 798e8e532e739d5def0370e2559f007bb60a5c9228184aa2f99cdad026024826
fetched_at: '2026-06-29T00:05:54.257294+00:00'
page_id: '1077463479'
product: rm
source: tdn-rm
title: PI - Integração - RD Station - Aplicativos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1077463479
version: 2
---

**Cadastros de tipos de Aplicativos no RDStation para integração com o Portal de Imóveis:**

### **Integração com o Marketing:**

---

Para que este procedimento seja realizado é necessário uma conta do RD Station:  <https://accounts.rdstation.com.br/>

* Informe o usuário de acesso a sua conta;
* Login \ Senha:
* Clique em Acessar: Acessar RM Station Marketing

* Acesse a conta na app store do RD Station onde vocÊ será direcionado para este site: <https://appstore.rdstation.com/>

* Clique em Acesse sua conta:

* Insira suas credenciais de acesso:

* Selecione a opção: Meus Apps (Para visualizar os Apps já existentes) ou Quero Criar um aplicativo (para inclusão de um novo aplicativo);

* Informe o nome do aplicativo que deseja criar, e selecione a opção: **Aplicativo Privado**

Informe os dados do APP nos campos:   
***Nome do aplicativo (informe um nome que você dará ao seu app criado);***  
***Categoria: Selecione Marketing;***  
***Idiomas do Aplicativo: (informe o idioma de preferencia que você utilizará);***  
***Site da empresa: (informe o site da sua empresa;***  
***URLs de Callback:*** ***(abaixo iremos instruir como criar o código para utilização); Após a geração da URL (Basta inserir o Cod neste campo e salvar as informações da tela)***

URL de Callback

**Criando uma URL de Callback:**

---

Para criar uma URL de Callback acesse o Portal de Imóveis > Backend > Integração > Adicionar , neste momento será gerado uma URL de Callback (neste momento a mesma será copiada para a área de transferência e deverá ser incluída no campo URLs de Calback (no RD Station) no momento da inclusão do Aplicativo.

Ainda na tela de integração, é possível clicar no botão URL Callback (Copiar URL), onde a mesma também poderá ser copiada.

* Neste momento será apresentada a tela onde foi criado os códigos do: Client\_ID e Client\_Secret.  
  Copie o código Client\_ID e em seguida retorne ao Portal de Imóveis no menu de Integração, clique no botão Editar deste aplicativo que está sendo configurado onde será apresentada a tela com os dados a serem preenchidos.  
  Cole o código no campo Client\_ID e em seguida retorne ao RD Station e desta vez copie o código Client\_Secret que deverá ser colado no campo Client\_Secret no Portal de Imóveis.
* Realizado estes passos, clique em salvar.

* ***Veja no menu integração > Aplicativos do Portal de Imóveis onde (ao clicar em Editar) os códigos que anteriormente foram copiados do site do RD Station serão colados respectivamentes;***

  
  

* Cole o código no campo Client\_ID e Client\_Secret (em seguida clique em salvar)

  

**Gerando o CODE de autorização.**

---

Neste momento será necessário gerar um código de autorização. Para realizar esta parametrização, acesse o Portal de Imóveis > Backend > Integração > (no Aplicativo que será configurado) ao final da linha > Clique em Editar > Gerar código no RD , esta ação irá redirecionar para o site do RD Station onde deverá ser selecionado o site que terá o acesso permitido (clique em continuar e na outra tela exibida: conectar), instantaneamente o CODE será gerado no Portal de imóveis para aquele aplicativo.

Com este conjunto de informações, é possível validar se a integração está validada ao clicar no botão Testar Integração.

Ao clicar neste botão será integrado e apresentado na tela estas informações.

Este processo possibilitará realizar chamadas das APIs no RD Station.  
  
Link documentação de criação do appstore   
para configurar no PI:  
<https://developers.rdstation.com/reference/criar-aplicativo-appstore>

**Integração com o CRM:**

---

* Este tópico ensina como criar os parametros da integração com CRM no RD Station e gerar o Token para integração.   
  Para geração do Token acesse as instruções no link:   
  <https://ajuda.rdstation.com/s/article/Gerar-e-visualizar-Token?language=pt_BR>   
    
  ***Observação:** Importante lembrar que após o Token gerado (se em algum momento) o usuário clicar em desativar Token (esta chave será excluída) sendo necessário gerar uma nova chave que deverá ser informada novamente no portal de imóveis.*
* Acesse o Portal de imóveis e acesse o menu: Backend > Integração > RD Station >Aplicativos, clique em ***Adicionar*** e em seguida Selecione CRM.
* Informe o token e em seguida clique em salvar.

**Importante: Evolução na Integração CRM (A partir da versão 12.1.2606)**

Se você utiliza o Portal de Imóveis na versão 12.1.2606 ou superior, a integração com o RD Station CRM evoluiu! A autenticação agora é feita de forma simplificada, utilizando o mesmo padrão de segurança do RD Station Marketing, via App Store.

Como configurar na nova versão: O processo é idêntico ao do Marketing. Basta acessar Integração > Aplicativos, selecionar a categoria "CRM" e preencher o Client ID e Client Secret gerados no seu aplicativo privado da RD.
