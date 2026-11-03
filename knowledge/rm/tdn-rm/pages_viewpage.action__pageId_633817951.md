---
content_hash: f298317c0d28edc9e55df28a42c0ae283c313864ba2eac3fefa5ba6a82be3d35
fetched_at: '2026-06-29T00:11:06.315555+00:00'
page_id: '633817951'
product: rm
source: tdn-rm
title: Incidência Exclusiva do Empregador - 13° Salário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=633817951
version: 9
---

false

**A partir das Versões:**

* 12.1.29.299
* 12.1.31.215
* 12.1.32.152
* e superiores.

# Objetivo:

---

Apresentar os tratamentos que foram realizados na geração do XML para o eSocial S-1010, GPS, Folha analítica e encargos para as novas incidências de 13° Salário( **Incidência exclusiva do empregador aba proventos e descontos**) no cadastro de eventos.

---

11AtualizadorAtualizador

Após a liberação da versão será necessário executar os script's de criação dos campos do sistema através do sistema **RM.Atualizador.exe.**

2Cadastro dos eventosCadastro dos eventos

Segue abaixo parametrização realizada no cadastro de eventos:

Foram criados dois eventos com o campo Incidência exclusiva do empregador marcado

S-1010 será gerado com a tag <codIncCP> 14- Exclusiva do empregador - 13° salário

S-1010 será gerado com a tag <codIncCP> 14- Exclusiva do empregador - 13° salário

true3Geração dos relatórios Geração dos relatórios 

No envelope de pagamento foi lançado os eventos criados anteriormente (aba "Cadastro de Eventos") com os seguintes valores:

* **BASE 13° SALARIO =** 363,00 (2ª PARCELA 13º SALARIO) = 363,00

* Ao gerar a GPS, o sistema irá considerar como **Base de INSS** o valor dos eventos que tem incidência de **INSS** + **Incidência exclusiva do empregador=** 363,00 (2ª PARCELA 13º SALARIO) + 952,38 (PROV - EXC. EMPREGADOR - MEDIA COMISSAO 2ª PARCELA 13º) - 35,00 (DESC- EXC. EMPREGADOR - EXCLUSIVA EMPREGADOR DESCONTO 13°) = 1.280,38

* Feito a geração do encargo de INSS de 13° Salário

* Na Folha analítica os valores serão descritos nos campos **Base INSS 13° - Envelope** e **Base INSS 13° - GPS**.

Segue abaixo exemplo do relatório gerado para o envelope demonstrado acima:

* **Base INSS - GPS**: o sistema considerou o valor dos eventos que tem incidência de **INSS** + **Incidência exclusiva do empregador=**363,00 (2ª PARCELA 13º SALARIO) + 952,38 (PROV - EXC. EMPREGADOR - MEDIA COMISSAO 2ª PARCELA 13º) - 35,00 (DESC- EXC. EMPREGADOR - EXCLUSIVA EMPREGADOR DESCONTO 13°) = 1.280,38
* **Base INSS - Envelope**:  o sistema considerou o valor dos eventos que tem incidência de **INSS** **=**363,00 (2ª PARCELA 13º SALARIO) = 363,00
