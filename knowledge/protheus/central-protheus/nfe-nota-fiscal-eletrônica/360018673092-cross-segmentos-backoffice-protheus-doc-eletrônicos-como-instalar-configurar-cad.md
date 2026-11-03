---
article_id: 360018673092
category: NFe - Nota Fiscal Eletrônica
content_hash: ef3731e1e0f739b692982740e3c9dc85b413573de90d47aa6301c48c9fd74a2b
fetched_at: '2026-06-28T22:40:00.092097+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como instalar (
  configurar / cadastrar ) o certificado digital modelo A1
type: support-article
updated_at: '2024-06-18T13:49:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018673092-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-instalar-configurar-cadastrar-o-certificado-digital-modelo-A1
---

**Dúvida**  
Como instalar ( configurar / cadastrar ) o certificado digital modelo A1 ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos  -a partir da versão 12.1.23

**Solução**

Quando ocorre erro na Wizard do TSS com uma mensagem de entidades certificadoras ausentes ou inválidas.  
Isso ocorre pelo motivo do tamanho do certificado digital estar com 3kb, diferente do valor 7 e 8 permitido.  
  
Você deve exportar novamente o certificado no seu navegador. Segue um exemplo:  
  
**Requisitos**

* ​​É recomendado pelas certificadoras o uso do Internet Explorer na exportação do certificado digital. Para passo a passo detalhado em outros navegadores ou sistemas operacionais, consulte a certificadora antes de qualquer ação.
* Possuir certificado digital e-CNPJ modelo A1 válido instalado com permissão para exportação de chave privada. Confira como instalar o certificado com a opção de chave privada.

**Instalando o certificado**  
1. Selecione o local que você deseja instalar o certificado:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24257965187735)  
  
.  
2. Insira a senha e marque as 2**opções de importação** abaixo. Apenas marcando essas opções será possível fazer a exportação do certificado com a chave privada.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24257984867735)  
  
Finalize a instalação do certificado e siga o tutorial de exportação :)  
.  
**Exportando o certificado com chave privada**  
1. No seu Windows no campo de busca digite opções da internet  e clique no ícone.

2. Selecione a aba **conteúdo - > Certificados.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20300776680087)

3. Escolha o certificado digital da sua empresa e clique em exportar.

![4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10809932198295)  
  
5. Marca a opção **Sim, exportar a chave privada**.  
![5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10809919574295)

6. Marque as opções:

* **Incluir todos os certificados no caminho de certificação, se possível**,
* **Exportar todas as propriedades estendidas**
* **Habilitar privacidade de certificados**.

![6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10809940622871)

6. Crie uma **senha** para o certificado e anote. Essa senha será adicionada na plataforma, anote ela para que você possa inserir a mesma na hora do upload do seu certificado;  
![7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10809941656087)

10. Escolha o local e salve o arquivo.  
![8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10810032416919)

11. Clique em **concluir**.  
![9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10810033664535)

12. Finalize confirmando e clicando em **OK**.

**Exportar o Certificado para o Protheus:**  
Na rotina de transmissão de Nota (NFESEFAZ)  
  
Na tela de Bem Vindo, clique em Avançar. Se aparecer a mensagem “Informe a URL do Servidor TOTVS Services”. Informe a URL (IP da máquina onde está instalado o TSS).  
Depois clique em avançar  
  
Se não aparecer a tela de Bem Vindo, após as configurações dos parâmetros para acessar a rotina, vá em Wiz Config.  
  
1. Na tela de Assistente de Configuração de Nota Fiscal Eletrônica, selecione o tipo de certificado com o formato .PFX   
2. Em informe o nome do arquivo do certificado digital, informe o diretório onde você salvou o certificado digital. (O certificado tem que ter o tamanho correto de no mínimo 7kb.)  
3. Em informe a senha do arquivo digital, digite a senha.

**Configuração de E-mail:**  
1. Na tela de Assistente de Configuração de Nota Fiscal Eletrônica, preencha os campos a seguir da seguinte forma:

Servidor SMTP: Informe o endereço do servidor SMTP utilizado. Ex: smtp.suaempresa.com.br  
Login do e-mail: Informe o login do e-mail  
Senha: Informe a senha do e-mail informado no campo anterior.  
Conta de e-mail: Informe a conta do e-mail utilizado (voce@suaempresa.com.br).  
Autenticação: Marque a opção de autenticação, caso seja necessário.  
E-mail de notificação: Informe um e-mail de notificação válido.  
Utilizar conexão segura: Marque a opção caso o servidor exija conexão segura (SSL).

Quando a instalação for concluída, irá aparecer a seguinte mensagem:  
Você concluiu com sucesso a configuração da integração do Protheus para o Totvs Services.
