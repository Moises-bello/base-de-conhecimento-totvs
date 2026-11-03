---
content_hash: 51594ddf81e6432c56d1346d107f00ad75f674fa42aaad7219a4c093ea9a7d71
fetched_at: '2026-06-29T00:05:48.204196+00:00'
page_id: '1024332327'
product: rm
source: tdn-rm
title: Cadastro de Atividades de Evento
type: documentation
url: https://tdn.totvs.com/display/LRM/Cadastro+de+Atividades+de+Evento
version: 10
---

# Conteúdo

2Conteúdonone

# 1. Visão Geral

A tela **Atividades de Evento** tem como objetivo cadastrar e manter as informações relativas às atividades de eventos que envolvem prestação de serviços enquadrados como **Eventos** para fins de **emissão de NFS-e Nacional** (itens indicados com 12).

Este cadastro é utilizado para identificar o evento, seu período de realização e o **local onde a atividade ocorre**, permitindo distinguir corretamente entre **endereço nacional** e **endereço no exterior**, conforme exigido pelo leiaute nacional da NFS-e.

---

# 2. Identificação do Evento

### Campos

* **ID do Evento**  
  Identificador interno do cadastro. Gerado automaticamente pelo sistema.
* **Nome**  
  Nome do evento (artístico, cultural, esportivo, corporativo, entre outros).

  + Campo obrigatório.
  + Corresponde ao campo **xNome** do leiaute da NFS-e Nacional.
* **ID Admin. Tributária Mun.**  
  Código identificador da atividade de evento, conforme definido pela **Administração Tributária Municipal**.

  + Deve ser informado quando exigido pelo município.
  + Corresponde ao campo **idAtvEv**.
* **Data Início**  
  Data de início da atividade do evento.

  + Formato: DD/MM/AAAA.
  + Campo obrigatório.
  + Corresponde ao campo **dtIni**.
* **Data Fim**  
  Data de término da atividade do evento.

  + Deve ser igual ou posterior à Data Início.
  + Corresponde ao campo **dtFim**.

---

# 3. Local da Atividade do Evento

A definição do endereço da atividade do evento depende da marcação da opção **Evento em endereço Nacional**.

### Opção: Evento em endereço Nacional

Esta opção determina quais campos de endereço estarão disponíveis para preenchimento.

---

# 4. Regras de Preenchimento - Endereço Nacional

Quando a opção **Evento em endereço Nacional** estiver **marcada**:

### Campos habilitados

* **Logradouro** (xLgr)  
  Tipo e nome do logradouro do endereço da atividade do evento.
* **Número** (nro)  
  Número do imóvel onde ocorre a atividade.
* **Cidade** (xCidade)  
  Município onde o evento é realizado.
* **Bairro** (xBairro)  
  Bairro do endereço da atividade.
* **Complemento** (xCpl)  
  Informações complementares do endereço, se houver.
* **CEP** (CEP)  
  Código de Endereçamento Postal do endereço nacional.

  + Deve conter apenas números.
  + Tamanho máximo: 8 caracteres.

### Regras

* Os campos referentes a **endereço no exterior** permanecem desabilitados.
* O campo **CEP (Exterior)** não deve ser preenchido.
* O preenchimento segue o padrão de endereço nacional brasileiro.

---

# 5. Regras de Preenchimento - Endereço no Exterior

Quando a opção **Evento em endereço Nacional** estiver **desmarcada**:

### Campos habilitados

* **Logradouro** (xLgr)  
  Tipo e nome do logradouro do endereço da atividade do evento.
* **Número** (nro)  
  Número do imóvel onde ocorre a atividade.
* **Cidade** (xCidade)  
  Município onde o evento é realizado.
* **Bairro** (xBairro)  
  Bairro do endereço da atividade.
* **Código de Endereçamento Postal (Exterior)** (cEndPost)  
  Código postal alfanumérico do endereço no exterior.
  + Campo de texto livre.
* **Estado, província ou região** (xEstProvReg)  
  Estado, província ou região do endereço no exterior.

  + Campo de texto livre.

### Regras

* Os campos de **logradouro, número, bairro, e cidade** permanecem habilitados.
* Não há validação de padrão brasileiro para os campos de endereço no exterior.
* As informações devem refletir fielmente o endereço internacional da atividade do evento.

---

# 6. Regras Gerais

* O cadastro do evento é obrigatório para a emissão de NFS-e Nacional quando o serviço estiver vinculado a atividades de eventos.
* As informações de endereço são utilizadas exclusivamente para identificação do **local da atividade do evento**, e não do tomador ou prestador.
* O sistema controla automaticamente quais campos podem ser editados com base na seleção de **endereço nacional** ou **exterior**, evitando preenchimentos inconsistentes.
