---
content_hash: 71569a8c5883747d458da03e7a430f702463aead415fed494bfbfe3255f78f12
fetched_at: '2026-06-29T00:11:16.930689+00:00'
page_id: '673801865'
product: rm
source: tdn-rm
title: Como realizar a geração do evento S-1207?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=673801865
version: 12
---

false

**A partir das Versões:**

* + 12.1.32.285
  + 12.1.33.245
  + 12.1.34.149

---

# Objetivo:

---

O objetivo deste documento é apresentar a geração do evento "S-1207-Benefícios Previdenciários RPPS", utilizado para transmitir ao governo informações referente ao pagamento de benefícios - entes públicos. Sua geração se dá pela rotina de "Gerar XML Eventos Periódicos", onde será identificado todos os beneficiários (S-2400 e S-2410) que atendam algumas condições.

---

11AtualizadorAtualizador

Após a liberação da versão será necessário executar os script's de adequação das tabelas e campos do sistema através do sistema **RM.Atualizador.exe.**

2Parametrização Parametrização 

Para a geração do evento será considerada o funcionário do tipo **W - Beneficiário** ou caso esteja marcado o campo  “**Beneficiário Entes Públicos**”.

Acesse RH | Folha de Pagamento | Administração de Pessoal | Funcionários | Anexos | Folha de Pagamento | Dados do benefício

Cadastre o Número do período para pagamento.

Importante: o cadastro do período não é obrigatorio, caso esteja preenchido será utilizado no lançamento da folha quando o parametro local seja o mesmo indicado no campo, caso contrario será necessário a sua vinculação manual pela ficha financeira.

Mais informações sobre o cadastro do beneficiário e benefício acesse:

3Vinculação do período ao beneficioVinculação do período ao beneficio11MensalMensal

**1)** **Grupo de eventos**

Acesse RH | Folha de Pagamento | Folha mensal | Grupo de eventos

Foi selecionado o período 1 nos parametros locais, conforme vinculado no cadastro dados do benefício.

Após o lançamento, é possivel verificar que o benefício foi vinculado. Acesse RH | Folha de Pagamento | Administração de Pessoal | Funcionários | Ficha Financeira.

**2)** **Lançamento pelo envelope**

Acesse RH | Folha de Pagamento | Administração de Pessoal | Funcionários | Envelope

Foi selecionado o período 1 nos parametros locais, conforme vinculado no cadastro dados do benefício.

Após o lançamento, é possivel verificar que o benefício foi vinculado. Acesse RH | Folha de Pagamento | Administração de Pessoal | Funcionários | Ficha Financeira.

**3) Vinculação manual do benefício (Quando não há vínculo do Número período para pagamento no Dados do benefício ou o lançamento do benefício foi realizado em outro número de período)**

Acesse RH | Folha de Pagamento | Administração de Pessoal | Funcionários | Ficha Financeira

Edite o período

Vá na aba Benefício e vincule o benefíco desejado

213° Salário13° Salário

**1)** **Grupo de eventos**

Acesse RH | Folha de Pagamento | Folha mensal | Grupo de eventos

Foi selecionado um período diferente do campo "Número do período para pagamento" configurado no cadastro do beneficio nos parametros locais.

falseImportante!

Evento correspondente a verba de 13° salário lançada para o beneficiario precisa ter o CC 102, para correto funcionamento da geração do evento S-1207 como anual para o eSocial.

Após o lançamento, é necessário vincular o benefício ao período. Acesse RH | Folha de Pagamento | Administração de Pessoal | Funcionários | Ficha Financeira.

Edite o período correspondente ao 13° salário.

Vá na aba Benefício e vincule o benefíco desejado.

**2)** **Lançamento pelo envelope**

Acesse RH | Folha de Pagamento | Administração de Pessoal | Funcionários | Envelope

Foi selecionado um período diferente do campo "Número do período para pagamento" configurado no cadastro do beneficio nos parametros locais.

falseImportante!

Evento correspondente a verba de 13° salário lançada para o beneficiario precisa ter o CC 102, para correto funcionamento da geração do evento S-1207 como anual para o eSocial.

Após o lançamento, é necessário vincular o benefício ao período. Acesse RH | Folha de Pagamento | Administração de Pessoal | Funcionários | Ficha Financeira.

Edite o período correspondente ao 13° salário.

Vá na aba Benefício e vincule o benefíco desejado.

4Geração do eventoGeração do evento11MensalMensal

Acesse RH | eSocial | Gerar XML

213° Salário13° Salário

Acesse RH | eSocial | Gerar XML
