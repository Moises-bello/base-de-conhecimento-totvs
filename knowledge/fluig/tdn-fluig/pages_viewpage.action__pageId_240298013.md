---
content_hash: d5e848ce620f6c0cdfc4ef6b5c397ed3b9497e5910784fb2153886ae21a61cf0
fetched_at: '2026-06-28T21:35:22.803548+00:00'
page_id: '240298013'
product: fluig
source: tdn-fluig
title: BPM 045 - Como personalizar um campo Identificador de uma solicitação?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=240298013
version: 8
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**fluig

**Versão:** todas

# Ocorrência

Desejamos colocar um campo do formulário visível na lista de solicitações para facilitar a identificação da solicitação.

**Campo Identificador**

# Solução

É possível personalizar a informação que aparecerá na coluna Identificador da solicitação de três formas:

0.5falsesamplesfadetrue1Passo 1  

* Acesse o menu **Processos → Configurar Processos**;

* Selecione o processo que deseja editar, clique em **Editar**;

* Após aberto o fluxo clique em **Formulário** no canto esquerdo superior;

* Clique sobre **Configurações do formulário** para expandir;

* No campo **Descrição Principal dos Registros** selecione o campo do formulário que será apresentado na coluna Identificador;

* Salve as alterações;

* Para alterar a descrição das solicitações já abertas, veja o **Passo 2**.

**Figura 1: Campo Descrição Principal dos Registros**

2Passo 2

* Localize o formulário do processo na Navegação de Documentos (menu Documentos) do fluig e acesse as **Propriedades** deste formulário;

* Na aba **Descrição Principal dos Registros de Formulário** desmarque a opção **Utilizar descrição padrão** para que seja possível selecionar o campo do formulário que será o campo descritor no bloco abaixo;

* Marque a opção **Alterar descrição em TODOS os registros de formulário ativos** para que todas as solicitações já abertas assumam este mesmo campo como Identificador;

* Confirme as alterações;

3Passo 3

* No fluig Studio, durante a exportação do formulário do processo, preencha no **Campo Descritor** o campo do formulário que será utilizado como Identificador;

* Para alterar o campo Identificador de todas as solicitações abertas verifique o **Passo 2**.
