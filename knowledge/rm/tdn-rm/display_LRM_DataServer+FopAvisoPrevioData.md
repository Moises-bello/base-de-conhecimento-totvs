---
content_hash: e5db445cad900f21c0106f5ba4c72f6d5f8f9befb0ac702d8b67c2b70308131a
fetched_at: '2026-06-29T00:12:16.211043+00:00'
page_id: '982919495'
product: rm
source: tdn-rm
title: DataServer FopAvisoPrevioData
type: documentation
url: https://tdn.totvs.com/display/LRM/DataServer+FopAvisoPrevioData
version: 2
---

O dataserver FopAvisoPrevioData é utilizado para o gerenciamento das informações relacionadas ao Aviso Prévio no módulo de Folha de Pagamento.  
Possibilita a integração / atualização de registros referentes a rescisões e avisos prévios de colaboradores, respeitando as regras de negócio.

### Tag DTAVISOPREVIOTRAB

* Descrição: Data de início do Aviso Prévio.
* Regra de Validação: A data informada deve estar dentro da competência vigente da Folha de Pagamento.

Dica: 

Foi identificado em testes:

Quando a data informada está fora do intervalo válido, ocorre a mensagem: "Estouro de SqlDateTime. Deve estar entre 1/1/1753 12:00:00 AM e 31/12/9999 11:59:59 PM"

### Tag RESCISAOCALCULADA

* Descrição: Indicador de cálculo da rescisão.
* Valores aceitos:

+ TRUE → ativa o cálculo da rescisão.
+ FALSE → mantém sem cálculo automático.

Dica: 

Foi identificado em testes:

Ao informar TRUE, quando existir rescisão cadastrada, é exibida a mensagem de que a rescisão já está cadastrada, impossibilitando duplicidade de cálculo.

### Tag CARREGOUAVISOPREVIO

* Descrição: Indica se o aviso prévio já foi carregado no sistema.
* Valores aceitos:

+ TRUE → o aviso já foi carregado.
+ FALSE → o aviso não foi carregado.

Dica: 

Foi identificado em testes:

Ao informar TRUE, quando existir rescisão cadastrada, pode ocorrer a mensagem informando que a rescisão já está cadastrada.

### Mensagens Conhecidas

* Estouro de SqlDateTime

* + Ocorre quando a data informada em DTAVISOPREVIOTRAB não está dentro da competência da Folha de Pagamento.
  + Intervalo aceito: 01/01/1753 00:00:00 até 31/12/9999 23:59:59.
* Rescisão já cadastrada  
  + Apresentada quando o sistema identifica que já existe um aviso/rescisão previamente registrado, principalmente ao utilizar os parâmetros RESCISAOCALCULADA = TRUE e/ou CARREGOUAVISOPREVIO = TRUE.

Observações Importantes:

* Recomenda-se validar previamente as datas antes de enviar ao dataserver, garantindo que DTAVISOPREVIOTRAB esteja compatível com a competência da folha.
* Para evitar inconsistências, recomenda-se verificar no banco de dados (PFUNC) se já existe rescisão cadastrada antes de setar RESCISAOCALCULADA e CARREGOUAVISOPREVIO como TRUE.
* Todas as tags devem ser respeitadas conforme as regras de negócio da Folha de Pagamento.
