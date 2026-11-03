---
content_hash: 93c7685546a665584a457ad02f7ddefc49083f775e125deada40b905baaa305e
fetched_at: '2026-06-29T00:09:49.294578+00:00'
page_id: '435105276'
product: rm
source: tdn-rm
title: Contrato de Locação - Aditivos - Alteração de vigência de contrato de locação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105276
version: 9
---

**Pré-condições**

* **1 -** Ter habilitado a permissão [02.03.01.24 e 25] para Efetivar / Desfazer aditivo de Alteração de vigência de contrato de locação, do perfil do TOTVS Gestão de Imóveis, localizada em *Serviços Globais / Segurança / Perfis.*
* **2 -** Ter efetivado o Contrato de Locação
* **3 -** Ter incluído um Motivo do Aditivo

**Incluindo um Aditivo de alteração de vigência do Contrato de Locação**

* **Passo 1 -** Selecione o Contrato de Locação e acesse: Anexo/Aditivo/Prorrogação do Contrato de Locação.
* **Passo 2 -** Clique em Incluir Aditivo de Prorrogação do Contrato de Locação.
* **Passo 3 -** Preencha os campos:

**Figura 1 - Prorrogação / Antecipação do Contrato de Locação**

* + Código do Aditivo: Campo de preenchimento automático
  + Data do Aditivo
  + Tipo do Aditivo: Campo de preenchimento automático
  + Situação do Aditivo: Preparação
  + Motivo do Aditivo: Informar um Motivo do Aditivo
  + Número do Aditivo no Cliente: Campo onde o cliente informar o número do Aditivo no Contrato físico. Podendo assim realizar o agrupamento de vários aditivos do sistema a um aditivo físico.
  + Em Tipo de Aditivo existem três opções, são elas:
    - Opção 1: **Prorrogação do Contrato de Locação**
    - Opção 2: **Alterar contrato de Locação para prazo indeterminado**
      * **Observação:** Para utilizar esta opção, o parâmetro de aluguel **Parâmetros do TIN | Aluguel | Contrato de Locação | Permite o Contrato de Locação ter prazo indeterminado** precisa estar marcado.
    - Opção 3: **Antecipação do contrato de locação**
      * **Observação: O sistema não irá permitir que o aditivo de antecipação do contrato de locação seja efetivado, caso existam parcelas baixadas em datas maiores ou iguais a data de antecipação.**
  + Data de vigência com prorrogação anterior: Campo de preenchimento automático
  + Nova data de vigência com prorrogação: é habilitado para preenchimento quando o tipo de aditivo é diferente da opção 2 (Alterar contrato de locação para prazo indeterminado).
  + **Passo 4 -** Salvar
* **Passo 5 -**
* **Passo 6 -** Verifique que o status do Aditivo foi alterado para Efetivado.
* **Passo 7 -** Selecione o Aditivo e clique em Editar Aditivo de Prorrogação do Contrato de Locação.
* **Passo 9 -** Acesse a aba Histórico. Será exibida a informação  do campo Observação preenchido ao efetivar o Aditivo
