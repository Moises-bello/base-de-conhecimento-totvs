---
article_id: 360016741911
category: RH - Rescisão
content_hash: 7cabc2ffa08010ccb19a9f941d36e7aefa885e295fd65105165a6f086f776d5b
fetched_at: '2026-06-28T22:43:50.875160+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Rescisão por acordo Art 484-A, como parametrizar
  o sistema
type: support-article
updated_at: '2025-09-12T17:28:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016741911-RH-Linha-Protheus-GPE-Rescis%C3%A3o-por-acordo-Art-484-A-como-parametrizar-o-sistema
---

**Dúvida**Com a Reforma trabalhista, o Contrato de Trabalho poderá ser extinto por acordo entre empregado e empregador. Como parametrizar o sistema? **Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Criado o **tipo de aviso A** - Acordo.  
Necessário criar um **novo tipo de rescisão** na tabela S043 com esse tipo de aviso, mantendo as mesmas características do Aviso Indenizado, apenas trocando o percentual da multa do FGTS para 20% e o tipo de Aviso para "A".

***Art. 484-A. O contrato de trabalho poderá ser extinto por acordo entre empregado e empregador, caso em que serão devidas as seguintes verbas trabalhistas:***  
***I – por metade:***  
***a) o aviso prévio, se indenizado; e***  
***b) a indenização sobre o saldo do Fundo de Garantia do Tempo de Serviço, prevista no § 1º do art. 18 da Lei nº 8.036, de 11 de maio de 1990;***  
***II – na integralidade, as demais verbas trabalhistas.***  
***§ 1º A extinção do contrato prevista no caput deste artigo permite a movimentação da conta vinculada do trabalhador no Fundo de Garantia do Tempo de Serviço na forma do inciso I-A do art. 20 da Lei nº 8.036, de 11 de maio de 1990, limitada até 80% (oitenta por cento) do valor dos depósitos.***  
***§ 2º A extinção do contrato por acordo prevista no caput deste artigo não autoriza o ingresso no Programa de Seguro-Desemprego***

1º Passo:  
Atualizar o sistema com o pacote indicado no link:  
[Documento Técnico Reforma Trabalhista Protheus](https://tdn.totvs.com/pages/viewpage.action?pageId=311632134)

2º Passo:  
Executar os procedimentos do documento técnico disponível no link:  
[Documento Técnico Reforma Trabalhista Protheus](https://tdn.totvs.com/pages/viewpage.action?pageId=311632134)

3º Passo: PROCESSO DE CÁLCULO  
Acesse a tabela S043 da rotina Manutenção de Tabelas para conferir as configurações do tipo de rescisão ACORDO

Em **Atualizações > Definições de Calculo > Manutenção de tabelas > Tabela S043 - Tipos de Rescisão**:

- Deixar a coluna Aviso Prévio com A  
- Configurar o % de FGTS com 20%;  
- Informar código de afastamento FGTS = I5  
- Deixar a coluna Cod.Homolognet em branco

![](https://tdn.totvs.com/download/attachments/315907197/image2018-2-12_9-9-19.png?version=1&modificationDate=1518433760000&api=v2)![](https://tdn.totvs.com/download/attachments/315907197/image2018-2-12_9-10-15.png?version=1&modificationDate=1518433816000&api=v2)

* + Não será gerada a verba de contribuição social referente a multa de 10% (id 0297) quando tipo de aviso for "A"
  + Cadastro de tipo de rescisão (S043) no campo Cod. Homolognet permitirá o cadastro "em branco"
  + TRCT campo 22 deverá constar com "Acordo Empregado e Empregador" - Essa informação vem da tabela S043
  + TRCT campo 27 ficará em branco - Essa informação vem da tabela S043 (cod. Homolognet)

Necessário acessar o menu Atualizações >Definições de Cálculos >Definições de Tabelas para que atualize a estrutura da tabela S043 e após isso acessar Manutenção de tabelas e preencher os campos Descrição e Cod. Homolognet corretamente.

Cálculo de rescisão:![](https://tdn.totvs.com/download/attachments/315907197/image2017-11-21_18-7-49.png?version=1&modificationDate=1511294870000&api=v2)

O sistema calculou metade dos dias dias aviso conforme legislação:![](https://tdn.totvs.com/download/attachments/315907197/image2017-11-22_11-37-25.png?version=1&modificationDate=1511357846000&api=v2)

Valor da multa do FGTS reduzida a 20%.

 TRCT:

![](https://tdn.totvs.com/download/attachments/315907197/image2018-2-12_9-15-50.png?version=1&modificationDate=1518434150000&api=v2)

 4º Passo: Geração da GRRF  
![](https://tdn.totvs.com/download/attachments/315907197/image2017-11-22_11-41-30.png?version=1&modificationDate=1511358090000&api=v2)![](https://tdn.totvs.com/download/attachments/315907197/image2017-11-22_11-41-44.png?version=1&modificationDate=1511358105000&api=v2)![](https://tdn.totvs.com/download/attachments/315907197/image2017-11-22_11-42-7.png?version=1&modificationDate=1511358127000&api=v2)

![](https://tdn.totvs.com/download/attachments/315907197/image2017-11-22_11-42-26.png?version=1&modificationDate=1511358147000&api=v2)

![](https://tdn.totvs.com/download/attachments/315907197/image2017-11-22_11-40-55.png?version=1&modificationDate=1511358056000&api=v2)

**Saiba mais**

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)

[RH - Linha Protheus - GPE - Como parametrizar o sistema para rescisão por acordo aviso trabalhado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059768093-RH-Linha-Protheus-GPE-Como-parametrizar-o-sistema-para-rescis%C3%A3o-por-acordo-aviso-trabalhado?source=search)
