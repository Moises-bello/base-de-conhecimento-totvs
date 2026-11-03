---
content_hash: 3e1826c4b5dae1cc0a95fc95558eaf60b8b5376d34f4479e418306e4f389216f
fetched_at: '2026-06-29T00:10:15.343611+00:00'
page_id: '464955038'
product: rm
source: tdn-rm
title: CNO
type: documentation
url: https://tdn.totvs.com/display/LRM/CNO
version: 6
---

# Objetivo:

---

O campo CEI existente no cadastro do cliente fornecedor é considerado nos eventos S-1005, S-1020, S-2299, S-2399 e S-1200

---

O Cadastro Nacional de Obras (CNO) foi instituído pela Instrução Normativa RFB 1.845 de 22 de novembro de 2018 para substituir o Cadastro Específico do INSS – CEI, conhecido como Matrícula CEI de Obras. Trata-se de um banco de dados que contém informações cadastrais de obras de construção civil e de seus responsáveis, pessoas físicas ou jurídicas.

As obras anteriormente obrigadas à inscrição no CEI/6 (obras de pessoas físicas) e no CEI/7 (obras de pessoas jurídicas) passaram a ser cadastradas no CNO.  
As obras anteriormente obrigadas à inscrição no CEI/6 (obras de pessoas físicas) e no CEI/7 (obras de pessoas jurídicas) passaram a ser cadastradas no CNO.

Obrigatoriedade de inscrição:  
Estão obrigadas à inscrição no CNO as obras de construção civil, sendo responsáveis por seu cadastramento:  
I – O proprietário do imóvel, dono da obra ou o incorporador de construção civil, pessoa física ou pessoa jurídica, inclusive o representante de nome coletivo;  
II – A pessoa jurídica construtora, quando contratada para execução de obra por empreitada total;  
III – A sociedade líder do consórcio, no caso de contrato para execução de obra de construção civil mediante empreitada total celebrado em nome das empresas consorciadas;  
IV – O consórcio, no caso de contrato para execução de obra de construção civil mediante empreitada total celebrado em seu nome.

Veja em qual situação se encontra a sua obra:

* A obra de construção civil que possui matrícula CEI:  
  A matrícula CEI deve ser migrada para o CNO a partir de 21 de janeiro de 2019. O número de inscrição no CNO permanece o mesmo número do CEI.   
  Desse modo, é possível saber que a inscrição no CNO é relativa à atividade anteriormente matriculada no CEI;

* A obra de construção civil que NÃO possui matrícula CEI:  
  A obra deve ser inscrita no CNO e o número gerado deve ser utilizado para o cumprimento das obrigações perante a Receita Federal do Brasil.

O campo CEI está disponível no anexo do cadastro do cliente fornecedor:

**Observação**: Para que o cadastro do cliente fornecedor fique visível no TOTVS Folha de Pagamento é necessário marcar o parâmetro "Utiliza tomadores de serviço" disponível no parametrizador:

No cadastro do cliente fornecedor, ao incluir ou alterar o campo CEI, será disparado um gatilho (inclusão ou alteração) para o evento S-1005 quando o campo "Obra Própria" estiver marcado:

No cadastro de lotação tributária, ao incluir ou alterar o campo CEI será disparado um gatilho (inclusão ou alteração) para o evento S-1020:

**S-1020**

Quando o funcionário estiver alocado na lotação tributária com CEI informado, o evento S-1200 será gerado conforme abaixo:

**S-1200**

falsefalsefalsefalse

**Produto:** Folha de Pagamento

false

**Rotina:** eSocial

false

**Versões:**

|  |
| --- |
| 12.1.23 |
| 12.1.22 |
| 12.1.21 |

**Status:** Finalizado

false

**Data:**

false

****Autor:****
