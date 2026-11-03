---
content_hash: 99ef66a2eafc8a156086b9f8b9392225c8ca340b118f8dba9a6932ae496cceef
fetched_at: '2026-06-29T00:11:13.351059+00:00'
page_id: '659592652'
product: rm
source: tdn-rm
title: Como gerar a tag <tpInsc> com valor "3-CAEPF" para situações onde existe mais
  de um CAEPF para o mesmo CPF?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=659592652
version: 8
---

false

**A partir das Versões:**

* 12.1.31.292
* 12.1.32.239
* 12.1.33.173
* E Superiores

# Objetivo:

---

Apresentar como o produto deve ser parametrizado para a correta geração da tag <tpInsc> no evento S-1005, quando existe mais de um CAEPF cadastrado para o mesmo CPF.

---

1true2ExemploExemplo

1) Menu RH | Folha de Pagamento | Configurações | eSocial | Configurações Gerais | Configurações Gerais 2/7

Marque o parâmetro "Utiliza quebra de CAEPF" e configure a máscara de quebra que será considerada para a geração do estabelecimento.

Deverá ser a mesma do "Código de quebra para CNPJ".

 

2) Menu Cadastros | Seções

Após realizar a configuração do item acima, será permitido cadastrar seções (nível de quebra de CNPJ/CPF) informando o mesmo CPF porém com CAEPF diferente.

3) Menu eSocial | Geração do XML

Na geração do xml do evento S-1005 serão gerados dois estabelecimentos, sendo um para cada CAEFP.

Na geração do xml do evento S-1200 será informado o CAEPF conforme alocação do funcionário.

## 

##
