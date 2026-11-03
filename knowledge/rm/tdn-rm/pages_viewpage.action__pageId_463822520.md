---
content_hash: f3f208cddb67e43b508540422cf677ddec2b31b21f43a5d16ea2f6e8b7a74f8e
fetched_at: '2026-06-29T00:10:15.262453+00:00'
page_id: '463822520'
product: rm
source: tdn-rm
title: Consulta pública de diplomas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=463822520
version: 18
---

## **Visão geral**

Seguindo a portaria Nº 1.095, DE 25 DE OUTUBRO DE 2018 do MEC, foi disponibilizado uma funcionalidade no portal do aluno para permitir a consulta pública de diplomas.

Através da URL http://<endereço do site>:<porta do site>/[web/app/Edu/PortalEducacional/js/aluno/diploma/](http://localhost:8080/web_src/app/Edu/PortalEducacional/js/aluno/diploma/) é possível o aluno realizar a consulta do seu diploma através dos seguintes filtros:

* Nome
* CPF
* Número de registro do diploma
* Número do processo do diploma

Para isso, a opção "Exibe diploma na web" precisa estar marcada na aba "Diploma" no cadastro da habilitação do aluno e o campo "Curso do MEC" dentro da matriz aplicada deve estar informado.

Os dados exibidos após a consulta, caso seja encontrado algum resultado são:

* **Nome do aluno diplomado:**  
  Essa informação é relativa ao nome do aluno, no cadastro do aluno.
* **Seis dígitos centrais do CPF do aluno diplomado:**  
  Essa informação é relativa ao CPF do aluno, sendo apresentado com os seis dígitos centrais.   
  EX: \*\*\*155721\*\*
* **Nome e código e-MEC do curso superior:**  
  Essas informações são relativas ao nome e código do e-MEC, informado na Matriz Aplicada do aluno/Curso do MEC
* **Nome e código e-MEC da IES expedidora do diploma:**  
  Essas informações são relativas ao nome e código do e-MEC, da instituição de **emissão**, informada no cadastro do [certificado/diploma](https://tdn.totvs.com/pages/viewpage.action?pageId=425459142#M%C3%B3dulodeDiploma%C3%A7%C3%B5es/Certifica%C3%A7%C3%B5es-Emiss%C3%A3omanualdecertificado).
* **Nome e código e-MEC da IES registradora do diploma:**Essas informações são relativas ao nome e código do e-MEC, da instituição de **registro**, informada no cadastro do [certificado/diploma](https://tdn.totvs.com/pages/viewpage.action?pageId=425459142#M%C3%B3dulodeDiploma%C3%A7%C3%B5es/Certifica%C3%A7%C3%B5es-Emiss%C3%A3omanualdecertificado).

* **Data de ingresso no curso:**  
  Essa informação é relativa à data de ingresso informada no anexo do aluno / Curso/habilitação / anexo Ingresso.
* **Data de conclusão do curso:**  
  Essa informação é relativa à data de conclusão de curso informada no anexo do aluno / Curso/habilitação / anexo Diploma.
* **Data da expedição do diploma:**  
  Essa informação é relativa à data de expedição do diploma informada no anexo do aluno / Curso/habilitação / anexo Diploma.
* **Data do registro do diploma:**  
  Essa informação é relativa à data de registro do diploma informada no anexo do aluno / Curso/habilitação / anexo Diploma.
* **Identificação do número da expedição:**  
  Essa informação é relativa ao número do processo de registro do diploma informada no anexo do aluno / Curso/habilitação / anexo Diploma.
* **Identificação do número do registro:**  
  Essa informação é relativa registro de conclusão do diploma informada no anexo do aluno / Curso/habilitação / anexo Diploma.
* **Data de publicação das informações do registro do diploma no DOU:**  
  Essa informação é relativa à data de publicação DOU informada no anexo do aluno / Curso/habilitação / anexo Diploma.

**Importante**: para que a consulta funcione a instituição deve utilizar a funcionalidade de diplomação do TOTVS Educacional.

## **Parametrização**

### Definir base de dados para realizar a consulta

Por padrão, o Alias deafult CorporeRM vem definido no web.config. Para alterar, acessar o passo abaixo.

Após a instalação do portal, acessar o caminho: Local\_de\_Instalação | FrameHTML | Web.Config localizar a tag: <add..key="ServiceAlias" value="CorporeRM" /> e alterar par ao nome desejado.

Configurar também a seguinte chave no arquivo RM.Host.Service.exe.config ou RM.Host.exe.config:

 <add key="**DefaultDB**" value=**"informe\_aqui\_o\_nome\_do\_alias"** />

### Filtros da consulta pública

A instituição de ensino poderá disponibilizar um filtro ou não configurando o arquivo "<Diretório de instalação>\FrameHTML\web\app\Edu\PortalEducacional\js\edu-contantes.global.config.js".

js10true

### reCAPTCHA

Por ser uma consulta pública e para evitar problemas de sobrecarga da aplicação é necessário a utilização do reCAPTCHA.

Acesse o site do Google (<https://www.google.com/recaptcha/>) para registrar o reCAPTCHA.

A chave de site deverá ser preenchida no arquivo  "<Diretório de instalação>\FrameHTML\web\app\Edu\PortalEducacional\js\edu-contantes.global.config.js", parâmetro KEY\_RECAPTCHA;

js10true

Já a chave secreta do reCAPTCHA deverá ser preenchido o parâmetro SECRET\_KEY existente no arquivo Web.config localizado em: "<Diretório de instalação>\FrameHTML\web.config".

js10true]]>Atenção

Caso a Consulta Pública ainda não funcione corretamente após realização dessas configurações, favor revisar as configurações gerais de instalação do Portal em:  <https://tdn.totvs.com/x/X3mPI>.

 Veja Também

---
