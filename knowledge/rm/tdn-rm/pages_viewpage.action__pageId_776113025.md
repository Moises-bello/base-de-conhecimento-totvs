---
content_hash: ae2dce69467c6899fc32958a05c642c438522ed3fb343c38c33b8899344fceb3
fetched_at: '2026-06-29T00:11:36.995385+00:00'
page_id: '776113025'
product: rm
source: tdn-rm
title: Alterações - S-1210 - Leiaute S-1.2
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=776113025
version: 72
---

false

**A partir das Versões:**

* 12.1.2302.235
* 12.1.2306.182
* 12.1.2310.116 e superiores

**CONTEÚDO**

IMPORTANTE!

---

## **01. VISÃO GERAL**

Este documento visa apresentar as mudanças no evento S-1210 para atender o Leiaute do eSocial versão S-1.2.

## **02. ALTERAÇÕES REALIZADAS**

### **02.01**Criação do grupo {infoIRComplem} e seu respectivo campo{dtLaudo}

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Grupo {infoIRComplem} | - | **OC** |

**Alteração:**Foi adicionado um campo no parametrizador do eSocial para especificar qual campo adicional do funcionário será usado para a data de moléstia grave. Certifique-se de configurar esse campo adicional como do tipo DATA.

  XML:

### **02.02 Criação do grupo {infoDep} e seus respectivos campos{cpfDep, dtNascto, nome, depIRRF, tpDep, descrDep}**

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Grupo {infoDep} | - | **OC** |

**Dependentes do Autônomos Externos  
Alteração**: Deverá preencher as tabelas PPAGTOAUTONOMOEXT e PPAGTOAUTONOMOEXTDEPEND. Para o preenchimento dessas tabelas. Para fazer isso, você pode utilizar a [Importação de Autônomos Externos](https://tdn.totvs.com/pages/viewpage.action?pageId=543064647), [Webs Services](https://tdn.totvs.com/pages/releaseview.action?pageId=425459227), Conceito ou outros meios disponíveis.

XML:

**Dependentes do TOTVS Gestão Financeira**

O sistema irá considerar os dependentes cadastrados no TOTVS Gestão Financeira. Para isso, é necessário cadastrar os dependentes no anexo "Dependentes" do cadastro do Cliente/Fornecedor no TOTVS Gestão Financeira, conforme demonstrado abaixo:

**ATENÇÃO:**

* + Para obter detalhes sobre o cadastro do dependente, acesse [Dependentes do Cliente/Fornecedor](https://tdn.totvs.com/pages/releaseview.action?pageId=787858319)
  + O sistema gerará automaticamente os dependentes que estiverem dentro do período de início e fim do período de apuração gerado para o S-1210.
  + Sempre que o sistema encontrar um dependente para o período de apuração, lançará automaticamente o grupo <dedDepen>, utilizando o valor cadastrado na tabela de valores fixos.

                            

Geração do XML do evento S-1210:

**Dependentes do TOTVS Folha de Pagamento**

O sistema irá considerar os dependentes cadastrados no TOTVS Folha de Pagamento para os autonomos cadastrados no sistema que não possuem o envio do evento S-2300 -Trabalhador Sem Vínculo de Emprego/Estatutário - Início. Para isso, é necessário cadastrar os dependentes no Anexos| Folha de Pagamento | Dependentes do cadastro do funcionário no TOTVS Folha de Pagamento, conforme demonstrado abaixo:

Importante: os dependentes serão impressos sempre que houver valores dos grupos (exemplo: penAlim,dedDepen,previdCompl e etc) a serem levados.

### **02.03 Criação do grupo {infoIRCR} e campo {tpCR}**

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Grupo {infoIRCR} | - | **OC** |

**Alteração**: O grupo será gerado sempre que houver um de seus subgrupos, como {dedDepen}, {penAlim} e {previdCompl}. Para mais detalhes, consulte o .

### **02.04 Criação do grupo {penAlim} e campos tpRend,cpfDep e vlrDedPenAlim**

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Grupo {penAlim} | - | **OC** |

**Alterações**:

* + Grupo será impresso sempre que tiver descontos de pensão em folha e movimentação da pensão de dependente vinculado no cadastrado do dependente do funcionário. Mais informações [acesse](https://tdn.totvs.com.br/display/LRM/Dependentes).
  + Caso possua mais de um recibo de férias, é necessario que o lançamento seja feito em períodos diferentes da folha, pois o campo período é chave para alimentar a movimentação da pensão de dependente vinculado no cadastrado do dependente do funcionário.
  + Para autônomos externos grupo será impresso sempre que o campo VALORDEDUCAOPENSAO da tabela PPAGTOAUTONOMOEXTDEPEND estiver preenchido.
  + Autônomos do sistema gestão financeira não tem a opção.

XML:

### **02.05 Criação do grupo {dedDepen} e campos tpRend,cpfDep e vlrDedDep**

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Grupo {dedDepen} |  | **N** (se tpCR = [188901]); **OC** (nos demais casos) |

**Alterações**:

* + Grupo será impresso sempre que tiver descontos de IRRF em folha e [Valor Dedução do Rendimento Tributável](https://tdn.totvs.com/pages/viewpage.action?pageId=784779468) vinculado no cadastrado do dependente do funcionário.
  + Para autônomos externos grupo será impresso sempre que o campo VALORDEDUCAO da tabela PPAGTOAUTONOMOEXTDEPEND estiver preenchido.
  + Autônomos do sistema gestão financeira será impresso sempre que o sistema encontrar um dependente para o período de apuração, o valor será lançado da tabela de valores fixos.

XML:

### **02.06 Criação do grupo {previdCompl} e campos tpPrev,cnpjEntidPC, vlrDedPC e** **vlrPatrocFunp**

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Grupo {previdCompl} | - | **OC** |

**Alteração**: O grupo será impresso sempre que houver lançamentos de eventos com os tipos codIncIRRF (46, 47, 48, 61, 62, 63, 64, 65, 66) no envelope de pagamento do funcionário.

No cadastro Administração de Pessoal | Eventos | Eventos, nas abas Inc. Descontos e Inc. Proventos, foi incluído o campo 'Tipo de Previdência Complementar' (Aba Inc. Descontos e Inc. Proventos). Observação: Caso utilize o código de cálculo referente à previdência complementar, a tag codIncIRRF será gerada automaticamente.

No menu eSocial | Previdência Complementar | Cadastro Previdência Complementar, foi incluído o cadastro para vinculação dos dados da previdência complementar. Para mais informações, acesse o link [Previdência Complementar](https://tdn.totvs.com/pages/viewpage.action?pageId=791847949)

XML:

### **02.07 Criação do grupo {planSaude,infoDepSau} e campos {cnpjOper,regANS ,vlrSaudeTit ,cpfDep,vlrSaudeDep}**

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Grupo {planSaude} | - | **OC** |
| Grupo {infoDepSau} | - | **OC** |

**Alteração**: O grupo será impresso quando houver desconto de assistência médica, seja para o titular ou para o dependente.

falseImportante!

1. Os dados do plano de saúde serão obtidos do cadastro da operadora de saúde.
2. Certifique-se de que os valores nos históricos de assistência médica e na ficha financeira sejam iguais, para a correta geração do XML.
3. Preencha o campo de natureza da rubrica do evento de assistência médica com o código 9219 (Desconto de assistência médica ou odontológica).
4. Cadastre os eventos de assistência médica e diferenças na aba Eventos da Operadora.
5. Conforme MOS, a coparticipação deverá ser enviada através da rubrica 9219, assim como o desconto mensal realizado para o funcionário (MOS S-1200 item 13.2).
6. No caso de férias, a fim de evitar a duplicidade de valores gerados no evento S-1210, é importante garantir que a rubrica associada aos eventos em "Eventos do Recibo" e "Eventos da Folha" para assistência médica não seja a mesma, e que as devidas incidências sejam mantidas apenas na verba de natureza 9219.

No menu eSocial | Operadora Saúde | Cadastro Operadora de Saúde, é possível cadastrar informações sobre a operadora de saúde e também os eventos relacionados a ela.

**Exemplo de utilização**

**1.** Quando um funcionário tem o desconto de assistência médica durante o período de férias:

**2.** Foi registrado o mapeamento de equivalência (DE/PARA) nos adicionais de férias, acessando Configurações | Parametrizador | Férias | Eventos Adicionais Globais.

falseImportante!

Para evitar a duplicidade de informações no evento S-1210, o evento de assistência médica a ser lançado na folha não deve ter o código da rubrica com o código 9219 - "Desconto de assistência médica ou odontológica". Escolha um código de rubrica diferente para o evento de assistência médica associado à folha, garantindo que não haja conflito com o desconto já presente no evento S-1210.

**3.** O histórico foi registrado de maneira adequada, com o tipo de movimento configurado como '1-Férias'.

**4.** O evento foi devidamente lançado no envelope de pagamento, sem a rubrica 9219 - "Desconto de assistência médica ou odontológica", conforme especificado.

**5.** Ao gerar o evento S-1210, foi criado de acordo com as configurações cadastradas, demonstrando que o processo ocorreu corretamente.

### **02.08 Criação dos** **grupos** **{infoReembMed,** **detReembTit,****infoReembDep,****detReembDep****}**

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Grupo {infoReembMed}: campos {indOrgReemb,cnpjOper,regANS} | - | **OC** |
| Grupo {detReembTit}: campos {tpInsc,nrInsc,vlrReemb,vlrReembAnt} | - | **OC** |
| Grupo {infoReembDep}: campos {cpfBenef} | - | **OC** |
| Grupo {detReembDep}: campos {tpInsc,nrInsc,vlrReemb,vlrReembAnt} | - | **OC** |

**Alterações**: Os grupos serão gerados sempre que houver informações no cadastro do menu Anuais | Dirf | Reembolso da Operadora de Assistência à Saúde. Para mais informações sobre o cadastro,  [clique aqui.](https://tdn.totvs.com/pages/viewpage.action?pageId=452718759)

 

XML:

## **03. MAPEAMENTO DO EVENTO**

Acesse o mapeamento do evento clicando no link abaixo:
