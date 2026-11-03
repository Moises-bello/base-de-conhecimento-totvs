---
content_hash: c8082fb1b1c3dbddbd539a255a2cc047ca740c07ad9b469816c09fd07d3634f4
fetched_at: '2026-06-29T00:11:10.106571+00:00'
page_id: '641446580'
product: rm
source: tdn-rm
title: S-2405 - Cadastro de Beneficiário - Entes Públicos - Alteração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=641446580
version: 9
---

false

**A partir das Versões:**

* 12.1.31.261
* 12.1.32.206
* 12.1.33.128
* e Superiores.

# Objetivo:

---

Apresentar a parametrização e geração do evento .

De acordo com o Manual de Orientações do eSocial (MOS):

"É o registro das alterações de dados cadastrais dos beneficiários, tais como: endereço, estado civil, contato. O evento deve ser informado sempre que ocorrerem mudanças nos dados informados relativos aos beneficiários, exceto CPF."

No MOS são apresentadas informações adicionais sobre este leiaute, com regras, orientações e definições que precisam ser considerados nos processos das empresas.

Estas informações adicionais estão disponíveis no [portal oficial do eSocial](https://www.gov.br/esocial). Recomendamos acessar a página de documentação técnica no site do eSocial e fazer o download da versão mais atual do MOS e buscar pelas informações adicionais deste leiaute.

### Quem está obrigado

Todo órgão público cujo beneficiário informado por meio do evento S-2400 apresente alteração dos dados cadastrais informados

---

13-1Campo "Beneficiário Entes Públicos"Campo "Beneficiário Entes Públicos"

Sempre que for realizada alteração dos dados do beneficiário  (dados pessoais, dados da aba Informações do beneficiário), que são considerados no leiaute do evento S-2405, o sistema irá gerar um gatilho.

1) Serão observados os campos dos dados pessoais e os campos abaixo existentes no menu RH | Folha de Pagamento | Administração de Pessoal | Funcionários 

2) Após Salvar a edição será gerado o gatilho com evento S-2405.

3-2Tipo de Funcionário WTipo de Funcionário W

Sempre que for realizada alteração dos dados do beneficiário  (dados pessoais, dados da aba Informações do beneficiário), que são considerados no leiaute do evento S-2405, o sistema irá gerar um gatilho.

1) Serão observados os campos dos dados pessoais e os campos abaixo existentes no menu RH | Folha de Pagamento | Administração de Pessoal | Funcionários 

2) Após Salvar a edição será gerado o gatilho com evento S-2405.
