---
article_id: 40441286267031
category: SIGAEST - CUSTOS
content_hash: 7543f15bf628a41a9eae1755c82a51867f2108f550c2c58b63f699d5873bb32d
fetched_at: '2026-06-28T22:39:02.330794+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Processo de configuração
  de MOD e GGF "Sem" e "Com" integração contábil
type: support-article
updated_at: '2026-05-13T15:06:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40441286267031-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Processo-de-configura%C3%A7%C3%A3o-de-MOD-e-GGF-Sem-e-Com-integra%C3%A7%C3%A3o-cont%C3%A1bil
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40441286243479) Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**

Como configurar o Cálculo do Custeio de Mão de Obra, produtos do tipo **MOD** e Gastos Gerais de Fabricação **GGF** no Protheus **(B1\_CCCUSTO, B1\_GCCUSTO, MOD e GGF)** com e sem integração contábil

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Passo a Passo**

![](https://tdn.totvs.com/download/attachments/423930063/image2018-10-18_16-24-51.png?version=1&modificationDate=1539890691873&api=v2)

É possível incluir no sistema um produto MOD de duas maneiras, sendo necessario escolhe apenas uma delas para funcionamento, não pode ser as duas.

* **Cadastrar o produto com o campo Código (B1\_COD)** = MOD + Código do Centro de Custo  
  Importante: Essa forma de cadastrar irá fazer com que todo valor do centro de custo seja alocado no produto.
* **Informar o campo CC p/ Custo (B1\_CCCUSTO)** = Código do Centro de Custo. Para utilizar este modelo, o parâmetro MV\_PRODMOD deverá estar habilitado.  
  Importante: Se for necessário dividir o valor do centro de custo entre mais de um produto, informar o campo Gr Cnt Custo (B1\_GCCUSTO),  
  para utilizar o conceito de Grupo dentro do Centro de Custo.

#### 

#### **Porque a MOD/GGF ficam com os saldos negativos em suas requisições?**

No Protheus, MOD e GGF são tratados como "tipo de serviços" ou puramente financeiros para compor o custo da produção. **O saldo negativo não é um erro de saldo físico**, mas sim um reflexo do fluxo de apropriação de custos, sendo assim é perfeitamente comum a MO ter saldo negativo em seus saldos.

**Como recalcular os saldos da MOD? Valide:**

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA300 - Refaz Saldos - Conceito e Informações](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4420659401751-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA300-Refaz-Saldos-Conceito-e-Informa%C3%A7%C3%B5es)

#### **A seguir, detalhamos as particularidades de cada abordagem para calculo da MOD/GGF com ou sem integração contabil:**

[Configurações e informações sobre o calculo do custo de MOD e GGF](https://tdn.totvs.com/x/357aFQ)

#### **Meu produto MOD/GGF não esta custeando, oque posso fazer pra validar?**

* **Possui integração contabil?**: Se sim, valide o valor existente que foi lançado no centro de custo do seu produto, e esse valor precisa esta a **Debito**, e precisa esta dentro do periodo que voce esta apurando o calculo.

  **Credito**não pode ser maior que o **Debito**, se estiver assim no seu contabil, corriga com seu contabil antes de prosseguir para o calculo e apuração.

  Certifique-se que durante o custeio de calculo, voce usa o despejo dos valores por "Contabil contabil", considerando como "Extracontabil ou Contabil", pois existe diferença de acordo sua configuração:

  **- Contábil:**  
  Considera o saldo da conta contábil da tabela **CQ1 - Saldo das Contas**

  **- ExtraContábil:**  
  Considera o saldo da conta contábil + centro de custo da tabela **CQ3 - Saldo dos Centros de Custo**
* **Não possui integração?**: Certifique que o seu produto possui valor no campo B2\_CM1, se acaso não possui, voce deve imputar o valor para que seja calculado o médio desejado, de acordo suas requisições, acesse a rotina MATA225 e então considere, qual é o custo médio desejado para o produto MOD. **(funcionalidade apenas caso você não use integração contabil).**
* O ambiente se encontra atualizado? enviar o ID da central

  [Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como enviar dados pela Central de Diagnóstico?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33711098138007-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-enviar-dados-pela-Central-de-Diagn%C3%B3stico)

**Saiba mais:**

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MOD/GGF - Conceito e Usabilidade*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402117444247)

[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)

[*MA330MOD - Customiza calculo do custo de mão-de-obra*](https://tdn.totvs.com/pages/releaseview.action?pageId=6087637)
