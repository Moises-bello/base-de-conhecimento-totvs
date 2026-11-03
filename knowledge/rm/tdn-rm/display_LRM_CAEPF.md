---
content_hash: 5a9105bcf8e1c1137bc2267edf41562b583b0711e61865cb25d82c323b9f538a
fetched_at: '2026-06-29T00:10:14.394350+00:00'
page_id: '458780869'
product: rm
source: tdn-rm
title: CAEPF
type: documentation
url: https://tdn.totvs.com/display/LRM/CAEPF
version: 22
---

# Objetivo:

---

O campo CAEPF existente no cadastro de seção passa a ser considerado nos eventos S-1005, S-2200, S-2206, S-2299, S-2399 e S-1200

---

Conforme Instrução Normativa RFB Nº 1828, de 10 de Setembro de 2018, "O CAEPF é o cadastro da Secretaria da Receita Federal do Brasil (RFB) com informações das atividades econômicas exercidas pela pessoa física, quando dispensadas de inscrição no Cadastro Nacional da Pessoa Jurídica (CNPJ)".

Ainda como descrito na IN, Art. 23, "no período de 1º de outubro de 2018 a 14 de janeiro de 2019 o Cadastro Específico do INSS (CEI) coexistirá com o CAEPF", ou seja, após o dia **15/01/2019**, a inscrição CAEPF é **obrigatória**.

A estrutura do CAEPF comporta os primeiros 8 (oito) dígitos do CPF, seguido do número de ordem respeitada cada inscrição do CAEPF e complementado pelo número de controle do cadastro conforme imagem abaixo:

O campo CAEPF está disponível no cadastro de seção quando a coligada é identificada por CPF ou CEI :

Ao incluir ou alterar este campo, será disparado um gatilho (inclusão ou alteração) para o evento S-1005:

Ao gerar o evento S-2200 ou S-1200 para funcionário onde a seção centralizadora possua o campo CAEPF preenchido, será exibida conforme abaixo:

**S-1200**

**S-2200**

**OBSERVAÇÃO:**

Os eventos S-2200, S-2206, S-2299, S-2399 ou S-1200 enviados posterior a **15/01/2019**em versões anteriores as citadas acima, deverão ser retificados para atualizar as informações do CAEPF no governo.

**Veja ainda:**

falsefalsefalsefalse

**Produto:** Folha de Pagamento

false

**Rotina:** eSocial

false

**Versões:**

|  |
| --- |
| 12.1.23.131 |
| 12.1.22.199 |
| 12.1.21.220 |

**Status:** Finalizado

false

**Data:**

false

****Autor:****
