---
content_hash: 4471580e1f4e87c1b0f89c8896e98d8513e9556ddfbd96e2fb4f6a7a9300a2b9
fetched_at: '2026-06-29T00:11:22.440334+00:00'
page_id: '704916146'
product: rm
source: tdn-rm
title: Nota Técnica nº 06/2022 - Leiaute S-1.0
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=704916146
version: 65
---

false

**A partir dos patches:**

* 12.1.34.232
* 12.1.2205.175
* 12.1.2209.117
* e Superiores

## Objetivo:

Em 09/08/2022 foi disponibilizado pelo eSocial a [NOTA TÉCNICA S-1.0 Nº 06/2022](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/nota-tecnica-s-1-0-06-2022.pdf), apontando ajustes no Layout S-1.0.

Seguem orientações referente ao produto TOTVS Folha de Pagamento, para atender essa alteração:

11AtualizadorAtualizador

Após a liberação da versão será necessário executar os script's de adequação das tabelas e campos do sistema através do sistema **RM.Atualizador.exe.**

true2ParametrizadorParametrizador

1) Disponibilizado no parametrizador o leiaute atendendo a NT 06/2022.

1S-1010S-1010

1) Tabela "21 - Códigos de Incidência Tributária da Rubrica para o IRRF", alterada a descrição dos valores [9046, 9047, 9048].

Estas descrições foram ajustadas no menuCadastros | Eventos | Aba Incidências 

2) No menuCadastros | Eventos | Aba Incidências | Campo Contribuições RPPS/Regime Militar, foi disponibilizado o código: "92 - Suspensão de incidência em decorrência de decisão judicial - 13º salário" .

   Exemplo da geração do XML do evento "S-1010 - Rubricas":

true2 S-2210Alterações

1) Incluída a tag **<ultDiaTrab>** no grupo <cat>.

Descrição: Último dia trabalhado. Validação: Preenchimento obrigatório se dtAcid >=[2023-01-16]). Se informada, deve ser uma data igual ou anterior à data atual e igual ou posterior à data de admissão do trabalhador. Se tpCat = [2], deve ser informada data posterior à data preenchida no evento de CAT anterior, quando informada em nrRecCatOrig. 

O sistema irá utilizar o campo "Ultimo dia trabalho" preenchido na CAT para preenchimento da tag <ultDiaTrab>.

2) Incluída a tag **<houveAfast>** no grupo <cat>

Houve afastamento?  
Valores válidos:  
S - Sim  
N - Não  
Validação: Preenchimento obrigatório se dtAcid >= [2023-01-16]).

O sistema irá utilizar o campo "Houve Afastamento" preenchido na CAT para preenchimento da tag <houveAfast>

Exemplo da CAT:

 Exemplo da geração do XML do evento "S-2210 - Comunicação de Acidente de Trabalho"

true2 S-2240Alterações

  1) Alterações no evento "S-2240 - Condições Ambientais do Trabalho - Agentes Nocivos"

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Grupos {EPI }: retirado o campo <dscEPI>da chave | Descrição do EPI.  Validação: Preenchimento obrigatório e exclusivo se {docAval} não for informado. | Descrição do EPI |
| Grupos {agNoc}: alteração tamanho campo <dscAgNoc> | 1-999 | 1-100 |
| Grupos {epi}: Alterada a ocorrência do campo <docAval> | 0-1 | 1 |

2) Exemplo da geração do XML do evento:

3) Tabela "24 - Agentes Nocivos e Atividades - Aposentadoria Especial", alterada descrição do código [01.19.035]

| De | Para |
| --- | --- |
| Estilbenzeno | Estilbenzeno (etilbenzeno) |

true2 S-2299Alterações

No menu Parametrizador | eSocial | De/Para Desligamento foi incluído o motivo "44 - Agrupamento contratual"
