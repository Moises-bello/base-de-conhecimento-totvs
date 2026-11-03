---
content_hash: 5b59070883b5dda90227897d789e3c550e37b5f75ad1d2a011f177cb915ca09f
fetched_at: '2026-06-29T00:10:22.725831+00:00'
page_id: '498709215'
product: rm
source: tdn-rm
title: Anexo Cliente/For
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=498709215
version: 4
---

false

**A partir da Versão 12.1.25**

# Objetivo:

---

Apresentar o novo anexo eSocial no cliente/fornecedor e  CEI, as informações contidas nesse anexo serão consideradas para geração dos eventos S-1005, S-1020, S-2299, S-2399 e S-1200.

---

1true1Cliente/FornecedorCliente/Fornecedor

As informações relativas ao eSocial, foram agrupadas nesse novo anexo.

**Tomador de serviços folha**

Indica que o Cliente/Fornecedor será lido na carga inicial pelo E-Social, e que a alteração de informações pertinentes ao mesmo, ativarão os gatilhos.

**Obra Própria:**

Marcando este parâmetro será gerado um gatilho de inclusão do evento S-1005, para tomador de serviço do tipo obra própria.  
Os campos CNAE /RAT/FAP/Registro de Ponto  serão habilitados e deverão ser preenchidos.

**Considera dados da Filial**

Selecionando este parâmetro será considerado as informações da filial selecionada.

**Código da Categoria eSocial**

Preencher com o código da categoria do trabalhador conforme tabela 1 do eSocial, caso seja autônomo  a ser enviado ao eSocial. 

**CPF**

É utilizado no eventos Periódicos do eSocial, nas seguinte situações:

* Quando o Cliente/Fornecedor for do tipo pessoa física, produtor rural, do estado de são paulo e no campo CPF/CNPJ estiver preenchido com CNPJ. Evento a ser considerado S-1250 // S-1260
* Quando o Cliente/Fornecedor for do tipo pessoa jurídica e porte empresa MEI e no campo CPF/CNPJ estiver preenchido com CNPJ. Evento a ser considerado S-1200.

**Indicativo da opção pelo produtor rural pela forma de tributação da contribuição previdenciária**

É a forma de tributação da contribuição previdenciária utilizada pelo produtor rural, está informação é utilizada no evento S-1250 - Aquisição de Produção Rural, e somente será habilitado caso o ramo de atividade seja produtor rural.

2CEICEI

As informações relativas ao eSocial do CEI, foram agrupadas nesse novo anexo.

**Considera dados da Filial**

Selecionando este parâmetro será considerado as informações da filial selecionada.

Com este parâmetro desmarcado os campos**CNAE / RAT/ FAP/ Registro de Ponto**  serão habilitados e deverão ser preenchidos.

Para habilitar o campo "Indicativo de Substituição da Contribuição Patronal da Obra de Construção Civil" da guia eSocial é necessário que o registro de Informações do Empregador esteja definido como "Construtora" no campo Indicativo de Construtora.
