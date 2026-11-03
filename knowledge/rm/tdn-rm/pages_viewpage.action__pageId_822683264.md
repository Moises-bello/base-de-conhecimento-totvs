---
content_hash: abf3127f8fe9ddbc44bfb9dfafe266597d0677821d3ce1d47a696cc6dc6419cd
fetched_at: '2026-06-29T00:11:46.452848+00:00'
page_id: '822683264'
product: rm
source: tdn-rm
title: regTrib - Grupo de informações relativas ao regime tributário do prestador
  do serviço
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=822683264
version: 18
---

| Nome | Pai | Obrigatório | Origem | Descrição |
| --- | --- | --- | --- | --- |
| **regTrib** |  | **Sim** | **Grupo** | **Grupo de informações relativas ao regime tributário do prestador do serviço** |
| opSimpNac | regTrib | Sim | DFILIAL.MICROEMPRESA | **Se** Filial ¹Não optante pelo simples  Então **1: Não Optante;**  **Senão, Se ²**Porte = Mei  Então **2: MEI**  **Senão, Se ²**Porte = ME ou EPP  Então **3: Optante ME ou EPP;**  ¹ Cadastro da Filial | Anexo Dados Fiscais | Tipo de Estabelecimento | Optante Regime Simplificado ² Cadastro da Filial | Anexo Dados Fiscais | Tipo de Estabelecimento | Porte |
| regApTribSN | regTrib | Não | DFILIAL.OPTANTESIMPLES | Este campo só é gerado caso a tag anterior (opSimpNac) seja gerada como 3 - Optante ME ou EPP.   Se opção "Sublimite excedido" estiver marcada o campo é gerado com 2  Se estiver desmarcada é gerado com 1  As outras opções não serão geradas. |
| regEspTrib | regTrib | Sim | DFILIAL.REGIMEESPECIALTRBIBSS | Tag gerada de acordo com a opção selecionada no campo "Regime Especial de Tributação ISS"  0 - Nenhum 1 - Ato Cooperado (Cooperativa) 2 - Estimativa 3 - Microempresa Municipal 4 - Notário ou Registrador 5 - Profissional Autônomo 6 - Sociedade de Profissionais |
