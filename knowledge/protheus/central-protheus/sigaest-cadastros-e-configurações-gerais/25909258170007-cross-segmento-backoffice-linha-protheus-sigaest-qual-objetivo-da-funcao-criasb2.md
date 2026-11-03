---
article_id: 25909258170007
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: eaa2a15387c20ee75647c70236ae8f22b5f0ce8b42fc3bd15145a495ac044bc1
fetched_at: '2026-06-28T22:39:09.741921+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Qual objetivo da funcao
  CriaSB2?
type: support-article
updated_at: '2025-03-12T11:43:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25909258170007-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Qual-objetivo-da-funcao-CriaSB2
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25909258153495) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Qual objetivo da funcao CriaSB2()?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Se trata de uma função padrão para criar registros no arquivo de saldos em estoque, na tabela (SB2).

**Sintaxe:** **CriaSB2(ExpC1,ExpC2,ExpC3)**

**Parâmetros**  
**ExpC1** = Código do produto  
**ExpC2** = Código do almoxarifado  
**ExpC3** = Código da Filial Destino (de Entrega - Compras)

Então se voce quiser usar em alguma customização/Ponto de entrada, saiba que essa função serve para gravar informações no registro SB2 que acaba de ser criado.

O Retorno deste Ponto de Entrada, **deverá ser um vetor contendo os campos e seus respectivos valores, que deverão ser gravados neste registro.**

**Exemplo de utilização da função**

```
// Função para criar um registro SB2  
User Function CriaExemploSB2()  
  Local cProduto := "PROD001" // Código do produto  
  Local cAlmox := "01" // Código do almoxarifado  
  Local cFilial := "FIL001" // Código da filial destino  
  
// Chama a função CriaSB2 com os parâmetros necessários  
If CriaSB2(cProduto, cAlmox, cFilial)  
  MsgInfo("Registro SB2 criado com sucesso!", "Aviso")  
Else  
  MsgStop("Erro ao criar registro SB2.", "Erro")  
EndIf  
Return
```

**ATENÇÃO:** Isso é apenas um exemplo, cada cliente deve adequar suas regras de customização.

**Possa interessar:** Abaixo temos a descrição dos Pontos de Entrada do módulo de Estoque/Custos com seus respectivos links onde são acompanhados de sua respectiva documentação.

[Pontos de Entrada de Estoque/Custos](https://tdn.totvs.com/pages/releaseview.action?pageId=235589202)

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)*
