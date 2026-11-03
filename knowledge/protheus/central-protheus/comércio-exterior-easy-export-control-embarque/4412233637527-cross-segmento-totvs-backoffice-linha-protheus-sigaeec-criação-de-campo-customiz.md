---
article_id: 4412233637527
category: Comércio Exterior - Easy Export Control - Embarque
content_hash: d7f2a3dd11848a9b787900e1c3c031c0251297178f7f9cca851450870dbfe6cc
fetched_at: '2026-06-28T22:36:39.158699+00:00'
product: protheus
section_id: 1500001549322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Criação de campo
  customizado na rotina de Despesas Nacionais
type: support-article
updated_at: '2021-11-04T14:02:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412233637527-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Cria%C3%A7%C3%A3o-de-campo-customizado-na-rotina-de-Despesas-Nacionais
---

**Dúvida**Preciso criar campos customizados na rotina de despesas nacionais (**EECDN400**) onde é exibido os embarque associados porém por se tratar de um fonte MVC os campos não estão sendo exibidos. Preciso de uma orientação como criar estes campos ou se é possível criar um ponto de entrada.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Export Control* – A partir da versão 12.1.27.

**Solução**Devido a estrutura desta rotina utilizar a mesma tabela para a montagem dos dados da capa e dos itens, ao criar campos customizados, os mesmos são lançados automaticamente na capa. Desta forma, será disponibilizados pontos de entrada na rotina, para que seja possível intervir na montagem da tela, retirando os campos customizados da capa e os adicionando na linha dos itens, onde constam as informações dos embarques. Será necessário:

1. Criar o campo customizado na tabela **EET** (**Despesas Exportação**) via configurador.
2. Aplicar a solução **DTRADE-6962** para que o conteúdo do campo customizado seja gravado.
3. Utilização do ponto de entrada  **"DN400INTEMB"**, responsável por enviar os dados destes campos adicionados ao grid para a gravação no Embarque. Segue exemplo do Ponto de entrada:

```
//Ponto de Entrada DN400INTEMB  
User Function DN400INTEMB()  
  
oEEB := PARAMIXB[1]//Modelo de dados para informacoes do fornecedor da despesa (EEB)  
oEET := PARAMIXB[2]//Modelo de dados para informacoes gerais da despesa, como por exemplo o documento (EET)  
oEmb := PARAMIXB[3]//Modelo de dados para informacoes da despesa especificas para cada embarque, como por exemplo o proprio numero do embarque ou o valor (EET)  
nLine := PARAMIXB[4]//Linha atual do modelo de dados do Embarque que esta sendo considerada na preparacao de dados para integracao  
  
//Possibilita adicionar novos campos na integracao da despesa com o Embarque  
aAdd(aEEC[Len(aEEC)][2][1], {"EET_CHAR", oEMB:GetValue("EET_CHAR", nLine), Nil})  
aAdd(aEEC[Len(aEEC)][2][1], {"EET_NUM", oEMB:GetValue("EET_NUM", nLine), Nil})  
  
Return Nil
```

**Saiba mais**

[DTRADE-6962 - PE Adicionar campos no grid de Embarques das Despesas Nacionais](https://tdn.totvs.com/display/public/PROT/DT+PE+Adicionar+campos+no+grid+de+Embarques+das+Despesas+Nacionais)

[Ponto de Entrada DN400INTEMB](https://tdn.totvs.com/display/public/PROT/DT+PE+DN400INTEMB+Despesas+Nacionais)
