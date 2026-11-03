---
content_hash: 120b254084795789c8c8dd06dfae6cb3af38c9f9115b91f3d2cdd0befd4b12d7
fetched_at: '2026-06-29T00:05:59.461542+00:00'
page_id: '190520246'
product: rm
source: tdn-rm
title: Configuração do Host para Geração de Planilhas em Lote
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=190520246
version: 40
---

# Índice:

---

.\*ndice:

# Introdução

---

          A configuração de Logon no serviço RM.Host.Service é necessária somente nos casos em que ao gerar a Planilha em Lote seja exibida uma mensagem de aviso. Nesta será informada um link de auxilio da configuração indicada.

false

 *Somente planilhas do **tipo Excel** são utilizadas neste processo. Além disso, o servidor que estiver executando job do processo deve possuir o **Excel instalado**.*

# Passo a passo:

---

    

falseDeckPasso 1

          Abra o RM.Host.ServiceManager.exe e selecione a opção ‘Informa usuário e senha específicos’. Preencha os três campos que serão habilitados:

* Usuário: usuário de rede;
* Senha: senha de rede;
* Domínio: domínio da rede.

**Observações:**

* Caso esteja utilizando o RM em ambiente 3 camadas, esta operação deverá ser realizada apenas no lado Server;
* Em eventual atualização da Biblioteca RM, todo o processo de Configuração do Host para Geração de Planilhas em Lote deverá ser realizado novamente.

Passo 2

          Após preencher os campos necessários clique em Instalar. Aguarde um instante e o serviço do host será inicializado.

Observação Complementar

**Caso a mensagem de aviso com referência à esta página persista após realização da configuração de utilização do RM.Host.ServiceManager.exe, as configurações abaixo devem ser realizadas.**

**Via terminal e com acesso de administrador, verifique se existe uma pasta chamada Desktop dentro de cada um dos seguintes diretórios:**

* **C:\Windows\SysWOW64\config\systemprofile\**
* **C:\Windows\System32\config\systemprofile\**

**Caso não exista, deve-se criar a pasta Desktop dentro dos dois diretórios citados.**

**Depois de efetuada as alterações reinicie o computador e repita a operação de Geração de Planilhas em Lote.**

false

*Para que o processo e configurações tenham sucesso torna-se necessário que o office esteja registrado.*

*Configurações de “Segurança GPO” podem bloquear a criação das pastas nos respectivos diretórios. Para maiores informações procure o departamento de TI da empresa.*

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.XX

false

**Processo:** Geração de Planilhas em Lote

falsefalse

**Status:** Finalizado

false

**Data: 09/07/2018**

false

**Autores:**
