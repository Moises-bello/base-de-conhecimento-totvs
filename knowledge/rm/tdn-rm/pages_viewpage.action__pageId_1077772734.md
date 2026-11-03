---
content_hash: 604393e5839f425ab88fcfe3e056cb7fc09676bf0b3261f9369fa89ffacc4399
fetched_at: '2026-06-29T00:05:54.265290+00:00'
page_id: '1077772734'
product: rm
source: tdn-rm
title: PI - Integração - RD Station - Inclusão de Leads
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1077772734
version: 5
---

### **Introdução:**

---

Nesta seção iremos visualizar a atualização de um Lead após uma venda ser enviada para o backoffice.

Observações:

Como Pré- Requisito, é necessário realizar a integração do Portal de imóveis com o RD Station para que os dados gerados sejam integrados:  
  
**Saiba mais acessando o link abaixo:**  
[RD Station - Token WebHook - Cadastro de Leads enviados pelo RD](https://tdn.totvs.com/pages/viewpage.action?pageId=687737814#RDSTATION-1513287362)

---

**Procedimentos para utilização:**

---

Para que este procedimento seja realizado é necessário acessar o RD Station incluído um Lead. Ao acessar esta tela observe alguns campos relevantes:

* **Nome do Lead**;
* **Cargo;**
* **Estágio do Funil;**
* **Dono do Lead**: Este campo, ao ser preenchido, irá registrar o nome do corretor no Portal de Imóveis. É importante observar que, para que o nome do corretor seja preenchido corretamente no momento da integração, ele deve já estar cadastrado no Portal de Imóveis com este mesmo e-mail informado no campo.  
  Em seguida marque a opção:  observando que a mesma estará sendo apresentada como a imagem abaixo:

Ao acessar o portal de imóveis observe que o cadastro já estará apresentando o registro integrado:

No portal de imóveis, a alteração da situação do lead para **'Banco'** atualiza os dados no RD Station e **desmarca a opção de oportunidade**. Caso o lead volte a manifestar interesse, será necessário marcar a oportunidade novamente de forma manual.

**OBS:** Ao cadastrar leads no RD Station, informe o número de celular no campo “Celular” com o formato: 55 (31) 99999-9999
