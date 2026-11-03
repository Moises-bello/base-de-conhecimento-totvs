---
content_hash: 270ddb8bf04274cd6fbe35744d5f83af577898a69034bac7109120f06406ed5a
fetched_at: '2026-06-29T00:11:07.123106+00:00'
page_id: '639197620'
product: rm
source: tdn-rm
title: S-2400 - Cadastro de Beneficiário - Entes Públicos - Início
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=639197620
version: 31
---

false

**A partir das Versões:**

* 12.1.31.261
* 12.1.32.206
* 12.1.33.128
* e Superiores.

# Objetivo:

---

Apresentar a parametrização e geração do evento [S-2400 - Cadastro de Beneficiários – Entes Públicos](https://tdn.totvs.com/pages/viewpage.action?pageId=639193643) no produto.

De acordo com o Manual de Orientações do eSocial (MOS):

"São as informações relativas ao cadastro dos beneficiários do sistema de previdência dos regimes próprios, incluindo os beneficiários das complementações de benefícios do RGPS, reserva, reforma e pensões de militares e aposentadorias e pensões dos parlamentares, bem como os de benefícios de natureza não previdenciária, incluindo pensões graciosas, a cargo de entes da administração pública direta ou indireta e suas subsidiárias."

No MOS são apresentadas informações adicionais sobre este leiaute, com regras, orientações e definições que precisam ser considerados nos processos das empresas.

Estas informações adicionais estão disponíveis no [portal oficial do eSocial](https://www.gov.br/esocial). Recomendamos acessar a página de documentação técnica no site do eSocial e fazer o download da versão mais atual do MOS e buscar pelas informações adicionais deste leiaute.

### Quem está obrigado

Todos os entes da administração pública direta ou indireta e suas subsidiárias que administrem benefícios, previdenciários ou não, constantes na "Tabela 25 – Tipos de Benefícios" do eSocial.

Para o cadastro do beneficiário temos algumas situações mapeadas e que serão detalhadas nas abas abaixo:

---

13-1Campo "Beneficiário Entes Públicos"Campo "Beneficiário Entes Públicos"

Situação em que o funcionário está ativo no produto e recebe algum benefício público.

1) Acessar o menu RH | Folha de Pagamento | Administração de Pessoal | Funcionários e marcar o parâmetro "Beneficiário Entes Públicos" para o sistema habilitar a aba "Informações do beneficiário".

2) Após salvar os dados será gerado o gatilho do evento S-2400 e ao gerar o XML serão geradas as informações abaixo:

3-2Tipo de Funcionário WTipo de Funcionário W

Foi necessário a criação do tipo de funcionário "W-Beneficiário" para que o sistema identifique qual cadastro de funcionário refere-se a um "Beneficiário".

Abaixo iremos descrever alguns exemplos de Beneficiários que identificamos ser necessário cadastrar na folha de pagamento e que deverão ser enviados ao eSocial:

**1a Situação:** Quando existe o funcionário cadastrado no produto somente para receber o benefício, exemplo recebe somente a aposentadoria.

**2a Situação:** Quando existe o funcionário demitido na base, porém esse possui um beneficiário, exemplo quando o funcionário falece e seu dependente (beneficiário) irá continuar recebendo sua remuneração.

**3a Situação:** Quando não existe o funcionário cadastrado no produto porém precisa pagar o benefício ao beneficiário.

Para os casos acima será necessário cadastrar o funcionário com o tipo "W-Beneficiário", para isso deverá:

1) Acessar o menu RH | Folha de Pagamento | Administração de Pessoal | Funcionários e selecionar o tipo de funcionário "W - Beneficiário":

2) Ao selecionar o tipo de funcionário "W - Beneficiário" será habilitada a aba para preenchimento das Informações do beneficiário:

3) Após o preenchimento dos dados será gerado o gatilho e ao gerar o XML as informações serão consideradas no evento S-2400.

3-3Carga InicialCarga Inicial

De acordo com o Manual de Orientações do eSocial (MOS):

"1.1. Os órgãos públicos, responsáveis pelo pagamento de benefícios devem utilizar este evento para o carregamento inicial da base de beneficiários, bem como para os novos beneficiários habilitados a partir do eSocial.  
1.2. No campo {dtInicio} deve ser informada a data em que foi transmitido o cadastro do beneficiário ou a data do início da obrigatoriedade dos eventos não periódicos para o declarante, no caso de benefício concedido antes dessa data."

Acessar o menu RH | Folha de Pagamento | eSocial | Gerar Gatilhos Eventos Iniciais

Deverá selecionar a "2a. Fase" e selecionar o evento "S-2400".

**ATENÇÃO:**

Para gerar o gatilho com status carga inicial o sistema irá verificar se a data de inicio do cadastro do beneficiário existente na aba informações do beneficiário é menor que a data preenchida no Parametrizador, campo "Não Periódicos", ou caso o campo "Economia Mista" esteja marcado, o sistema irá considerar a data do campo "Não Periódicos" da economia mista.
