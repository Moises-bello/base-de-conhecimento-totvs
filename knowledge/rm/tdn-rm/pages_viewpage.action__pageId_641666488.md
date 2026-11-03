---
content_hash: 0fd0411029cab0d8f4105fbb7d01bf4c461f5699e794d0721356bb1f813dd094
fetched_at: '2026-06-29T00:11:10.150898+00:00'
page_id: '641666488'
product: rm
source: tdn-rm
title: S-2410 - Cadastro de Benefício - Entes Públicos - Início
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=641666488
version: 14
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

"São as informações relativas ao cadastro dos benefícios do sistema de previdência dos regimes próprios, incluindo os de complementações de benefícios do RGPS, reserva, reforma e pensões de militares e aposentadorias e pensões dos parlamentares, bem como os benefícios de natureza não previdenciária, incluindo pensões graciosas, a cargo de entes da administração pública direta ou  
indireta, e suas subsidiárias."

No MOS são apresentadas informações adicionais sobre este leiaute, com regras, orientações e definições que precisam ser considerados nos processos das empresas.

Estas informações adicionais estão disponíveis no [portal oficial do eSocial](https://www.gov.br/esocial). Recomendamos acessar a página de documentação técnica no site do eSocial e fazer o download da versão mais atual do MOS e buscar pelas informações adicionais deste leiaute.

### Quem está obrigado

Todos os entes da administração pública direta ou indireta e suas subsidiárias que administrem benefícios, previdenciários ou não, constantes na "Tabela 25 – Tipos de Benefícios" do eSocial.

---

13-1Cadastro do benefícioCadastro do benefício

Para cadastrar o benefício no produto, é necessário:

1) Acessar o menu RH | Folha de Pagamento | Administração de Pessoal | Funcionários | Registro

**ATENÇÃO:**

* O campo "**Matrícula****Benefício**" deverá ser igual a matrícula do servidor/militar (campo **Matrícula eSocial**) constante na base do TOTVS Folha de Pagamento do órgão cujo vínculo deu ensejo ao benefício. No caso de pensão por morte, informar a matrícula do instituidor da pensão.
* Em caso onde o benefício é não oriundo de um vínculo laboral e/ou bem como os concedidos antes da obrigatoriedade dos eventos não periódicos, o cadastro desse campo fica opcional.
* No caso dos benefícios concedidos por órgão diverso do declarante do vínculo laboral, o cadastro desse campo não possui uma  mascara pre determinada.

2) Acessar o menu RH | Folha de Pagamento | Administração de Pessoal | Funcionários | Anexos | Folha de Pagamento | Dados do Benefício

Clique em  incluir e cadastre os dados do benefício.

**ATENÇÃO:**

* Este cadastro só será habilitado caso o funcionário esteja com o parâmetro "Beneficiário Entes Públicos" marcado ou o tipo de funcionário for "W-Beneficiário".
* O campo **"Dependência do instituidor da pensão"** é obrigatório se o campo "Tipo de dependente do instituidor da pensão" for do tipo: **Agregados/Outros (99)**
* O campo **"Data da homologação do benefício pelo Tribunal de Contas"** é obrigatório se o campo "Homologação pelo Tribunal de Contas" for do tipo: Homologado (1)

3) Após Salvar os dados será gerado o gatilho com evento S-2410.

3-2Carga InicialCarga Inicial

De acordo com o Manual de Orientações do eSocial (MOS):

"Os órgãos públicos, responsáveis pelo pagamento de benefícios devem utilizar este evento para a carga inicial da base de todos os benefícios existentes na data do início da obrigatoriedade dos eventos não periódicos, tipificados na “Tabela 25 – Tipos de Benefícios” do eSocial, bem como para os benefícios concedidos a partir de então."

Acessar o menu RH | Folha de Pagamento | eSocial | Gerar Gatilhos Eventos Iniciais

Deverá selecionar a "2a. Fase" e selecionar o evento "S-2410".

**ATENÇÃO:**

Para gerar o gatilho com status carga inicial o sistema irá verificar se a data de inicio do cadastro do beneficiário existente na aba informações do beneficiário é menor que a data preenchida no Parametrizador, campo "Não Periódicos", ou caso o campo "Economia Mista" esteja marcado, o sistema irá considerar a data do campo "Não Periódicos" da economia mista.
