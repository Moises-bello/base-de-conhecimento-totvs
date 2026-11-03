---
content_hash: e1efe159028e04c0aa585bfcd866bbf9ebb012b5861c33bc3843d9353d6e4527
fetched_at: '2026-06-28T21:35:30.371945+00:00'
page_id: '849550372'
product: fluig
source: tdn-fluig
title: Lista de eventos de formulário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=849550372
version: 2
---

# Eventos

---

Os eventos de formulários são um conjunto de scripts carregados pela API de Formulários, os quais são desenvolvidos utilizando Javascript e são chamados durante a execução de ação em formulários ou em momentos específicos de interação em formulários.

## beforeProcessing

---

Esse evento é o primeiro a ser disparado. Exemplificar a utilidade

## displayFields

---

É disparado no momento em que os objetos do formulário são apresentados  e é o permite a alteração antes da renderização.  Pode ser utilizado para esconder um campo ou mesmo para alterar os valores a serem apresentados no campo do formulário. 

## enableFields

---

É disparado no momento em que os objetos do formulário são habilitados e pode ser utilizado para esconder um campo no formulário.

## 

---

É disparado no momento em que os dados do formulário são passados para a camada de negócio responsável por formulário do Fluig e pode ser utilizado para fazer algumas transformações dos valores que são enviados a fim de evitar erros como o formato de data que podem variar conforme o navegador

(...)
